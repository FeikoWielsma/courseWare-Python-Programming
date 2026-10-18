---
layout: default
title: Filtering into a New List
pills: ["demo02 · comprehension_with_predicate"]
---

# Filtering into a New List

<script setup>
const run = {
  "source": {"name": "filenames", "rows": [{"id": "files", "items": [{"id": "s0", "text": "'sales.csv'"}, {"id": "s1", "text": "'notes.txt'"}, {"id": "s2", "text": "'stock.csv'"}]}]},
  "variables": {"item": "name"},
  "result": {"name": "csv_files"},
  "states": [
    {"list": false, "cursor": null, "tested": {}, "result": [], "bound": false},
    {"list": true, "cursor": {"row": "files", "item": "s0"}, "tested": {"s0": true}, "result": ["s0"], "bound": false},
    {"list": true, "cursor": {"row": "files", "item": "s1"}, "tested": {"s0": true, "s1": false}, "result": ["s0"], "bound": false},
    {"list": true, "cursor": {"row": "files", "item": "s2"}, "tested": {"s0": true, "s1": false, "s2": true}, "result": ["s0", "s2"], "bound": false},
    {"list": true, "cursor": null, "tested": {"s0": true, "s1": false, "s2": true}, "result": ["s0", "s2"], "bound": true},
    {"list": true, "cursor": null, "tested": {"s0": true, "s1": false, "s2": true}, "result": ["s0", "s2"], "bound": true}
  ],
  "output": [[], [], [], [], [], ["['sales.csv', 'stock.csv']"]],
  "captions": [
    "`filenames` refers to a list of three file names",
    "`name` receives `'sales.csv'`; the condition is true, so the expression `name` goes into the new list",
    "For `'notes.txt'` the condition is false, so nothing is added",
    "`'stock.csv'` passes the condition and is added after `'sales.csv'`",
    "The finished list is bound to `csv_files`; `filenames` is unchanged",
    "The new list refers to the same two strings as `filenames`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack">

```python {1|2|2|2|2|3}
filenames = ["sales.csv", "notes.txt", "stock.csv"]
csv_files = [name for name in filenames if name.endswith(".csv")]
print(csv_files)  # ['sales.csv', 'stock.csv']
```

<template #visual="{ step }">
<MiddleComprehension :run="run" :step="step" :cell-width="150" :label-width="140" />
</template>
</DataStructuresRun>
