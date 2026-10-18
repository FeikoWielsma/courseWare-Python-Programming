---
layout: default
title: Computed on Every Read
pills: ["demo06 · computedproperty"]
---

# Computed on Every Read

<script setup>
const run = {
  "boxes": [{"id": "hero", "label": "hero", "tag": "Character object", "x": 0, "y": 0, "width": 250}, {"id": "character", "label": "Character", "tag": "class", "x": 0, "y": 180, "width": 250}],
  "links": [{"from": "hero", "to": "character"}],
  "states": [
    {"attrs": {"character": {"__init__": "function", "is_alive": "property"}}, "mark": [{"box": "character", "attr": "__init__"}, {"box": "character", "attr": "is_alive"}], "active": ["character"]},
    {"attrs": {"character": {"__init__": "function", "is_alive": "property"}, "hero": {"name": "'Aria'", "health": "30"}}, "mark": [{"box": "hero", "attr": "name"}, {"box": "hero", "attr": "health"}], "active": ["hero"]},
    {"attrs": {"character": {"__init__": "function", "is_alive": "property"}, "hero": {"name": "'Aria'", "health": "30"}}, "read": [{"box": "character", "attr": "is_alive", "via": "hero"}, {"box": "hero", "attr": "health"}], "note": {"box": "character", "attr": "is_alive", "text": "30 > 0 is True"}, "active": ["hero", "character"]},
    {"attrs": {"character": {"__init__": "function", "is_alive": "property"}, "hero": {"name": "'Aria'", "health": "0"}}, "mark": [{"box": "hero", "attr": "health", "tone": "change"}], "active": ["hero"]},
    {"attrs": {"character": {"__init__": "function", "is_alive": "property"}, "hero": {"name": "'Aria'", "health": "0"}}, "read": [{"box": "character", "attr": "is_alive", "via": "hero"}, {"box": "hero", "attr": "health"}], "note": {"box": "character", "attr": "is_alive", "text": "0 > 0 is False"}, "active": ["hero", "character"]},
    {"attrs": {"character": {"__init__": "function", "is_alive": "property"}, "hero": {"name": "'Aria'", "health": "0"}}, "read": [{"box": "character", "attr": "is_alive", "via": "hero"}], "mark": [{"box": "character", "attr": "is_alive", "tone": "remove"}], "note": {"box": "character", "attr": "is_alive", "text": "no setter", "tone": "remove"}, "active": ["hero", "character"]}
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
    "`Character(\"Aria\", 30)` makes an object; `__init__` stores only `name` and `health` on it",
    "`hero.is_alive` is not on the object, so Python finds the property on the class; its getter returns `self.health > 0`",
    "Assigning `hero.health` changes the stored value; there is no stored `is_alive` to update",
    "Reading `hero.is_alive` again computes it from the current `health`",
    "The property has no setter, so assigning `hero.is_alive` raises `AttributeError`"
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

hero = Character("Aria", 30)
print(hero.is_alive)  # no parentheses
hero.health = 0
print(hero.is_alive)  # always current
hero.is_alive = True  # read-only : there is no setter
```

<template #visual="{ step }">
<StatefulObjects :run="run" :step="step" />
</template>
</DataStructuresRun>
