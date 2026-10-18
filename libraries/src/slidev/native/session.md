---
layout: default
title: A Book Through a Transaction
pills: ["demo07 · session_and_persistence"]
---

# A Book Through a Transaction

<script setup>
const run = {
  "boxes": [
    {
      "id": "transient",
      "label": "Transient",
      "tag": "book",
      "x": 0,
      "y": 0,
      "width": 250
    },
    {
      "id": "pending",
      "label": "Pending",
      "tag": "book",
      "x": 285,
      "y": 0,
      "width": 250
    },
    {
      "id": "flushed",
      "label": "Flushed",
      "tag": "book",
      "x": 570,
      "y": 0,
      "width": 250
    },
    {
      "id": "committed",
      "label": "Committed",
      "tag": "book",
      "x": 855,
      "y": 0,
      "width": 250
    }
  ],
  "states": [
    {
      "attrs": {
        "transient": {
          "title": "Sharp Objects",
          "id": "None"
        }
      },
      "active": [
        "transient"
      ]
    },
    {
      "attrs": {
        "transient": {
          "title": "Sharp Objects",
          "id": "None"
        }
      },
      "active": [
        "transient"
      ]
    },
    {
      "attrs": {
        "pending": {
          "title": "Sharp Objects",
          "id": "None"
        }
      },
      "active": [
        "pending"
      ]
    },
    {
      "attrs": {
        "pending": {
          "title": "Sharp Objects",
          "id": "None"
        }
      },
      "active": [
        "pending"
      ]
    },
    {
      "attrs": {
        "flushed": {
          "title": "Sharp Objects",
          "id": "1"
        }
      },
      "active": [
        "flushed"
      ]
    },
    {
      "attrs": {
        "flushed": {
          "title": "Sharp Objects",
          "id": "1"
        }
      },
      "active": [
        "flushed"
      ]
    },
    {
      "attrs": {
        "committed": {
          "title": "Sharp Objects",
          "id": "1"
        }
      },
      "active": [
        "committed"
      ]
    },
    {
      "attrs": {
        "committed": {
          "title": "Sharp Objects",
          "id": "1"
        }
      },
      "active": [
        "committed"
      ]
    }
  ],
  "output": [
    [],
    [],
    [],
    [
      "None None"
    ],
    [],
    [
      "1 2"
    ],
    [],
    [
      "1 2"
    ]
  ],
  "captions": [
    "Constructed objects have not yet been added to the session.",
    "Constructed objects have not yet been added to the session.",
    "Added objects are pending; no generated id is available yet.",
    "Added objects are pending; no generated id is available yet.",
    "Flush assigns ids, but the transaction is still open.",
    "Flush assigns ids, but the transaction is still open.",
    "Commit makes the transaction permanent.",
    "Commit makes the transaction permanent."
  ]
}
</script>

<DataStructuresRun :run="run" layout="pair" output-width="300px">

```python {1-2|1-3|1-4|1-5|1-7|1-8|1-11|1-12}
with Session(engine) as session:
    first = Book(title="Sharp Objects", price_gbp=47.82, rating=4)
    second = Book(title="In a Dark, Dark Wood", price_gbp=19.63, rating=1)
    session.add_all([first, second])
    print(first.id, second.id)

    session.flush()
    print(first.id, second.id)

    # Flush assigns ids inside the transaction; commit makes the writes permanent.
    session.commit()
    print(first.id, second.id)
```

<template #visual="{ step }">
<StatefulObjects :run="run" :step="step" />
</template>
</DataStructuresRun>
