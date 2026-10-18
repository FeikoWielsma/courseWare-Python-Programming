---
layout: default
title: A List as a Stack
pills: ["demo04 · listsasstacks"]
---

# A List as a Stack

<script setup>
const run = {
  "name": "stack",
  "objects": {"3": "3", "4": "4", "5": "5", "6": "6", "7": "7"},
  "states": [
    {"items": ["3", "4", "5"], "active": null},
    {"items": ["3", "4", "5", "6"], "active": "6"},
    {"items": ["3", "4", "5", "6", "7"], "active": "7"},
    {"items": ["3", "4", "5", "6"], "active": null, "returned": "7"},
    {"items": ["3", "4", "5", "6"], "active": null}
  ],
  "output": [[], [], [], ["7"], ["[3, 4, 5, 6]"]],
  "captions": [
    "`stack` holds three items; the last item is the top",
    "`append()` puts an item on top",
    "The top is always the last index, here `4`",
    "`pop()` removes the top item and returns it",
    "Index `0` is the bottom of the stack"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|1-2|1-3|1-4|1-5}
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack.pop())  # 7
print(stack)  # [3, 4, 5, 6]
```

<template #visual="{ step }">
<DataStructuresSequence :run="run" :step="step" orientation="stack" :cell-width="170" :cell-height="68" />
</template>
</DataStructuresRun>
