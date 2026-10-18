from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

print(tracks.isna().sum())
print(tracks.loc[tracks["last_played"].isna(), ["artist", "last_played"]])
print(len(tracks.dropna(subset=["last_played"])))
filled = tracks.fillna({"last_played": "never"})
print(filled.loc["Hey Jude", "last_played"])
