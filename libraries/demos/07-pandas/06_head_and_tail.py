from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

print(tracks[["genre", "plays"]].head(2))
print(tracks[["genre", "plays"]].tail(2))
print(tracks[["genre", "plays"]].sample(3, random_state=0))
