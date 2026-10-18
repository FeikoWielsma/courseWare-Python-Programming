---
layout: default
title: One Item per Pass
pills: ["demo07 · for"]
---

# One Item per Pass

<script setup>
const run = {
  "rows": [{"id": "playlist", "label": "playlist", "variable": "title", "items": ["'Imagine'", "'Yesterday'", "'Respect'"], "width": 168}],
  "states": [
    {"cursor": null, "status": {"playlist": []}, "ended": []},
    {"cursor": {"row": "playlist", "at": 0}, "status": {"playlist": ["ran"]}, "ended": []},
    {"cursor": {"row": "playlist", "at": 1}, "status": {"playlist": ["ran", "ran"]}, "ended": []},
    {"cursor": {"row": "playlist", "at": 2}, "status": {"playlist": ["ran", "ran", "ran"]}, "ended": []},
    {"cursor": {"row": "playlist", "at": 2}, "status": {"playlist": ["ran", "ran", "ran"]}, "ended": ["playlist"]}
  ],
  "output": [[], ["Now playing: Imagine"], ["Now playing: Yesterday"], ["Now playing: Respect"], ["Playlist finished"]],
  "captions": [
    "`playlist` refers to a list of three titles",
    "`title` receives the first item, then the block runs",
    "The next pass binds `title` to the next item",
    "The block runs once for each item, in order",
    "No items are left, so the loop ends and the unindented `print` runs"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1|2-3|2-3|2-3|4}
playlist = ["Imagine", "Yesterday", "Respect"]
for title in playlist:
    print(f"Now playing: {title}")
print("Playlist finished")
```

<template #visual="{ step }">
<CoreLoop :run="run" :step="step" :label-width="96" />
</template>
</DataStructuresRun>
