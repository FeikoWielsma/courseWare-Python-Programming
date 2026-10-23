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


@st.cache_data(ttl="10m")
def load_statistics(entity_id: str) -> pd.DataFrame:
    connection = sqlite3.connect(DATABASE)
    statistics = pd.read_sql(
        "SELECT hour, mean, low, high FROM statistics WHERE entity_id = ?", connection,
        params=(entity_id,), parse_dates=["hour"],
    )
    connection.close()
    return statistics


st.title("Home sensors")
entity_id = st.selectbox("Sensor", SENSORS)
days = st.slider("Days", min_value=1, max_value=28, value=28)

statistics = load_statistics(entity_id)
recent = statistics[statistics["hour"] > statistics["hour"].max() - pd.Timedelta(days=days)]

lowest, highest = st.columns(2)
lowest.metric("Lowest", f"{recent['low'].min():.1f}")
highest.metric("Highest", f"{recent['high'].max():.1f}")
st.plotly_chart(px.line(recent, x="hour", y="mean", title=entity_id))
