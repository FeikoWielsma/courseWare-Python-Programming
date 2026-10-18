---
layout: default
title: Several Names for One Object
pills: ["demo03 · multipleassignment"]
---

# Several Names for One Object

<script setup>
const run = {
  "frames": [{"id": "names", "label": "names"}],
  "states": [
    {"names": {"names": {"a": "one", "b": "one", "c": "one"}}, "objects": {"one": {"type": "int", "value": "1"}}, "active": ["names.a", "names.b", "names.c"], "mark": {"object": "one"}},
    {"names": {"names": {"a": "one", "b": "one", "c": "one"}}, "objects": {"one": {"type": "int", "value": "1"}}, "active": ["names.a", "names.b", "names.c"]},
    {"names": {"names": {"a": "eleven", "b": "one", "c": "one"}}, "objects": {"one": {"type": "int", "value": "1"}, "eleven": {"type": "int", "value": "11"}}, "active": ["names.a"], "mark": {"object": "eleven"}},
    {"names": {"names": {"a": "eleven", "b": "one", "c": "one"}}, "objects": {"one": {"type": "int", "value": "1"}, "eleven": {"type": "int", "value": "11"}}, "active": ["names.a", "names.b", "names.c"]},
    {"names": {"names": {"a": "one", "b": "two", "c": "john"}}, "objects": {"one": {"type": "int", "value": "1"}, "eleven": {"type": "int", "value": "11"}, "two": {"type": "int", "value": "2"}, "john": {"type": "str", "value": "'john'"}}, "active": ["names.a", "names.b", "names.c"], "mark": [{"object": "two"}, {"object": "john"}]},
    {"names": {"names": {"a": "one", "b": "two", "c": "john"}}, "objects": {"one": {"type": "int", "value": "1"}, "two": {"type": "int", "value": "2"}, "john": {"type": "str", "value": "'john'"}}, "active": ["names.a", "names.b", "names.c"]}
  ],
  "output": [[], ["1 1 1"], [], ["11 1 1"], [], ["1 2 john"]],
  "captions": [
    "`a = b = c = 1` binds three names to one `int` object",
    "All three names show `1`, because they refer to the same object",
    "`a = 11` rebinds only `a`; `b` and `c` still refer to `1`",
    "The integer `1` was never changed, only the binding of `a`",
    "Each name gets the object in its position; `a` is bound to the existing `1` again",
    "The three names now refer to three different objects"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|2|3|4|5|6}
a = b = c = 1
print(a, b, c)
a = 11
print(a, b, c)
a, b, c = 1, 2, "john"
print(a, b, c)
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="200" :gap="150" />
</template>
</DataStructuresRun>
