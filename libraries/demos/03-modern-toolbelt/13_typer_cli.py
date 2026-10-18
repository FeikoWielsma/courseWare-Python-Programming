import csv
import sys
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

DATA = Path(__file__).resolve().parents[2] / "data"
app = typer.Typer(add_completion=False, help="Query a playlist.")


def load() -> list[dict[str, str]]:
    with (DATA / "tracks.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def show_tracks(genre: str | None, limit: int) -> None:
    rows = [row for row in load() if genre is None or row["genre"] == genre]
    table = Table("Title", "Genre", title="Playlist")
    for row in rows[:limit]:
        table.add_row(row["title"], row["genre"])
    Console().print(table)


@app.command("list")
def list_tracks(
    genre: Annotated[str | None, typer.Option("--genre")] = None,
    limit: Annotated[int, typer.Option("--limit")] = 5,
) -> None:
    """List tracks, optionally filtered by genre."""
    show_tracks(genre, limit)


@app.command()
def stats() -> None:
    """Count tracks and fictional plays."""
    rows = load()
    Console().print({"tracks": len(rows), "plays": sum(int(row["plays"]) for row in rows)})


@app.command()
def top(limit: int = 5) -> None:
    """List the most-played tracks."""
    for row in sorted(load(), key=lambda row: int(row["plays"]), reverse=True)[:limit]:
        Console().print(f"{row['title']}: {row['plays']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        app()
    else:
        for args in (["list", "--genre", "Soul"], ["stats"], ["top", "--limit", "3"]):
            app(args=args, standalone_mode=False)
