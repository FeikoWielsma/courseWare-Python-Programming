---
layout: default
title: The Condition Before Each Pass
pills: ["demo05 · while"]
---

# The Condition Before Each Pass

<script setup>
const run = {
  "frames": [{"id": "names", "label": "names"}],
  "states": [
    {"names": {"names": {"shot": "i1"}}, "objects": {"i1": {"type": "int", "value": "1"}}, "active": ["names.shot"], "mark": {"object": "i1"}},
    {"names": {"names": {"shot": "i2"}}, "objects": {"i1": {"type": "int", "value": "1"}, "i2": {"type": "int", "value": "2"}}, "active": ["names.shot"], "mark": {"object": "i2"}},
    {"names": {"names": {"shot": "i3"}}, "objects": {"i1": {"type": "int", "value": "1"}, "i2": {"type": "int", "value": "2"}, "i3": {"type": "int", "value": "3"}}, "active": ["names.shot"], "mark": {"object": "i3"}},
    {"names": {"names": {"shot": "i4"}}, "objects": {"i1": {"type": "int", "value": "1"}, "i2": {"type": "int", "value": "2"}, "i3": {"type": "int", "value": "3"}, "i4": {"type": "int", "value": "4"}}, "active": ["names.shot"], "mark": {"object": "i4"}},
    {"names": {"names": {"shot": "i5"}}, "objects": {"i1": {"type": "int", "value": "1"}, "i2": {"type": "int", "value": "2"}, "i3": {"type": "int", "value": "3"}, "i4": {"type": "int", "value": "4"}, "i5": {"type": "int", "value": "5"}}, "active": ["names.shot"], "mark": {"object": "i5"}},
    {"names": {"names": {"shot": "i6"}}, "objects": {"i1": {"type": "int", "value": "1"}, "i2": {"type": "int", "value": "2"}, "i3": {"type": "int", "value": "3"}, "i4": {"type": "int", "value": "4"}, "i5": {"type": "int", "value": "5"}, "i6": {"type": "int", "value": "6"}}, "active": ["names.shot"], "mark": {"object": "i6"}},
    {"names": {"names": {"shot": "i6"}}, "objects": {"i1": {"type": "int", "value": "1"}, "i2": {"type": "int", "value": "2"}, "i3": {"type": "int", "value": "3"}, "i4": {"type": "int", "value": "4"}, "i5": {"type": "int", "value": "5"}, "i6": {"type": "int", "value": "6"}}, "active": ["names.shot"]}
  ],
  "output": [[], ["Photo 1"], ["Photo 2"], ["Photo 3"], ["Photo 4"], ["Photo 5"], []],
  "captions": [
    "`shot` refers to `1`",
    "`1 <= 5` is true, so the block runs; it prints `Photo 1` and rebinds `shot` to `2`",
    "The condition is tested again before each pass; `2 <= 5` is true",
    "`shot += 1` works out `shot + 1` and rebinds `shot` to the result",
    "Each pass labels a photo with the current `shot` number",
    "`5 <= 5` is still true, so `Photo 5` is printed and `shot` becomes `6`",
    "`6 <= 5` is false, so the loop ends without running the block"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|2-4|2-4|2-4|2-4|2-4|2}
shot = 1
while shot <= 5:
    print(f"Photo {shot}")
    shot += 1
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="160" :gap="70" :cell-width="64" direction="row" />
</template>
</DataStructuresRun>
