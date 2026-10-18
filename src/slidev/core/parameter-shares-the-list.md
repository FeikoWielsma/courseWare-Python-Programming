---
layout: default
title: A Parameter Shares the List
pills: ["demo02 · objectreferences"]
---

# A Parameter Shares the List

<script setup>
const run = {
  "frames": [{"id": "global", "label": "global"}, {"id": "call", "label": "change_me1()"}],
  "states": [
    {"names": {"global": {"change_me1": "fn"}}, "objects": {"fn": {"type": "function", "value": "change_me1"}}, "active": ["global.change_me1"], "mark": {"object": "fn"}},
    {"names": {"global": {"change_me1": "fn", "my_list_outer": "outer"}}, "objects": {"fn": {"type": "function", "value": "change_me1"}, "outer": {"type": "list", "items": ["10", "20", "30"]}}, "active": ["global.my_list_outer"], "mark": {"object": "outer"}},
    {"names": {"global": {"change_me1": "fn", "my_list_outer": "outer"}, "call": {"mylist": "outer"}}, "objects": {"fn": {"type": "function", "value": "change_me1"}, "outer": {"type": "list", "items": ["10", "20", "30"]}}, "active": ["global.my_list_outer", "call.mylist"]},
    {"names": {"global": {"change_me1": "fn", "my_list_outer": "outer"}, "call": {"mylist": "outer"}}, "objects": {"fn": {"type": "function", "value": "change_me1"}, "outer": {"type": "list", "items": ["10", "20", "30", "40"]}}, "active": ["call.mylist"], "mark": {"object": "outer", "index": 3}},
    {"names": {"global": {"change_me1": "fn", "my_list_outer": "outer"}, "call": {"mylist": "outer"}}, "objects": {"fn": {"type": "function", "value": "change_me1"}, "outer": {"type": "list", "items": ["10", "20", "30", "40"]}}, "active": ["call.mylist"]},
    {"names": {"global": {"change_me1": "fn", "my_list_outer": "outer"}}, "objects": {"fn": {"type": "function", "value": "change_me1"}, "outer": {"type": "list", "items": ["10", "20", "30", "40"]}}, "active": ["global.my_list_outer"]}
  ],
  "output": [[], [], [], [], ["List inside the function change_me1: [10, 20, 30, 40]"], ["List outside the function: [10, 20, 30, 40]"]],
  "captions": [
    "`def` makes a function object and binds the name `change_me1` to it",
    "`my_list_outer` refers to a new list",
    "The call binds the parameter `mylist` to the same list object",
    "`append()` changes that one list through the name `mylist`",
    "Inside the function, `mylist` shows the added item",
    "The call has returned and `mylist` is gone; `my_list_outer` sees the change"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="560px">

```python {1|5|6|2|3|7}
def change_me1(mylist: list[int]) -> None:
    mylist.append(40)
    print("List inside the function change_me1:", mylist)

my_list_outer = [10, 20, 30]
change_me1(my_list_outer)
print("List outside the function:", my_list_outer)
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="230" :gap="110" :cell-width="54" />
</template>
</DataStructuresRun>
