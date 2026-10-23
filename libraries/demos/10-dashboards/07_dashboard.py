# INTERACTIVE : start it with `uv run streamlit run demos/10-dashboards/07_dashboard.py`

import sqlite3
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATABASE = Path(__file__).resolve().parents[2] / "data" / "sensors.db"
SENSORS = [
    "sensor.living_room_temperature", "sensor.outdoor_temperature",
    "sensor.living_room_humidity",
]


@st.cache_data(ttl="10m")
def load_readings(entity_id: str) -> pd.DataFrame:
    connection = sqlite3.connect(DATABASE)
    readings = pd.read_sql(
        "SELECT time, value FROM readings WHERE entity_id = ?", connection,
        params=(entity_id,), parse_dates=["time"],
    )
    connection.close()
    return readings


st.title("Home sensors")
if not DATABASE.exists():
    st.error("Run 03_store_in_sqlite.py first to create sensors.db")
    st.stop()

entity_id = st.selectbox("Sensor", SENSORS)
days = st.slider("Days", min_value=1, max_value=28, value=7)

readings = load_readings(entity_id)
recent = readings[readings["time"] > readings["time"].max() - pd.Timedelta(days=days)]

latest, lowest, highest = st.columns(3)
latest.metric("Latest", f"{recent['value'].iloc[-1]:.1f}")
lowest.metric("Lowest", f"{recent['value'].min():.1f}")
highest.metric("Highest", f"{recent['value'].max():.1f}")
st.plotly_chart(px.line(recent, x="time", y="value"))
