---
layout: default
title: Using the Returned Duration
pills: ["demo02 · returnstatement"]
---

# Using the Returned Duration

<script setup>
const run = {
  "frames": [
    {
      "id": "global",
      "label": "global"
    },
    {
      "id": "call",
      "label": "format_duration()"
    }
  ],
  "order": [
    "fn",
    "seconds",
    "minutes",
    "remainder",
    "label",
    "message"
  ],
  "states": [
    {
      "names": {
        "global": {
          "format_duration": "fn"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "format_duration"
        }
      },
      "active": [
        "global.format_duration"
      ]
    },
    {
      "names": {
        "global": {
          "format_duration": "fn"
        },
        "call": {
          "seconds": "seconds"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "format_duration"
        },
        "seconds": {
          "type": "int",
          "value": "222"
        }
      },
      "active": [
        "call.seconds"
      ]
    },
    {
      "names": {
        "global": {
          "format_duration": "fn"
        },
        "call": {
          "seconds": "seconds",
          "minutes": "minutes"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "format_duration"
        },
        "seconds": {
          "type": "int",
          "value": "222"
        },
        "minutes": {
          "type": "int",
          "value": "3"
        }
      },
      "active": [
        "call.minutes"
      ]
    },
    {
      "names": {
        "global": {
          "format_duration": "fn"
        },
        "call": {
          "seconds": "seconds",
          "minutes": "minutes",
          "remainder": "remainder"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "format_duration"
        },
        "seconds": {
          "type": "int",
          "value": "222"
        },
        "minutes": {
          "type": "int",
          "value": "3"
        },
        "remainder": {
          "type": "int",
          "value": "42"
        }
      },
      "active": [
        "call.remainder"
      ]
    },
    {
      "names": {
        "global": {
          "format_duration": "fn"
        },
        "call": {
          "seconds": "seconds",
          "minutes": "minutes",
          "remainder": "remainder",
          "return": "label"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "format_duration"
        },
        "seconds": {
          "type": "int",
          "value": "222"
        },
        "minutes": {
          "type": "int",
          "value": "3"
        },
        "remainder": {
          "type": "int",
          "value": "42"
        },
        "label": {
          "type": "str",
          "value": "'3:42'"
        }
      },
      "active": [
        "call.return"
      ]
    },
    {
      "names": {
        "global": {
          "format_duration": "fn",
          "label": "label"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "format_duration"
        },
        "label": {
          "type": "str",
          "value": "'3:42'"
        }
      },
      "active": [
        "global.label"
      ]
    },
    {
      "names": {
        "global": {
          "format_duration": "fn",
          "label": "label",
          "message": "message"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "format_duration"
        },
        "label": {
          "type": "str",
          "value": "'3:42'"
        },
        "message": {
          "type": "str",
          "value": "'Orbit [3:42]'"
        }
      },
      "active": [
        "global.message"
      ]
    },
    {
      "names": {
        "global": {
          "format_duration": "fn",
          "label": "label",
          "message": "message"
        }
      },
      "objects": {
        "fn": {
          "type": "function",
          "value": "format_duration"
        },
        "label": {
          "type": "str",
          "value": "'3:42'"
        },
        "message": {
          "type": "str",
          "value": "'Orbit [3:42]'"
        }
      },
      "active": [
        "global.message"
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
    [],
    [
      "Orbit [3:42]"
    ]
  ],
  "captions": [
    "The definition binds the name `format_duration`",
    "The call supplies a track length of `222` seconds",
    "`222 // 60` gives `3` complete minutes",
    "`222 % 60` gives `42` remaining seconds",
    "The formatted string `3:42` is returned to the caller",
    "The caller stores the returned string in `label`",
    "The caller uses `label` to build a track description",
    "The message is printed; the function binding and caller variables remain"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side" output-width="400px">

```python {1|6|2|3|4|6|7|8}
def format_duration(seconds):
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}:{remainder:02d}"

label = format_duration(222)
message = f"Orbit [{label}]"
print(message)
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="250" :gap="70" />
</template>
</DataStructuresRun>
