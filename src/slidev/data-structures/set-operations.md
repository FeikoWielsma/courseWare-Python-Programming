---
layout: default
title: Set Operations by Region
pills: ["demo09 · setsandfrozensets"]
---

# Set Operations by Region

<script setup>
const run = {
  "sets": {
    "left": {
      "name": "day_one",
      "members": [
        "Nova",
        "Echo",
        "Pulse",
        "Orbit"
      ]
    },
    "right": {
      "name": "day_two",
      "members": [
        "Pulse",
        "Muse",
        "Vega"
      ]
    }
  },
  "states": [
    {
      "expr": null,
      "result": null
    },
    {
      "expr": "\"Pulse\" in day_two",
      "test": "Pulse",
      "within": "day_two",
      "result": null
    },
    {
      "expr": "day_one | day_two",
      "result": [
        "Echo",
        "Muse",
        "Nova",
        "Orbit",
        "Pulse",
        "Vega"
      ]
    },
    {
      "expr": "day_one & day_two",
      "result": [
        "Pulse"
      ]
    },
    {
      "expr": "day_one - day_two",
      "result": [
        "Echo",
        "Nova",
        "Orbit"
      ]
    },
    {
      "expr": "day_one ^ day_two",
      "result": [
        "Echo",
        "Muse",
        "Nova",
        "Orbit",
        "Vega"
      ]
    }
  ],
  "output": [
    [],
    [
      "True"
    ],
    [
      "['Echo', 'Muse', 'Nova', 'Orbit', 'Pulse', 'Vega']"
    ],
    [
      "['Pulse']"
    ],
    [
      "['Echo', 'Nova', 'Orbit']"
    ],
    [
      "['Echo', 'Muse', 'Nova', 'Orbit', 'Vega']"
    ]
  ],
  "captions": [
    "`day_one` and `day_two` have one name in common",
    "`in` tests whether a value is a member of the set",
    "`|` gives every name in either set, each once",
    "`&` keeps the names that are in both sets",
    "`-` keeps the names in `day_one` that are not in `day_two`",
    "`^` keeps the names that are in exactly one of the two sets"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="680px">

```python {1-2|1-3|1-4|1-5|1-6|1-7}
day_one = {"Nova", "Echo", "Pulse", "Orbit"}
day_two = {"Pulse", "Muse", "Vega"}
print("Pulse" in day_two)  # True
print(sorted(day_one | day_two))  # union, in either set
print(sorted(day_one & day_two))  # intersection, in both
print(sorted(day_one - day_two))  # difference, in day_one only
print(sorted(day_one ^ day_two))  # in one of the two, not both
```

<template #visual="{ step }">
<DataStructuresSets :run="run" :step="step" />
</template>
</DataStructuresRun>
