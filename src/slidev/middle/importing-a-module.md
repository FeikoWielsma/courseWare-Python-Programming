---
layout: default
title: Importing a Module
pills: ["demo01 · importmodule"]
---

# Importing a Module

<script setup>
const run = {
  "frames": [{"id": "global", "label": "global"}, {"id": "timing", "label": "module timing"}],
  "order": ["mod", "f50", "fn"],
  "states": [
    {"names": {"global": {}, "timing": {"SECONDS_PER_MINUTE": "f50", "format_duration": "fn"}}, "objects": {"f50": {"type": "int", "value": "60"}, "fn": {"type": "function", "value": "format_duration"}}, "active": ["timing.SECONDS_PER_MINUTE", "timing.format_duration"], "mark": [{"object": "f50"}, {"object": "fn"}]},
    {"names": {"global": {"timing": "mod"}, "timing": {"SECONDS_PER_MINUTE": "f50", "format_duration": "fn"}}, "objects": {"mod": {"type": "module", "value": "timing"}, "f50": {"type": "int", "value": "60"}, "fn": {"type": "function", "value": "format_duration"}}, "active": ["global.timing"], "mark": {"object": "mod"}},
    {"names": {"global": {"timing": "mod"}, "timing": {"SECONDS_PER_MINUTE": "f50", "format_duration": "fn"}}, "objects": {"mod": {"type": "module", "value": "timing"}, "f50": {"type": "int", "value": "60"}, "fn": {"type": "function", "value": "format_duration"}}, "active": ["global.timing", "timing.format_duration"], "mark": {"object": "fn"}},
    {"names": {"global": {"timing": "mod"}, "timing": {"SECONDS_PER_MINUTE": "f50", "format_duration": "fn"}}, "objects": {"mod": {"type": "module", "value": "timing"}, "f50": {"type": "int", "value": "60"}, "fn": {"type": "function", "value": "format_duration"}}, "active": ["global.timing", "timing.format_duration"], "mark": {"object": "fn"}},
    {"names": {"global": {"timing": "mod", "clock": "mod"}, "timing": {"SECONDS_PER_MINUTE": "f50", "format_duration": "fn"}}, "objects": {"mod": {"type": "module", "value": "timing"}, "f50": {"type": "int", "value": "60"}, "fn": {"type": "function", "value": "format_duration"}}, "active": ["global.clock"], "mark": {"object": "mod"}},
    {"names": {"global": {"timing": "mod", "clock": "mod"}, "timing": {"SECONDS_PER_MINUTE": "f50", "format_duration": "fn"}}, "objects": {"mod": {"type": "module", "value": "timing"}, "f50": {"type": "int", "value": "60"}, "fn": {"type": "function", "value": "format_duration"}}, "active": ["global.clock", "timing.SECONDS_PER_MINUTE"], "mark": {"object": "f50"}}
  ],
  "output": [[], [], ["3:42"], ["1:05"], [], ["60"]],
  "captions": [
    "`import timing` runs `timing.py`, which binds `SECONDS_PER_MINUTE` and `format_duration` in the module",
    "Then it binds the name `timing` to the module",
    "`timing.format_duration` finds `format_duration` in the module and calls it",
    "The same formatter displays `65` seconds as `1:05`",
    "`import timing as clock` binds a second name to the same module; `timing.py` does not run again",
    "`clock.SECONDS_PER_MINUTE` reaches the module's `SECONDS_PER_MINUTE`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|1|3|4|6|8}
import timing

print(timing.format_duration(222))  # 3:42
print(timing.format_duration(65))  # 1:05

import timing as clock

print(clock.SECONDS_PER_MINUTE)  # 60
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="240" :gap="110" />
</template>
</DataStructuresRun>
