---
layout: default
title: Inserts Wait for the Commit
pills: ["demo05 · lastinsertedrowid"]
---

# Inserts Wait for the Commit

<script setup>
const run = {
  "names": [{"id": "con", "x": 0, "y": 22, "width": 330}, {"id": "cur", "x": 0, "y": 84, "width": 330}, {"id": "lid", "x": 0, "y": 146, "width": 120}],
  "table": {"x": 470, "y": 0, "label": "table Friends", "columns": [{"text": "Id", "width": 52}, {"text": "Name", "width": 132}]},
  "rows": [
    {"id": "f1", "cells": ["1", "'Tom'"]},
    {"id": "f2", "cells": ["2", "'Rebecca'"]},
    {"id": "f3", "cells": ["3", "'Jim'"]},
    {"id": "f4", "cells": ["4", "'Robert'"]}
  ],
  "states": [
    {"names": {"con": "Connection, :memory:"}, "table": false, "rows": {}, "active": ["con"]},
    {"names": {"con": "Connection, :memory:", "cur": "Cursor"}, "table": true, "rows": {}, "active": ["cur"]},
    {"names": {"con": "Connection, :memory:", "cur": "Cursor, lastrowid 1"}, "badges": {"con": "transaction open"}, "table": true, "rows": {"f1": "pending"}, "active": ["cur"]},
    {"names": {"con": "Connection, :memory:", "cur": "Cursor, lastrowid 4"}, "badges": {"con": "transaction open"}, "table": true, "rows": {"f1": "pending", "f2": "pending", "f3": "pending", "f4": "pending"}, "active": ["cur"]},
    {"names": {"con": "Connection, :memory:", "cur": "Cursor, lastrowid 4", "lid": "4"}, "badges": {"con": "transaction open"}, "table": true, "rows": {"f1": "pending", "f2": "pending", "f3": "pending", "f4": "pending"}, "active": ["cur", "lid"]},
    {"names": {"con": "Connection, :memory:", "cur": "Cursor, lastrowid 4", "lid": "4"}, "badges": {"con": "transaction open"}, "table": true, "rows": {"f1": "pending", "f2": "pending", "f3": "pending", "f4": "pending"}, "active": ["lid"]},
    {"names": {"con": "Connection, :memory:", "cur": "Cursor, lastrowid 4", "lid": "4"}, "table": true, "rows": {"f1": "committed", "f2": "committed", "f3": "committed", "f4": "committed"}, "active": ["con"]}
  ],
  "output": [
    [],
    [],
    [],
    [],
    [],
    ["The last Id of the inserted row is 4"],
    []
  ],
  "captions": [
    "`\":memory:\"` opens a new, empty database that exists only while the program runs",
    "Inside the block, the cursor creates the empty `Friends` table",
    "The first `INSERT` adds a row; SQLite gives the `INTEGER PRIMARY KEY` column the value 1",
    "Three more rows; each change belongs to the open transaction, not committed yet",
    "`lastrowid` is the `Id` of the row the cursor inserted last",
    "The f-string prints it",
    "The block ends without an exception, so `with con` commits : the four rows are saved"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1-2|3-5|6|7-9|10|11|3}
import sqlite3
con = sqlite3.connect(":memory:")
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT)")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")
    lid = cur.lastrowid
    print(f"The last Id of the inserted row is {lid}")
```

<template #visual="{ step }">
<StatefulRecords :run="run" :step="step" />
</template>
</DataStructuresRun>
