---
layout: default
title: One Row per fetchone
pills: ["demo09 · fetchone"]
---

# One Row per fetchone

<script setup>
const run = {
  "names": [{"id": "con", "x": 0, "y": 0, "width": 230}, {"id": "cur", "x": 0, "y": 62, "width": 230}, {"id": "row", "x": 291, "y": 322, "width": 322}],
  "table": {"x": 350, "y": 0, "label": "result of the SELECT", "columns": [{"text": "id", "width": 44}, {"text": "title", "width": 180}, {"text": "minutes", "width": 90}]},
  "rows": [
    {"id": "r1", "cells": ["1", "'Spirited Away'", "125"]},
    {"id": "r2", "cells": ["2", "'Amélie'", "122"]},
    {"id": "r3", "cells": ["3", "'Arrival'", "116"]},
    {"id": "r4", "cells": ["4", "'Paddington 2'", "104"]},
    {"id": "r5", "cells": ["5", "'Coco'", "105"]},
    {"id": "r6", "cells": ["6", "'Parasite'", "132"]}
  ],
  "states": [
    {"names": {"con": "Connection"}, "table": false, "rows": {}, "next": null, "active": ["con"]},
    {"names": {"con": "Connection", "cur": "Cursor"}, "table": true, "rows": {"r1": "result", "r2": "result", "r3": "result", "r4": "result", "r5": "result", "r6": "result"}, "next": 0, "active": ["cur"]},
    {"names": {"con": "Connection", "cur": "Cursor", "row": {"row": "r1"}}, "table": true, "rows": {"r1": "gone", "r2": "result", "r3": "result", "r4": "result", "r5": "result", "r6": "result"}, "next": 1, "active": ["cur", "row"]},
    {"names": {"con": "Connection", "cur": "Cursor", "row": {"row": "r1"}}, "table": true, "rows": {"r1": "gone", "r2": "result", "r3": "result", "r4": "result", "r5": "result", "r6": "result"}, "next": 1, "active": ["row"]},
    {"names": {"con": "Connection", "cur": "Cursor", "row": {"row": "r2"}}, "table": true, "rows": {"r1": "gone", "r2": "gone", "r3": "result", "r4": "result", "r5": "result", "r6": "result"}, "next": 2, "active": ["cur", "row"]},
    {"names": {"con": "Connection", "cur": "Cursor", "row": {"row": "r6"}}, "table": true, "rows": {"r1": "gone", "r2": "gone", "r3": "gone", "r4": "gone", "r5": "gone", "r6": "gone"}, "next": 6, "active": ["cur", "row"]},
    {"names": {"con": "Connection", "cur": "Cursor", "row": "None"}, "table": true, "rows": {"r1": "gone", "r2": "gone", "r3": "gone", "r4": "gone", "r5": "gone", "r6": "gone"}, "next": 6, "active": ["cur", "row"]},
    {"names": {"con": "Connection", "cur": "Cursor", "row": "None"}, "table": true, "rows": {"r1": "gone", "r2": "gone", "r3": "gone", "r4": "gone", "r5": "gone", "r6": "gone"}, "next": null, "active": ["row"]}
  ],
  "output": [
    [],
    [],
    [],
    ["1 Spirited Away 125"],
    ["2 Amélie 122"],
    ["3 Arrival 116", "4 Paddington 2 104", "5 Coco 105", "6 Parasite 132"],
    [],
    []
  ],
  "captions": [
    "`connect` opens `watchlist.db` and returns a connection object",
    "`execute` runs the query; the cursor holds its result and stands before the first row",
    "`fetchone()` hands over the next row, a tuple, to `row`; the cursor moves past it",
    "`row` is not `None`, so the loop prints its three columns",
    "The next pass fetches the second row; nothing refers to the first one any more",
    "The loop repeats for rows 3 to 6, one `fetchone()` each",
    "No rows are left, so `fetchone()` returns `None`",
    "`row is None`, so `break` leaves the loop"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1-2|3-5|6-7|8,10|6-8,10|6-8,10|6-7|8-9}
import sqlite3
con = sqlite3.connect("watchlist.db")
with con:
    cur = con.cursor()
    cur.execute("SELECT id, title, minutes FROM films")
    while True:
        row = cur.fetchone()
        if row is None:
            break
        print(row[0], row[1], row[2])
```

<template #visual="{ step }">
<StatefulRecords :run="run" :step="step" />
</template>
</DataStructuresRun>
