---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Dashboards and Time Series
language: python
---

# What is a Time Series?

- A time series is a sequence of values, each with a timestamp :
  - A room temperature every 15 minutes
  - The power use of a house every second
- New values arrive all the time; old values do not change
- Most questions select a time range and summarise it :
  - The average per hour
  - The lowest and highest value per day
- Detail matters for recent data, summaries for older data

| time | sensor | value |
| --- | --- | --- |
| `2026-09-01T00:00` | `sensor.outdoor_temperature` | `12.3` |
| `2026-09-01T00:15` | `sensor.outdoor_temperature` | `12.1` |


---

# Home Assistant History

- Home Assistant's recorder stores every state change in a database :
  - SQLite by default, in the file `home-assistant_v2.db`
  - Detailed states are deleted after 10 days, set by `purge_keep_days`
- Sensors with `state_class: measurement` also get long-term statistics :
  - The mean, minimum and maximum per hour, kept indefinitely
  - Energy and water meters keep a running total instead
- The History page downloads the detailed states as a CSV file
- A state is text, so a sensor without a reading reports `unavailable` or `unknown`

```text
entity_id,state,last_changed
sensor.outdoor_temperature,12.3,2026-09-01T00:00:00.000Z
sensor.outdoor_temperature,unavailable,2026-09-14T02:00:00.000Z
```


---

# Reading Sensor History

- `parse_dates` turns the timestamp column into datetimes :
  - The `Z` suffix means UTC, so the values are time-zone aware
- `state` stays text because of the `unavailable` rows

```python
history = pd.read_csv(DATA / "sensor-history.csv", parse_dates=["last_changed"])

print(history.dtypes)
print(history["entity_id"].value_counts())
```

```text
entity_id                       str
state                           str
last_changed    datetime64[us, UTC]

sensor.living_room_humidity       2688
sensor.living_room_temperature    2688
sensor.outdoor_temperature        2688
```

> `demo01 · read_history`


---

# Unavailable Readings

- `pd.to_numeric` converts the text states to numbers
- `errors="coerce"` turns text that is not a number into `NaN`
- `dropna` keeps only the rows with a reading

```python
history["value"] = pd.to_numeric(history["state"], errors="coerce")
print(history[history["value"].isna()]["state"].value_counts())

readings = history.dropna(subset=["value"])
print(len(history), "rows,", len(readings), "readings")
```

```text
state
unavailable    16
unknown         3
8064 rows, 8045 readings
```

> `demo02 · clean_readings`


---

# Storing Readings

- One table holds every sensor, with a primary key on sensor and time :
  - One reading per sensor per moment
- `INSERT OR IGNORE` skips a row whose key is already stored

```python
connection.execute("""
    CREATE TABLE IF NOT EXISTS readings (
        entity_id TEXT NOT NULL,
        time TEXT NOT NULL,
        value REAL NOT NULL,
        PRIMARY KEY (entity_id, time)
    )
""")
inserted = connection.executemany("INSERT OR IGNORE INTO readings VALUES (?, ?, ?)", rows)
connection.commit()
print(inserted.rowcount, "new readings")
```

```text
8045 new readings
8045 readings stored
```

- A second run of the same download prints `0 new readings`

> `demo03 · store_in_sqlite`


---

# Querying a Time Range

- A `WHERE` on the time column selects a range :
  - ISO 8601 timestamps sort in time order as text
- `date(time)` keeps the date part, so `GROUP BY` gives one row per day :
  - `strftime('%Y-%m-%d %H:00', time)` keeps the hour, for one row per hour
- The primary key's index makes the range fast for one sensor

```python
query = """
    SELECT date(time) AS day, min(value) AS low, max(value) AS high
    FROM readings
    WHERE entity_id = ? AND time >= ? AND time < ?
    GROUP BY day
"""
week = pd.read_sql(
    query, connection, params=("sensor.outdoor_temperature", "2026-09-22", "2026-09-29"),
)
```

```text
          day  low  high
0  2026-09-22  4.8  15.0
1  2026-09-23  4.7  14.8
```

> `demo04 · query_a_range`


---

# Downsampling

- `resample` groups a time index into fixed periods :
  - `"1h"` per hour, `"1D"` per day, `"15min"` per quarter hour
- `agg` computes several statistics per period
- A period without readings gives `NaN` :
  - The outdoor sensor was unavailable from 02:00 to 06:00

```python
hourly = readings["value"].resample("1h").agg(["mean", "min", "max"]).round(1)
print(len(readings), "readings,", len(hourly), "hours")
```

```text
2672 readings, 672 hours
                           mean  min  max
time
2026-09-14 01:00:00+00:00   6.5  6.3  6.7
2026-09-14 02:00:00+00:00   NaN  NaN  NaN
2026-09-14 03:00:00+00:00   NaN  NaN  NaN
```

> `demo05 · resample`


---

# Time Series Databases

- A time series database stores timestamped values and downsamples them automatically
- SQLite stores millions of readings in one file on one machine
- The usual Home Assistant routes to long-term storage :

| Storage | How Home Assistant writes to it | Query language |
| --- | --- | --- |
| SQLite | the recorder, by default | SQL |
| PostgreSQL | the recorder, with `db_url` | SQL |
| TimescaleDB | a PostgreSQL extension, set up separately | SQL with `time_bucket` |
| InfluxDB | the InfluxDB integration | InfluxQL, Flux or SQL |

- Grafana draws dashboards from all of them without Python

```sql
SELECT time_bucket('1 hour', time) AS hour, avg(value)
FROM readings
WHERE entity_id = 'sensor.outdoor_temperature'
GROUP BY hour
```


---

# Interactive Charts with Plotly

- `plotly.express` draws a chart from a DataFrame in one call :
  - Name the columns for `x` and `y`
  - `color` draws one line per value in a column
- The chart zooms, pans and shows values on hover
- `write_html` saves a page that works offline; `show` opens it in a browser

```python
figure = px.line(readings, x="time", y="value", color="entity_id", title="Temperature")
figure.update_layout(yaxis_title="°C")
figure.write_html(DATA / "temperature-chart.html")
```

> `demo06 · plotly_chart`


---

# Streamlit

- Streamlit turns a Python script into a web page :
  - `st.title`, `st.metric` and `st.plotly_chart` add parts to the page
  - A widget call such as `st.selectbox` returns its current value
- The script runs again from the top after every change to a widget
- `@st.cache_data` keeps a function's result between runs :
  - The database is read once per sensor
  - `ttl` reads it again after ten minutes, so new readings appear
- `streamlit run` starts the server and opens a browser

```bash
uv run streamlit run demos/10-dashboards/07_dashboard.py
```


---

# A Streamlit Dashboard

```python
@st.cache_data(ttl="10m")
def load_readings(entity_id: str) -> pd.DataFrame:
    connection = sqlite3.connect(DATABASE)
    readings = pd.read_sql(
        "SELECT time, value FROM readings WHERE entity_id = ?", connection,
        params=(entity_id,), parse_dates=["time"],
    )
    connection.close()
    return readings


entity_id = st.selectbox("Sensor", SENSORS)
days = st.slider("Days", min_value=1, max_value=28, value=7)

readings = load_readings(entity_id)
recent = readings[readings["time"] > readings["time"].max() - pd.Timedelta(days=days)]

latest, lowest, highest = st.columns(3)
latest.metric("Latest", f"{recent['value'].iloc[-1]:.1f}")
lowest.metric("Lowest", f"{recent['value'].min():.1f}")
highest.metric("Highest", f"{recent['value'].max():.1f}")
st.plotly_chart(px.line(recent, x="time", y="value"))
```

> `demo07 · dashboard`


---

# Streamlit, Dash and Grafana

| Tool | Written in | Suits |
| --- | --- | --- |
| Streamlit | a Python script | a dashboard in an afternoon |
| Plotly Dash | Python, with a layout and callbacks | larger applications with many pages |
| Grafana | configuration in the browser | monitoring live data from a database |

- Streamlit and Dash both draw Plotly charts
- Dash runs the callbacks whose inputs changed, and the callbacks that depend on them
- Grafana suits a database that is already filled, such as InfluxDB


---

# Reading from Home Assistant

- The REST API returns the history of a sensor as JSON :
  - `GET /api/history/period/<start>` with `filter_entity_id`
- A long-lived access token from the user profile authorises the request
- The result is a list with one list of states per sensor

```python
response = requests.get(
    f"{os.environ['HA_URL']}/api/history/period/{start}",
    headers={"Authorization": f"Bearer {os.environ['HA_TOKEN']}"},
    params={"filter_entity_id": SENSOR},
    timeout=10,
)
response.raise_for_status()
history = response.json()
states = pd.DataFrame(history[0])
```

- The demo reads a saved answer; `--live` asks a real Home Assistant

> `demo08 · home_assistant_api`


---

# Summary : Dashboards and Time Series

- A time series is a sequence of timestamped values
- `to_numeric` with `errors="coerce"` removes readings that are not numbers
- SQLite with a primary key on sensor and time stores readings without duplicates
- `resample` and `GROUP BY` turn detail into hourly or daily statistics
- InfluxDB and TimescaleDB are time series databases that Home Assistant can write to
- Plotly draws interactive charts; Streamlit turns a script into a dashboard

> `exercise10 · Dashboards and Time Series`
