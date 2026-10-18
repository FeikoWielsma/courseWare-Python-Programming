import csv
import os
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"


def load(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

def emit(path: Path) -> None:
    print(f"Reading {path.name}", file=sys.stderr)
    for row in load(path):
        print(row["title"])
    print("Finished", file=sys.stderr)


if __name__ == "__main__":
    try:
        emit(DATA / "tracks.csv")
    except BrokenPipeError:
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
