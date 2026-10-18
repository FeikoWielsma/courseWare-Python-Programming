---
layout: default
title: Blocks and Line Endings
pills: ["demo04 · lines_and_identation"]
---

# Blocks and Line Endings

<script setup>
const run = {
  "states": [
    {"writes": []},
    {"writes": [{"text": "Photo ready", "newline": true}]},
    {"writes": [{"text": "Photo ready", "newline": true}]},
    {"writes": [{"text": "Photo ready", "newline": true}, {"text": "Photos selected: 5", "newline": true}]},
    {"writes": [{"text": "Photo ready", "newline": true}, {"text": "Photos selected: 5", "newline": true}, {"text": "Playing ", "newline": false}]},
    {"writes": [{"text": "Photo ready", "newline": true}, {"text": "Photos selected: 5", "newline": true}, {"text": "Playing ", "newline": false}, {"text": "Orbit", "newline": true}]}
  ],
  "output": [[], ["Photo ready"], [], ["Photos selected: 5"], [], ["Playing Orbit"]],
  "captions": [
    "`if True:` is true, so the indented block under it runs",
    "`print()` writes `Photo ready`, then ends the line with a newline",
    "The `else` block is skipped; execution continues at the next unindented line",
    "The comment line does nothing; `print()` separates its arguments with a space",
    "`end=\" \"` replaces the newline, so the line stays open",
    "The next `print()` continues on the same line, then ends it"
  ]
}
</script>

<DataStructuresRun :run="run" layout="rows">

```python {1|2|6|8|9|10}
if True:  # The indented block runs.
    print("Photo ready")
else:
    print("Photo missing")

photos = 5
# This comment does not change the photo count.
print("Photos selected:", photos)
print("Playing", end=" ")
print("Orbit")
```

<template #visual="{ step }">
<CoreStream :run="run" :step="step" />
</template>
</DataStructuresRun>

<style>
.ds-code .slidev-code { --slidev-code-font-size: 16px; --slidev-code-line-height: 1.35; }
</style>
