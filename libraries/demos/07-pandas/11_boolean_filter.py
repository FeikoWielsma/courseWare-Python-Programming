from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

popular = tracks["plays"] >= 50
print(tracks[popular][["genre", "plays"]].head(4))
print(int(popular.sum()))
print(tracks[tracks["genre"] == "Soul"][["plays"]])
