---
layout: default
title: Local and Global Names
pills: ["demo12 · variablescope"]
---

# Local and Global Names

<script setup>
const run = {
  "frames": [{"id": "global", "label": "global"}, {"id": "func1", "label": "func1()"}, {"id": "func2", "label": "func2()"}],
  "order": ["i50", "f1", "f2", "i2"],
  "states": [
    {"names": {"global": {"x": "i50", "y": "i50"}}, "objects": {"i50": {"type": "int", "value": "50"}}, "active": ["global.x", "global.y"], "mark": {"object": "i50"}},
    {"names": {"global": {"x": "i50", "y": "i50", "func1": "f1", "func2": "f2"}}, "objects": {"i50": {"type": "int", "value": "50"}, "f1": {"type": "function", "value": "func1"}, "f2": {"type": "function", "value": "func2"}}, "active": ["global.func1", "global.func2"], "mark": [{"object": "f1"}, {"object": "f2"}]},
    {"names": {"global": {"x": "i50", "y": "i50", "func1": "f1", "func2": "f2"}, "func1": {}}, "objects": {"i50": {"type": "int", "value": "50"}, "f1": {"type": "function", "value": "func1"}, "f2": {"type": "function", "value": "func2"}}, "active": ["global.func1"]},
    {"names": {"global": {"x": "i50", "y": "i50", "func1": "f1", "func2": "f2"}, "func1": {"x": "i2"}}, "objects": {"i50": {"type": "int", "value": "50"}, "f1": {"type": "function", "value": "func1"}, "f2": {"type": "function", "value": "func2"}, "i2": {"type": "int", "value": "2"}}, "active": ["func1.x"], "mark": {"object": "i2"}},
    {"names": {"global": {"x": "i50", "y": "i50", "func1": "f1", "func2": "f2"}, "func1": {"x": "i2"}}, "objects": {"i50": {"type": "int", "value": "50"}, "f1": {"type": "function", "value": "func1"}, "f2": {"type": "function", "value": "func2"}, "i2": {"type": "int", "value": "2"}}, "active": ["func1.x"]},
    {"names": {"global": {"x": "i50", "y": "i50", "func1": "f1", "func2": "f2"}}, "objects": {"i50": {"type": "int", "value": "50"}, "f1": {"type": "function", "value": "func1"}, "f2": {"type": "function", "value": "func2"}, "i2": {"type": "int", "value": "2"}}, "active": ["global.x"]},
    {"names": {"global": {"x": "i50", "y": "i50", "func1": "f1", "func2": "f2"}, "func2": {}}, "objects": {"i50": {"type": "int", "value": "50"}, "f1": {"type": "function", "value": "func1"}, "f2": {"type": "function", "value": "func2"}}, "active": ["global.func2"]},
    {"names": {"global": {"x": "i50", "y": "i2", "func1": "f1", "func2": "f2"}, "func2": {"global y": null}}, "objects": {"i50": {"type": "int", "value": "50"}, "f1": {"type": "function", "value": "func1"}, "f2": {"type": "function", "value": "func2"}, "i2": {"type": "int", "value": "2"}}, "active": ["global.y", "func2.global y"], "mark": {"object": "i2"}},
    {"names": {"global": {"x": "i50", "y": "i2", "func1": "f1", "func2": "f2"}}, "objects": {"i50": {"type": "int", "value": "50"}, "f1": {"type": "function", "value": "func1"}, "f2": {"type": "function", "value": "func2"}, "i2": {"type": "int", "value": "2"}}, "active": ["global.y"]}
  ],
  "output": [[], [], [], [], ["Local x   : 2"], ["x is still: 50"], [], [], ["y is now  : 2"]],
  "captions": [
    "`x` and `y` are global names, both referring to `50`",
    "The two `def` statements bind `func1` and `func2`; the bodies do not run yet",
    "Calling `func1` starts a new local scope",
    "`x = 2` creates a local `x`; the global `x` is not touched",
    "Inside `func1` the local `x` is found first",
    "The local scope ends with the call; the global `x` is still `50`",
    "Calling `func2` starts another local scope",
    "`global y` makes `y` mean the global name, so `y = 2` rebinds it",
    "The global `y` now refers to `2`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1-2|4,8|12|5|6|13|14|9-10|15}
x = 50
y = 50

def func1() -> None:
    x = 2
    print("Local x   :", x)

def func2() -> None:
    global y
    y = 2

func1()
print("x is still:", x)
func2()
print("y is now  :", y)
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="200" :gap="120" />
</template>
</DataStructuresRun>
