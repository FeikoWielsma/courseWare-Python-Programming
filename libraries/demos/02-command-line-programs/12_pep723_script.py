# /// script
# requires-python = ">=3.12"
# dependencies = ["rich>=13.9"]
# ///

# On Linux and macOS: chmod +x 12_pep723_script.py && ./12_pep723_script.py

import argparse
from collections import Counter
from pathlib import Path

from rich.console import Console
from rich.table import Table

DATA = Path(__file__).resolve().parents[2] / "data"

LEVEL_COLOURS = {"INFO": "green", "WARN": "yellow", "ERROR": "red"}


def count_levels(path: Path) -> Counter[str]:
    return Counter(line.split()[2] for line in path.read_text(encoding="utf-8").splitlines())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Summarise a log file as a table.")
    parser.add_argument("logfile", type=Path, nargs="?", default=DATA / "listening.log")
    args = parser.parse_args(argv)

    table = Table(title=f"Levels in {args.logfile.name}")
    table.add_column("Level")
    table.add_column("Lines", justify="right")
    for level, count in count_levels(args.logfile).most_common():
        table.add_row(f"[{LEVEL_COLOURS.get(level, 'white')}]{level}[/]", str(count))

    Console().print(table)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
