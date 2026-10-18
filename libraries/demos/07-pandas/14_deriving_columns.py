from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

tracks = pd.read_csv(DATA / "tracks.csv", index_col="title")

tracks["initial"] = tracks["artist"].str.upper().str[:1]
tracks["style"] = tracks["genre"].map({"Rock": "guitar", "Pop": "vocal"})
tracks["status"] = np.where(tracks["plays"] > 50, "favourite", "occasional")
tracks.loc[tracks["last_played"].isna(), "status"] = "never"
print(tracks[["initial", "style", "status"]].head(6))
