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
    {"names": {"names": {"var1": "i10"}}, "objects": {"i10": {"type": "int", "value": "10"}}, "active": ["names.var1"], "mark": {"object": "i10"}},
    {"names": {"names": {"var1": "i10", "var2": "i20"}}, "objects": {"i10": {"type": "int", "value": "10"}, "i20": {"type": "int", "value": "20"}}, "active": ["names.var2"], "mark": {"object": "i20"}},
    {"names": {"names": {"var1": "i10", "var2": "i20", "var3": "i30"}}, "objects": {"i10": {"type": "int", "value": "10"}, "i20": {"type": "int", "value": "20"}, "i30": {"type": "int", "value": "30"}}, "active": ["names.var1", "names.var2", "names.var3"], "mark": {"object": "i30"}},
    {"names": {"names": {"var1": "i10", "var2": "i20", "var3": "i30"}}, "objects": {"i10": {"type": "int", "value": "10"}, "i20": {"type": "int", "value": "20"}, "i30": {"type": "int", "value": "30"}}, "active": ["names.var3"]},
    {"names": {"names": {"var1": "s1", "var2": "i20", "var3": "i30"}}, "objects": {"i10": {"type": "int", "value": "10"}, "i20": {"type": "int", "value": "20"}, "i30": {"type": "int", "value": "30"}, "s1": {"type": "str", "value": "'somestring'"}}, "active": ["names.var1"], "mark": {"object": "s1"}},
    {"names": {"names": {"var1": "s1", "var2": "s2", "var3": "i30"}}, "objects": {"i20": {"type": "int", "value": "20"}, "i30": {"type": "int", "value": "30"}, "s1": {"type": "str", "value": "'somestring'"}, "s2": {"type": "str", "value": "'otherstring'"}}, "active": ["names.var2"], "mark": {"object": "s2"}},
    {"names": {"names": {"var1": "s1", "var2": "s2", "var3": "s3"}}, "objects": {"i30": {"type": "int", "value": "30"}, "s1": {"type": "str", "value": "'somestring'"}, "s2": {"type": "str", "value": "'otherstring'"}, "s3": {"type": "str", "value": "'somestringotherstring'"}}, "active": ["names.var1", "names.var2", "names.var3"], "mark": {"object": "s3"}},
    {"names": {"names": {"var1": "s1", "var2": "s2", "var3": "s3"}}, "objects": {"s1": {"type": "str", "value": "'somestring'"}, "s2": {"type": "str", "value": "'otherstring'"}, "s3": {"type": "str", "value": "'somestringotherstring'"}}, "active": ["names.var3"]}
  ],
  "output": [[], [], [], ["30"], [], [], [], ["somestringotherstring"]],
  "captions": [
    "`var1 = 10` binds the name `var1` to an `int` object",
    "Each assignment binds one more name",
    "`var1 + var2` makes a new object, `30`, and `var3` is bound to it",
    "`print(var3)` follows the name to its object",
    "Rebinding `var1` moves the name to a `str` object; `10` has no name left",
    "`var2` is rebound the same way; the type belongs to the object, not the name",
    "The same expression on two strings makes a new, joined `str`",
    "The same names and the same code, now working on strings"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|2|3|4|5|6|7|8}
var1 = 10
var2 = 20
var3 = var1 + var2
print(var3)
var1 = "somestring"
var2 = "otherstring"
var3 = var1 + var2
print(var3)
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="200" :gap="130" />
</template>
</DataStructuresRun>
