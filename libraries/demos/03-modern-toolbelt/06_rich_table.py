import csv
from pathlib import Path

from rich import box
from rich.console import Console
from rich.table import Table

DATA = Path(__file__).resolve().parents[2] / "data"
console = Console()


def load() -> list[dict[str, str]]:
    with (DATA / "servers.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def usage_style(fraction: float) -> str:
    if fraction >= 0.85:
        return "bold red"
    if fraction >= 0.60:
        return "yellow"
    return "green"


def main() -> None:
    servers: list[dict[str, str]] = load()

    table = Table(
        title="Server inventory",
        box=box.ROUNDED,
        header_style="bold magenta",
        row_styles=["", "dim"],  # zebra striping, free
    )
    # Alignment and width are per column, declared once, and every row obeys.
    table.add_column("Host", style="cyan", no_wrap=True)
    table.add_column("Site", justify="center")
    table.add_column("Role")
    table.add_column("Cores", justify="right")
    table.add_column("Disk GB", justify="right")
    table.add_column("Used", justify="right")

    used_total: float = 0.0
    disk_total: float = 0.0
    for row in servers:
        disk = float(row["disk_gb"])
        disk_total += disk

        # The fixture has one host with no reading. Say so in the cell rather
        # than inventing a zero, which would quietly drag the total down.
        if row["used_gb"]:
            used = float(row["used_gb"])
            used_total += used
            fraction = used / disk
            used_cell = f"[{usage_style(fraction)}]{fraction:.0%}[/]"
        else:
            used_cell = "[dim italic]no data[/]"

        table.add_row(
            row["hostname"],
            row["site"],
            row["role"],
            row["cpu_cores"],
            f"{disk:,.0f}",
            used_cell,
        )

    # show_footer on the table plus footer= on a column gives a totals row.
    table.show_footer = True
    table.columns[0].footer = f"{len(servers)} hosts"
    table.columns[4].footer = f"{disk_total:,.0f}"
    table.columns[5].footer = f"{used_total / disk_total:.0%}"

    console.print(table)


if __name__ == "__main__":
    main()
