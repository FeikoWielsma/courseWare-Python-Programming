import argparse
import csv
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"


def load(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

def cmd_list(args: argparse.Namespace) -> int:
    rows = [row for row in load(args.file) if args.genre is None or row["genre"] == args.genre]
    for row in rows[:args.limit]:
        print(f"{row['title']}: {row['genre']}")
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    rows = load(args.file)
    print(f"{len(rows)} tracks, {sum(int(row['plays']) for row in rows)} fictional plays")
    return 0


def cmd_top(args: argparse.Namespace) -> int:
    rows = sorted(load(args.file), key=lambda row: int(row["plays"]), reverse=True)
    for row in rows[:args.limit]:
        print(f"{row['title']}: {row['plays']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="playlist")
    parser.add_argument("--file", type=Path, default=DATA / "tracks.csv")
    verbs = parser.add_subparsers(dest="command", required=True)
    listing = verbs.add_parser("list", help="list tracks")
    listing.add_argument("--genre")
    listing.add_argument("--limit", type=int, default=5)
    listing.set_defaults(handler=cmd_list)
    stats = verbs.add_parser("stats", help="count tracks and plays")
    stats.set_defaults(handler=cmd_stats)
    top = verbs.add_parser("top", help="show most-played tracks")
    top.add_argument("--limit", type=int, default=5)
    top.set_defaults(handler=cmd_top)
    return parser


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv)
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:] or ["list", "--genre", "Soul"]))
