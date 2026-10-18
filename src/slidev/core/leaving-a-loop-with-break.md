---
layout: default
title: Leaving a Loop with break
pills: ["demo09 · breakandcontinue"]
---

# Leaving a Loop with break

<script setup>
const run = {
  "rows": [
    {
      "id": "tracks",
      "label": "playlist",
      "variable": "track",
      "items": [
        "Intro",
        "Orbit",
        "Echo",
        "Pulse",
        "Outro"
      ],
      "width": 100
    }
  ],
  "states": [
    {
      "cursor": {
        "row": "tracks",
        "at": 0
      },
      "status": {
        "tracks": [
          "ran"
        ]
      },
      "ended": []
    },
    {
      "cursor": {
        "row": "tracks",
        "at": 1
      },
      "status": {
        "tracks": [
          "ran",
          "ran"
        ]
      },
      "ended": []
    },
    {
      "cursor": {
        "row": "tracks",
        "at": 2
      },
      "status": {
        "tracks": [
          "ran",
          "ran",
          "ran"
        ]
      },
      "ended": []
    },
    {
      "cursor": {
        "row": "tracks",
        "at": 3
      },
      "status": {
        "tracks": [
          "ran",
          "ran",
          "ran",
          "stop",
          "never"
        ]
      },
      "ended": []
    },
    {
      "cursor": {
        "row": "tracks",
        "at": 3
      },
      "status": {
        "tracks": [
          "ran",
          "ran",
          "ran",
          "stop",
          "never"
        ]
      },
      "ended": []
    }
  ],
  "output": [
    [
      "Checked Intro"
    ],
    [
      "Checked Orbit"
    ],
    [
      "Checked Echo"
    ],
    [],
    [
      "Search complete"
    ]
  ],
  "captions": [
    "`track` receives `Intro`; the test is false, so the search continues",
    "The next pass checks `Orbit`",
    "The next pass checks `Echo`",
    "`Pulse` matches; `break` ends the search before `Outro`",
    "Execution continues after the loop; `track` still refers to `Pulse`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="pair">

```python {1-2,4|1-2,4|1-2,4|1-3|5}
for track in ["Intro", "Orbit", "Echo", "Pulse", "Outro"]:
    if track == "Pulse":
        break
    print(f"Checked {track}")
print("Search complete")
```

<template #visual="{ step }">
<CoreLoop :run="run" :step="step" :label-width="190" />
</template>
</DataStructuresRun>
