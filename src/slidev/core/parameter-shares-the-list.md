---
layout: default
title: Adding an Let It Be
pills: ["demo09 · objectreferences"]
---

# Adding an Let It Be

<script setup>
const run = {
  "frames": [
    {
      "id": "global",
      "label": "global"
    },
    {
      "id": "call",
      "label": "add_encore()"
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
          "add_encore": "fn"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "add_encore"
        }
      },
      "active": [
        "global.add_encore"
      ]
    },
    {
      "names": {
        "global": {
          "add_encore": "fn",
          "queue": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "add_encore"
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
          "add_encore": "fn",
          "queue": "original"
        },
        "call": {
          "tracks": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "add_encore"
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
          "add_encore": "fn",
          "queue": "original"
        },
        "call": {
          "tracks": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "add_encore"
        },
        "original": {
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
        "object": "original",
        "index": 2
      }
    },
    {
      "names": {
        "global": {
          "add_encore": "fn",
          "queue": "original"
        },
        "call": {
          "tracks": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "add_encore"
        },
        "original": {
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
      ]
    },
    {
      "names": {
        "global": {
          "add_encore": "fn",
          "queue": "original"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "add_encore"
        },
        "original": {
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
    }
  ],
  "output": [
    [],
    [],
    [],
    [],
    [
      "Inside: ['Imagine', 'Yesterday', 'Let It Be']"
    ],
    [
      "After call: ['Imagine', 'Yesterday', 'Let It Be']"
    ]
  ],
  "captions": [
    "`def` defines the task of adding the encore mix track",
    "`queue` refers to the original track list",
    "The parameter `tracks` refers to that same list",
    "`append` adds `Let It Be` to the existing list",
    "The function prints the extended track list",
    "The caller sees the added track in `queue`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="400px">

```python {1|5|6|2|3|7}
def add_encore(tracks: list[str]) -> None:
    tracks.append("Let It Be")
    print(f"Inside: {tracks}")

queue = ["Imagine", "Yesterday"]
add_encore(queue)
print(f"After call: {queue}")
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="290" :gap="60" :cell-width="118" />
</template>
</DataStructuresRun>
