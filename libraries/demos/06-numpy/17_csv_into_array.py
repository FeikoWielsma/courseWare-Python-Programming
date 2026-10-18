from pathlib import Path

import numpy as np

DATA = Path(__file__).resolve().parents[2] / "data"
plays = np.loadtxt(DATA / "plays-hourly.csv", delimiter=",", skiprows=1,
                   usecols=range(1, 25), dtype=int)

print(plays.shape)
print(plays.sum(axis=0))
print(plays.sum(axis=1))
print(int(np.argmax(plays.sum(axis=0))))
np.savetxt(DATA / "plays-hourly-mean.csv", plays.mean(axis=0),
           delimiter=",", fmt="%.2f")
