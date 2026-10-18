import argparse
import csv
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"


def load(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

parser = argparse.ArgumentParser(prog="playlist", description="List tracks from a CSV.")
parser.add_argument("file", type=Path, nargs="?", default=DATA / "tracks.csv")
parser.add_argument("--genre", choices=["Rock", "Pop", "Soul", "Country", "Electronic"])
parser.add_argument("--limit", type=int, default=5)
parser.add_argument("-v", "--verbose", action="count", default=0)
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()
if args.dry_run:
    print(f"Would read {args.file.name}, up to {args.limit} tracks")
else:
    rows = [row for row in load(args.file) if args.genre is None or row["genre"] == args.genre]
    for row in rows[:args.limit]:
        print(f"{row['title']}: {row['duration_s']} s")
    if args.verbose:
        print(f"{len(rows)} matching tracks", file=sys.stderr)
