import argparse
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"


def existing_file(text: str) -> Path:
    path = Path(text).expanduser()
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"{path} is not an existing file")
    return path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Count log lines at one level.")
    # type= takes any callable, so Path itself is a perfectly good converter.
    parser.add_argument(
        "logfile",
        type=existing_file,
        nargs="?",
        default=DATA / "cli-sample.log",
        help="the log file to read (default: the shipped sample)",
    )
    parser.add_argument("--level", default="ERROR", help="the level to count")
    return parser


def main(argv: list[str]) -> None:
    args = build_parser().parse_args(argv)
    path: Path = args.logfile

    # Because it is a Path, it answers questions about itself straight away.
    print(f"file   : {path.name} ({path.suffix or 'no suffix'})")
    print(f"folder : {path.parent}")
    print(f"size   : {path.stat().st_size} bytes")

    lines = path.read_text(encoding="utf-8").splitlines()
    hits = [line for line in lines if f" {args.level} " in line]
    print(f"{len(hits)} of {len(lines)} lines are {args.level}")


if __name__ == "__main__":
    main(sys.argv[1:])
