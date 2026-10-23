"""Home sensors dashboard: run `uv run streamlit run` with the path of this file."""

import sqlite3
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATABASE = Path(__file__).resolve().parents[2] / "data" / "home.db"
SENSORS = [
    "sensor.living_room_temperature", "sensor.outdoor_temperature",
    "sensor.living_room_humidity",
]

# Step 4 : write load_statistics here.


st.title("Home sensors")
