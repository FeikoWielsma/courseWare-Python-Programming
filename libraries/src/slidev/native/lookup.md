---
layout: default
title: Method Lookup
pills: ["demo04 · overriding"]
---

# Method Lookup

<script setup>
const run = {
  "boxes": [
    {
      "id": "Mage",
      "label": "Mage",
      "tag": "class",
      "x": 0,
      "y": 0,
      "width": 260
    },
    {
      "id": "Character",
      "label": "Character",
      "tag": "class",
      "x": 290,
      "y": 0,
      "width": 260
    },
    {
      "id": "object",
      "label": "object",
      "tag": "class",
      "x": 580,
      "y": 0,
      "width": 260
    }
  ],
  "states": [
    {
      "attrs": {
        "Mage": {
          "attack": "yes",
          "__str__": "-"
        },
        "Character": {
          "attack": "yes",
          "__str__": "-"
        },
        "object": {
          "attack": "-",
          "__str__": "yes"
        }
      },
      "active": [
        "Mage"
      ]
    },
    {
      "attrs": {
        "Mage": {
          "attack": "yes",
          "__str__": "-"
        },
        "Character": {
          "attack": "yes",
          "__str__": "-"
        },
        "object": {
          "attack": "-",
          "__str__": "yes"
        }
      },
      "active": [
        "Mage"
      ]
    },
    {
      "attrs": {
        "Mage": {
          "attack": "yes",
          "__str__": "-"
        },
        "Character": {
          "attack": "yes",
          "__str__": "-"
        },
        "object": {
          "attack": "-",
          "__str__": "yes"
        }
      },
      "active": [
        "Character"
      ]
    },
    {
      "attrs": {
        "Mage": {
          "attack": "yes",
          "__str__": "-"
        },
        "Character": {
          "attack": "yes",
          "__str__": "-"
        },
        "object": {
          "attack": "-",
          "__str__": "yes"
        }
      },
      "active": [
        "object"
      ]
    },
    {
      "attrs": {
        "Mage": {
          "attack": "yes",
          "__str__": "-"
        },
        "Character": {
          "attack": "yes",
          "__str__": "-"
        },
        "object": {
          "attack": "-",
          "__str__": "yes"
        }
      },
      "active": [
        "object"
      ]
    }
  ],
  "output": [
    [],
    [
      "Jaina casts Frostbolt"
    ],
    [
      "Jaina attacks"
    ],
    [
      "['Mage', 'Character', 'object']"
    ],
    [
      "True"
    ]
  ],
  "captions": [
    "Jaina's class is Mage.",
    "Mage supplies the first attack implementation in the MRO.",
    "The explicit Character call uses the base implementation.",
    "The method resolution order includes Mage, Character and object.",
    "Neither course class defines __str__; the inherited method belongs to object."
  ]
}
</script>

<DataStructuresRun :run="run" layout="pair" output-width="300px">

```python {1-1|1-2|1-3|1-4|1-5}
jaina = Mage("Jaina")
print(jaina.attack())
print(Character.attack(jaina))
print([cls.__name__ for cls in Mage.__mro__])
print(Mage.__str__ is object.__str__)
```

<template #visual="{ step }">
<StatefulObjects :run="run" :step="step" />
</template>
</DataStructuresRun>
