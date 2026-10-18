from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

per_genre = tracks.groupby("genre").agg(
    titles=("artist", "count"),
    total_plays=("plays", "sum"),
    mean_duration=("duration_s", "mean"),
).round(1).reset_index()
print(per_genre)
tracks["decade"] = tracks["year"] // 10 * 10
print(tracks.groupby(["genre", "decade"])["plays"].sum())
