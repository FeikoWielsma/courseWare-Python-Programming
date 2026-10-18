---
layout: default
title: Inserts Wait for the Commit
pills: ["demo05 · lastinsertedrowid"]
---

# Inserts Wait for the Commit

<script setup>
const run = {
  "names": [{"id": "con", "x": 0, "y": 22, "width": 300}, {"id": "cur", "x": 0, "y": 84, "width": 300}, {"id": "film_id", "x": 0, "y": 146, "width": 120}],
  "table": {"x": 470, "y": 0, "label": "table films", "columns": [{"text": "id", "width": 52}, {"text": "title", "width": 200}]},
  "rows": [
    {"id": "f1", "cells": ["1", "'Spirited Away'"]},
    {"id": "f2", "cells": ["2", "'Arrival'"]},
    {"id": "f3", "cells": ["3", "'Paddington 2'"]}
  ],
  "states": [
    {"names": {"con": "Connection, :memory:"}, "table": false, "rows": {}, "active": ["con"]},
    {"names": {"con": "Connection, :memory:", "cur": "Cursor"}, "table": true, "rows": {}, "active": ["cur"]},
    {"names": {"con": "Connection, :memory:", "cur": "Cursor, lastrowid 1"}, "badges": {"con": "transaction open"}, "table": true, "rows": {"f1": "pending"}, "active": ["cur"]},
    {"names": {"con": "Connection, :memory:", "cur": "Cursor, lastrowid 3"}, "badges": {"con": "transaction open"}, "table": true, "rows": {"f1": "pending", "f2": "pending", "f3": "pending"}, "active": ["cur"]},
    {"names": {"con": "Connection, :memory:", "cur": "Cursor, lastrowid 3", "film_id": "3"}, "badges": {"con": "transaction open"}, "table": true, "rows": {"f1": "pending", "f2": "pending", "f3": "pending"}, "active": ["cur", "film_id"]},
    {"names": {"con": "Connection, :memory:", "cur": "Cursor, lastrowid 3", "film_id": "3"}, "badges": {"con": "transaction open"}, "table": true, "rows": {"f1": "pending", "f2": "pending", "f3": "pending"}, "active": ["film_id"]},
    {"names": {"con": "Connection, :memory:", "cur": "Cursor, lastrowid 3", "film_id": "3"}, "table": true, "rows": {"f1": "committed", "f2": "committed", "f3": "committed"}, "active": ["con"]}
  ],
  "output": [
    [],
    [],
    [],
    [],
    [],
    ["Paddington 2 was added with id 3"],
    []
  ],
  "captions": [
    "`\":memory:\"` opens a new, empty database that exists only while the program runs",
    "Inside the block, the cursor creates the empty `films` table",
    "The first `INSERT` leaves out `id`; SQLite gives the `INTEGER PRIMARY KEY` column the value 1",
    "Two more films, numbered 2 and 3; each change belongs to the open transaction, not committed yet",
    "`lastrowid` is the `id` SQLite generated for the row the cursor inserted last",
    "The f-string prints it",
    "The block ends without an exception, so `with con` commits : the three films are saved"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1-2|3-5|6|7-8|9|10|3}
import sqlite3
con = sqlite3.connect(":memory:")
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE films(id INTEGER PRIMARY KEY, title TEXT)")
    cur.execute("INSERT INTO films(title) VALUES('Spirited Away')")
    cur.execute("INSERT INTO films(title) VALUES('Arrival')")
    cur.execute("INSERT INTO films(title) VALUES('Paddington 2')")
    film_id = cur.lastrowid
    print(f"Paddington 2 was added with id {film_id}")
```

<template #visual="{ step }">
<StatefulRecords :run="run" :step="step" :label-width="96" />
</template>
</DataStructuresRun>
