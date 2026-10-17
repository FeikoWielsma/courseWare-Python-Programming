import csv
import time
from pathlib import Path

from rich.console import Console
from rich.table import Table
from tqdm import tqdm

# The exercise puts health.py at the top of the tree, where this would be
# parent / "data". This solution lives two levels down, hence parents[2].
DATA = Path(__file__).resolve().parents[2] / "data"

WARNING_AT: float = 0.60
FULL_AT: float = 0.85

console = Console()


def load() -> list[dict[str, str]]:
    with (DATA / "servers.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def usage(server: dict[str, str]) -> float | None:
    if not server["used_gb"]:
        return None
    return float(server["used_gb"]) / float(server["disk_gb"])


def check(server: dict[str, str]) -> str:
    time.sleep(0.2)
    fraction = usage(server)
    if fraction is None:
        return "unknown"
    if fraction >= FULL_AT:
        return "full"
    if fraction >= WARNING_AT:
        return "warning"
    return "ok"


STYLES: dict[str, str] = {
    "ok": "green",
    "warning": "yellow",
    "full": "bold red",
    "unknown": "dim italic",
}


def build_table(rows: list[tuple[dict[str, str], str]]) -> Table:
    table = Table(title="Disk usage", header_style="bold magenta", row_styles=["", "dim"])
    table.add_column("Host", style="cyan", no_wrap=True)
    table.add_column("Site", justify="center")
    table.add_column("Disk GB", justify="right")
    table.add_column("Used", justify="right")
    table.add_column("State", justify="center")

    disk_total: float = 0.0
    used_total: float = 0.0
    for server, state in rows:
        disk = float(server["disk_gb"])
        disk_total += disk
        fraction = usage(server)
        if fraction is None:
            used_cell = "[dim italic]no data[/]"
        else:
            used_total += fraction * disk
            used_cell = f"[{STYLES[state]}]{fraction:.0%}[/]"
        table.add_row(
            server["hostname"],
            server["site"],
            f"{disk:,.0f}",
            used_cell,
            f"[{STYLES[state]}]{state}[/]",
        )

    table.show_footer = True
    table.columns[0].footer = f"{len(rows)} hosts"
    table.columns[2].footer = f"{disk_total:,.0f}"
    table.columns[3].footer = f"{used_total / disk_total:.0%}"
    return table


def main() -> None:
    servers: list[dict[str, str]] = load()
    console.print(f"Loaded [bold]{len(servers)}[/] hosts")

    results: list[tuple[dict[str, str], str]] = []
    for server in tqdm(servers, desc="Checking", unit="host"):
        state = check(server)
        results.append((server, state))
        if state != "ok":
            # Step 4 : tqdm.write clears the bar, prints, and repaints it.
            # A bare print() here leaves a trail of half-drawn bars instead.
            fraction = usage(server)
            measured = "no reading" if fraction is None else f"{fraction:.0%} used"
            tqdm.write(f"  {server['hostname']:<9} {measured}")

    # Step 6 : sort worst first, because that is the part anybody reads.
    # Unmeasured hosts sort to the top rather than being hidden at the bottom.
    results.sort(key=lambda pair: (usage(pair[0]) is not None, usage(pair[0]) or 0), reverse=True)

    console.print(build_table(results))


if __name__ == "__main__":
    main()
