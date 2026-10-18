from pathlib import Path
from typing import Annotated

import typer
from library_check import DATA, build_table, find_issues, load
from rich.console import Console

app = typer.Typer(add_completion=False)


@app.command()
def report(
    source: Annotated[
        Path, typer.Argument(help="CSV import to inspect.")
    ] = DATA / "tracks-import.csv",
    strict: Annotated[bool, typer.Option("--strict", help="Exit 1 when issues are found.")] = False,
) -> None:
    """Report missing durations and duplicate titles."""
    try:
        rows = load(source)
    except OSError as error:
        Console(stderr=True).print(f"library_check: {error}")
        raise typer.Exit(code=2) from error
    issues = find_issues(rows)
    Console().print(build_table(issues))
    print(f"{len(rows)} records, {len(issues)} issues")
    if strict and issues:
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
