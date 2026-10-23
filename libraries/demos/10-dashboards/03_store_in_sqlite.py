import sqlite3
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

history = pd.read_csv(DATA / "sensor-history.csv")
history["value"] = pd.to_numeric(history["state"], errors="coerce")
readings = history.dropna(subset=["value"])
rows = readings[["entity_id", "last_changed", "value"]].itertuples(index=False)

connection = sqlite3.connect(DATA / "sensors.db")
connection.execute("""
    CREATE TABLE IF NOT EXISTS readings (
        entity_id TEXT NOT NULL,
        time TEXT NOT NULL,
        value REAL NOT NULL,
        PRIMARY KEY (entity_id, time)
    )
""")
inserted = connection.executemany("INSERT OR IGNORE INTO readings VALUES (?, ?, ?)", rows)
connection.commit()
print(inserted.rowcount, "new readings")

total = connection.execute("SELECT count(*) FROM readings").fetchone()[0]
print(total, "readings stored")
connection.close()
