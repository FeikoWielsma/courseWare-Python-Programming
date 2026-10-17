from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv", index_col="hostname")

# The comparison is the interesting half. One True or False per row, aligned
# to the index, and a value like any other.
big = servers["memory_gb"] >= 64
print(big)

print(servers[big])

# Usually written in one line.
print(servers[servers["disk_gb"] > 1000][["site", "role", "disk_gb"]])

# A mask is a Series of booleans, so summing it counts the matches.
print(int(big.sum()), "of", len(servers))

print(servers[servers["role"] == "web"][["site", "os"]])
