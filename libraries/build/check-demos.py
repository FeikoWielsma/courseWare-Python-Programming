"""Compile every demo and run non-interactive demos without Python networking."""

import sys

from check_support import ROOT, run_case, workspace


def main() -> int:
    failed = compiled = executed = 0
    with workspace() as (course, environment):
        for original in sorted((ROOT / "demos").rglob("*.py")):
            relative = original.relative_to(ROOT).as_posix()
            source = original.read_text(encoding="utf-8")
            try:
                compile(source, relative, "exec")
            except SyntaxError as error:
                print(f"FAIL {relative}: {error}")
                failed += 1
                continue
            compiled += 1
            if any(line.startswith("# INTERACTIVE") for line in source.splitlines()):
                print(f"COMPILE {relative} (interactive)")
                continue
            executed += 1
            failed += not run_case(course, environment, relative)
    print(f"{compiled} compiled, {executed} executed, {failed} failed")
    return int(failed > 0)


if __name__ == "__main__":
    sys.exit(main())
