from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title",
                     parse_dates=["last_played"])
print(tracks[["artist", "duration_s", "last_played"]].head(3))
