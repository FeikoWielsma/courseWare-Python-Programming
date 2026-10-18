import csv
import time
from pathlib import Path

from tqdm import tqdm

DATA = Path(__file__).resolve().parents[2] / "data"
with (DATA / "tracks.csv").open(encoding="utf-8", newline="") as handle:
    tracks: list[dict[str, str]] = list(csv.DictReader(handle))

for _track in tqdm(tracks, desc="Converting", unit="track"):
    time.sleep(0.01)  # Simulated conversion; no audio files are read.
print(f"Converted {len(tracks)} track records")
rows = (track for track in tracks)
for _track in tqdm(rows, total=len(tracks), desc="From a generator"):
    pass
