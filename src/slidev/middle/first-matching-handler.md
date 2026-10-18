---
layout: default
title: The First Matching Handler
pills: ["demo03 · typedexceptionhandling"]
---

# The First Matching Handler

<script setup>
const run = {
  "frames": [
    {"id": "module", "label": "<module>", "clauses": [{"id": "try", "text": "try:"}, {"id": "notfound", "text": "except ValueError:"}, {"id": "oserror", "text": "except Exception as error:"}, {"id": "else", "text": "else:"}]}
  ],
  "exceptions": {"fnf": {"type": "ValueError", "message": "invalid literal for int() with base 10: 'three'"}},
  "states": [
    {"frames": ["module"], "clauses": {"module.try": "raised"}, "exception": {"id": "fnf", "at": "module.try", "handled": false}},
    {"frames": ["module"], "clauses": {"module.try": "raised", "module.notfound": "match"}, "exception": {"id": "fnf", "at": "module.notfound", "handled": false}},
    {"frames": ["module"], "clauses": {"module.try": "raised", "module.notfound": "match", "module.oserror": "unchecked", "module.else": "skip"}, "exception": {"id": "fnf", "at": "module.notfound", "handled": true}}
  ],
  "output": [[], [], ["Track length must be a whole number"]],
  "captions": [
    "`int('three')` raises `ValueError`, so `seconds` is never bound",
    "Python tries the handlers in order; the first, `ValueError`, matches",
    "Its block runs; `except Exception` would also match but is not checked, and `else` is skipped"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1-2|3|4}
try:
    seconds = int("three")
except ValueError:
    print("Track length must be a whole number")
except Exception as error:
    print(f"Other problem: {error}")
else:
    print(f"Track length: {seconds}")
```

<template #visual="{ step }">
<MiddleExceptions :run="run" :step="step" :frame-width="300" :gap="32" :card-width="240" />
</template>
</DataStructuresRun>
