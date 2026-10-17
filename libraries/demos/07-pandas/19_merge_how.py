from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv")
sites = pd.read_csv(DATA / "sites.csv")

# vpn01 sits at site BRU, which is not in sites.csv. Site GRQ is in sites.csv
# but has no servers. Those two rows are what how= is about.
for how in ("inner", "left", "right", "outer"):
    merged = servers.merge(sites, on="site", how=how)
    print(f"how={how:<6} rows={len(merged):>2}")

left = servers.merge(sites, on="site", how="left")
print(left[left["city"].isna()][["hostname", "site", "city", "tier"]])

outer = servers.merge(sites, on="site", how="outer", indicator=True)
print(outer[outer["_merge"] != "both"][["hostname", "site", "city", "_merge"]])

# indicator=True is the fastest way to answer "did my join lose rows?", which
# is the question worth asking every single time.
print(outer["_merge"].value_counts())
