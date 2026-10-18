import argparse
import csv
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"


def load(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    args = parser.parse_args(argv)
    try:
        rows = load(args.file)
    except OSError as error:
        print(f"playlist: {error}", file=sys.stderr)
        return 2
    print(f"{len(rows)} tracks")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        raise SystemExit(main(sys.argv[1:]))
    for file in (DATA / "tracks.csv", DATA / "missing.csv"):
        print(f"status: {main([str(file)])}")
