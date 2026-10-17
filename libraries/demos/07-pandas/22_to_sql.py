import sqlite3
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv")
sites = pd.read_csv(DATA / "sites.csv")

conn = sqlite3.connect(DATA / "pandas-demo.db")

# if_exists='replace' drops and recreates; 'append' adds rows; 'fail', the
# default, raises rather than touch an existing table.
servers.to_sql("servers", conn, if_exists="replace", index=False)
sites.to_sql("sites", conn, if_exists="replace", index=False)
conn.commit()
print(len(servers), "servers and", len(sites), "sites written")

# The types pandas chose for the columns.
print(pd.read_sql("PRAGMA table_info(servers)", conn)[["name", "type"]].to_string())

# The round trip is the point : a summary computed in pandas can be stored back
# as a table for something else to query.
per_site = servers.groupby("site", as_index=False).agg(
    servers=("hostname", "count"), total_cores=("cpu_cores", "sum")
)
per_site.to_sql("site_summary", conn, if_exists="replace", index=False)
conn.commit()

print(pd.read_sql("SELECT * FROM site_summary ORDER BY total_cores DESC", conn))

# The join can be done on either side of the fence.
query = """
SELECT s.hostname, s.role, t.city
FROM servers AS s JOIN sites AS t ON s.site = t.site
ORDER BY t.city, s.hostname LIMIT 5
"""
print(pd.read_sql(query, conn))

conn.close()
