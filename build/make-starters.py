#!/usr/bin/env python3
"""Build the exercise starters from the reference solutions.

Every exercise from 3 onwards continues the Wordle project. A student who fell
behind starts from a starter instead of their own code, and the starter for
exercise N is, by definition :

    solutions/<N-1>-<name>/        the previous exercise, finished
  + exercises/handouts/<N>-<name>/ anything exercise N hands out (tests, data)

Keeping that a rule rather than a habit is the point of this script : starters
are generated, never edited by hand, so they cannot drift from the solutions.

Run from the course root :

    uv run python build/make-starters.py           rewrite exercises/starters/
    uv run python build/make-starters.py --check   fail if anything is stale (CI)
"""

from __future__ import annotations

import filecmp
import re
import shutil
import sys
import tempfile
from pathlib import Path

SOLUTIONS = Path("solutions")
HANDOUTS = Path("exercises/handouts")
STARTERS = Path("exercises/starters")

STAGE = re.compile(r"^(\d\d)-[a-z0-9-]+$")
IGNORE = shutil.ignore_patterns(
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "*.db", "uv.lock"
)


def stages(root: Path) -> dict[int, Path]:
    """Map exercise number to folder, for folders named like `05-functions`."""
    found = {}
    for folder in root.iterdir() if root.exists() else []:
        m = STAGE.match(folder.name)
        if folder.is_dir() and m:
            found[int(m.group(1))] = folder
    return found


def build(into: Path) -> list[str]:
    """Write every starter under `into`. Returns the starter names."""
    solutions = stages(SOLUTIONS)
    handouts = stages(HANDOUTS)
    built = []
    for number, solution in sorted(solutions.items()):
        previous = solutions.get(number - 1)
        if previous is None:
            continue
        target = into / solution.name
        shutil.copytree(previous, target, ignore=IGNORE)
        if number in handouts:
            shutil.copytree(handouts[number], target, ignore=IGNORE, dirs_exist_ok=True)
        built.append(solution.name)
    return built


def same_tree(a: Path, b: Path) -> bool:
    cmp = filecmp.dircmp(a, b, ignore=["__pycache__", ".pytest_cache", ".venv"])
    if cmp.left_only or cmp.right_only or cmp.diff_files or cmp.funny_files:
        return False
    _, mismatch, errors = filecmp.cmpfiles(a, b, cmp.common_files, shallow=False)
    if mismatch or errors:
        return False
    return all(same_tree(a / d, b / d) for d in cmp.common_dirs)


def main() -> int:
    check = "--check" in sys.argv
    with tempfile.TemporaryDirectory() as tmp:
        fresh = Path(tmp)
        names = build(fresh)
        if check:
            stale = [n for n in names if not (STARTERS / n).exists()
                     or not same_tree(fresh / n, STARTERS / n)]
            existing = {p.name for p in STARTERS.iterdir()} if STARTERS.exists() else set()
            extra = sorted(existing - set(names))
            for n in stale:
                print(f"stale starter : {STARTERS / n}")
            for n in extra:
                print(f"starter without a solution behind it : {STARTERS / n}")
            if stale or extra:
                print("Run  uv run python build/make-starters.py  and commit the result.")
                return 1
            print(f"{len(names)} starters up to date.")
            return 0
        if STARTERS.exists():
            shutil.rmtree(STARTERS)
        shutil.copytree(fresh, STARTERS)
        print(f"Wrote {len(names)} starters to {STARTERS}: {', '.join(names)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
