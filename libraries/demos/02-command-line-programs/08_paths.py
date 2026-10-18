import argparse
import csv
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"


def load(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

parser = argparse.ArgumentParser()
parser.add_argument("file", type=Path, nargs="?", default=DATA / "tracks.csv")
args = parser.parse_args()
if not args.file.is_file():
    print(f"Missing file: {args.file}", file=sys.stderr)
    raise SystemExit(2)
print(f"{args.file.name}: {len(load(args.file))} tracks")
