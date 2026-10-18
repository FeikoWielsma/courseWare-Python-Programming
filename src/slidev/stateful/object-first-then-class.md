---
layout: default
title: Object First, Then Class
pills: ["demo03 · classattributes"]
---

# Object First, Then Class

<script setup>
const run = {
  "boxes": [{"id": "a", "label": "a", "tag": "Car object", "x": 0, "y": 0, "width": 210}, {"id": "car", "label": "Car", "tag": "class", "x": 290, "y": 0, "width": 210}, {"id": "b", "label": "b", "tag": "Car object", "x": 580, "y": 0, "width": 190}],
  "links": [{"from": "a", "to": "car"}, {"from": "b", "to": "car"}],
  "states": [
    {"attrs": {"car": {"wheels": "4", "__init__": "function"}}, "mark": [{"box": "car", "attr": "wheels"}, {"box": "car", "attr": "__init__"}], "active": ["car"]},
    {"attrs": {"car": {"wheels": "4", "__init__": "function"}, "a": {"plate": "'ABC 111'"}}, "mark": [{"box": "a", "attr": "plate"}], "active": ["a"]},
    {"attrs": {"car": {"wheels": "4", "__init__": "function"}, "a": {"plate": "'ABC 111'"}, "b": {"plate": "'XYX 123'"}}, "mark": [{"box": "b", "attr": "plate"}], "active": ["b"]},
    {"attrs": {"car": {"wheels": "4", "__init__": "function"}, "a": {"plate": "'ABC 111'"}, "b": {"plate": "'XYX 123'"}}, "read": [{"box": "a", "attr": "plate"}, {"box": "b", "attr": "plate"}], "active": ["a", "b"]},
    {"attrs": {"car": {"wheels": "4", "__init__": "function"}, "a": {"plate": "'ABC 111'"}, "b": {"plate": "'XYX 123'"}}, "read": [{"box": "car", "attr": "wheels", "via": "a"}, {"box": "car", "attr": "wheels", "via": "b"}], "active": ["a", "b", "car"]},
    {"attrs": {"car": {"wheels": "6", "__init__": "function"}, "a": {"plate": "'ABC 111'"}, "b": {"plate": "'XYX 123'"}}, "mark": [{"box": "car", "attr": "wheels", "tone": "change"}], "active": ["car"]},
    {"attrs": {"car": {"wheels": "6", "__init__": "function"}, "a": {"plate": "'ABC 111'"}, "b": {"plate": "'XYX 123'"}}, "read": [{"box": "car", "attr": "wheels", "via": "a"}, {"box": "car", "attr": "wheels", "via": "b"}], "active": ["a", "b", "car"]},
    {"attrs": {"car": {"wheels": "6", "__init__": "function"}, "a": {"plate": "'ABC 111'", "wheels": "3"}, "b": {"plate": "'XYX 123'"}}, "mark": [{"box": "a", "attr": "wheels"}], "active": ["a"]},
    {"attrs": {"car": {"wheels": "6", "__init__": "function"}, "a": {"plate": "'ABC 111'", "wheels": "3"}, "b": {"plate": "'XYX 123'"}}, "read": [{"box": "a", "attr": "wheels"}, {"box": "car", "attr": "wheels", "via": "b"}, {"box": "car", "attr": "wheels"}], "active": ["a", "b", "car"]}
  ],
  "output": [
    [],
    [],
    [],
    ["ABC 111 XYX 123"],
    ["4 4"],
    [],
    ["6 6"],
    [],
    ["3 6 6"]
  ],
  "captions": [
    "The class body runs once : the class `Car` holds `wheels` and the function `__init__`",
    "Calling `Car` makes an object, and `__init__` stores `plate` on it",
    "A second object, with its own `plate`",
    "Each object has its own `plate`",
    "Neither object has `wheels`, so Python looks on the class and finds 4 for both",
    "`Car.wheels = 6` changes the one value both objects share",
    "Both lookups reach the class again and find 6",
    "Assigning `a.wheels` creates an attribute on `a`; the class is not changed",
    "`a.wheels` is found on `a` first; `b.wheels` and `Car.wheels` still read the class"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1-3|6|7|8|9|10|11|12|13}
class Car:
    wheels = 4  # class attribute, one value shared by every car
    def __init__(self, plate: str) -> None:
        self.plate = plate  # instance attribute, one value per car

a = Car("ABC 111")
b = Car("XYX 123")
print(a.plate, b.plate)  # ABC 111 XYX 123
print(a.wheels, b.wheels)  # 4 4
Car.wheels = 6  # changes the shared value
print(a.wheels, b.wheels)  # 6 6
a.wheels = 3  # creates an instance attribute on a only
print(a.wheels, b.wheels, Car.wheels)  # 3 6 6
```

<template #visual="{ step }">
<StatefulObjects :run="run" :step="step" />
</template>
</DataStructuresRun>
