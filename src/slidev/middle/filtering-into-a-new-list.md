---
layout: default
title: Filtering into a New List
pills: ["demo02 · comprehension_with_predicate"]
---

# Filtering into a New List

<script setup>
const run = {
  "source": {"name": "filenames", "rows": [{"id": "files", "items": [{"id": "s0", "text": "'cover.jpg'"}, {"id": "s1", "text": "'notes.txt'"}, {"id": "s2", "text": "'stage.jpg'"}]}]},
  "variables": {"item": "name"},
  "result": {"name": "photo_files"},
  "states": [
    {"list": false, "cursor": null, "tested": {}, "result": [], "bound": false},
    {"list": true, "cursor": {"row": "files", "item": "s0"}, "tested": {"s0": true}, "result": ["s0"], "bound": false},
    {"list": true, "cursor": {"row": "files", "item": "s1"}, "tested": {"s0": true, "s1": false}, "result": ["s0"], "bound": false},
    {"list": true, "cursor": {"row": "files", "item": "s2"}, "tested": {"s0": true, "s1": false, "s2": true}, "result": ["s0", "s2"], "bound": false},
    {"list": true, "cursor": null, "tested": {"s0": true, "s1": false, "s2": true}, "result": ["s0", "s2"], "bound": true},
    {"list": true, "cursor": null, "tested": {"s0": true, "s1": false, "s2": true}, "result": ["s0", "s2"], "bound": true}
  ],
  "output": [[], [], [], [], [], ["['cover.jpg', 'stage.jpg']"]],
  "captions": [
    "`filenames` refers to a list of three file names",
    "`name` receives `'cover.jpg'`; the condition is true, so the expression `name` goes into the new list",
    "For `'notes.txt'` the condition is false, so nothing is added",
    "`'stage.jpg'` passes the condition and is added after `'cover.jpg'`",
    "The finished list is bound to `photo_files`; `filenames` is unchanged",
    "The new list refers to the same two strings as `filenames`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack">

```python {1|2|2|2|2|3}
filenames = ["cover.jpg", "notes.txt", "stage.jpg"]
photo_files = [name for name in filenames if name.endswith(".jpg")]
print(photo_files)  # ['cover.jpg', 'stage.jpg']
```

<template #visual="{ step }">
<MiddleComprehension :run="run" :step="step" :cell-width="150" :label-width="140" />
</template>
</DataStructuresRun>
