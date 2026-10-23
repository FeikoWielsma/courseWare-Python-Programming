import json
import os
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pandas as pd
import requests

DATA = Path(__file__).resolve().parents[2] / "data"
SENSOR = "sensor.outdoor_temperature"

if "--live" in sys.argv:
    # HA_URL is for example http://homeassistant.local:8123; HA_TOKEN is a long-lived token.
    start = (datetime.now(UTC) - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    response = requests.get(
        f"{os.environ['HA_URL']}/api/history/period/{start}",
        headers={"Authorization": f"Bearer {os.environ['HA_TOKEN']}"},
        params={"filter_entity_id": SENSOR},
        timeout=10,
    )
    response.raise_for_status()
    history = response.json()
else:
    history = json.loads((DATA / "ha-history.json").read_text(encoding="utf-8"))

states = pd.DataFrame(history[0])
print(states[["last_changed", "state"]])
print(states["attributes"].iloc[0]["unit_of_measurement"])
