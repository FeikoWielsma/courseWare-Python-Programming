"""The server inventory as a browser data app, for comparison with tkinter demo 05.

Not part of the course environment. Install it first :

    uv pip install streamlit
    streamlit run reference/gui/inventory_streamlit.py

It opens a browser tab rather than a window. Note that there is no event loop,
no callbacks and no widget objects to keep hold of: the script runs top to
bottom again on every interaction, and each widget call returns its current
value. That is the whole model.
"""

from pathlib import Path

import pandas as pd
import streamlit as st

DATA = Path(__file__).resolve().parents[2] / "data"

st.set_page_config(page_title="Server inventory", layout="wide")
st.title("Server inventory")


@st.cache_data
def load() -> pd.DataFrame:
    """cache_data stops the CSV being re-read on every single interaction."""
    frame = pd.read_csv(DATA / "servers.csv")
    frame["used_pct"] = (frame["used_gb"] / frame["disk_gb"] * 100).round(1)
    return frame


servers = load()

# Sidebar widgets. Each call returns the value the user has chosen, right now.
with st.sidebar:
    st.header("Filters")
    sites = st.multiselect("Site", sorted(servers["site"].unique()))
    threshold = st.slider("Minimum disk used (%)", 0, 100, 0)

view = servers
if sites:
    view = view[view["site"].isin(sites)]
view = view[view["used_pct"].fillna(0) >= threshold]

left, right = st.columns([3, 1])
with left:
    st.subheader("Hosts")
    # A DataFrame renders as a sortable, scrollable, resizable table with no
    # further work. This is the line that sells Streamlit to data people.
    st.dataframe(
        view,
        use_container_width=True,
        hide_index=True,
        column_config={
            "used_pct": st.column_config.ProgressColumn(
                "Used", format="%.1f%%", min_value=0, max_value=100
            )
        },
    )
with right:
    st.subheader("Totals")
    st.metric("Hosts shown", len(view))
    st.metric("Disk TB", f"{view['disk_gb'].sum() / 1000:.1f}")
    st.metric("Fullest", f"{view['used_pct'].max():.0f}%")

st.subheader("Disk used by site")
st.bar_chart(view.groupby("site")["disk_gb"].sum())
