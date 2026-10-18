---
layout: default
title: The First Matching Handler
pills: ["demo03 · typedexceptionhandling"]
---

# The First Matching Handler

<script setup>
const run = {
  "frames": [
    {"id": "module", "label": "<module>", "clauses": [{"id": "try", "text": "try:"}, {"id": "notfound", "text": "except FileNotFoundError:"}, {"id": "oserror", "text": "except OSError as error:"}, {"id": "else", "text": "else:"}]}
  ],
  "exceptions": {"fnf": {"type": "FileNotFoundError", "message": "[Errno 2] No such file or directory: 'somefile'"}},
  "states": [
    {"frames": ["module"], "clauses": {"module.try": "raised"}, "exception": {"id": "fnf", "at": "module.try", "handled": false}},
    {"frames": ["module"], "clauses": {"module.try": "raised", "module.notfound": "match"}, "exception": {"id": "fnf", "at": "module.notfound", "handled": false}},
    {"frames": ["module"], "clauses": {"module.try": "raised", "module.notfound": "match", "module.oserror": "unchecked", "module.else": "skip"}, "exception": {"id": "fnf", "at": "module.notfound", "handled": true}}
  ],
  "output": [[], [], ["The file does not exist"]],
  "captions": [
    "`open` raises `FileNotFoundError`, so `fh` is never bound",
    "Python tries the handlers in order; the first, `FileNotFoundError`, matches",
    "Its block runs; `except OSError` would also match but is not checked, and `else` is skipped"
  ]
}
</script>

<DataStructuresRun :run="run" layout="side">

```python {1-2|3|4}
try:
    fh = open("somefile", "r")
except FileNotFoundError:
    print("The file does not exist")
except OSError as error:
    print(f"Cannot open the file: {error}")
else:
    fh.close()
```

<template #visual="{ step }">
<MiddleExceptions :run="run" :step="step" :frame-width="300" :gap="32" :card-width="240" />
</template>
</DataStructuresRun>
