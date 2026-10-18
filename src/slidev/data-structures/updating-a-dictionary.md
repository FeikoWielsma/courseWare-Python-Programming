---
layout: default
title: Updating a Dictionary
pills: ["demo10 · dictionaries"]
---

# Updating a Dictionary

<script setup>
const run = {
  "name": "dict1",
  "states": [
    {"rows": [{"id": "albert", "key": "'Albert'", "value": "2341"}, {"id": "robert", "key": "'Robert'", "value": "9102"}, {"id": "enrico", "key": "'Enrico'", "value": "3258"}], "active": null},
    {"rows": [{"id": "albert", "key": "'Albert'", "value": "2341"}, {"id": "robert", "key": "'Robert'", "value": "9102"}, {"id": "enrico", "key": "'Enrico'", "value": "3258"}, {"id": "werner", "key": "'Werner'", "value": "3490"}], "active": "werner"},
    {"rows": [{"id": "albert", "key": "'Albert'", "value": "2341"}, {"id": "robert", "key": "'Robert'", "value": "9102"}, {"id": "enrico", "key": "'Enrico'", "value": "3258"}, {"id": "werner", "key": "'Werner'", "value": "3490"}, {"id": "two", "key": "2", "value": "'Data'"}], "active": "two"},
    {"rows": [{"id": "albert", "key": "'Albert'", "value": "2341"}, {"id": "robert", "key": "'Robert'", "value": "9102"}, {"id": "enrico", "key": "'Enrico'", "value": "3258"}, {"id": "werner", "key": "'Werner'", "value": "3490"}, {"id": "two", "key": "2", "value": "'Data'"}], "active": "robert"},
    {"rows": [{"id": "albert", "key": "'Albert'", "value": "2341"}, {"id": "robert", "key": "'Robert'", "value": "9102"}, {"id": "enrico", "key": "'Enrico'", "value": "9999"}, {"id": "werner", "key": "'Werner'", "value": "3490"}, {"id": "two", "key": "2", "value": "'Data'"}], "active": "enrico", "tone": "change"},
    {"rows": [{"id": "robert", "key": "'Robert'", "value": "9102"}, {"id": "enrico", "key": "'Enrico'", "value": "9999"}, {"id": "werner", "key": "'Werner'", "value": "3490"}, {"id": "two", "key": "2", "value": "'Data'"}], "active": null}
  ],
  "output": [[], [], [], ["9102"], [], []],
  "captions": [
    "`dict1` maps three keys to their values, in insertion order",
    "Assigning to a new key adds a pair after the existing ones",
    "Keys can be of different hashable types, such as the number `2`",
    "Square brackets with a key return its value",
    "Assigning to an existing key replaces its value; the key keeps its place",
    "`del` removes the key and its value"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|1-2|1-3|1-4|1-5|1-6}
dict1 = {"Albert": 2341, "Robert": 9102, "Enrico": 3258}
dict1["Werner"] = 3490
dict1[2] = "Data"
print(dict1["Robert"])  # 9102
dict1["Enrico"] = 9999
del dict1["Albert"]
```

<template #visual="{ step }">
<DataStructuresDict :run="run" :step="step" />
</template>
</DataStructuresRun>
