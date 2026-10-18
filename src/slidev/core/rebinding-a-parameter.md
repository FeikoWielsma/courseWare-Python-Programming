---
layout: default
title: Keeping the Original Playlist
pills: ["demo10 · overwritingreferences"]
---

# Keeping the Original Playlist

<script setup>
const run = {
  "frames": [
    {
      "id": "global",
      "label": "global"
    },
    {
      "id": "call",
      "label": "with_encore()"
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
          "with_encore": "fn"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_encore"
        }
      },
      "active": [
        "global.with_encore"
      ]
    },
    {
      "names": {
        "global": {
          "with_encore": "fn",
          "queue": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_encore"
        },
        "original": {
          "type": "list",
          "items": [
            "'Imagine'",
            "'Yesterday'"
          ]
        }
      },
      "active": [
        "global.queue"
      ]
    },
    {
      "names": {
        "global": {
          "with_encore": "fn",
          "queue": "original"
        },
        "call": {
          "tracks": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_encore"
        },
        "original": {
          "type": "list",
          "items": [
            "'Imagine'",
            "'Yesterday'"
          ]
        }
      },
      "active": [
        "call.tracks"
      ]
    },
    {
      "names": {
        "global": {
          "with_encore": "fn",
          "queue": "original"
        },
        "call": {
          "tracks": "new"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_encore"
        },
        "original": {
          "type": "list",
          "items": [
            "'Imagine'",
            "'Yesterday'"
          ]
        },
        "new": {
          "type": "list",
          "items": [
            "'Imagine'",
            "'Yesterday'",
            "'Let It Be'"
          ]
        }
      },
      "active": [
        "call.tracks"
      ],
      "mark": {
        "object": "new"
      }
    },
    {
      "names": {
        "global": {
          "with_encore": "fn",
          "queue": "original"
        },
        "call": {
          "tracks": "new",
          "return": "new"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_encore"
        },
        "original": {
          "type": "list",
          "items": [
            "'Imagine'",
            "'Yesterday'"
          ]
        },
        "new": {
          "type": "list",
          "items": [
            "'Imagine'",
            "'Yesterday'",
            "'Let It Be'"
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
          "with_encore": "fn",
          "queue": "original",
          "extended": "new"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_encore"
        },
        "original": {
          "type": "list",
          "items": [
            "'Imagine'",
            "'Yesterday'"
          ]
        },
        "new": {
          "type": "list",
          "items": [
            "'Imagine'",
            "'Yesterday'",
            "'Let It Be'"
          ]
        }
      },
      "active": [
        "global.extended"
      ]
    },
    {
      "names": {
        "global": {
          "with_encore": "fn",
          "queue": "original",
          "extended": "new"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_encore"
        },
        "original": {
          "type": "list",
          "items": [
            "'Imagine'",
            "'Yesterday'"
          ]
        },
        "new": {
          "type": "list",
          "items": [
            "'Imagine'",
            "'Yesterday'",
            "'Let It Be'"
          ]
        }
      },
      "active": [
        "global.queue"
      ]
    },
    {
      "names": {
        "global": {
          "with_encore": "fn",
          "queue": "original",
          "extended": "new"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "with_encore"
        },
        "original": {
          "type": "list",
          "items": [
            "'Imagine'",
            "'Yesterday'"
          ]
        },
        "new": {
          "type": "list",
          "items": [
            "'Imagine'",
            "'Yesterday'",
            "'Let It Be'"
          ]
        }
      },
      "active": [
        "global.extended"
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
      "Original: ['Imagine', 'Yesterday']"
    ],
    [
      "With encore: ['Imagine', 'Yesterday', 'Let It Be']"
    ]
  ],
  "captions": [
    "The function builds a track list for a separate export",
    "`queue` holds the original tracks",
    "The call starts with both names referring to the original list",
    "`+` creates a new list; the local name `tracks` now refers to it",
    "`return` passes the new list back to the caller",
    "`extended` receives the new list; `queue` keeps the original",
    "The original list still contains only `id` and `total`",
    "The encore mix uses the new list including `Let It Be`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="400px">

```python {1|5|6|2|3|6|7|8}
def with_encore(tracks: list[str]) -> list[str]:
    tracks = tracks + ["Let It Be"]
    return tracks

queue = ["Imagine", "Yesterday"]
extended = with_encore(queue)
print(f"Original: {queue}")
print(f"With encore: {extended}")
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="290" :gap="60" :cell-width="118" />
</template>
</DataStructuresRun>
