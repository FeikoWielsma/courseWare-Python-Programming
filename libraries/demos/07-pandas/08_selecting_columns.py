from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv", index_col="hostname")

print(type(servers["memory_gb"]).__name__)
print(servers["memory_gb"].head(3))

# Note the double brackets. The inner pair is an ordinary list of column names;
# the outer pair is the selection.
print(type(servers[["site", "role", "memory_gb"]]).__name__)
print(servers[["site", "role", "memory_gb"]].head(3))

print(type(servers[["memory_gb"]]).__name__)

# Selecting with a list also reorders, which is how a report gets the columns
# in the order the reader expects.
print(servers[["role", "site", "disk_gb", "cpu_cores"]].head(3))
