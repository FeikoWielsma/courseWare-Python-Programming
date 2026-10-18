from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", parse_dates=["last_played"])

tracks.info()
print(tracks[["duration_s", "plays"]].describe().round(1))
