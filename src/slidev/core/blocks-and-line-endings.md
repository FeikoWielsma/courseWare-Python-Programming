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
    {"writes": [{"text": "True", "newline": true}]},
    {"writes": [{"text": "True", "newline": true}]},
    {"writes": [{"text": "True", "newline": true}, {"text": "I repeat, the value is 5", "newline": true}]},
    {"writes": [{"text": "True", "newline": true}, {"text": "I repeat, the value is 5", "newline": true}, {"text": "hello python", "newline": false}]},
    {"writes": [{"text": "True", "newline": true}, {"text": "I repeat, the value is 5", "newline": true}, {"text": "hello python", "newline": false}, {"text": " on the same line as previous print output", "newline": true}]}
  ],
  "output": [[], ["True"], [], ["I repeat, the value is 5"], [], ["hello python on the same line as previous print output"]],
  "captions": [
    "`if True:` is true, so the indented block under it runs",
    "`print()` writes `True`, then ends the line with a newline",
    "The `else` block is skipped; execution continues at the next unindented line",
    "The comment line does nothing; `print()` separates its arguments with a space",
    "`end=\"\"` replaces the newline, so the line stays open",
    "The next `print()` continues on the same line, then ends it"
  ]
}
</script>

<DataStructuresRun :run="run" layout="rows">

```python {1|2|6|8|9|10}
if True:  # Both blocks in first example are fine
    print("True")
else:
    print("False")

i = 5
# print('Value is', i); # Error! Notice a single space at the start of the line
print("I repeat, the value is", i)
print("hello python", end="")
print(" on the same line as previous print output")
```

<template #visual="{ step }">
<CoreStream :run="run" :step="step" />
</template>
</DataStructuresRun>

<style>
.ds-code .slidev-code { --slidev-code-font-size: 16px; --slidev-code-line-height: 1.35; }
</style>
