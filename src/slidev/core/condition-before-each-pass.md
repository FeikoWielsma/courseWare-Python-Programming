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
    {"names": {"names": {"x": "i1"}}, "objects": {"i1": {"type": "int", "value": "1"}}, "active": ["names.x"], "mark": {"object": "i1"}},
    {"names": {"names": {"x": "i2"}}, "objects": {"i1": {"type": "int", "value": "1"}, "i2": {"type": "int", "value": "2"}}, "active": ["names.x"], "mark": {"object": "i2"}},
    {"names": {"names": {"x": "i3"}}, "objects": {"i1": {"type": "int", "value": "1"}, "i2": {"type": "int", "value": "2"}, "i3": {"type": "int", "value": "3"}}, "active": ["names.x"], "mark": {"object": "i3"}},
    {"names": {"names": {"x": "i4"}}, "objects": {"i1": {"type": "int", "value": "1"}, "i2": {"type": "int", "value": "2"}, "i3": {"type": "int", "value": "3"}, "i4": {"type": "int", "value": "4"}}, "active": ["names.x"], "mark": {"object": "i4"}},
    {"names": {"names": {"x": "i5"}}, "objects": {"i1": {"type": "int", "value": "1"}, "i2": {"type": "int", "value": "2"}, "i3": {"type": "int", "value": "3"}, "i4": {"type": "int", "value": "4"}, "i5": {"type": "int", "value": "5"}}, "active": ["names.x"], "mark": {"object": "i5"}},
    {"names": {"names": {"x": "i6"}}, "objects": {"i1": {"type": "int", "value": "1"}, "i2": {"type": "int", "value": "2"}, "i3": {"type": "int", "value": "3"}, "i4": {"type": "int", "value": "4"}, "i5": {"type": "int", "value": "5"}, "i6": {"type": "int", "value": "6"}}, "active": ["names.x"], "mark": {"object": "i6"}},
    {"names": {"names": {"x": "i6"}}, "objects": {"i1": {"type": "int", "value": "1"}, "i2": {"type": "int", "value": "2"}, "i3": {"type": "int", "value": "3"}, "i4": {"type": "int", "value": "4"}, "i5": {"type": "int", "value": "5"}, "i6": {"type": "int", "value": "6"}}, "active": ["names.x"]}
  ],
  "output": [[], ["1"], ["2"], ["3"], ["4"], ["5"], []],
  "captions": [
    "`x` refers to `1`",
    "`1 <= 5` is true, so the block runs; it prints `1` and rebinds `x` to `2`",
    "The condition is tested again before each pass; `2 <= 5` is true",
    "`x += 1` works out `x + 1` and rebinds `x` to the result",
    "Each pass prints the value `x` refers to at that moment",
    "`5 <= 5` is still true, so `5` is printed and `x` becomes `6`",
    "`6 <= 5` is false, so the loop ends without running the block"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|2-4|2-4|2-4|2-4|2-4|2}
x = 1
while x <= 5:
    print(x)
    x += 1
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="160" :gap="70" :cell-width="64" direction="row" />
</template>
</DataStructuresRun>
