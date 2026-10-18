import argparse
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"
VERSION = "1.0"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="logmatch", description="Print the log lines containing a pattern."
    )
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument(
        "logfile",
        type=Path,
        nargs="?",
        default=DATA / "listening.log",
        help="the file to search, or - for standard input",
    )
    parser.add_argument("-c", "--count", action="store_true", help="print the match count only")
    parser.add_argument("-q", "--quiet", action="store_true", help="print nothing, set the status")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return parser


def read_lines(source: Path) -> list[str]:
    if str(source) == "-":
        return sys.stdin.read().splitlines()
    return source.read_text(encoding="utf-8").splitlines()


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        lines = read_lines(args.logfile)
    except OSError as error:
        # The reason goes to stderr, so a pipeline downstream still sees clean data.
        print(f"logmatch: {error.strerror}: {args.logfile}", file=sys.stderr)
        return 2

    matches = [line for line in lines if args.pattern in line]
    if not args.quiet:
        print(len(matches) if args.count else "\n".join(matches))

    # grep's convention: 0 when something was found, 1 when nothing was.
    return 0 if matches else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:] or ["PLAY", "--count"]))
