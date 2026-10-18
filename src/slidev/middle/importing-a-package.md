---
layout: default
title: Importing a Package
pills: ["demo07 · implicitimport"]
---

# Importing a Package

<script setup>
const run = {
  "frames": [{"id": "global", "label": "global"}, {"id": "reports", "label": "module reports"}, {"id": "shipping", "label": "module reports.shipping"}],
  "order": ["pkg", "mod", "fn", "f50"],
  "states": [
    {"names": {"global": {}, "reports": {}, "shipping": {"FREE_SHIPPING": "f50", "delivery_cost": "fn"}}, "objects": {"fn": {"type": "function", "value": "delivery_cost"}, "f50": {"type": "float", "value": "50.0"}}, "active": ["shipping.FREE_SHIPPING", "shipping.delivery_cost"], "mark": [{"object": "fn"}, {"object": "f50"}]},
    {"names": {"global": {}, "reports": {"shipping": "mod", "delivery_cost": "fn"}, "shipping": {"FREE_SHIPPING": "f50", "delivery_cost": "fn"}}, "objects": {"mod": {"type": "module", "value": "reports.shipping"}, "fn": {"type": "function", "value": "delivery_cost"}, "f50": {"type": "float", "value": "50.0"}}, "active": ["reports.shipping", "reports.delivery_cost"], "mark": [{"object": "mod"}, {"object": "fn"}]},
    {"names": {"global": {"reports": "pkg"}, "reports": {"shipping": "mod", "delivery_cost": "fn"}, "shipping": {"FREE_SHIPPING": "f50", "delivery_cost": "fn"}}, "objects": {"pkg": {"type": "module", "value": "reports"}, "mod": {"type": "module", "value": "reports.shipping"}, "fn": {"type": "function", "value": "delivery_cost"}, "f50": {"type": "float", "value": "50.0"}}, "active": ["global.reports"], "mark": {"object": "pkg"}},
    {"names": {"global": {"reports": "pkg"}, "reports": {"shipping": "mod", "delivery_cost": "fn"}, "shipping": {"FREE_SHIPPING": "f50", "delivery_cost": "fn"}}, "objects": {"pkg": {"type": "module", "value": "reports"}, "mod": {"type": "module", "value": "reports.shipping"}, "fn": {"type": "function", "value": "delivery_cost"}, "f50": {"type": "float", "value": "50.0"}}, "active": ["global.reports", "reports.delivery_cost"], "mark": {"object": "fn"}},
    {"names": {"global": {"reports": "pkg", "delivery_cost": "fn"}, "reports": {"shipping": "mod", "delivery_cost": "fn"}, "shipping": {"FREE_SHIPPING": "f50", "delivery_cost": "fn"}}, "objects": {"pkg": {"type": "module", "value": "reports"}, "mod": {"type": "module", "value": "reports.shipping"}, "fn": {"type": "function", "value": "delivery_cost"}, "f50": {"type": "float", "value": "50.0"}}, "active": ["global.delivery_cost"], "mark": {"object": "fn"}},
    {"names": {"global": {"reports": "pkg", "delivery_cost": "fn"}, "reports": {"shipping": "mod", "delivery_cost": "fn"}, "shipping": {"FREE_SHIPPING": "f50", "delivery_cost": "fn"}}, "objects": {"pkg": {"type": "module", "value": "reports"}, "mod": {"type": "module", "value": "reports.shipping"}, "fn": {"type": "function", "value": "delivery_cost"}, "f50": {"type": "float", "value": "50.0"}}, "active": ["global.delivery_cost"], "mark": {"object": "fn"}}
  ],
  "output": [[], [], [], ["4.95"], [], ["0.0"]],
  "captions": [
    "`import reports` runs `reports/__init__.py`, whose import first runs `reports/shipping.py`",
    "Back in `__init__.py`, the package gets the names `shipping` and `delivery_cost`",
    "Then `import reports` binds the name `reports` to the package",
    "`reports.delivery_cost` is the name that `__init__.py` bound",
    "`from reports import delivery_cost` runs nothing again; it binds the same function in the calling file",
    "Called without a prefix, the function returns `0.0`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|1|1|3|5|7}
import reports

print(reports.delivery_cost(35.0))  # 4.95

from reports import delivery_cost

print(delivery_cost(75.0))  # 0.0
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="250" :gap="110" />
</template>
</DataStructuresRun>
