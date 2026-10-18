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
      "name": "physics",
      "members": [
        "Einstein",
        "Bohr",
        "Curie",
        "Fermi"
      ]
    },
    "right": {
      "name": "chemistry",
      "members": [
        "Curie",
        "Rutherford",
        "Pauling"
      ]
    }
  },
  "states": [
    {
      "expr": null,
      "result": null
    },
    {
      "expr": "\"Curie\" in chemistry",
      "test": "Curie",
      "within": "chemistry",
      "result": null
    },
    {
      "expr": "physics | chemistry",
      "result": [
        "Bohr",
        "Curie",
        "Einstein",
        "Fermi",
        "Pauling",
        "Rutherford"
      ]
    },
    {
      "expr": "physics & chemistry",
      "result": [
        "Curie"
      ]
    },
    {
      "expr": "physics - chemistry",
      "result": [
        "Bohr",
        "Einstein",
        "Fermi"
      ]
    },
    {
      "expr": "physics ^ chemistry",
      "result": [
        "Bohr",
        "Einstein",
        "Fermi",
        "Pauling",
        "Rutherford"
      ]
    }
  ],
  "output": [
    [],
    [
      "True"
    ],
    [
      "['Bohr', 'Curie', 'Einstein', 'Fermi', 'Pauling', 'Rutherford']"
    ],
    [
      "['Curie']"
    ],
    [
      "['Bohr', 'Einstein', 'Fermi']"
    ],
    [
      "['Bohr', 'Einstein', 'Fermi', 'Pauling', 'Rutherford']"
    ]
  ],
  "captions": [
    "`physics` and `chemistry` have one name in common : Curie",
    "`in` tests whether a value is a member of the set",
    "`|` gives every name in either set, each once",
    "`&` keeps the names that are in both sets",
    "`-` keeps the names in `physics` that are not in `chemistry`",
    "`^` keeps the names that are in exactly one of the two sets"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="680px">

```python {1-2|1-3|1-4|1-5|1-6|1-7}
physics = {"Einstein", "Bohr", "Curie", "Fermi"}
chemistry = {"Curie", "Rutherford", "Pauling"}
print("Curie" in chemistry)  # True
print(sorted(physics | chemistry))  # union, in either set
print(sorted(physics & chemistry))  # intersection, in both
print(sorted(physics - chemistry))  # difference, in physics only
print(sorted(physics ^ chemistry))  # in one of the two, not both
```

<template #visual="{ step }">
<DataStructuresSets :run="run" :step="step" />
</template>
</DataStructuresRun>
