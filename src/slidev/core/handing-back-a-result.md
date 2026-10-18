---
layout: default
title: Using the Returned Delivery Cost
pills: ["demo02 · returnstatement"]
---

# Using the Returned Delivery Cost

<script setup>
const run = {
  "frames": [
    {
      "id": "global",
      "label": "global"
    },
    {
      "id": "call",
      "label": "delivery_cost()"
    }
  ],
  "order": [
    "fn",
    "amount",
    "fee",
    "grand"
  ],
  "states": [
    {
      "names": {
        "global": {
          "delivery_cost": "fn"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "delivery_cost"
        }
      },
      "active": [
        "global.delivery_cost"
      ]
    },
    {
      "names": {
        "global": {
          "delivery_cost": "fn"
        },
        "call": {
          "total": "amount"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "delivery_cost"
        },
        "amount": {
          "type": "float",
          "value": "35.0"
        }
      },
      "active": [
        "call.total"
      ]
    },
    {
      "names": {
        "global": {
          "delivery_cost": "fn"
        },
        "call": {
          "total": "amount"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "delivery_cost"
        },
        "amount": {
          "type": "float",
          "value": "35.0"
        }
      },
      "active": [
        "call.total"
      ]
    },
    {
      "names": {
        "global": {
          "delivery_cost": "fn"
        },
        "call": {
          "total": "amount",
          "return": "fee"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "delivery_cost"
        },
        "amount": {
          "type": "float",
          "value": "35.0"
        },
        "fee": {
          "type": "float",
          "value": "4.95"
        }
      },
      "active": [
        "call.return"
      ],
      "mark": {
        "object": "fee"
      }
    },
    {
      "names": {
        "global": {
          "delivery_cost": "fn",
          "shipping": "fee"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "delivery_cost"
        },
        "amount": {
          "type": "float",
          "value": "35.0"
        },
        "fee": {
          "type": "float",
          "value": "4.95"
        }
      },
      "active": [
        "global.shipping"
      ]
    },
    {
      "names": {
        "global": {
          "delivery_cost": "fn",
          "shipping": "fee",
          "grand_total": "grand"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "delivery_cost"
        },
        "fee": {
          "type": "float",
          "value": "4.95"
        },
        "grand": {
          "type": "float",
          "value": "39.95"
        }
      },
      "active": [
        "global.grand_total"
      ],
      "mark": {
        "object": "grand"
      }
    },
    {
      "names": {
        "global": {
          "delivery_cost": "fn",
          "shipping": "fee",
          "grand_total": "grand"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "delivery_cost"
        },
        "fee": {
          "type": "float",
          "value": "4.95"
        },
        "grand": {
          "type": "float",
          "value": "39.95"
        }
      },
      "active": [
        "global.grand_total"
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
      "Order total: 39.95"
    ]
  ],
  "captions": [
    "The definition names the delivery calculation",
    "The call supplies an order total of `35.0`",
    "The order is below `50.0`, so delivery is not free",
    "`return 4.95` ends the call and supplies its result",
    "The caller stores the returned charge in `shipping`",
    "The caller adds `shipping` to the order total",
    "The result can be used in the caller\u2019s calculation and printed"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side" output-width="400px">

```python {1|6|2|4|6|7|8}
def delivery_cost(total):
    if total >= 50.0:
        return 0.0
    return 4.95

shipping = delivery_cost(35.0)
grand_total = 35.0 + shipping
print(f"Order total: {grand_total:.2f}")
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="230" :gap="90" />
</template>
</DataStructuresRun>
