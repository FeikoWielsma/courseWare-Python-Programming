---
layout: default
title: Keeping the Original Columns
pills: ["demo10 · overwritingreferences"]
---

# Keeping the Original Columns

<script setup>
const run = {
  "frames": [
    {
      "id": "global",
      "label": "global"
    },
    {
      "id": "call",
      "label": "with_status_column()"
    }
  ],
  "order": [
    "fn",
    "original",
    "new"
  ],
  "states": [
    {
      "names": {
        "global": {
          "with_status_column": "fn"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_status_column"
        }
      },
      "active": [
        "global.with_status_column"
      ]
    },
    {
      "names": {
        "global": {
          "with_status_column": "fn",
          "fields": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_status_column"
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
          "with_status_column": "fn",
          "fields": "original"
        },
        "call": {
          "columns": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_status_column"
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
          "with_status_column": "fn",
          "fields": "original"
        },
        "call": {
          "columns": "new"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_status_column"
        },
        "original": {
          "type": "list",
          "items": [
            "'id'",
            "'total'"
          ]
        },
        "new": {
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
        "object": "new"
      }
    },
    {
      "names": {
        "global": {
          "with_status_column": "fn",
          "fields": "original"
        },
        "call": {
          "columns": "new",
          "return": "new"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_status_column"
        },
        "original": {
          "type": "list",
          "items": [
            "'id'",
            "'total'"
          ]
        },
        "new": {
          "type": "list",
          "items": [
            "'id'",
            "'total'",
            "'status'"
          ]
        }
      },
      "active": [
        "call.return"
      ]
    },
    {
      "names": {
        "global": {
          "with_status_column": "fn",
          "fields": "original",
          "updated": "new"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_status_column"
        },
        "original": {
          "type": "list",
          "items": [
            "'id'",
            "'total'"
          ]
        },
        "new": {
          "type": "list",
          "items": [
            "'id'",
            "'total'",
            "'status'"
          ]
        }
      },
      "active": [
        "global.updated"
      ]
    },
    {
      "names": {
        "global": {
          "with_status_column": "fn",
          "fields": "original",
          "updated": "new"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_status_column"
        },
        "original": {
          "type": "list",
          "items": [
            "'id'",
            "'total'"
          ]
        },
        "new": {
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
    },
    {
      "names": {
        "global": {
          "with_status_column": "fn",
          "fields": "original",
          "updated": "new"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_status_column"
        },
        "original": {
          "type": "list",
          "items": [
            "'id'",
            "'total'"
          ]
        },
        "new": {
          "type": "list",
          "items": [
            "'id'",
            "'total'",
            "'status'"
          ]
        }
      },
      "active": [
        "global.updated"
      ]
    }
  ],
  "output": [
    [],
    [],
    [],
    [],
    [],
    [],
    [
      "Original: ['id', 'total']"
    ],
    [
      "Export: ['id', 'total', 'status']"
    ]
  ],
  "captions": [
    "The function builds a column list for a separate export",
    "`fields` holds the original columns",
    "The call starts with both names referring to the original list",
    "`+` creates a new list; the local name `columns` now refers to it",
    "`return` passes the new list back to the caller",
    "`updated` receives the new list; `fields` keeps the original",
    "The original list still contains only `id` and `total`",
    "The export uses the new list including `status`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="400px">

```python {1|5|6|2|3|6|7|8}
def with_status_column(columns: list[str]) -> list[str]:
    columns = columns + ["status"]
    return columns

fields = ["id", "total"]
updated = with_status_column(fields)
print(f"Original: {fields}")
print(f"Export: {updated}")
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="290" :gap="60" :cell-width="118" />
</template>
</DataStructuresRun>
