---
layout: default
title: finally While an Exception Propagates
pills: ["demo07 · tryfinally"]
---

# finally While an Exception Propagates

<script setup>
const run = {
  "frames": [
    {"id": "module", "label": "<module>", "clauses": [{"id": "try", "text": "try:"}, {"id": "except", "text": "except ZeroDivisionError:"}]},
    {"id": "divide", "label": "divide()", "clauses": [{"id": "try", "text": "try:"}, {"id": "finally", "text": "finally:"}]}
  ],
  "exceptions": {"zde": {"type": "ZeroDivisionError", "message": "division by zero"}},
  "states": [
    {"frames": ["module", "divide"], "clauses": {"module.try": "run"}, "exception": null},
    {"frames": ["module", "divide"], "clauses": {"module.try": "run", "divide.try": "raised"}, "exception": {"id": "zde", "at": "divide.try", "handled": false}},
    {"frames": ["module", "divide"], "clauses": {"module.try": "run", "divide.try": "raised", "divide.finally": "run"}, "exception": {"id": "zde", "at": "divide.finally", "handled": false}},
    {"frames": ["module"], "clauses": {"module.try": "raised"}, "exception": {"id": "zde", "at": "module.try", "handled": false}},
    {"frames": ["module"], "clauses": {"module.try": "raised", "module.except": "match"}, "exception": {"id": "zde", "at": "module.except", "handled": false}},
    {"frames": ["module"], "clauses": {"module.try": "raised", "module.except": "match"}, "exception": {"id": "zde", "at": "module.except", "handled": true}}
  ],
  "output": [[], [], ["This always runs"], [], [], ["Cannot divide by zero"]],
  "captions": [
    "The `try` block calls `divide(10, 0)`",
    "`total / count` raises `ZeroDivisionError`, so `return` hands nothing back",
    "On the way out, `finally` runs; the exception still has no handler",
    "`divide` has no handler, so the call ends and the exception reaches its caller",
    "`except ZeroDivisionError` matches the exception",
    "The handler runs; the program continues after the `try` statement"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {8-9|2-3|4-5|9|10|11}
def divide(total: int, count: int) -> float:
    try:
        return total / count
    finally:
        print("This always runs")


try:
    divide(10, 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

<template #visual="{ step }">
<MiddleExceptions :run="run" :step="step" :frame-width="300" :gap="32" :card-width="220" />
</template>
</DataStructuresRun>
