from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

print(tracks["plays"].head(3))
print(tracks[["plays"]].head(3))
print(tracks[["genre", "artist", "duration_s"]].head(3))
