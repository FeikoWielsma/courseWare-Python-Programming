#!/usr/bin/env python3
"""Check the Python code fences in the slides and the exercise guides.

Slide fences are snippets, so most of them are not valid modules on their own :
a class body shown without its class, a grammar with `[, name2]` notation, an
elided `...`. Demanding that every fence parse would be noise. What this checks
instead are the defects the PDF conversion actually leaves behind, each of which
would break for a student who typed the code off the slide :

  * a slide title glued onto a line of code, such as `t.start()Daemon Threads`
  * a Python 2 `print` statement
  * a smart quote, en-dash, ellipsis or arrow sitting inside code
  * anything ruff's modernisation rules flag on a fence that does parse

Run from the course root :  uv run python build/check-fences.py
"""

from __future__ import annotations

import ast
import pathlib
import re
import subprocess
import sys
import tempfile

ROOTS = ["src/slides", "src/exercises"]
# Dated syntax only. Layout rules are deliberately left out : the semicolons and
# one-line bodies on the slides are there to save vertical space, and `await`
# outside a coroutine is normal in a snippet that shows only the inside of one.
RUFF_SELECT = "UP,W6,RUF001,RUF002,RUF003"
# UP015 : the IO module is about file modes, so `open(name, "r")` spells out the
#         default on purpose rather than leaving the reader to know it.
# UP018 : the conversion-functions slide calls `str('abc')` to show what the
#         function does; rewriting it as a literal deletes the example.

# UP031 : the format-specification slide closes with one `%` example, so the
#         older style can be recognised in other people's code.
# UP032 : the same fence shows `str.format` once, for the same reason.
RUFF_IGNORE = "UP015,UP018,UP031,UP032"

FENCE_OPEN = re.compile(r"^```python[ \t]*$")
FENCE_CLOSE = re.compile(r"^[ \t]*```[ \t]*$")

# `)Word`, `:Word` or `1demo09_name` : a footer the conversion glued on.
GLUED = re.compile(r"(?:[)\]:]|\d)(?:[A-Z][a-z]+(?:\s[A-Z]?[a-z]+)*|demo\d+_\w+)\s*$")
# `print x` with no parentheses is the Python 2 statement.
PY2_PRINT = re.compile(r"^\s*print\s+[^(=\s]")
# A bare `print` on its own line is a no-op in Python 3.
BARE_PRINT = re.compile(r"^\s*print\s*$")
# Characters a PDF leaves behind that are not valid where they sit. Named by
# codepoint so that this file does not itself contain the characters it rejects.
BAD_CHARS = {
    chr(0x2018): "LEFT SINGLE QUOTATION MARK",
    chr(0x2019): "RIGHT SINGLE QUOTATION MARK",
    chr(0x201C): "LEFT DOUBLE QUOTATION MARK",
    chr(0x201D): "RIGHT DOUBLE QUOTATION MARK",
    chr(0x2013): "EN DASH",
    chr(0x2014): "EM DASH",
    chr(0x2026): "HORIZONTAL ELLIPSIS",
    chr(0x2192): "RIGHTWARDS ARROW",
}


def fences(root: pathlib.Path):
    """Yield (path, first_body_line_number, body_lines) for every python fence."""
    for md in sorted(root.rglob("*.md")):
        lines = md.read_text(encoding="utf-8").splitlines()
        i = 0
        while i < len(lines):
            if not FENCE_OPEN.match(lines[i]):
                i += 1
                continue
            j = i + 1
            while j < len(lines) and not FENCE_CLOSE.match(lines[j]):
                j += 1
            yield md, i + 2, lines[i + 1 : j]
            i = j + 1


def main() -> int:
    # The findings quote the characters they object to, several of which a
    # Windows console cannot encode in its default code page. Without this the
    # script dies on the first smart quote it reports.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    problems: list[str] = []
    unparsed = 0
    total = 0
    parseable: list[tuple[pathlib.Path, int, list[str]]] = []

    for name in ROOTS:
        root = pathlib.Path(name)
        if not root.exists():
            continue
        for md, start, body in fences(root):
            total += 1
            for offset, line in enumerate(body):
                where = f"{md.as_posix()}:{start + offset}"
                if GLUED.search(line) and not line.lstrip().startswith("#"):
                    problems.append(f"{where}: slide title glued onto code : {line.strip()}")
                if PY2_PRINT.match(line) or BARE_PRINT.match(line):
                    problems.append(f"{where}: Python 2 print statement : {line.strip()}")
                for ch, label in BAD_CHARS.items():
                    if ch in line:
                        problems.append(f"{where}: {label} inside code : {line.strip()}")
            try:
                ast.parse("\n".join(body))
            except SyntaxError:
                unparsed += 1
            else:
                parseable.append((md, start, body))

    # Ruff over the fences that are complete modules.
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = pathlib.Path(tmp)
        index = {}
        for n, (md, start, body) in enumerate(parseable):
            f = tmpdir / f"fence{n:04d}.py"
            f.write_text("\n".join(body) + "\n", encoding="utf-8")
            index[f.name] = (md, start)
        if index:
            out = subprocess.run(
                [sys.executable, "-m", "ruff", "check", str(tmpdir), "--no-cache",
                 "--isolated", "--select", RUFF_SELECT, "--ignore", RUFF_IGNORE,
                 "--target-version", "py314", "--output-format", "concise"],
                capture_output=True, text=True, check=False,
            ).stdout
            for line in out.splitlines():
                m = re.match(r"^.*?(fence\d{4}\.py):(\d+):(\d+): (.*)$", line)
                if not m:
                    continue
                fname, fl, _fc, msg = m.groups()
                md, start = index[fname]
                problems.append(f"{md.as_posix()}:{start + int(fl) - 1}: {msg}")

    print(f"{total} python fences checked, {len(parseable)} parse as a module, "
          f"{unparsed} are snippets")
    if problems:
        print(f"\n{len(problems)} problem(s):\n")
        for p in problems:
            print("  " + p)
        return 1
    print("No problems found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
