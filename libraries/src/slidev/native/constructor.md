---
layout: default
title: Initialising One Mage
pills: ["demo03 · super_init"]
---

# Initialising One Mage

<script setup>
const run = {
  "boxes": [
    {
      "id": "base",
      "label": "Character.__init__",
      "tag": "",
      "x": 0,
      "y": 0,
      "width": 330
    },
    {
      "id": "mage",
      "label": "jaina",
      "tag": "Mage object",
      "x": 380,
      "y": 0,
      "width": 330
    }
  ],
  "states": [
    {
      "attrs": {
        "base": {
          "sets": "name, health"
        },
        "mage": {}
      },
      "active": [
        "mage"
      ]
    },
    {
      "attrs": {
        "base": {
          "sets": "name, health"
        },
        "mage": {
          "name": "'Jaina'"
        }
      },
      "active": [
        "base"
      ]
    },
    {
      "attrs": {
        "base": {
          "sets": "name, health"
        },
        "mage": {
          "name": "'Jaina'",
          "health": "100"
        }
      },
      "active": [
        "base"
      ]
    },
    {
      "attrs": {
        "base": {
          "sets": "name, health"
        },
        "mage": {
          "name": "'Jaina'",
          "health": "100",
          "mana": "80"
        }
      },
      "active": [
        "mage"
      ]
    }
  ],
  "output": [
    [],
    [],
    [],
    [
      "{'name': 'Jaina', 'health': 100, 'mana': 80}"
    ]
  ],
  "captions": [
    "The subclass initialiser starts with an empty instance.",
    "Character.__init__ stores name on that same instance.",
    "The base initialiser also stores health.",
    "The subclass stores mana after super returns."
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1-4|1-3|1-3|1-8}
class Mage(Character):
    def __init__(self, name: str, mana: int = 100) -> None:
        super().__init__(name)
        self.mana: int = mana


jaina = Mage("Jaina", mana=80)
print(vars(jaina))
```

<template #visual="{ step }">
<StatefulObjects :run="run" :step="step" />
</template>
</DataStructuresRun>
