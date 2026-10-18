---
layout: default
title: Replacing and Deleting Items
pills: ["demo02 · updatinglists"]
---

# Replacing and Deleting Items

<script setup>
const run = {
  "name": "li",
  "objects": {"p": "'physics'", "c": "'chemistry'", "b": "'biology'", "m": "'mathematics'", "s": "'computer science'"},
  "states": [
    {"items": ["p", "c", "b", "s"], "active": null},
    {"items": ["p", "c", "m", "s"], "active": "m", "tone": "change"},
    {"items": ["p", "c", "s"], "active": "s"},
    {"items": ["p", "c", "s"], "active": null},
    {"items": ["c", "s"], "active": null},
    {"items": ["c", "s"], "active": null}
  ],
  "output": [[], [], [], ["['physics', 'chemistry', 'computer science']"], [], ["['chemistry', 'computer science']"]],
  "captions": [
    "`li` holds four strings at indexes 0 to 3",
    "Assigning to an index replaces the item there; the length stays the same",
    "`del li[2]` removes the item, and every item after it moves down one index",
    "The list now holds three items",
    "`remove()` deletes the first item equal to its argument, wherever it is",
    "Both deletions changed the same list object in place"
  ]
}
</script>

<DataStructuresRun :run="run" layout="rows">

```python {1|1-2|1-3|1-4|1-5|1-6}
li = ["physics", "chemistry", "biology", "computer science"]
li[2] = "mathematics"
del li[2]
print(li)  # ['physics', 'chemistry', 'computer science']
li.remove("physics")
print(li)  # ['chemistry', 'computer science']
```

<template #visual="{ step }">
<DataStructuresSequence :run="run" :step="step" :cell-width="236" />
</template>
</DataStructuresRun>
