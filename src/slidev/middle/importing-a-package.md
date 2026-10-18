---
layout: default
title: Importing a Package
pills: ["demo07 · implicitimport"]
---

# Importing a Package

<script setup>
const run = {
  "frames": [{"id": "global", "label": "global"}, {"id": "player", "label": "module player"}, {"id": "timing", "label": "module player.timing"}],
  "order": ["pkg", "mod", "fn", "f50"],
  "states": [
    {"names": {"global": {}, "player": {}, "timing": {"SECONDS_PER_MINUTE": "f50", "format_duration": "fn"}}, "objects": {"fn": {"type": "function", "value": "format_duration"}, "f50": {"type": "int", "value": "60"}}, "active": ["timing.SECONDS_PER_MINUTE", "timing.format_duration"], "mark": [{"object": "fn"}, {"object": "f50"}]},
    {"names": {"global": {}, "player": {"timing": "mod", "format_duration": "fn"}, "timing": {"SECONDS_PER_MINUTE": "f50", "format_duration": "fn"}}, "objects": {"mod": {"type": "module", "value": "player.timing"}, "fn": {"type": "function", "value": "format_duration"}, "f50": {"type": "int", "value": "60"}}, "active": ["player.timing", "player.format_duration"], "mark": [{"object": "mod"}, {"object": "fn"}]},
    {"names": {"global": {"player": "pkg"}, "player": {"timing": "mod", "format_duration": "fn"}, "timing": {"SECONDS_PER_MINUTE": "f50", "format_duration": "fn"}}, "objects": {"pkg": {"type": "module", "value": "player"}, "mod": {"type": "module", "value": "player.timing"}, "fn": {"type": "function", "value": "format_duration"}, "f50": {"type": "int", "value": "60"}}, "active": ["global.player"], "mark": {"object": "pkg"}},
    {"names": {"global": {"player": "pkg"}, "player": {"timing": "mod", "format_duration": "fn"}, "timing": {"SECONDS_PER_MINUTE": "f50", "format_duration": "fn"}}, "objects": {"pkg": {"type": "module", "value": "player"}, "mod": {"type": "module", "value": "player.timing"}, "fn": {"type": "function", "value": "format_duration"}, "f50": {"type": "int", "value": "60"}}, "active": ["global.player", "player.format_duration"], "mark": {"object": "fn"}},
    {"names": {"global": {"player": "pkg", "format_duration": "fn"}, "player": {"timing": "mod", "format_duration": "fn"}, "timing": {"SECONDS_PER_MINUTE": "f50", "format_duration": "fn"}}, "objects": {"pkg": {"type": "module", "value": "player"}, "mod": {"type": "module", "value": "player.timing"}, "fn": {"type": "function", "value": "format_duration"}, "f50": {"type": "int", "value": "60"}}, "active": ["global.format_duration"], "mark": {"object": "fn"}},
    {"names": {"global": {"player": "pkg", "format_duration": "fn"}, "player": {"timing": "mod", "format_duration": "fn"}, "timing": {"SECONDS_PER_MINUTE": "f50", "format_duration": "fn"}}, "objects": {"pkg": {"type": "module", "value": "player"}, "mod": {"type": "module", "value": "player.timing"}, "fn": {"type": "function", "value": "format_duration"}, "f50": {"type": "int", "value": "60"}}, "active": ["global.format_duration"], "mark": {"object": "fn"}}
  ],
  "output": [[], [], [], ["3:42"], [], ["1:05"]],
  "captions": [
    "`import player` runs `player/__init__.py`, whose import first runs `player/timing.py`",
    "Back in `__init__.py`, the package gets the names `timing` and `format_duration`",
    "Then `import player` binds the name `player` to the package",
    "`player.format_duration` is the name that `__init__.py` bound",
    "`from player import format_duration` runs nothing again; it binds the same function in the calling file",
    "Called without a prefix, the function returns `1:05`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1|1|1|3|5|7}
import player

print(player.format_duration(222))  # 3:42

from player import format_duration

print(format_duration(65))  # 1:05
```

<template #visual="{ step }">
<CoreNames :run="run" :step="step" :frame-width="250" :gap="110" />
</template>
</DataStructuresRun>
