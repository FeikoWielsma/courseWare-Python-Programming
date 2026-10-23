import sqlite3
import sys
from pathlib import Path

import pandas as pd
import plotly.express as px

DATA = Path(__file__).resolve().parents[2] / "data"

if not (DATA / "sensors.db").exists():
    sys.exit("Run 03_store_in_sqlite.py first to create sensors.db")

connection = sqlite3.connect(DATA / "sensors.db")
readings = pd.read_sql(
    "SELECT entity_id, time, value FROM readings WHERE entity_id LIKE '%temperature'",
    connection, parse_dates=["time"],
)
connection.close()

figure = px.line(readings, x="time", y="value", color="entity_id", title="Temperature")
figure.update_layout(yaxis_title="°C")
figure.write_html(DATA / "temperature-chart.html")
print("Open", DATA / "temperature-chart.html")
