# Exercise 10 : Dashboards and Time Series

Home Assistant keeps detailed sensor states for ten days. In this exercise you keep them for as long as you like : you import a history download into your own SQLite database, summarise it per hour, and show it on a Streamlit dashboard. The readings in `data/sensor-history.csv` are made up, not from a real house, but the file has the same shape as the download from Home Assistant's History page.

Start from `exercises/starters/10-dashboards/`. Copy it to `work/10-dashboards/`, so that the paths in the starter find `data/`, and run everything from `libraries/`. The solution is in `solutions/solution10-dashboards/`.

---

### Step 1 : Read the download

:::task
Write `load_history` in `store.py` : read the CSV file and keep the states that are numbers.
:::

```text
10-dashboards/
    store.py             <- change
    dashboard.py
```

:::hint
The slide *Unavailable Readings* shows the operation used in this step.
:::

Complete this function, and return only the three columns the database needs :

```python
def load_history(path: Path) -> pd.DataFrame:
    """Read a history download and keep the states that are numbers."""
    history = pd.read_csv(path)
    ...
    return history.dropna(subset=["value"])[["entity_id", "last_changed", "value"]]
```

Then call it at the bottom of the file and print the number of readings :

```python
if __name__ == "__main__":
    readings = load_history(DATA / "sensor-history.csv")
    print(len(readings), "readings in the download")
```

```bash
uv run work/10-dashboards/store.py
```

```text
8045 readings in the download
```

:::solution
```python
def load_history(path: Path) -> pd.DataFrame:
    """Read a history download and keep the states that are numbers."""
    history = pd.read_csv(path)
    history["value"] = pd.to_numeric(history["state"], errors="coerce")
    return history.dropna(subset=["value"])[["entity_id", "last_changed", "value"]]
```
:::

---

### Step 2 : Store the readings

:::task
Write `save_readings`, which stores the readings in a `readings` table and returns how many were new.
:::

:::hint
The slide *Storing Readings* shows the table and the insert.
:::

```python
def save_readings(connection: sqlite3.Connection, readings: pd.DataFrame) -> int:
    """Store readings that are not stored yet; return how many were new."""
    ...
```

Create the table if it does not exist, insert the rows with `INSERT OR IGNORE`, commit, and return the `rowcount`. `readings.itertuples(index=False)` gives the rows in the order of the columns. Add this to the bottom of `store.py` :

```python
    connection = sqlite3.connect(DATABASE)
    print(save_readings(connection, readings), "new readings")
    connection.close()
```

Run `store.py` twice. The first run prints `8045 new readings`, the second `0 new readings`. A new download from Home Assistant overlaps the old one, and only the readings that were not stored yet are added.

:::solution
```python
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
```
:::

---

### Step 3 : Hourly statistics

:::task
Write `hourly_statistics`, which returns the mean, lowest and highest value per sensor per hour, and store the result in a `statistics` table.
:::

:::hint
The slide *Querying a Time Range* shows `GROUP BY` on the date and on the hour. The slide *to_sql* of the pandas module writes a DataFrame to a table.
:::

Home Assistant's long-term statistics keep the same three values. It weights the mean by how long each state lasted; for readings every 15 minutes that is the plain average. Complete the query; round the mean to one decimal with `round(avg(value), 1)` :

```python
def hourly_statistics(connection: sqlite3.Connection) -> pd.DataFrame:
    """The mean, lowest and highest value per sensor per hour."""
    query = """
        SELECT entity_id, ... AS hour,
               ... AS mean, ... AS low, ... AS high
        FROM readings
        GROUP BY ...
    """
    return pd.read_sql(query, connection)
```

Store the result with `to_sql`, replacing the table on every run, and print its size before closing the connection :

```python
    statistics = hourly_statistics(connection)
    statistics.to_sql("statistics", connection, if_exists="replace", index=False)
    print(len(statistics), "hourly statistics")
```

```text
8045 readings in the download
0 new readings
2012 hourly statistics
```

Three sensors for 28 days of 24 hours make 2016 rows. Four are missing : the outdoor sensor was unavailable for four hours on 14 September.

:::solution
```python
def hourly_statistics(connection: sqlite3.Connection) -> pd.DataFrame:
    """The mean, lowest and highest value per sensor per hour."""
    query = """
        SELECT entity_id, strftime('%Y-%m-%d %H:00', time) AS hour,
               round(avg(value), 1) AS mean, min(value) AS low, max(value) AS high
        FROM readings
        GROUP BY entity_id, hour
    """
    return pd.read_sql(query, connection)
```
:::

---

### Step 4 : The dashboard

:::task
Show the hourly mean of one sensor in `dashboard.py`, with a box to choose the sensor.
:::

```text
10-dashboards/
    store.py
    dashboard.py         <- change
```

:::hint
The slide *A Streamlit Dashboard* shows a cached loading function, a select box and a chart.
:::

Write `load_statistics(entity_id)` with `@st.cache_data(ttl="10m")`, so that the dashboard shows new readings after the next import. It reads the columns `hour`, `mean`, `low` and `high` of one sensor from the `statistics` table, with `parse_dates=["hour"]`. Below the title, add a `st.selectbox` with the `SENSORS` and a `px.line` chart of `mean` against `hour`.

Start the dashboard :

```bash
uv run streamlit run work/10-dashboards/dashboard.py
```

A browser tab opens with the chart. Choose another sensor; the script runs again and the chart follows. Stop the server with `Ctrl+C`.

:::solution
```python
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
statistics = load_statistics(entity_id)
st.plotly_chart(px.line(statistics, x="hour", y="mean", title=entity_id))
```
:::

---

### Step 5 : Recent days (optional)

:::task
Add a slider for the number of days to show, and the lowest and highest value of that period.
:::

:::hint
The slide *A Streamlit Dashboard* shows `st.slider`, the filter on the last days and `st.metric`.
:::

The lowest value of a period is the lowest of its `low` column, and the highest the highest of its `high` column. With all 28 days of the outdoor sensor the dashboard shows `4.0` and `18.1`.

---

### Try one of these

- Point demo `home_assistant_api` at your own Home Assistant with `--live`, and save the answer with `save_readings`.
- Draw `low`, `mean` and `high` in one chart : `px.line` accepts a list of columns for `y`.
- Use the `statistics` table in Grafana, with its SQLite data source plugin.
