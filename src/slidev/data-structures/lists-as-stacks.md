---
layout: default
title: A List as a Stack
pills: ["demo04 · listsasstacks"]
---

# A List as a Stack

<script setup>
const run = {
  "name": "history",
  "objects": {
    "3": "'Library'",
    "4": "'Album'",
    "5": "'Track'",
    "6": "'Queue'",
    "7": "'Artist'"
  },
  "states": [
    {
      "items": [
        "3",
        "4",
        "5"
      ],
      "active": null
    },
    {
      "items": [
        "3",
        "4",
        "5",
        "6"
      ],
      "active": "6"
    },
    {
      "items": [
        "3",
        "4",
        "5",
        "6",
        "7"
      ],
      "active": "7"
    },
    {
      "items": [
        "3",
        "4",
        "5",
        "6"
      ],
      "active": null,
      "returned": "7"
    },
    {
      "items": [
        "3",
        "4",
        "5",
        "6"
      ],
      "active": null
    }
  ],
  "output": [
    [],
    [],
    [],
    [
      "Artist"
    ],
    [
      "['Library', 'Album', 'Track', 'Queue']"
    ]
  ],
  "captions": [
    "`history` records visited player views; the latest view is on top",
    "`append()` puts an item on top",
    "The top is always the last index, here `4`",
    "`pop()` removes and returns the most recently visited view",
    "Index `0` is the bottom of the stack"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|1-2|1-3|1-4|1-5}
history = ["Library", "Album", "Track"]
history.append("Queue")
history.append("Artist")
print(history.pop())  # Artist
print(history)  # ['Library', 'Album', 'Track', 'Queue']
```

<template #visual="{ step }">
<DataStructuresSequence :run="run" :step="step" orientation="stack" :cell-width="170" :cell-height="68" />
</template>
</DataStructuresRun>
