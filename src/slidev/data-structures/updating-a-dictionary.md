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
    {"rows": [{"id": "albert", "key": "'Imagine'", "value": "183"}, {"id": "robert", "key": "'Yesterday'", "value": "125"}, {"id": "enrico", "key": "'Respect'", "value": "149"}], "active": null},
    {"rows": [{"id": "albert", "key": "'Imagine'", "value": "183"}, {"id": "robert", "key": "'Yesterday'", "value": "125"}, {"id": "enrico", "key": "'Respect'", "value": "149"}, {"id": "werner", "key": "'Toxic'", "value": "199"}], "active": "werner"},
    {"rows": [{"id": "albert", "key": "'Imagine'", "value": "183"}, {"id": "robert", "key": "'Yesterday'", "value": "125"}, {"id": "enrico", "key": "'Respect'", "value": "149"}, {"id": "werner", "key": "'Toxic'", "value": "199"}, {"id": "two", "key": "'Thriller'", "value": "357"}], "active": "two"},
    {"rows": [{"id": "albert", "key": "'Imagine'", "value": "183"}, {"id": "robert", "key": "'Yesterday'", "value": "125"}, {"id": "enrico", "key": "'Respect'", "value": "149"}, {"id": "werner", "key": "'Toxic'", "value": "199"}, {"id": "two", "key": "'Thriller'", "value": "357"}], "active": "robert"},
    {"rows": [{"id": "albert", "key": "'Imagine'", "value": "183"}, {"id": "robert", "key": "'Yesterday'", "value": "125"}, {"id": "enrico", "key": "'Respect'", "value": "147"}, {"id": "werner", "key": "'Toxic'", "value": "199"}, {"id": "two", "key": "'Thriller'", "value": "357"}], "active": "enrico", "tone": "change"},
    {"rows": [{"id": "robert", "key": "'Yesterday'", "value": "125"}, {"id": "enrico", "key": "'Respect'", "value": "147"}, {"id": "werner", "key": "'Toxic'", "value": "199"}, {"id": "two", "key": "'Thriller'", "value": "357"}], "active": null}
  ],
  "output": [[], [], [], ["125"], [], []],
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
durations = {"Imagine": 183, "Yesterday": 125, "Respect": 149}
durations["Toxic"] = 199
durations["Thriller"] = 357
print(durations["Yesterday"])  # 125
durations["Respect"] = 147
del durations["Imagine"]
```

<template #visual="{ step }">
<DataStructuresDict :run="run" :step="step" />
</template>
</DataStructuresRun>
