import csv
import time
from pathlib import Path

from rich.progress import Progress, track

DATA = Path(__file__).resolve().parents[2] / "data"
with (DATA / "tracks.csv").open(encoding="utf-8", newline="") as handle:
    tracks: list[dict[str, str]] = list(csv.DictReader(handle))

for _song in track(tracks[:3], description="Converting"):
    time.sleep(0.02)
with Progress() as progress:
    task = progress.add_task("Preparing playlist", total=3)
    for _ in range(3):
        time.sleep(0.02)
        progress.update(task, advance=1)
