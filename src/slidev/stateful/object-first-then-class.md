---
layout: default
title: Object First, Then Class
pills: ["demo04 · classattributes"]
---

# Object First, Then Class

<script setup>
const run = {
  "boxes": [{"id": "jaina", "label": "jaina", "tag": "Character object", "x": 0, "y": 0, "width": 215}, {"id": "character", "label": "Character", "tag": "class", "x": 280, "y": 0, "width": 215}, {"id": "thrall", "label": "thrall", "tag": "Character object", "x": 560, "y": 0, "width": 215}],
  "links": [{"from": "jaina", "to": "character"}, {"from": "thrall", "to": "character"}],
  "states": [
    {"attrs": {"character": {"max_level": "60", "__init__": "function"}}, "mark": [{"box": "character", "attr": "max_level"}, {"box": "character", "attr": "__init__"}], "active": ["character"]},
    {"attrs": {"character": {"max_level": "60", "__init__": "function"}, "jaina": {"name": "'Jaina'"}}, "mark": [{"box": "jaina", "attr": "name"}], "active": ["jaina"]},
    {"attrs": {"character": {"max_level": "60", "__init__": "function"}, "jaina": {"name": "'Jaina'"}, "thrall": {"name": "'Thrall'"}}, "mark": [{"box": "thrall", "attr": "name"}], "active": ["thrall"]},
    {"attrs": {"character": {"max_level": "60", "__init__": "function"}, "jaina": {"name": "'Jaina'"}, "thrall": {"name": "'Thrall'"}}, "read": [{"box": "jaina", "attr": "name"}, {"box": "thrall", "attr": "name"}], "active": ["jaina", "thrall"]},
    {"attrs": {"character": {"max_level": "60", "__init__": "function"}, "jaina": {"name": "'Jaina'"}, "thrall": {"name": "'Thrall'"}}, "read": [{"box": "character", "attr": "max_level", "via": "jaina"}, {"box": "character", "attr": "max_level", "via": "thrall"}], "active": ["jaina", "thrall", "character"]},
    {"attrs": {"character": {"max_level": "70", "__init__": "function"}, "jaina": {"name": "'Jaina'"}, "thrall": {"name": "'Thrall'"}}, "mark": [{"box": "character", "attr": "max_level", "tone": "change"}], "active": ["character"]},
    {"attrs": {"character": {"max_level": "70", "__init__": "function"}, "jaina": {"name": "'Jaina'"}, "thrall": {"name": "'Thrall'"}}, "read": [{"box": "character", "attr": "max_level", "via": "jaina"}, {"box": "character", "attr": "max_level", "via": "thrall"}], "active": ["jaina", "thrall", "character"]},
    {"attrs": {"character": {"max_level": "70", "__init__": "function"}, "jaina": {"name": "'Jaina'", "max_level": "80"}, "thrall": {"name": "'Thrall'"}}, "mark": [{"box": "jaina", "attr": "max_level"}], "active": ["jaina"]},
    {"attrs": {"character": {"max_level": "70", "__init__": "function"}, "jaina": {"name": "'Jaina'", "max_level": "80"}, "thrall": {"name": "'Thrall'"}}, "read": [{"box": "jaina", "attr": "max_level"}, {"box": "character", "attr": "max_level", "via": "thrall"}, {"box": "character", "attr": "max_level"}], "active": ["jaina", "thrall", "character"]}
  ],
  "output": [
    [],
    [],
    [],
    ["Jaina Thrall"],
    ["60 60"],
    [],
    ["70 70"],
    [],
    ["80 70 70"]
  ],
  "captions": [
    "The class body runs once : the class `Character` holds `max_level` and the function `__init__`",
    "Calling `Character` makes an object, and `__init__` stores `name` on it",
    "A second object, with its own `name`",
    "Each object has its own `name`",
    "Neither object has `max_level`, so Python looks on the class and finds 60 for both",
    "`Character.max_level = 70` raises the one cap both characters share",
    "Both lookups reach the class again and find 70",
    "Assigning `jaina.max_level` creates an attribute on `jaina`; the class is not changed",
    "`jaina.max_level` is found on `jaina` first; `thrall.max_level` and `Character.max_level` still read the class"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1-3|6|7|8|9|10|11|12|13}
class Character:
    max_level = 60  # class attribute, one value shared by every character
    def __init__(self, name: str) -> None:
        self.name = name  # instance attribute, one value per character

jaina = Character("Jaina")
thrall = Character("Thrall")
print(jaina.name, thrall.name)  # Jaina Thrall
print(jaina.max_level, thrall.max_level)  # 60 60
Character.max_level = 70  # an expansion raises the cap for everyone
print(jaina.max_level, thrall.max_level)  # 70 70
jaina.max_level = 80  # creates an instance attribute on jaina only
print(jaina.max_level, thrall.max_level, Character.max_level)  # 80 70 70
```

<template #visual="{ step }">
<StatefulObjects :run="run" :step="step" />
</template>
</DataStructuresRun>
