---
layout: default
title: Updating a Dictionary
pills: ["demo10 · dictionaries"]
---

# Updating a Dictionary

<script setup>
const run = {
  "name": "durations",
  "states": [
    {"rows": [{"id": "albert", "key": "'Orbit'", "value": "222"}, {"id": "robert", "key": "'Echo'", "value": "185"}, {"id": "enrico", "key": "'Pulse'", "value": "204"}], "active": null},
    {"rows": [{"id": "albert", "key": "'Orbit'", "value": "222"}, {"id": "robert", "key": "'Echo'", "value": "185"}, {"id": "enrico", "key": "'Pulse'", "value": "204"}, {"id": "werner", "key": "'Nova'", "value": "196"}], "active": "werner"},
    {"rows": [{"id": "albert", "key": "'Orbit'", "value": "222"}, {"id": "robert", "key": "'Echo'", "value": "185"}, {"id": "enrico", "key": "'Pulse'", "value": "204"}, {"id": "werner", "key": "'Nova'", "value": "196"}, {"id": "two", "key": "'Intro'", "value": "90"}], "active": "two"},
    {"rows": [{"id": "albert", "key": "'Orbit'", "value": "222"}, {"id": "robert", "key": "'Echo'", "value": "185"}, {"id": "enrico", "key": "'Pulse'", "value": "204"}, {"id": "werner", "key": "'Nova'", "value": "196"}, {"id": "two", "key": "'Intro'", "value": "90"}], "active": "robert"},
    {"rows": [{"id": "albert", "key": "'Orbit'", "value": "222"}, {"id": "robert", "key": "'Echo'", "value": "185"}, {"id": "enrico", "key": "'Pulse'", "value": "210"}, {"id": "werner", "key": "'Nova'", "value": "196"}, {"id": "two", "key": "'Intro'", "value": "90"}], "active": "enrico", "tone": "change"},
    {"rows": [{"id": "robert", "key": "'Echo'", "value": "185"}, {"id": "enrico", "key": "'Pulse'", "value": "210"}, {"id": "werner", "key": "'Nova'", "value": "196"}, {"id": "two", "key": "'Intro'", "value": "90"}], "active": null}
  ],
  "output": [[], [], [], ["185"], [], []],
  "captions": [
    "`durations` maps three keys to their values, in insertion order",
    "Assigning to a new key adds a pair after the existing ones",
    "A short intro gets its own duration entry",
    "Square brackets with a key return its value",
    "Assigning to an existing key replaces its value; the key keeps its place",
    "`del` removes the key and its value"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|1-2|1-3|1-4|1-5|1-6}
durations = {"Orbit": 222, "Echo": 185, "Pulse": 204}
durations["Nova"] = 196
durations["Intro"] = 90
print(durations["Echo"])  # 185
durations["Pulse"] = 210
del durations["Orbit"]
```

<template #visual="{ step }">
<DataStructuresDict :run="run" :step="step" />
</template>
</DataStructuresRun>
