import csv
import sys
import time
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.progress import track
from rich.table import Table

DATA = Path(__file__).resolve().parents[2] / "data"

console = Console()
app = typer.Typer(add_completion=False, help="Report disk usage across the estate.")


def load(site: str | None) -> list[dict[str, str]]:
    with (DATA / "servers.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return [row for row in rows if site is None or row["site"] == site]


def usage(server: dict[str, str]) -> float | None:
    if not server["used_gb"]:
        return None
    return float(server["used_gb"]) / float(server["disk_gb"])


@app.command()
def report(
    site: Annotated[str | None, typer.Option("--site", "-s", help="Restrict to one site.")] = None,
    threshold: Annotated[
        int, typer.Option("--threshold", "-t", help="Percent that counts as alarming.")
    ] = 85,
) -> None:
    servers = load(site)
    if not servers:
        console.print(f"[red]no hosts at site[/] {site}")
        raise typer.Exit(code=2)

    table = Table(title=f"Disk usage{f' at {site}' if site else ''}", header_style="bold magenta")
    table.add_column("Host", style="cyan", no_wrap=True)
    table.add_column("Site", justify="center")
    table.add_column("Disk GB", justify="right")
    table.add_column("Used", justify="right")

    alarming: int = 0
    # Step 8 :
    for server in track(servers, description="Checking", console=console):
        time.sleep(0.15)
        fraction = usage(server)
        if fraction is None:
            cell = "[dim italic]no data[/]"
        else:
            over = fraction * 100 >= threshold
            alarming += int(over)
            cell = f"[{'bold red' if over else 'green'}]{fraction:.0%}[/]"
        table.add_row(server["hostname"], server["site"], f"{float(server['disk_gb']):,.0f}", cell)

    console.print(table)
    console.print(f"{alarming} host(s) at or over {threshold}%")

    # A real tool reports failure through its exit code, not only on screen.
    if alarming:
        raise typer.Exit(code=1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        app()
    else:
        # No arguments : show the generated help, then a real run, so that the
        # file still demonstrates something when it is run unattended.
        console.rule("[bold cyan]$ health_cli --help")
        app(args=["--help"], prog_name="health_cli", standalone_mode=False)
        console.rule("[bold cyan]$ health_cli --site AMS --threshold 70")
        app(args=["--site", "AMS", "-t", "70"], prog_name="health_cli", standalone_mode=False)
