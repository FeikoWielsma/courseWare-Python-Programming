---
layout: default
title: One Item per Pass
pills: ["demo07 · for"]
---

# One Item per Pass

<script setup>
const run = {
  "rows": [{"id": "files", "label": "files", "variable": "filename", "items": ["'cover.jpg'", "'stage.jpg'", "'crowd.jpg'"], "width": 168}],
  "states": [
    {"cursor": null, "status": {"files": []}, "ended": []},
    {"cursor": {"row": "files", "at": 0}, "status": {"files": ["ran"]}, "ended": []},
    {"cursor": {"row": "files", "at": 1}, "status": {"files": ["ran", "ran"]}, "ended": []},
    {"cursor": {"row": "files", "at": 2}, "status": {"files": ["ran", "ran", "ran"]}, "ended": []},
    {"cursor": {"row": "files", "at": 2}, "status": {"files": ["ran", "ran", "ran"]}, "ended": ["files"]}
  ],
  "output": [[], ["Processing cover.jpg"], ["Processing stage.jpg"], ["Processing crowd.jpg"], ["All files processed"]],
  "captions": [
    "`files` refers to a list of three file names",
    "`filename` receives the first item, then the block runs",
    "The next pass binds `filename` to the next item",
    "The block runs once for each item, in order",
    "No items are left, so the loop ends and the unindented `print` runs"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1|2-3|2-3|2-3|4}
files = ["cover.jpg", "stage.jpg", "crowd.jpg"]
for filename in files:
    print(f"Processing {filename}")
print("All files processed")
```

<template #visual="{ step }">
<CoreLoop :run="run" :step="step" :label-width="96" />
</template>
</DataStructuresRun>
