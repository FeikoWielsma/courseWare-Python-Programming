---
layout: default
title: Each Object Has Its Own Health
pills: ["demo03 · character"]
---

# Each Object Has Its Own Health

<script setup>
const run = {
  "boxes": [
    {"id": "jaina", "label": "jaina", "tag": "Character object", "x": 0, "y": 0, "width": 230},
    {"id": "hogger", "label": "hogger", "tag": "Character object", "x": 260, "y": 0, "width": 230},
    {"id": "character", "label": "Character", "tag": "class", "x": 0, "y": 160, "width": 300}
  ],
  "links": [{"from": "jaina", "to": "character"}, {"from": "hogger", "to": "character"}],
  "states": [
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "jaina": {"name": "'Jaina'", "health": "100"}}, "mark": [{"box": "jaina", "attr": "name"}, {"box": "jaina", "attr": "health"}], "active": ["jaina"]},
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "jaina": {"name": "'Jaina'", "health": "100"}, "hogger": {"name": "'Hogger'", "health": "60"}}, "mark": [{"box": "hogger", "attr": "name"}, {"box": "hogger", "attr": "health"}], "active": ["hogger"]},
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "jaina": {"name": "'Jaina'", "health": "100"}, "hogger": {"name": "'Hogger'", "health": "35"}}, "read": [{"box": "character", "attr": "take_damage", "via": "hogger"}], "mark": [{"box": "hogger", "attr": "health", "tone": "change"}], "note": {"box": "character", "attr": "take_damage", "text": "self is hogger, 60 - 25 = 35"}, "active": ["hogger", "character"]},
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "jaina": {"name": "'Jaina'", "health": "90"}, "hogger": {"name": "'Hogger'", "health": "35"}}, "read": [{"box": "character", "attr": "take_damage", "via": "jaina"}], "mark": [{"box": "jaina", "attr": "health", "tone": "change"}], "note": {"box": "character", "attr": "take_damage", "text": "self is jaina, 100 - 10 = 90"}, "active": ["jaina", "character"]},
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "jaina": {"name": "'Jaina'", "health": "95"}, "hogger": {"name": "'Hogger'", "health": "35"}}, "read": [{"box": "character", "attr": "heal", "via": "jaina"}], "mark": [{"box": "jaina", "attr": "health", "tone": "change"}], "note": {"box": "character", "attr": "heal", "text": "self is jaina, min(95, 100) = 95"}, "active": ["jaina", "character"]},
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "jaina": {"name": "'Jaina'", "health": "95"}, "hogger": {"name": "'Hogger'", "health": "35"}}, "read": [{"box": "character", "attr": "show_status", "via": "jaina"}, {"box": "jaina", "attr": "name"}, {"box": "jaina", "attr": "health"}], "note": {"box": "character", "attr": "show_status", "text": "self is jaina"}, "active": ["jaina", "character"]},
    {"attrs": {"character": {"__init__": "function", "take_damage": "function", "heal": "function", "show_status": "function"}, "jaina": {"name": "'Jaina'", "health": "95"}, "hogger": {"name": "'Hogger'", "health": "35"}}, "read": [{"box": "character", "attr": "show_status", "via": "hogger"}, {"box": "hogger", "attr": "name"}, {"box": "hogger", "attr": "health"}], "note": {"box": "character", "attr": "show_status", "text": "self is hogger"}, "active": ["hogger", "character"]}
  ],
  "output": [
    [],
    [],
    [],
    [],
    [],
    ["Jaina : 95 health"],
    ["Hogger : 35 health"]
  ],
  "captions": [
    "Calling `Character` makes an object; `__init__` stores its own `name` and `health` on it",
    "A second object, with a `health` of its own",
    "`take_damage` is found on the class; Python passes `hogger` as `self`, so only Hogger's health drops",
    "The same method with `jaina` as `self` changes Jaina's health; Hogger keeps 35",
    "`heal` adds 5 and keeps the result at most 100",
    "`show_status` reads `self.name` and `self.health` of Jaina",
    "The same method on `hogger` prints Hogger's own values"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|2|4|5|6|8|9}
jaina = Character("Jaina", 100)
hogger = Character("Hogger", 60)

hogger.take_damage(25)
jaina.take_damage(10)
jaina.heal(5)

jaina.show_status()
hogger.show_status()
```

<template #visual="{ step }">
<StatefulObjects :run="run" :step="step" />
</template>
</DataStructuresRun>
