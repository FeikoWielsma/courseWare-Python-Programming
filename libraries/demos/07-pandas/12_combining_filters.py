from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

mask = (tracks["plays"] >= 50) & (tracks["duration_s"] < 240)
print(tracks[mask][["duration_s", "plays"]].head(4))
print(tracks[tracks["genre"].isin(["Soul", "Country"])][["genre"]].head(4))
print(tracks[tracks["year"].between(1980, 1999)][["year"]].head(4))
print(tracks[~tracks["genre"].isin(["Rock", "Pop"])][["genre"]].head(4))
