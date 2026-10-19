"""Compile every demo and run non-interactive demos without Python networking."""

import contextlib
import io
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from check_support import ROOT, run_case, workspace


def check_files(files: list[Path]) -> tuple[str, int, int, int]:
    """Check demos in order, in their own copy of the course; return the report and counts."""
    failed = compiled = executed = 0
    report = io.StringIO()
    with contextlib.redirect_stdout(report), workspace() as (course, environment):
        for original in files:
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
    return report.getvalue(), failed, compiled, executed


def main() -> int:
    # Module folders are independent: each runs in order in its own copy of the course, the
    # folders in parallel, and the reports print in the order of the files.
    groups: dict[str, list[Path]] = {}
    for original in sorted((ROOT / "demos").rglob("*.py")):
        groups.setdefault(original.relative_to(ROOT / "demos").parts[0], []).append(original)
    failed = compiled = executed = 0
    with ProcessPoolExecutor(max_workers=min(len(groups), os.cpu_count() or 1)) as pool:
        for report, folder_failed, folder_compiled, folder_executed in pool.map(
            check_files, groups.values(),
        ):
            print(report, end="", flush=True)
            failed += folder_failed
            compiled += folder_compiled
            executed += folder_executed
    print(f"{compiled} compiled, {executed} executed, {failed} failed")
    return int(failed > 0)


if __name__ == "__main__":
    sys.exit(main())
