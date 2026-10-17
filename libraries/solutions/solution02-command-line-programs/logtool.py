# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///


import argparse
import sys
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"
DEFAULT_LOG = DATA / "cli-sample.log"

OK = 0  # the job was done and there is nothing to report
FOUND = 1  # the job was done and the answer is "yes, there are errors"
TROUBLE = 2  # the job could not be done at all


def read_lines(path: Path) -> list[str]:
    if str(path) == "-":
        return sys.stdin.read().splitlines()
    return path.read_text(encoding="utf-8").splitlines()


def cmd_count(args: argparse.Namespace) -> int:
    counts = Counter(line.split()[2] for line in read_lines(args.logfile))
    if not args.quiet:
        for level, count in counts.most_common():
            print(f"{level:<6}{count}")
    return OK


def cmd_errors(args: argparse.Namespace) -> int:
    matches = [line for line in read_lines(args.logfile) if f" {args.level} " in line]
    if not args.quiet:
        for line in matches:
            print(line)
    return FOUND if matches else OK


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="logtool", description="Summarise and search a log file.")
    # Options shared by both verbs are declared once, on a parent parser.
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "logfile",
        type=Path,
        nargs="?",
        default=DEFAULT_LOG,
        help="the log file to read, or - for standard input",
    )
    common.add_argument("-q", "--quiet", action="store_true", help="set the status, print nothing")

    verbs = parser.add_subparsers(dest="command", metavar="COMMAND")

    counting = verbs.add_parser("count", parents=[common], help="count the lines per level")
    counting.set_defaults(handler=cmd_count)

    errors = verbs.add_parser("errors", parents=[common], help="show the lines at one level")
    errors.add_argument("--level", default="ERROR", help="the level to look for")
    errors.set_defaults(handler=cmd_errors)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    # Run with no verb at all, the tool explains itself rather than failing.
    if args.command is None:
        parser.print_help()
        return OK

    try:
        return args.handler(args)
    except OSError as error:
        # The reason goes to stderr so that a pipeline downstream sees only data.
        print(f"logtool: {error.strerror}: {args.logfile}", file=sys.stderr)
        return TROUBLE


if __name__ == "__main__":
    raise SystemExit(main())
