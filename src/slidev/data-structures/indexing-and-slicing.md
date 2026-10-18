---
layout: default
title: Indexing and Slicing a List
pills: ["demo01 · lists"]
---

# Indexing and Slicing a List

<script setup>
const run = {
  "list": {"name": "list1", "values": ["'Thriller'", "'Imagine'", "'Yesterday'", "'Respect'", "'Hey Jude'"]},
  "states": [
    {"expr": null, "key": null, "picked": [], "result": null},
    {"expr": "list1[0]", "key": {"index": 0}, "picked": [0], "result": "item"},
    {"expr": "list1[1:3]", "key": {"start": 1, "stop": 3, "step": null}, "picked": [1, 2], "result": "list"},
    {"expr": "list1[::-1]", "key": {"start": null, "stop": null, "step": -1}, "picked": [4, 3, 2, 1, 0], "result": "list"}
  ],
  "output": [[], ["Thriller"], ["['Imagine', 'Yesterday']"], ["['Hey Jude', 'Respect', 'Yesterday', 'Imagine', 'Thriller']"]],
  "captions": [
    "`list1` holds five items, counted from `0` at the front and from `-1` at the back",
    "An index gives one item, not a list",
    "A slice gives a new list, up to but not including its second index",
    "A step of `-1` copies the items from the back to the front"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="380px">

```python {1|1-2|1-3|1-4}
list1 = ["Thriller", "Imagine", "Yesterday", "Respect", "Hey Jude"]
print(list1[0])  # Prints first element of the list
print(list1[1:3])  # Prints the 2nd and 3rd elements
print(list1[::-1])  # Prints complete list in reverse order
```

<template #visual="{ step }">
<DataStructuresSlicing :run="run" :step="step" />
</template>
</DataStructuresRun>
