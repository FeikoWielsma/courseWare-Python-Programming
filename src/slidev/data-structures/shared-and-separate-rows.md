---
layout: default
title: Shared and Separate Rows
pills: ["demo03 · multidimensionallists"]
---

# Shared and Separate Rows

<script setup>
const run = {
  "names": ["shared", "rows"],
  "states": [
    {"refs": {"shared": ["a", "a"]}, "objects": {"a": ["0", "0", "0"]}, "changed": null, "via": null, "reading": null},
    {"refs": {"shared": ["a", "a"]}, "objects": {"a": ["1", "0", "0"]}, "changed": {"object": "a", "index": 0}, "via": {"name": "shared", "slot": 0}, "reading": null},
    {"refs": {"shared": ["a", "a"]}, "objects": {"a": ["1", "0", "0"]}, "changed": null, "via": null, "reading": "shared"},
    {"refs": {"shared": ["a", "a"], "rows": ["b", "c"]}, "objects": {"a": ["1", "0", "0"], "b": ["0", "0", "0"], "c": ["0", "0", "0"]}, "changed": null, "via": null, "reading": null},
    {"refs": {"shared": ["a", "a"], "rows": ["b", "c"]}, "objects": {"a": ["1", "0", "0"], "b": ["1", "0", "0"], "c": ["0", "0", "0"]}, "changed": {"object": "b", "index": 0}, "via": {"name": "rows", "slot": 0}, "reading": null},
    {"refs": {"shared": ["a", "a"], "rows": ["b", "c"]}, "objects": {"a": ["1", "0", "0"], "b": ["1", "0", "0"], "c": ["0", "0", "0"]}, "changed": null, "via": null, "reading": "rows"}
  ],
  "output": [[], [], ["[[1, 0, 0], [1, 0, 0]]"], [], [], ["[[1, 0, 0], [0, 0, 0]]"]],
  "captions": [
    "`* 2` repeats the reference, so both slots of `shared` refer to one list",
    "`shared[0][0] = 1` follows slot 0 and changes that list",
    "Row 1 shows the change too, because it is the same list",
    "Two separate `[0] * 3` expressions create two lists",
    "`rows[0][0] = 1` changes only the list in slot 0",
    "Each row is its own list, so row 1 is unchanged"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1|1-2|1-3|1-4|1-5|1-6}
shared = [[0] * 3] * 2
shared[0][0] = 1
print(shared)  # [[1, 0, 0], [1, 0, 0]], both rows are one list
rows = [[0] * 3, [0] * 3]
rows[0][0] = 1
print(rows)  # [[1, 0, 0], [0, 0, 0]], two separate lists
```

<template #visual="{ step }">
<DataStructuresReferences :run="run" :step="step" />
</template>
</DataStructuresRun>
