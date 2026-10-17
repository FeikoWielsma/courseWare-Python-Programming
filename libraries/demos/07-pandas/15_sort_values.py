from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"
COLUMNS = ["site", "role", "disk_gb", "used_gb"]

servers = pd.read_csv(DATA / "servers.csv", index_col="hostname")

print(servers.sort_values("disk_gb", ascending=False)[COLUMNS].head(4))

# Several keys, with a direction for each. The list of booleans lines up with
# the list of column names.
print(servers.sort_values(["site", "disk_gb"], ascending=[True, False])[COLUMNS].head(6))

# sort_values returns a new frame; the original is untouched.
print(servers[COLUMNS].head(2))

# nlargest is sort plus head, and says what it means.
print(servers.nlargest(3, "used_gb")[COLUMNS])

# print(servers.sort_index()[COLUMNS].head(4))
