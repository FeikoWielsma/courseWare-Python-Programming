import csv
from pathlib import Path

from tqdm import tqdm

DATA = Path(__file__).resolve().parents[2] / "data"
with (DATA / "tracks.csv").open(encoding="utf-8", newline="") as handle:
    tracks: list[dict[str, str]] = list(csv.DictReader(handle))

for track in tqdm(tracks, desc="Checking"):
    if not track["last_played"]:
        tqdm.write(f"Never played: {track['title']}")
