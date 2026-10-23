import sqlite3
import sys
from pathlib import Path

import pandas as pd

DATABASE = Path(__file__).resolve().parents[2] / "data" / "sensors.db"

if not DATABASE.exists():
    sys.exit("Run 03_store_in_sqlite.py first to create sensors.db")

connection = sqlite3.connect(DATABASE)
readings = pd.read_sql(
    "SELECT time, value FROM readings WHERE entity_id = ?", connection,
    params=("sensor.outdoor_temperature",), parse_dates=["time"], index_col="time",
)
connection.close()

hourly = readings["value"].resample("1h").agg(["mean", "min", "max"]).round(1)
print(len(readings), "readings,", len(hourly), "hours")
print(hourly.loc["2026-09-14 01:00":"2026-09-14 03:00"])
