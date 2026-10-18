import csv
import time
from pathlib import Path

from tqdm import tqdm

DATA = Path(__file__).resolve().parents[2] / "data"
with (DATA / "tracks.csv").open(encoding="utf-8", newline="") as handle:
    tracks: list[dict[str, str]] = list(csv.DictReader(handle))

with tqdm(total=len(tracks), desc="Converting", unit="track") as bar:
    for track in tracks:
        time.sleep(0.01)
        bar.update(1)
        bar.set_postfix(title=track["title"][:12])
