---
layout: default
title: Computed on Every Read
pills: ["demo06 · computedproperty"]
---

# Computed on Every Read

<script setup>
const run = {
  "boxes": [{"id": "sq", "label": "sq", "tag": "Square object", "x": 0, "y": 0, "width": 250}, {"id": "square", "label": "Square", "tag": "class", "x": 0, "y": 150, "width": 250}],
  "links": [{"from": "sq", "to": "square"}],
  "states": [
    {"attrs": {"square": {"__init__": "function", "area": "property"}}, "mark": [{"box": "square", "attr": "__init__"}, {"box": "square", "attr": "area"}], "active": ["square"]},
    {"attrs": {"square": {"__init__": "function", "area": "property"}, "sq": {"length": "5"}}, "mark": [{"box": "sq", "attr": "length"}], "active": ["sq"]},
    {"attrs": {"square": {"__init__": "function", "area": "property"}, "sq": {"length": "5"}}, "read": [{"box": "square", "attr": "area", "via": "sq"}, {"box": "sq", "attr": "length"}], "note": {"box": "square", "attr": "area", "text": "5 * 5 = 25"}, "active": ["sq", "square"]},
    {"attrs": {"square": {"__init__": "function", "area": "property"}, "sq": {"length": "6"}}, "mark": [{"box": "sq", "attr": "length", "tone": "change"}], "active": ["sq"]},
    {"attrs": {"square": {"__init__": "function", "area": "property"}, "sq": {"length": "6"}}, "read": [{"box": "square", "attr": "area", "via": "sq"}, {"box": "sq", "attr": "length"}], "note": {"box": "square", "attr": "area", "text": "6 * 6 = 36"}, "active": ["sq", "square"]},
    {"attrs": {"square": {"__init__": "function", "area": "property"}, "sq": {"length": "6"}}, "read": [{"box": "square", "attr": "area", "via": "sq"}], "mark": [{"box": "square", "attr": "area", "tone": "remove"}], "note": {"box": "square", "attr": "area", "text": "no setter", "tone": "remove"}, "active": ["sq", "square"]}
  ],
  "output": [
    [],
    [],
    ["25"],
    [],
    ["36"],
    ["AttributeError: property 'area' of 'Square' object has no setter"]
  ],
  "captions": [
    "The class holds `__init__` and `area`; `@property` makes `area` a property",
    "`Square(5)` makes an object; `__init__` stores only `length` on it",
    "`sq.area` is not on the object, so Python finds the property on the class; its getter returns `self.length * self.length`",
    "Assigning `sq.length` changes the stored value; there is no stored area to update",
    "Reading `sq.area` again computes it from the current `length`",
    "The property has no setter, so assigning `sq.area` raises `AttributeError`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1-5|8|9|10|11|12}
class Square:
    def __init__(self, length: float) -> None:
        self.length = length
    @property
    def area(self) -> float:
        return self.length * self.length

sq = Square(5)
print(sq.area)  # no parentheses
sq.length = 6
print(sq.area)  # always current
sq.area = 50  # read-only : there is no setter
```

<template #visual="{ step }">
<StatefulObjects :run="run" :step="step" />
</template>
</DataStructuresRun>
