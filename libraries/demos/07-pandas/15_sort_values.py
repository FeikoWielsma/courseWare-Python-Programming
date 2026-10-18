from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

print(tracks.sort_values("plays", ascending=False)[["plays"]].head(3))
print(tracks.sort_values(["genre", "plays"], ascending=[True, False])
      [["genre", "plays"]].head(4))
print(tracks.nlargest(3, "plays")[["plays"]])
print(tracks.nsmallest(2, "duration_s")[["duration_s"]])
print(tracks.sort_index()[["plays"]].head(2))
