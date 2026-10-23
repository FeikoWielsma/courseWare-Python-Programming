"""Run every solution and exercise the documented CLI exit conventions offline."""

import sys

from check_support import ROOT, run_case, workspace


def main() -> int:
    failed = executed = 0
    with workspace() as (course, environment):
        for original in sorted((ROOT / "solutions").rglob("*.py")):
            # The web application starts a server; check-web.py tests it instead.
            if "solution09-web-apps" in original.parts:
                continue
            # The dashboard needs a Streamlit session; check-dashboards.py tests it instead.
            if original.name == "dashboard.py":
                continue
            relative = original.relative_to(ROOT).as_posix()
            # The CLI deliberately exits 1 when it finds invalid imported records.
            arguments = ["--strict"] if (
                original.name == "library_check_cli.py"
            ) else []
            expected = 1 if original.name == "library_check_cli.py" else 0
            failed += not run_case(course, environment, relative, arguments, expected)
            executed += 1
        library_cli = "solutions/solution03-modern-toolbelt/library_check_cli.py"
        for arguments, expected, label in [
            (["--help"], 0, "help"),
            ([], 0, "report"),
            ([str(course / "data" / "tracks.csv"), "--strict"], 0, "clean-import"),
            ([str(course / "missing.csv")], 2, "missing-file"),
        ]:
            failed += not run_case(
                course, environment, library_cli, arguments, expected, label,
                stderr_contains="library_check:" if label == "missing-file" else "",
                stdout_empty=label == "missing-file",
            )
            executed += 1
        logtool = "solutions/solution02-command-line-programs/logtool.py"
        logfile = str(course / "data" / "listening.log")
        cases = [
            (["--help"], 0, "help"),
            (["count", logfile], 0, "count"),
            (["count", "--help"], 0, "count-help"),
            (["errors", logfile], 1, "errors"),
            (["errors", logfile, "--level", "WARN"], 1, "warnings"),
            (["errors", logfile, "--level", "FATAL"], 0, "no-matches"),
            (["count", str(course / "missing.log")], 2, "missing-file"),
            (["count", "-"], 0, "stdin"),
            (["count", logfile, "--since", "2026-10-13"], 0, "since"),
        ]
        for arguments, expected, label in cases:
            counts = "Imagine PLAY=1 SKIP=0" if label in {"count", "stdin"} else ""
            failed += not run_case(
                course, environment, logtool, arguments, expected, label,
                stdin=(course / "data" / "listening.log").read_text(encoding="utf-8"),
                quoted=counts,
                stderr_contains="logtool:" if label == "missing-file" else "",
                stdout_empty=label in {"missing-file", "no-matches", "since"},
            )
            executed += 1
    print(f"{executed} solution commands, {failed} failed")
    return int(failed > 0)


if __name__ == "__main__":
    sys.exit(main())
