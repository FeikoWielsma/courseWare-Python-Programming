from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv", index_col="hostname")

print(servers.iloc[0, 4])
print(servers.iloc[:3, :4])
print(servers.iloc[-2:, :4])

# An integer slice stops before its end, exactly like a list slice, which is
# the opposite of what loc does.
print(servers.iloc[1:3, :4])

print(servers.iloc[[0, 5, 2], [0, 1]])

# The same cell, reached both ways.
print(servers.loc["db01", "memory_gb"], servers.iloc[2, 4])
