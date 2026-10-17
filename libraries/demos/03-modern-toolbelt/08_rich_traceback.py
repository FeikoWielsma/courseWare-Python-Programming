import csv
from pathlib import Path

from rich.console import Console

# rich.traceback.install() replaces the interpreter's traceback handler for the whole
# process, so every uncaught exception from here on is rendered by rich.

DATA = Path(__file__).resolve().parents[2] / "data"
console = Console()


def parse_patch_date(row: dict[str, str]) -> tuple[int, int, int]:
    year, month, day = row["last_patched"].split("-")
    return int(year), int(month), int(day)


def oldest_patch() -> tuple[int, int, int]:
    with (DATA / "servers.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return min(parse_patch_date(row) for row in rows)


def main() -> None:
    console.rule("[bold]A traceback you can actually read")
    try:
        console.print(oldest_patch())
    except ValueError:
        console.print_exception(show_locals=True, max_frames=4)

    console.print(
        "\n[yellow]db02 has an empty last_patched field.[/] "
        "The locals panel names the row without adding a single print()."
    )


if __name__ == "__main__":
    main()
