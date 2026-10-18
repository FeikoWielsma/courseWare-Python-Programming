---
layout: default
title: Handing Back a Result
pills: ["demo11 · returnstatement"]
---

# Handing Back a Result

<script setup>
const run = {
  "frames": [{"id": "global", "label": "global"}, {"id": "call", "label": "summation()"}],
  "order": ["fn", "i10", "i20", "i30"],
  "states": [
    {"names": {"global": {"summation": "fn"}}, "objects": {"fn": {"type": "function", "value": "summation"}}, "active": ["global.summation"], "mark": {"object": "fn"}},
    {"names": {"global": {"summation": "fn"}, "call": {"arg1": "i10", "arg2": "i20"}}, "objects": {"fn": {"type": "function", "value": "summation"}, "i10": {"type": "int", "value": "10"}, "i20": {"type": "int", "value": "20"}}, "active": ["call.arg1", "call.arg2"], "mark": [{"object": "i10"}, {"object": "i20"}]},
    {"names": {"global": {"summation": "fn"}, "call": {"arg1": "i10", "arg2": "i20", "tot": "i30"}}, "objects": {"fn": {"type": "function", "value": "summation"}, "i10": {"type": "int", "value": "10"}, "i20": {"type": "int", "value": "20"}, "i30": {"type": "int", "value": "30"}}, "active": ["call.arg1", "call.arg2", "call.tot"], "mark": {"object": "i30"}},
    {"names": {"global": {"summation": "fn"}, "call": {"arg1": "i10", "arg2": "i20", "tot": "i30"}}, "objects": {"fn": {"type": "function", "value": "summation"}, "i10": {"type": "int", "value": "10"}, "i20": {"type": "int", "value": "20"}, "i30": {"type": "int", "value": "30"}}, "active": ["call.tot"]},
    {"names": {"global": {"summation": "fn"}, "call": {"arg1": "i10", "arg2": "i20", "tot": "i30", "return": "i30"}}, "objects": {"fn": {"type": "function", "value": "summation"}, "i10": {"type": "int", "value": "10"}, "i20": {"type": "int", "value": "20"}, "i30": {"type": "int", "value": "30"}}, "active": ["call.tot", "call.return"]},
    {"names": {"global": {"summation": "fn", "total": "i30"}}, "objects": {"fn": {"type": "function", "value": "summation"}, "i10": {"type": "int", "value": "10"}, "i20": {"type": "int", "value": "20"}, "i30": {"type": "int", "value": "30"}}, "active": ["global.total"], "mark": {"object": "i30"}},
    {"names": {"global": {"summation": "fn", "total": "i30"}}, "objects": {"fn": {"type": "function", "value": "summation"}, "i30": {"type": "int", "value": "30"}}, "active": ["global.total"]}
  ],
  "output": [[], [], [], ["Inside the function : 30"], [], [], ["Outside the function : 30"]],
  "captions": [
    "`def` binds `summation` to a function object; the body does not run yet",
    "The call binds the parameters `arg1` and `arg2` to the arguments",
    "`tot` is a local name for the sum",
    "Inside the function, `tot` refers to `30`",
    "`return tot` hands that object back to the caller and ends the call",
    "The result of the call is bound to `total`; it is the same object, not a copy",
    "Only `total` remains; the parameters and `tot` ended with the call"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|6|2|3|4|6|7}
def summation(arg1: int, arg2: int) -> int:
    tot = arg1 + arg2
    print("Inside the function :", tot)
    return tot

total = summation(10, 20)
print("Outside the function :", total)
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="210" :gap="120" />
</template>
</DataStructuresRun>
