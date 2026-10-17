import csv
import sys
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

DATA = Path(__file__).resolve().parents[2] / "data"
console = Console()

# There is no parser, no add_argument, no parse_args and no dest= to spell twice.
app = typer.Typer(help="Query the server inventory.", add_completion=False)


def load() -> list[dict[str, str]]:
    with (DATA / "servers.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


@app.command("list")
def list_hosts(
    site: Annotated[str | None, typer.Option("--site", "-s", help="Filter by site code.")] = None,
    limit: Annotated[int, typer.Option("--limit", "-n", help="Rows to show.")] = 20,
) -> None:
    rows = [row for row in load() if site is None or row["site"] == site]
    table = Table(title=f"Hosts{f' at {site}' if site else ''}", header_style="bold magenta")
    for column in ("Host", "Site", "Role", "OS"):
        table.add_column(column)
    for row in rows[:limit]:
        table.add_row(row["hostname"], row["site"], row["role"], row["os"])
    console.print(table)


@app.command()
def show(
    hostname: Annotated[str, typer.Argument(help="The host to describe.")],
) -> None:
    matches = [row for row in load() if row["hostname"] == hostname]
    if not matches:
        # typer.Exit carries the exit code, so a CLI still behaves in a
        # pipeline without main() having to thread a return value out.
        console.print(f"[red]no such host:[/] {hostname}")
        raise typer.Exit(code=1)
    console.print(matches[0])


def tour() -> None:
    for argv in (["--help"], ["list", "--site", "AMS"], ["show", "db01"]):
        console.rule(f"[bold cyan]$ inventory {' '.join(argv)}")
        # standalone_mode=False stops typer calling sys.exit between runs.
        app(args=argv, prog_name="inventory", standalone_mode=False)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        app()
    else:
        tour()
