---
layout: default
title: Two for Clauses, One List
pills: ["demo03 · nested_comprehensions"]
---

# Two for Clauses, One List

<script setup>
const run = {
  "source": {"name": "readings", "nested": true, "rows": [{"id": "r0", "items": [{"id": "v0", "text": "18.2"}, {"id": "v1", "text": "19.6"}]}, {"id": "r1", "items": [{"id": "v2", "text": "20.1"}, {"id": "v3", "text": "21.8"}]}]},
  "variables": {"row": "row", "item": "value"},
  "result": {"name": "flat"},
  "states": [
    {"list": false, "cursor": null, "result": [], "bound": false},
    {"list": true, "cursor": {"row": "r0", "item": "v0"}, "result": ["v0"], "bound": false},
    {"list": true, "cursor": {"row": "r0", "item": "v1"}, "result": ["v0", "v1"], "bound": false},
    {"list": true, "cursor": {"row": "r1", "item": "v2"}, "result": ["v0", "v1", "v2"], "bound": false},
    {"list": true, "cursor": {"row": "r1", "item": "v3"}, "result": ["v0", "v1", "v2", "v3"], "bound": false},
    {"list": true, "cursor": null, "result": ["v0", "v1", "v2", "v3"], "bound": true},
    {"list": true, "cursor": null, "result": ["v0", "v1", "v2", "v3"], "bound": true}
  ],
  "output": [[], [], [], [], [], [], ["[18.2, 19.6, 20.1, 21.8]"]],
  "captions": [
    "`readings` refers to a list of two lists, one per location",
    "The first `for` binds `row` to the first list; the second binds `value` to its first reading",
    "The second `for` finishes the row before the first `for` moves on",
    "The first `for` takes the next row, and `value` starts again at its first reading",
    "The readings arrive in the same order as in the nested loops",
    "The finished list is bound to `flat`; it refers to the same four readings",
    "The structure is gone : one list, four floats"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack">

```python {1|2|2|2|2|2|3}
readings = [[18.2, 19.6], [20.1, 21.8]]
flat = [value for row in readings for value in row]
print(flat)  # [18.2, 19.6, 20.1, 21.8]
```

<template #visual="{ step }">
<MiddleComprehension :run="run" :step="step" :cell-width="96" :label-width="130" />
</template>
</DataStructuresRun>
