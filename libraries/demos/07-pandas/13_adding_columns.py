from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

tracks["available"] = True
tracks["listened_s"] = tracks["duration_s"] * tracks["plays"]
report = tracks.assign(minutes=tracks["listened_s"] / 60)
print(report[["plays", "minutes"]].head(3).round(1))
print(tracks.drop(columns=["available"]).columns.tolist())
