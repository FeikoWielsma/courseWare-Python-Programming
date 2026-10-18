import csv
from pathlib import Path

from rich.console import Console
from rich.table import Table

DATA = Path(__file__).resolve().parents[2] / "data"
with (DATA / "tracks.csv").open(encoding="utf-8", newline="") as handle:
    tracks: list[dict[str, str]] = list(csv.DictReader(handle))

table = Table(title="Top tracks", row_styles=["", "dim"])
table.add_column("Title", style="cyan")
table.add_column("Plays", justify="right")
for track in sorted(tracks, key=lambda row: int(row["plays"]), reverse=True)[:5]:
    table.add_row(track["title"], track["plays"])
table.show_footer = True
table.columns[0].footer = "Shown"
table.columns[1].footer = "5"
Console().print(table)
