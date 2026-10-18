from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv")

artists = pd.read_csv(DATA / "artists.csv")
joined = tracks.merge(artists, on="artist")
print(joined[["title", "artist", "country"]].head(3))
print(joined.groupby("country")["plays"].sum())
