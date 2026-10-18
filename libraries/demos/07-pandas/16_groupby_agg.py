from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

print(tracks.groupby("genre")["plays"].sum())
print(tracks.groupby("genre")["duration_s"].mean().round(1))
print(tracks.groupby("genre").size())
print(tracks.groupby("genre")["plays"].agg(["count", "sum", "mean", "max"]))
print(tracks.groupby("genre").agg({"plays": "sum", "year": "min"}))

# A small sample keeps every input row visible.
sample = tracks.iloc[:3][["genre", "plays"]]
groups = sample.groupby("genre")
totals = groups["plays"].sum()
print(totals)
