---
layout: default
title: finally While an Exception Propagates
pills: ["demo07 · tryfinally"]
---

# finally While an Exception Propagates

<script setup>
const run = {
  "frames": [
    {"id": "module", "label": "<module>", "clauses": [{"id": "try", "text": "try:"}, {"id": "except", "text": "except ValueError:"}]},
    {"id": "parse_seconds", "label": "parse_seconds()", "clauses": [{"id": "try", "text": "try:"}, {"id": "finally", "text": "finally:"}]}
  ],
  "exceptions": {"zde": {"type": "ValueError", "message": "invalid literal for int() with base 10: 'live'"}},
  "states": [
    {"frames": ["module", "parse_seconds"], "clauses": {"module.try": "run"}, "exception": null},
    {"frames": ["module", "parse_seconds"], "clauses": {"module.try": "run", "parse_seconds.try": "raised"}, "exception": {"id": "zde", "at": "parse_seconds.try", "handled": false}},
    {"frames": ["module", "parse_seconds"], "clauses": {"module.try": "run", "parse_seconds.try": "raised", "parse_seconds.finally": "run"}, "exception": {"id": "zde", "at": "parse_seconds.finally", "handled": false}},
    {"frames": ["module"], "clauses": {"module.try": "raised"}, "exception": {"id": "zde", "at": "module.try", "handled": false}},
    {"frames": ["module"], "clauses": {"module.try": "raised", "module.except": "match"}, "exception": {"id": "zde", "at": "module.except", "handled": false}},
    {"frames": ["module"], "clauses": {"module.try": "raised", "module.except": "match"}, "exception": {"id": "zde", "at": "module.except", "handled": true}}
  ],
  "output": [[], [], ["Duration check finished"], [], [], ["Duration unavailable"]],
  "captions": [
    "The `try` block calls `parse_seconds('live')`",
    "`int(text)` raises `ValueError`, so `return` hands nothing back",
    "On the way out, `finally` runs; the exception still has no handler",
    "`parse_seconds` has no handler, so the call ends and the exception reaches its caller",
    "`except ValueError` matches the exception",
    "The handler runs; the program continues after the `try` statement"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {8-9|2-3|4-5|9|10|11}
def parse_seconds(text: str) -> int:
    try:
        return int(text)
    finally:
        print("Duration check finished")


try:
    parse_seconds("live")
except ValueError:
    print("Duration unavailable")
```

<template #visual="{ step }">
<MiddleExceptions :run="run" :step="step" :frame-width="300" :gap="32" :card-width="220" />
</template>
</DataStructuresRun>
