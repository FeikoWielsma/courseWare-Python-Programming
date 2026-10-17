from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv")
print(servers.head(2))

servers = pd.read_csv(DATA / "servers.csv", index_col="hostname")
print(servers.head(2))
