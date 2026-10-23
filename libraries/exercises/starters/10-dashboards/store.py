"""Import a Home Assistant history download into SQLite, with hourly statistics."""

import sqlite3
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"
DATABASE = DATA / "home.db"

# Step 1 : write load_history here.

# Step 2 : write save_readings here.

# Step 3 : write hourly_statistics here.


if __name__ == "__main__":
    # Step 1 : load the download and print the number of readings.
    ...
