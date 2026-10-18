---
layout: default
title: Leaving a Loop with break
pills: ["demo09 · breakandcontinue"]
---

# Leaving a Loop with break

<script setup>
const run = {
  "rows": [{"id": "word", "label": "\"Programming\"", "variable": "letter", "items": ["P", "r", "o", "g", "r", "a", "m", "m", "i", "n", "g"], "width": 56}],
  "states": [
    {"cursor": {"row": "word", "at": 0}, "status": {"word": ["ran"]}, "ended": []},
    {"cursor": {"row": "word", "at": 1}, "status": {"word": ["ran", "ran"]}, "ended": []},
    {"cursor": {"row": "word", "at": 7}, "status": {"word": ["ran", "ran", "ran", "ran", "ran", "ran", "ran", "ran"]}, "ended": []},
    {"cursor": {"row": "word", "at": 8}, "status": {"word": ["ran", "ran", "ran", "ran", "ran", "ran", "ran", "ran", "stop", "never", "never"]}, "ended": []},
    {"cursor": {"row": "word", "at": 8}, "status": {"word": ["ran", "ran", "ran", "ran", "ran", "ran", "ran", "ran", "stop", "never", "never"]}, "ended": []}
  ],
  "output": [["Current Letter : P"], ["Current Letter : r"], ["Current Letter : o", "Current Letter : g", "Current Letter : r", "Current Letter : a", "Current Letter : m", "Current Letter : m"], [], ["After second loop!"]],
  "captions": [
    "`letter` receives `'P'`; the test is false, so `print` runs",
    "Each pass binds `letter` to the next character",
    "Six more passes run the whole block",
    "At `'i'` the test is true, and `break` leaves the loop at once",
    "The rest is never reached; execution continues after the loop"
  ]
}
</script>

<DataStructuresRun :run="run" layout="pair">

```python {1-2,4|1-2,4|1-2,4|1-3|5}
for letter in "Programming":
    if letter == "i":
        break
    print("Current Letter :", letter)
print("After second loop!")
```

<template #visual="{ step }">
<CoreLoop :run="run" :step="step" :label-width="190" />
</template>
</DataStructuresRun>
