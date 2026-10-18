---
layout: default
title: Importing a Module
pills: ["demo01 · importmodule"]
---

# Importing a Module

<script setup>
const run = {
  "frames": [{"id": "global", "label": "global"}, {"id": "shipping", "label": "module shipping"}],
  "order": ["mod", "f50", "fn"],
  "states": [
    {"names": {"global": {}, "shipping": {"FREE_SHIPPING": "f50", "delivery_cost": "fn"}}, "objects": {"f50": {"type": "float", "value": "50.0"}, "fn": {"type": "function", "value": "delivery_cost"}}, "active": ["shipping.FREE_SHIPPING", "shipping.delivery_cost"], "mark": [{"object": "f50"}, {"object": "fn"}]},
    {"names": {"global": {"shipping": "mod"}, "shipping": {"FREE_SHIPPING": "f50", "delivery_cost": "fn"}}, "objects": {"mod": {"type": "module", "value": "shipping"}, "f50": {"type": "float", "value": "50.0"}, "fn": {"type": "function", "value": "delivery_cost"}}, "active": ["global.shipping"], "mark": {"object": "mod"}},
    {"names": {"global": {"shipping": "mod"}, "shipping": {"FREE_SHIPPING": "f50", "delivery_cost": "fn"}}, "objects": {"mod": {"type": "module", "value": "shipping"}, "f50": {"type": "float", "value": "50.0"}, "fn": {"type": "function", "value": "delivery_cost"}}, "active": ["global.shipping", "shipping.delivery_cost"], "mark": {"object": "fn"}},
    {"names": {"global": {"shipping": "mod"}, "shipping": {"FREE_SHIPPING": "f50", "delivery_cost": "fn"}}, "objects": {"mod": {"type": "module", "value": "shipping"}, "f50": {"type": "float", "value": "50.0"}, "fn": {"type": "function", "value": "delivery_cost"}}, "active": ["global.shipping", "shipping.delivery_cost"], "mark": {"object": "fn"}},
    {"names": {"global": {"shipping": "mod", "delivery": "mod"}, "shipping": {"FREE_SHIPPING": "f50", "delivery_cost": "fn"}}, "objects": {"mod": {"type": "module", "value": "shipping"}, "f50": {"type": "float", "value": "50.0"}, "fn": {"type": "function", "value": "delivery_cost"}}, "active": ["global.delivery"], "mark": {"object": "mod"}},
    {"names": {"global": {"shipping": "mod", "delivery": "mod"}, "shipping": {"FREE_SHIPPING": "f50", "delivery_cost": "fn"}}, "objects": {"mod": {"type": "module", "value": "shipping"}, "f50": {"type": "float", "value": "50.0"}, "fn": {"type": "function", "value": "delivery_cost"}}, "active": ["global.delivery", "shipping.FREE_SHIPPING"], "mark": {"object": "f50"}}
  ],
  "output": [[], [], ["4.95"], ["0.0"], [], ["50.0"]],
  "captions": [
    "`import shipping` runs `shipping.py`, which binds `FREE_SHIPPING` and `delivery_cost` in the module",
    "Then it binds the name `shipping` to the module",
    "`shipping.delivery_cost` finds `delivery_cost` in the module and calls it",
    "The same function, called with `75.0`, returns `0.0`",
    "`import shipping as delivery` binds a second name to the same module; `shipping.py` does not run again",
    "`delivery.FREE_SHIPPING` reaches the module's `FREE_SHIPPING`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|1|3|4|6|8}
import shipping

print(shipping.delivery_cost(35.0))  # 4.95
print(shipping.delivery_cost(75.0))  # 0.0

import shipping as delivery

print(delivery.FREE_SHIPPING)  # 50.0
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="240" :gap="110" />
</template>
</DataStructuresRun>
