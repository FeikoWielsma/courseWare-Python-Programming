---
layout: default
title: One Row per fetchone
pills: ["demo09 · fetchone"]
---

# One Row per fetchone

<script setup>
const run = {
  "names": [{"id": "con", "x": 0, "y": 0, "width": 290}, {"id": "cur", "x": 0, "y": 62, "width": 290}, {"id": "row", "x": 0, "y": 160, "width": 290}],
  "table": {"x": 400, "y": 0, "label": "result of SELECT * FROM Cars", "columns": [{"text": "Id", "width": 44}, {"text": "Name", "width": 148}, {"text": "Price", "width": 98}]},
  "rows": [
    {"id": "r1", "cells": ["1", "'Audi'", "52642"]},
    {"id": "r2", "cells": ["2", "'Mercedes'", "57127"]},
    {"id": "r3", "cells": ["3", "'Skoda'", "9000"]},
    {"id": "r4", "cells": ["4", "'Volvo'", "29000"]},
    {"id": "r5", "cells": ["5", "'Bentley'", "350000"]},
    {"id": "r6", "cells": ["6", "'Citroen'", "21000"]},
    {"id": "r7", "cells": ["7", "'Hummer'", "41400"]},
    {"id": "r8", "cells": ["8", "'Volkswagen'", "21600"]}
  ],
  "states": [
    {"names": {"con": "Connection, cars.db"}, "table": false, "rows": {}, "next": null, "active": ["con"]},
    {"names": {"con": "Connection, cars.db", "cur": "Cursor"}, "table": true, "rows": {"r1": "result", "r2": "result", "r3": "result", "r4": "result", "r5": "result", "r6": "result", "r7": "result", "r8": "result"}, "next": 0, "active": ["cur"]},
    {"names": {"con": "Connection, cars.db", "cur": "Cursor", "row": {"row": "r1"}}, "table": true, "rows": {"r1": "gone", "r2": "result", "r3": "result", "r4": "result", "r5": "result", "r6": "result", "r7": "result", "r8": "result"}, "next": 1, "active": ["cur", "row"]},
    {"names": {"con": "Connection, cars.db", "cur": "Cursor", "row": {"row": "r1"}}, "table": true, "rows": {"r1": "gone", "r2": "result", "r3": "result", "r4": "result", "r5": "result", "r6": "result", "r7": "result", "r8": "result"}, "next": 1, "active": ["row"]},
    {"names": {"con": "Connection, cars.db", "cur": "Cursor", "row": {"row": "r2"}}, "table": true, "rows": {"r1": "gone", "r2": "gone", "r3": "result", "r4": "result", "r5": "result", "r6": "result", "r7": "result", "r8": "result"}, "next": 2, "active": ["cur", "row"]},
    {"names": {"con": "Connection, cars.db", "cur": "Cursor", "row": {"row": "r8"}}, "table": true, "rows": {"r1": "gone", "r2": "gone", "r3": "gone", "r4": "gone", "r5": "gone", "r6": "gone", "r7": "gone", "r8": "gone"}, "next": 8, "active": ["cur", "row"]},
    {"names": {"con": "Connection, cars.db", "cur": "Cursor", "row": "None"}, "table": true, "rows": {"r1": "gone", "r2": "gone", "r3": "gone", "r4": "gone", "r5": "gone", "r6": "gone", "r7": "gone", "r8": "gone"}, "next": 8, "active": ["cur", "row"]},
    {"names": {"con": "Connection, cars.db", "cur": "Cursor", "row": "None"}, "table": true, "rows": {"r1": "gone", "r2": "gone", "r3": "gone", "r4": "gone", "r5": "gone", "r6": "gone", "r7": "gone", "r8": "gone"}, "next": null, "active": ["row"]}
  ],
  "output": [
    [],
    [],
    [],
    ["1 Audi 52642"],
    ["2 Mercedes 57127"],
    ["3 Skoda 9000", "4 Volvo 29000", "5 Bentley 350000", "6 Citroen 21000", "7 Hummer 41400", "8 Volkswagen 21600"],
    [],
    []
  ],
  "captions": [
    "`connect` opens `cars.db` and returns a connection object",
    "`execute` runs the query; the cursor holds its result and stands before the first row",
    "`fetchone()` hands over the next row, a tuple, and the cursor moves past it",
    "`row` is not `None`, so the loop prints its three columns",
    "The next pass fetches the second row; nothing refers to the first one any more",
    "The loop repeats for rows 3 to 8, one `fetchone()` each",
    "No rows are left, so `fetchone()` returns `None`",
    "`row is None`, so `break` leaves the loop"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1-2|3-5|6-7|8,10|6-8,10|6-8,10|6-7|8-9}
import sqlite3
con = sqlite3.connect("cars.db")
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
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
