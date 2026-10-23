"""Import a Home Assistant history download into SQLite, with hourly statistics."""

import sqlite3
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"
DATABASE = DATA / "home.db"


def load_history(path: Path) -> pd.DataFrame:
    """Read a history download and keep the states that are numbers."""
    history = pd.read_csv(path)
    history["value"] = pd.to_numeric(history["state"], errors="coerce")
    return history.dropna(subset=["value"])[["entity_id", "last_changed", "value"]]


def save_readings(connection: sqlite3.Connection, readings: pd.DataFrame) -> int:
    """Store readings that are not stored yet; return how many were new."""
    connection.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            entity_id TEXT NOT NULL,
            time TEXT NOT NULL,
            value REAL NOT NULL,
            PRIMARY KEY (entity_id, time)
        )
    """)
    inserted = connection.executemany(
        "INSERT OR IGNORE INTO readings VALUES (?, ?, ?)", readings.itertuples(index=False),
    )
    connection.commit()
    return inserted.rowcount


def hourly_statistics(connection: sqlite3.Connection) -> pd.DataFrame:
    """The mean, lowest and highest value per sensor per hour."""
    query = """
        SELECT entity_id, strftime('%Y-%m-%d %H:00', time) AS hour,
               round(avg(value), 1) AS mean, min(value) AS low, max(value) AS high
        FROM readings
        GROUP BY entity_id, hour
    """
    return pd.read_sql(query, connection)


if __name__ == "__main__":
    readings = load_history(DATA / "sensor-history.csv")
    print(len(readings), "readings in the download")

    connection = sqlite3.connect(DATABASE)
    print(save_readings(connection, readings), "new readings")

    statistics = hourly_statistics(connection)
    statistics.to_sql("statistics", connection, if_exists="replace", index=False)
    print(len(statistics), "hourly statistics")
    print(statistics.head(3))
    connection.close()
