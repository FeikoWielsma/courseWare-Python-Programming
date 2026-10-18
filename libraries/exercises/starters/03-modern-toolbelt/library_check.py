import csv
from pathlib import Path

DATA = Path("data")


def load(source: Path) -> list[dict[str, str]]:
    with source.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


# Add validation, progress and the report described in the handout.
