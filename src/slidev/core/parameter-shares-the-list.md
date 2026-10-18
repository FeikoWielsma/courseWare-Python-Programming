---
layout: default
title: Adding an Export Column
pills: ["demo09 · objectreferences"]
---

# Adding an Export Column

<script setup>
const run = {
  "frames": [
    {
      "id": "global",
      "label": "global"
    },
    {
      "id": "call",
      "label": "add_status_column()"
    }
  ],
  "order": [
    "fn",
    "original"
  ],
  "states": [
    {
      "names": {
        "global": {
          "add_status_column": "fn"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "add_status_column"
        }
      },
      "active": [
        "global.add_status_column"
      ]
    },
    {
      "names": {
        "global": {
          "add_status_column": "fn",
          "fields": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "add_status_column"
        },
        "original": {
          "type": "list",
          "items": [
            "'id'",
            "'total'"
          ]
        }
      },
      "active": [
        "global.fields"
      ]
    },
    {
      "names": {
        "global": {
          "add_status_column": "fn",
          "fields": "original"
        },
        "call": {
          "columns": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "add_status_column"
        },
        "original": {
          "type": "list",
          "items": [
            "'id'",
            "'total'"
          ]
        }
      },
      "active": [
        "call.columns"
      ]
    },
    {
      "names": {
        "global": {
          "add_status_column": "fn",
          "fields": "original"
        },
        "call": {
          "columns": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "add_status_column"
        },
        "original": {
          "type": "list",
          "items": [
            "'id'",
            "'total'",
            "'status'"
          ]
        }
      },
      "active": [
        "call.columns"
      ],
      "mark": {
        "object": "original",
        "index": 2
      }
    },
    {
      "names": {
        "global": {
          "add_status_column": "fn",
          "fields": "original"
        },
        "call": {
          "columns": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "add_status_column"
        },
        "original": {
          "type": "list",
          "items": [
            "'id'",
            "'total'",
            "'status'"
          ]
        }
      },
      "active": [
        "call.columns"
      ]
    },
    {
      "names": {
        "global": {
          "add_status_column": "fn",
          "fields": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "add_status_column"
        },
        "original": {
          "type": "list",
          "items": [
            "'id'",
            "'total'",
            "'status'"
          ]
        }
      },
      "active": [
        "global.fields"
      ]
    }
  ],
  "output": [
    [],
    [],
    [],
    [],
    [
      "Inside: ['id', 'total', 'status']"
    ],
    [
      "After call: ['id', 'total', 'status']"
    ]
  ],
  "captions": [
    "`def` defines the task of adding the export column",
    "`fields` refers to the original column list",
    "The parameter `columns` refers to that same list",
    "`append` adds `status` to the existing list",
    "The function prints the updated column list",
    "The caller sees the added column in `fields`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="400px">

```python {1|5|6|2|3|7}
def add_status_column(columns: list[str]) -> None:
    columns.append("status")
    print(f"Inside: {columns}")

fields = ["id", "total"]
add_status_column(fields)
print(f"After call: {fields}")
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="290" :gap="60" :cell-width="118" />
</template>
</DataStructuresRun>
