---
layout: default
title: Local and Shared Delivery Settings
pills: ["demo15 · variablescope"]
---

# Local and Shared Delivery Settings

<script setup>
const run = {
  "frames": [
    {
      "id": "global",
      "label": "global"
    },
    {
      "id": "preview",
      "label": "preview_fee()"
    },
    {
      "id": "settings",
      "label": "set_threshold()"
    }
  ],
  "order": [
    "fee",
    "threshold",
    "preview_fn",
    "setter_fn",
    "preview_fee",
    "new_threshold"
  ],
  "states": [
    {
      "names": {
        "global": {
          "delivery_fee": "fee",
          "free_from": "threshold"
        }
      },
      "objects": {
        "fee": {
          "type": "float",
          "value": "4.95"
        },
        "threshold": {
          "type": "float",
          "value": "50.0"
        }
      },
      "active": [
        "global.delivery_fee",
        "global.free_from"
      ]
    },
    {
      "names": {
        "global": {
          "delivery_fee": "fee",
          "free_from": "threshold",
          "preview_fee": "preview_fn",
          "set_threshold": "setter_fn"
        }
      },
      "objects": {
        "fee": {
          "type": "float",
          "value": "4.95"
        },
        "threshold": {
          "type": "float",
          "value": "50.0"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_fee"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_threshold"
        }
      },
      "active": [
        "global.preview_fee",
        "global.set_threshold"
      ]
    },
    {
      "names": {
        "global": {
          "delivery_fee": "fee",
          "free_from": "threshold",
          "preview_fee": "preview_fn",
          "set_threshold": "setter_fn"
        },
        "preview": {}
      },
      "objects": {
        "fee": {
          "type": "float",
          "value": "4.95"
        },
        "threshold": {
          "type": "float",
          "value": "50.0"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_fee"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_threshold"
        }
      },
      "active": [
        "global.preview_fee"
      ]
    },
    {
      "names": {
        "global": {
          "delivery_fee": "fee",
          "free_from": "threshold",
          "preview_fee": "preview_fn",
          "set_threshold": "setter_fn"
        },
        "preview": {
          "delivery_fee": "preview_fee"
        }
      },
      "objects": {
        "fee": {
          "type": "float",
          "value": "4.95"
        },
        "threshold": {
          "type": "float",
          "value": "50.0"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_fee"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_threshold"
        },
        "preview_fee": {
          "type": "float",
          "value": "0.0"
        }
      },
      "active": [
        "preview.delivery_fee"
      ]
    },
    {
      "names": {
        "global": {
          "delivery_fee": "fee",
          "free_from": "threshold",
          "preview_fee": "preview_fn",
          "set_threshold": "setter_fn"
        },
        "preview": {
          "delivery_fee": "preview_fee"
        }
      },
      "objects": {
        "fee": {
          "type": "float",
          "value": "4.95"
        },
        "threshold": {
          "type": "float",
          "value": "50.0"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_fee"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_threshold"
        },
        "preview_fee": {
          "type": "float",
          "value": "0.0"
        }
      },
      "active": [
        "preview.delivery_fee"
      ]
    },
    {
      "names": {
        "global": {
          "delivery_fee": "fee",
          "free_from": "threshold",
          "preview_fee": "preview_fn",
          "set_threshold": "setter_fn"
        }
      },
      "objects": {
        "fee": {
          "type": "float",
          "value": "4.95"
        },
        "threshold": {
          "type": "float",
          "value": "50.0"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_fee"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_threshold"
        },
        "preview_fee": {
          "type": "float",
          "value": "0.0"
        }
      },
      "active": [
        "global.delivery_fee"
      ]
    },
    {
      "names": {
        "global": {
          "delivery_fee": "fee",
          "free_from": "threshold",
          "preview_fee": "preview_fn",
          "set_threshold": "setter_fn"
        },
        "settings": {}
      },
      "objects": {
        "fee": {
          "type": "float",
          "value": "4.95"
        },
        "threshold": {
          "type": "float",
          "value": "50.0"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_fee"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_threshold"
        }
      },
      "active": [
        "global.set_threshold"
      ]
    },
    {
      "names": {
        "global": {
          "delivery_fee": "fee",
          "free_from": "new_threshold",
          "preview_fee": "preview_fn",
          "set_threshold": "setter_fn"
        },
        "settings": {
          "global free_from": null
        }
      },
      "objects": {
        "fee": {
          "type": "float",
          "value": "4.95"
        },
        "threshold": {
          "type": "float",
          "value": "50.0"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_fee"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_threshold"
        },
        "new_threshold": {
          "type": "float",
          "value": "75.0"
        }
      },
      "active": [
        "global.free_from",
        "settings.global free_from"
      ]
    },
    {
      "names": {
        "global": {
          "delivery_fee": "fee",
          "free_from": "new_threshold",
          "preview_fee": "preview_fn",
          "set_threshold": "setter_fn"
        }
      },
      "objects": {
        "fee": {
          "type": "float",
          "value": "4.95"
        },
        "preview_fn": {
          "type": "function",
          "value": "preview_fee"
        },
        "setter_fn": {
          "type": "function",
          "value": "set_threshold"
        },
        "new_threshold": {
          "type": "float",
          "value": "75.0"
        }
      },
      "active": [
        "global.free_from"
      ]
    }
  ],
  "output": [
    [],
    [],
    [],
    [],
    [
      "Preview fee: 0.00"
    ],
    [
      "Current fee: 4.95"
    ],
    [],
    [],
    [
      "Free from: 75.00"
    ]
  ],
  "captions": [
    "The module stores the delivery fee and free-delivery threshold",
    "The definitions bind the two function names",
    "`preview_fee()` starts a local scope",
    "Its local `delivery_fee` is separate from the module\u2019s configured fee",
    "The preview prints its local value",
    "After the call, the configured fee is still `4.95`",
    "`set_threshold()` starts another local scope",
    "`global free_from` directs the assignment to the module\u2019s name",
    "The configured threshold is now `75.0`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side" output-width="400px">

```python {1-2|4,8|12|5|6|13|14|9-10|15}
delivery_fee = 4.95
free_from = 50.0

def preview_fee() -> None:
    delivery_fee = 0.0
    print(f"Preview fee: {delivery_fee:.2f}")

def set_threshold() -> None:
    global free_from
    free_from = 75.0

preview_fee()
print(f"Current fee: {delivery_fee:.2f}")
set_threshold()
print(f"Free from: {free_from:.2f}")
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="230" :gap="90" />
</template>
</DataStructuresRun>
