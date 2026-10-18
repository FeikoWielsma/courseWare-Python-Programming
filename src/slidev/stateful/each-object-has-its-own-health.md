---
layout: default
title: Each Object Has Its Own Health
pills: ["demo02 · character"]
---

# Each Object Has Its Own Health

<script setup>
const run = {
  "boxes": [
    {"id": "hero", "label": "hero", "tag": "Character object", "x": 0, "y": 0, "width": 230},
    {"id": "troll", "label": "troll", "tag": "Character object", "x": 260, "y": 0, "width": 230},
    {"id": "character", "label": "Character", "tag": "class", "x": 0, "y": 160, "width": 300}
  ],
  "links": [{"from": "hero", "to": "character"}, {"from": "troll", "to": "character"}],
  "states": [
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "hero": {"name": "'Aria'", "health": "100"}}, "mark": [{"box": "hero", "attr": "name"}, {"box": "hero", "attr": "health"}], "active": ["hero"]},
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "hero": {"name": "'Aria'", "health": "100"}, "troll": {"name": "'Grok'", "health": "60"}}, "mark": [{"box": "troll", "attr": "name"}, {"box": "troll", "attr": "health"}], "active": ["troll"]},
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "hero": {"name": "'Aria'", "health": "100"}, "troll": {"name": "'Grok'", "health": "35"}}, "read": [{"box": "character", "attr": "take_damage", "via": "troll"}], "mark": [{"box": "troll", "attr": "health", "tone": "change"}], "note": {"box": "character", "attr": "take_damage", "text": "self is troll, 60 - 25 = 35"}, "active": ["troll", "character"]},
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "hero": {"name": "'Aria'", "health": "90"}, "troll": {"name": "'Grok'", "health": "35"}}, "read": [{"box": "character", "attr": "take_damage", "via": "hero"}], "mark": [{"box": "hero", "attr": "health", "tone": "change"}], "note": {"box": "character", "attr": "take_damage", "text": "self is hero, 100 - 10 = 90"}, "active": ["hero", "character"]},
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "hero": {"name": "'Aria'", "health": "95"}, "troll": {"name": "'Grok'", "health": "35"}}, "read": [{"box": "character", "attr": "heal", "via": "hero"}], "mark": [{"box": "hero", "attr": "health", "tone": "change"}], "note": {"box": "character", "attr": "heal", "text": "self is hero, min(95, 100) = 95"}, "active": ["hero", "character"]},
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "hero": {"name": "'Aria'", "health": "95"}, "troll": {"name": "'Grok'", "health": "35"}}, "read": [{"box": "character", "attr": "show_status", "via": "hero"}, {"box": "hero", "attr": "name"}, {"box": "hero", "attr": "health"}], "note": {"box": "character", "attr": "show_status", "text": "self is hero"}, "active": ["hero", "character"]},
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "hero": {"name": "'Aria'", "health": "95"}, "troll": {"name": "'Grok'", "health": "35"}}, "read": [{"box": "character", "attr": "show_status", "via": "troll"}, {"box": "troll", "attr": "name"}, {"box": "troll", "attr": "health"}], "note": {"box": "character", "attr": "show_status", "text": "self is troll"}, "active": ["troll", "character"]}
  ],
  "output": [
    [],
    [],
    [],
    [],
    [],
    ["Aria : 95 health"],
    ["Grok : 35 health"]
  ],
  "captions": [
    "Calling `Character` makes an object; `__init__` stores its own `name` and `health` on it",
    "A second object, with a `health` of its own",
    "`take_damage` is found on the class; Python passes `troll` as `self`, so only the troll's health drops",
    "The same method with `hero` as `self` changes the hero's health; the troll keeps 35",
    "`heal` adds 5 and keeps the result at most 100",
    "`show_status` reads `self.name` and `self.health` of the hero",
    "The same method on `troll` prints the troll's own values"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|2|4|5|6|8|9}
hero = Character("Aria", 100)
troll = Character("Grok", 60)

troll.take_damage(25)
hero.take_damage(10)
hero.heal(5)

hero.show_status()
troll.show_status()
```

<template #visual="{ step }">
<StatefulObjects :run="run" :step="step" />
</template>
</DataStructuresRun>
