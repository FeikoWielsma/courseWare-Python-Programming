---
layout: default
title: Binding and Rebinding Names
pills: ["demo01 · variables"]
---

# Binding and Rebinding Names

<script setup>
const run = {
  "frames": [{"id": "names", "label": "names"}],
  "order": ["s1", "s2", "s3", "i10", "i20", "i30"],
  "states": [
    {"names": {"names": {"first": "i10"}}, "objects": {"i10": {"type": "int", "value": "10"}}, "active": ["names.first"], "mark": {"object": "i10"}},
    {"names": {"names": {"first": "i10", "second": "i20"}}, "objects": {"i10": {"type": "int", "value": "10"}, "i20": {"type": "int", "value": "20"}}, "active": ["names.second"], "mark": {"object": "i20"}},
    {"names": {"names": {"first": "i10", "second": "i20", "combined": "i30"}}, "objects": {"i10": {"type": "int", "value": "10"}, "i20": {"type": "int", "value": "20"}, "i30": {"type": "int", "value": "30"}}, "active": ["names.first", "names.second", "names.combined"], "mark": {"object": "i30"}},
    {"names": {"names": {"first": "i10", "second": "i20", "combined": "i30"}}, "objects": {"i10": {"type": "int", "value": "10"}, "i20": {"type": "int", "value": "20"}, "i30": {"type": "int", "value": "30"}}, "active": ["names.combined"]},
    {"names": {"names": {"first": "s1", "second": "i20", "combined": "i30"}}, "objects": {"i10": {"type": "int", "value": "10"}, "i20": {"type": "int", "value": "20"}, "i30": {"type": "int", "value": "30"}, "s1": {"type": "str", "value": "'Orbit '"}}, "active": ["names.first"], "mark": {"object": "s1"}},
    {"names": {"names": {"first": "s1", "second": "s2", "combined": "i30"}}, "objects": {"i20": {"type": "int", "value": "20"}, "i30": {"type": "int", "value": "30"}, "s1": {"type": "str", "value": "'Orbit '"}, "s2": {"type": "str", "value": "'Echo'"}}, "active": ["names.second"], "mark": {"object": "s2"}},
    {"names": {"names": {"first": "s1", "second": "s2", "combined": "s3"}}, "objects": {"i30": {"type": "int", "value": "30"}, "s1": {"type": "str", "value": "'Orbit '"}, "s2": {"type": "str", "value": "'Echo'"}, "s3": {"type": "str", "value": "'Orbit Echo'"}}, "active": ["names.first", "names.second", "names.combined"], "mark": {"object": "s3"}},
    {"names": {"names": {"first": "s1", "second": "s2", "combined": "s3"}}, "objects": {"s1": {"type": "str", "value": "'Orbit '"}, "s2": {"type": "str", "value": "'Echo'"}, "s3": {"type": "str", "value": "'Orbit Echo'"}}, "active": ["names.combined"]}
  ],
  "output": [[], [], [], ["30"], [], [], [], ["Orbit Echo"]],
  "captions": [
    "`first = 10` binds the name `first` to an `int` object",
    "Each assignment binds one more name",
    "`first + second` makes a new object, `30`, and `combined` is bound to it",
    "`print(combined)` follows the name to its object",
    "Rebinding `first` moves the name to a `str` object; `10` has no name left",
    "`second` is rebound the same way; the type belongs to the object, not the name",
    "The same expression on two strings makes a new, joined `str`",
    "The same names and the same code, now working on strings"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|2|3|4|5|6|7|8}
first = 10
second = 20
combined = first + second
print(combined)
first = "Orbit "
second = "Echo"
combined = first + second
print(combined)
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="200" :gap="130" />
</template>
</DataStructuresRun>
