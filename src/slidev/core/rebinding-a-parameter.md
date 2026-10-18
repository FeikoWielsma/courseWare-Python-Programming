---
layout: default
title: Rebinding a Parameter
pills: ["demo03 · overwritingreferences"]
---

# Rebinding a Parameter

<script setup>
const run = {
  "frames": [{"id": "global", "label": "global"}, {"id": "call", "label": "change_me2()"}],
  "states": [
    {"names": {"global": {"change_me2": "fn"}}, "objects": {"fn": {"type": "function", "value": "change_me2"}}, "active": ["global.change_me2"], "mark": {"object": "fn"}},
    {"names": {"global": {"change_me2": "fn", "my_list_outer": "outer"}}, "objects": {"fn": {"type": "function", "value": "change_me2"}, "outer": {"type": "list", "items": ["10", "20", "30"]}}, "active": ["global.my_list_outer"], "mark": {"object": "outer"}},
    {"names": {"global": {"change_me2": "fn", "my_list_outer": "outer"}, "call": {"mylist": "outer"}}, "objects": {"fn": {"type": "function", "value": "change_me2"}, "outer": {"type": "list", "items": ["10", "20", "30"]}}, "active": ["global.my_list_outer", "call.mylist"]},
    {"names": {"global": {"change_me2": "fn", "my_list_outer": "outer"}, "call": {"mylist": "new"}}, "objects": {"fn": {"type": "function", "value": "change_me2"}, "outer": {"type": "list", "items": ["10", "20", "30"]}, "new": {"type": "list", "items": ["1", "2", "3", "4"]}}, "active": ["call.mylist"], "mark": {"object": "new"}},
    {"names": {"global": {"change_me2": "fn", "my_list_outer": "outer"}, "call": {"mylist": "new"}}, "objects": {"fn": {"type": "function", "value": "change_me2"}, "outer": {"type": "list", "items": ["10", "20", "30"]}, "new": {"type": "list", "items": ["1", "2", "3", "4"]}}, "active": ["call.mylist"]},
    {"names": {"global": {"change_me2": "fn", "my_list_outer": "outer"}}, "objects": {"fn": {"type": "function", "value": "change_me2"}, "outer": {"type": "list", "items": ["10", "20", "30"]}, "new": {"type": "list", "items": ["1", "2", "3", "4"]}}, "active": ["global.my_list_outer"]}
  ],
  "output": [[], [], [], [], ["Values inside the function change_me2: [1, 2, 3, 4]"], ["Values outside the function: [10, 20, 30]"]],
  "captions": [
    "`def` binds the name `change_me2` to a function object",
    "`my_list_outer` refers to a new list",
    "As before, the call binds `mylist` to the caller's list",
    "Assignment rebinds the local name `mylist` to a new list; the caller's list is untouched",
    "Inside the function, `mylist` shows the new list",
    "The call has returned; the new list has no name, and `my_list_outer` is unchanged"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="560px">

```python {1|5|6|2|3|7}
def change_me2(mylist: list[int]) -> None:
    mylist = [1, 2, 3, 4]  # This would assign new reference
    print("Values inside the function change_me2:", mylist)

my_list_outer = [10, 20, 30]
change_me2(my_list_outer)
print("Values outside the function:", my_list_outer)
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="230" :gap="110" :cell-width="54" />
</template>
</DataStructuresRun>
