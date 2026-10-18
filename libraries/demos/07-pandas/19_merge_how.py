from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv")

artists = pd.read_csv(DATA / "artists.csv")
for how in ("inner", "left", "right", "outer"):
    merged = tracks.merge(artists, on="artist", how=how)
    print(f"{how}: {len(merged)} rows")
outer = tracks.merge(artists, on="artist", how="outer", indicator=True)
print(outer.loc[outer["_merge"] != "both", ["title", "artist", "_merge"]])

# A small join makes unmatched keys visible.
tracks = pd.DataFrame({"title": ["Imagine", "Yesterday", "Respect"],
                       "artist": ["John Lennon", "The Beatles", "Aretha Franklin"]})
artists = pd.DataFrame({"artist": ["The Beatles", "Aretha Franklin", "Fleetwood Mac"],
                        "country": ["UK", "USA", "UK"]})
inner = tracks.merge(artists, on="artist", how="inner")
print(len(inner))
left = tracks.merge(artists, on="artist", how="left")
print(len(left))
right = tracks.merge(artists, on="artist", how="right")
print(len(right))
outer = tracks.merge(artists, on="artist", how="outer")
print(len(outer))
