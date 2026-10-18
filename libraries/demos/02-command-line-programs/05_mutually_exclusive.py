import argparse
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"


def load(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

parser = argparse.ArgumentParser(prog="playlist")
parser.add_argument("file", type=Path, nargs="?", default=DATA / "tracks.csv")
order = parser.add_mutually_exclusive_group()
order.add_argument("--longest", action="store_true")
order.add_argument("--shortest", action="store_true")
args = parser.parse_args()
rows = sorted(load(args.file), key=lambda row: int(row["duration_s"]),
              reverse=not args.shortest)
for row in rows[:3]:
    print(f"{row['title']}: {row['duration_s']} s")
