---
layout: default
title: Object First, Then Class
pills: ["demo03 · classattributes"]
---

# Object First, Then Class

<script setup>
const run = {
  "boxes": [{"id": "hero", "label": "hero", "tag": "Character object", "x": 0, "y": 0, "width": 215}, {"id": "character", "label": "Character", "tag": "class", "x": 280, "y": 0, "width": 215}, {"id": "mage", "label": "mage", "tag": "Character object", "x": 560, "y": 0, "width": 215}],
  "links": [{"from": "hero", "to": "character"}, {"from": "mage", "to": "character"}],
  "states": [
    {"attrs": {"character": {"max_health": "100", "__init__": "function"}}, "mark": [{"box": "character", "attr": "max_health"}, {"box": "character", "attr": "__init__"}], "active": ["character"]},
    {"attrs": {"character": {"max_health": "100", "__init__": "function"}, "hero": {"name": "'Aria'"}}, "mark": [{"box": "hero", "attr": "name"}], "active": ["hero"]},
    {"attrs": {"character": {"max_health": "100", "__init__": "function"}, "hero": {"name": "'Aria'"}, "mage": {"name": "'Lumi'"}}, "mark": [{"box": "mage", "attr": "name"}], "active": ["mage"]},
    {"attrs": {"character": {"max_health": "100", "__init__": "function"}, "hero": {"name": "'Aria'"}, "mage": {"name": "'Lumi'"}}, "read": [{"box": "hero", "attr": "name"}, {"box": "mage", "attr": "name"}], "active": ["hero", "mage"]},
    {"attrs": {"character": {"max_health": "100", "__init__": "function"}, "hero": {"name": "'Aria'"}, "mage": {"name": "'Lumi'"}}, "read": [{"box": "character", "attr": "max_health", "via": "hero"}, {"box": "character", "attr": "max_health", "via": "mage"}], "active": ["hero", "mage", "character"]},
    {"attrs": {"character": {"max_health": "120", "__init__": "function"}, "hero": {"name": "'Aria'"}, "mage": {"name": "'Lumi'"}}, "mark": [{"box": "character", "attr": "max_health", "tone": "change"}], "active": ["character"]},
    {"attrs": {"character": {"max_health": "120", "__init__": "function"}, "hero": {"name": "'Aria'"}, "mage": {"name": "'Lumi'"}}, "read": [{"box": "character", "attr": "max_health", "via": "hero"}, {"box": "character", "attr": "max_health", "via": "mage"}], "active": ["hero", "mage", "character"]},
    {"attrs": {"character": {"max_health": "120", "__init__": "function"}, "hero": {"name": "'Aria'", "max_health": "150"}, "mage": {"name": "'Lumi'"}}, "mark": [{"box": "hero", "attr": "max_health"}], "active": ["hero"]},
    {"attrs": {"character": {"max_health": "120", "__init__": "function"}, "hero": {"name": "'Aria'", "max_health": "150"}, "mage": {"name": "'Lumi'"}}, "read": [{"box": "hero", "attr": "max_health"}, {"box": "character", "attr": "max_health", "via": "mage"}, {"box": "character", "attr": "max_health"}], "active": ["hero", "mage", "character"]}
  ],
  "output": [
    [],
    [],
    [],
    ["Aria Lumi"],
    ["100 100"],
    [],
    ["120 120"],
    [],
    ["150 120 120"]
  ],
  "captions": [
    "The class body runs once : the class `Character` holds `max_health` and the function `__init__`",
    "Calling `Character` makes an object, and `__init__` stores `name` on it",
    "A second object, with its own `name`",
    "Each object has its own `name`",
    "Neither object has `max_health`, so Python looks on the class and finds 100 for both",
    "`Character.max_health = 120` changes the one value both characters share",
    "Both lookups reach the class again and find 120",
    "Assigning `hero.max_health` creates an attribute on `hero`; the class is not changed",
    "`hero.max_health` is found on `hero` first; `mage.max_health` and `Character.max_health` still read the class"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1-3|6|7|8|9|10|11|12|13}
class Character:
    max_health = 100  # class attribute, one value shared by every character
    def __init__(self, name: str) -> None:
        self.name = name  # instance attribute, one value per character

hero = Character("Aria")
mage = Character("Lumi")
print(hero.name, mage.name)  # Aria Lumi
print(hero.max_health, mage.max_health)  # 100 100
Character.max_health = 120  # changes the shared value
print(hero.max_health, mage.max_health)  # 120 120
hero.max_health = 150  # creates an instance attribute on hero only
print(hero.max_health, mage.max_health, Character.max_health)  # 150 120 120
```

<template #visual="{ step }">
<StatefulObjects :run="run" :step="step" />
</template>
</DataStructuresRun>
