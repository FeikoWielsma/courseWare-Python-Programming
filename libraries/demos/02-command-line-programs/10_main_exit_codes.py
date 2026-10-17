import argparse
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"

OK = 0  # nothing to report
FOUND = 1  # ran fine, but the answer is "yes, there are problems"
TROUBLE = 2  # could not do the job at all


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Report errors in a log file.")
    parser.add_argument("logfile", type=Path, help="the log file to check")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if not args.logfile.is_file():
        print(f"no such file: {args.logfile}", file=sys.stderr)
        return TROUBLE

    errors = [
        line for line in args.logfile.read_text(encoding="utf-8").splitlines() if " ERROR " in line
    ]
    for line in errors:
        print(line)
    return FOUND if errors else OK


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # SystemExit(int) is how a Python program chooses its exit status.
        raise SystemExit(main())

    # Run bare, the demo calls main itself so the codes can be shown side by side.
    for sample in ([str(DATA / "cli-sample.log")], [str(DATA / "absent.log")]):
        print(f"$ logcheck {Path(sample[0]).name}")
        print(f"[exit status {main(sample)}]\n")
