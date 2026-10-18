---
layout: default
title: Computed on Every Read
pills: ["demo07 · computedproperty"]
---

# Computed on Every Read

<script setup>
const run = {
  "boxes": [{"id": "jaina", "label": "jaina", "tag": "Character object", "x": 0, "y": 0, "width": 250}, {"id": "character", "label": "Character", "tag": "class", "x": 0, "y": 180, "width": 250}],
  "links": [{"from": "jaina", "to": "character"}],
  "states": [
    {"attrs": {"character": {"__init__": "function", "is_alive": "property"}}, "mark": [{"box": "character", "attr": "__init__"}, {"box": "character", "attr": "is_alive"}], "active": ["character"]},
    {"attrs": {"character": {"__init__": "function", "is_alive": "property"}, "jaina": {"name": "'Jaina'", "health": "30"}}, "mark": [{"box": "jaina", "attr": "name"}, {"box": "jaina", "attr": "health"}], "active": ["jaina"]},
    {"attrs": {"character": {"__init__": "function", "is_alive": "property"}, "jaina": {"name": "'Jaina'", "health": "30"}}, "read": [{"box": "character", "attr": "is_alive", "via": "jaina"}, {"box": "jaina", "attr": "health"}], "note": {"box": "character", "attr": "is_alive", "text": "30 > 0 is True"}, "active": ["jaina", "character"]},
    {"attrs": {"character": {"__init__": "function", "is_alive": "property"}, "jaina": {"name": "'Jaina'", "health": "0"}}, "mark": [{"box": "jaina", "attr": "health", "tone": "change"}], "active": ["jaina"]},
    {"attrs": {"character": {"__init__": "function", "is_alive": "property"}, "jaina": {"name": "'Jaina'", "health": "0"}}, "read": [{"box": "character", "attr": "is_alive", "via": "jaina"}, {"box": "jaina", "attr": "health"}], "note": {"box": "character", "attr": "is_alive", "text": "0 > 0 is False"}, "active": ["jaina", "character"]},
    {"attrs": {"character": {"__init__": "function", "is_alive": "property"}, "jaina": {"name": "'Jaina'", "health": "0"}}, "read": [{"box": "character", "attr": "is_alive", "via": "jaina"}], "mark": [{"box": "character", "attr": "is_alive", "tone": "remove"}], "note": {"box": "character", "attr": "is_alive", "text": "no setter", "tone": "remove"}, "active": ["jaina", "character"]}
  ],
  "output": [
    [],
    [],
    ["True"],
    [],
    ["False"],
    ["AttributeError: property 'is_alive' of 'Character' object has no setter"]
  ],
  "captions": [
    "The class holds `__init__` and `is_alive`; `@property` makes `is_alive` a property",
    "`Character(\"Jaina\", 30)` makes an object; `__init__` stores only `name` and `health` on it",
    "`jaina.is_alive` is not on the object, so Python finds the property on the class; its getter returns `self.health > 0`",
    "Assigning `jaina.health` changes the stored value; there is no stored `is_alive` to update",
    "Reading `jaina.is_alive` again computes it from the current `health`",
    "The property has no setter, so assigning `jaina.is_alive` raises `AttributeError`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1-7|9|10|11|12|13}
class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
    @property
    def is_alive(self) -> bool:
        return self.health > 0

jaina = Character("Jaina", 30)
print(jaina.is_alive)  # no parentheses
jaina.health = 0
print(jaina.is_alive)  # always current
jaina.is_alive = True  # read-only : there is no setter
```

<template #visual="{ step }">
<StatefulObjects :run="run" :step="step" />
</template>
</DataStructuresRun>
