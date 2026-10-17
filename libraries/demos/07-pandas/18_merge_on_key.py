from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv")
sites = pd.read_csv(DATA / "sites.csv")

print(servers[["hostname", "site", "role"]].head(4))
print(sites)

# on= names the column that exists in both frames. The default join keeps only
# the rows whose key is present on both sides.
joined = servers.merge(sites, on="site")
print(joined[["hostname", "site", "city", "country", "tier"]].head(6))
print(len(joined), "of", len(servers))

# The joined frame is an ordinary frame, so it groups like any other. This is
# the whole point : the lookup column is now available to the summary.
print(joined.groupby("city").size().sort_values(ascending=False))
