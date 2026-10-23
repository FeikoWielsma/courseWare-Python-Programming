import sqlite3
import sys
from pathlib import Path

import pandas as pd

DATABASE = Path(__file__).resolve().parents[2] / "data" / "sensors.db"

if not DATABASE.exists():
    sys.exit("Run 03_store_in_sqlite.py first to create sensors.db")

query = """
    SELECT date(time) AS day, min(value) AS low, max(value) AS high
    FROM readings
    WHERE entity_id = ? AND time >= ? AND time < ?
    GROUP BY day
"""
connection = sqlite3.connect(DATABASE)
week = pd.read_sql(
    query, connection, params=("sensor.outdoor_temperature", "2026-09-22", "2026-09-29"),
)
connection.close()
print(week)
