from pathlib import Path

import numpy as np

DATA = Path(__file__).resolve().parents[2] / "data"
plays = np.loadtxt(DATA / "plays-hourly.csv", delimiter=",", skiprows=1,
                   usecols=range(1, 25), dtype=int)

print(plays.sum(), plays.mean().round(2))
print(plays.min(), plays.max(), plays.std().round(2))
print(np.median(plays), np.percentile(plays, 95))
day, hour = np.unravel_index(np.argmax(plays), plays.shape)
print(f"peak: day {day}, hour {hour:02d}")
