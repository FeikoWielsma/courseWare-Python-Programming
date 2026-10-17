import pandas as pd

# Each key becomes a column name, each list a column.
servers = pd.DataFrame(
    {
        "hostname": ["web01", "web02", "db01", "log01"],
        "site": ["AMS", "AMS", "AMS", "EIN"],
        "cpu_cores": [4, 4, 16, 8],
        "memory_gb": [8, 8, 128, 32],
    }
)
print(servers)

print(servers.shape)
print(list(servers.columns))
print(list(servers.index))

# One column is a Series, and it carries the frame's index.
print(servers["memory_gb"])
print(type(servers).__name__, type(servers["memory_gb"]).__name__)
