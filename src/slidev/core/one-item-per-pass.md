---
layout: default
title: One Item per Pass
pills: ["demo07 · for"]
---

# One Item per Pass

<script setup>
const run = {
  "rows": [{"id": "files", "label": "files", "variable": "filename", "items": ["'sales.csv'", "'stock.csv'", "'prices.csv'"], "width": 168}],
  "states": [
    {"cursor": null, "status": {"files": []}, "ended": []},
    {"cursor": {"row": "files", "at": 0}, "status": {"files": ["ran"]}, "ended": []},
    {"cursor": {"row": "files", "at": 1}, "status": {"files": ["ran", "ran"]}, "ended": []},
    {"cursor": {"row": "files", "at": 2}, "status": {"files": ["ran", "ran", "ran"]}, "ended": []},
    {"cursor": {"row": "files", "at": 2}, "status": {"files": ["ran", "ran", "ran"]}, "ended": ["files"]}
  ],
  "output": [[], ["Processing sales.csv"], ["Processing stock.csv"], ["Processing prices.csv"], ["All files processed"]],
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
files = ["sales.csv", "stock.csv", "prices.csv"]
for filename in files:
    print(f"Processing {filename}")
print("All files processed")
```

<template #visual="{ step }">
<CoreLoop :run="run" :step="step" :label-width="96" />
</template>
</DataStructuresRun>
