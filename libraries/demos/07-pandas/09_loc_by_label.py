from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

print(tracks.loc["Imagine", "duration_s"])
print(tracks.loc["Imagine", ["artist", "genre"]])
print(tracks.loc["Imagine":"Respect", "year":"plays"])
print(tracks.loc[:, ["genre", "plays"]].head(3))
