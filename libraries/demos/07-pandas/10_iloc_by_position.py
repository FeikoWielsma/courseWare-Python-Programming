from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

print(tracks.iloc[0, 3])
print(tracks.iloc[:3, :2])
print(tracks.iloc[-2:, :2])
print(tracks.iloc[[0, 5, 2], [0, 1]])

# Compare labels and positions on a three-row sample.
frame = tracks.iloc[:3][["genre", "plays"]]
print(frame.loc["Yesterday", "plays"])
print(frame.iloc[0, 1])
print(frame.loc["Imagine":"Yesterday", ["plays"]])
