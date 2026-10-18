---
layout: default
title: Local and Shared Player Settings
pills: ["demo15 · variablescope"]
---

# Local and Shared Player Settings

<script setup>
const run = {
  "frames": [
    {
      "id": "global",
      "label": "global"
    },
    {
      "id": "preview",
      "label": "preview_volume()"
    },
    {
      "id": "settings",
      "label": "set_limit()"
    }
  ],
  "order": [
    "fee",
    "threshold",
    "preview_fn",
    "setter_fn",
    "preview_volume",
    "new_threshold"
  ],
  "states": [
    {
      "names": {
        "global": {
          "volume": "fee",
          "queue_limit": "threshold"
        }
      },
      "objects": {
        "fee": {
          "type": "int",
          "value": "50"
        },
        "threshold": {
          "type": "int",
          "value": "20"
        }
      },
      "active": [
        "global.volume",
        "global.queue_limit"
      ]
    },
    {
      "names": {
        "global": {
          "volume": "fee",
          "queue_limit": "threshold",
          "preview_volume": "preview_fn",
          "set_limit": "setter_fn"
        }
      },
      "objects": {
        "fee": {
          "type": "int",
          "value": "50"
        },
        "threshold": {
          "type": "int",
          "value": "20"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_volume"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_limit"
        }
      },
      "active": [
        "global.preview_volume",
        "global.set_limit"
      ]
    },
    {
      "names": {
        "global": {
          "volume": "fee",
          "queue_limit": "threshold",
          "preview_volume": "preview_fn",
          "set_limit": "setter_fn"
        },
        "preview": {}
      },
      "objects": {
        "fee": {
          "type": "int",
          "value": "50"
        },
        "threshold": {
          "type": "int",
          "value": "20"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_volume"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_limit"
        }
      },
      "active": [
        "global.preview_volume"
      ]
    },
    {
      "names": {
        "global": {
          "volume": "fee",
          "queue_limit": "threshold",
          "preview_volume": "preview_fn",
          "set_limit": "setter_fn"
        },
        "preview": {
          "volume": "preview_volume"
        }
      },
      "objects": {
        "fee": {
          "type": "int",
          "value": "50"
        },
        "threshold": {
          "type": "int",
          "value": "20"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_volume"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_limit"
        },
        "preview_volume": {
          "type": "int",
          "value": "10"
        }
      },
      "active": [
        "preview.volume"
      ]
    },
    {
      "names": {
        "global": {
          "volume": "fee",
          "queue_limit": "threshold",
          "preview_volume": "preview_fn",
          "set_limit": "setter_fn"
        },
        "preview": {
          "volume": "preview_volume"
        }
      },
      "objects": {
        "fee": {
          "type": "int",
          "value": "50"
        },
        "threshold": {
          "type": "int",
          "value": "20"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_volume"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_limit"
        },
        "preview_volume": {
          "type": "int",
          "value": "10"
        }
      },
      "active": [
        "preview.volume"
      ]
    },
    {
      "names": {
        "global": {
          "volume": "fee",
          "queue_limit": "threshold",
          "preview_volume": "preview_fn",
          "set_limit": "setter_fn"
        }
      },
      "objects": {
        "fee": {
          "type": "int",
          "value": "50"
        },
        "threshold": {
          "type": "int",
          "value": "20"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_volume"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_limit"
        },
        "preview_volume": {
          "type": "int",
          "value": "10"
        }
      },
      "active": [
        "global.volume"
      ]
    },
    {
      "names": {
        "global": {
          "volume": "fee",
          "queue_limit": "threshold",
          "preview_volume": "preview_fn",
          "set_limit": "setter_fn"
        },
        "settings": {}
      },
      "objects": {
        "fee": {
          "type": "int",
          "value": "50"
        },
        "threshold": {
          "type": "int",
          "value": "20"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_volume"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_limit"
        }
      },
      "active": [
        "global.set_limit"
      ]
    },
    {
      "names": {
        "global": {
          "volume": "fee",
          "queue_limit": "new_threshold",
          "preview_volume": "preview_fn",
          "set_limit": "setter_fn"
        },
        "settings": {
          "global queue_limit": null
        }
      },
      "objects": {
        "fee": {
          "type": "int",
          "value": "50"
        },
        "threshold": {
          "type": "int",
          "value": "20"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_volume"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_limit"
        },
        "new_threshold": {
          "type": "int",
          "value": "30"
        }
      },
      "active": [
        "global.queue_limit",
        "settings.global queue_limit"
      ]
    },
    {
      "names": {
        "global": {
          "volume": "fee",
          "queue_limit": "new_threshold",
          "preview_volume": "preview_fn",
          "set_limit": "setter_fn"
        }
      },
      "objects": {
        "fee": {
          "type": "int",
          "value": "50"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_volume"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_limit"
        },
        "new_threshold": {
          "type": "int",
          "value": "30"
        }
      },
      "active": [
        "global.queue_limit"
      ]
    }
  ],
  "output": [
    [],
    [],
    [],
    [],
    [
      "Preview volume: 10"
    ],
    [
      "Current volume: 50"
    ],
    [],
    [],
    [
      "Queue limit: 30"
    ]
  ],
  "captions": [
    "The module stores the player volume and queue limit",
    "The definitions bind the two function names",
    "`preview_volume()` starts a local scope",
    "Its local `volume` is separate from the module\u2019s configured volume",
    "The preview prints its local value",
    "After the call, the configured volume is still `50`",
    "`set_limit()` starts another local scope",
    "`global queue_limit` directs the assignment to the module\u2019s name",
    "The queue limit is now `30`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side" output-width="400px">

```python {1-2|4,8|12|5|6|13|14|9-10|15}
volume = 50
queue_limit = 20

def preview_volume() -> None:
    volume = 10
    print(f"Preview volume: {volume}")

def set_limit() -> None:
    global queue_limit
    queue_limit = 30

preview_volume()
print(f"Current volume: {volume}")
set_limit()
print(f"Queue limit: {queue_limit}")
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="230" :gap="90" />
</template>
</DataStructuresRun>
