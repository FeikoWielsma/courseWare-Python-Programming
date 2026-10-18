---
layout: default
title: with Closes the File
pills: ["demo08 · usingwith"]
---

# with Closes the File

<script setup>
const run = {
  "file": {"name": "foo.txt"},
  "cells": ["o", "n", "e", " ", "l", "i", "n", "e", "\n"],
  "handles": [{"id": "fw", "mode": "w"}, {"id": "fr", "mode": "r"}],
  "states": [
    {"disk": 0, "buffer": null, "handles": {"fw": {"status": "open", "position": 0}}, "active": ["fw"]},
    {"disk": 0, "buffer": {"handle": "fw", "count": 9}, "handles": {"fw": {"status": "open", "position": 9}}, "active": ["fw"]},
    {"disk": 9, "buffer": null, "handles": {"fw": {"status": "closed", "position": 9}}, "active": ["fw"]},
    {"disk": 9, "buffer": null, "handles": {"fw": {"status": "closed", "position": 9}}, "active": ["fw"]},
    {"disk": 9, "buffer": null, "handles": {"fw": {"status": "closed", "position": 9}, "fr": {"status": "open", "position": 0}}, "active": ["fr"]},
    {"disk": 9, "buffer": null, "handles": {"fw": {"status": "closed", "position": 9}, "fr": {"status": "open", "position": 9}}, "read": {"from": 0, "to": 9}, "active": ["fr"]},
    {"disk": 9, "buffer": null, "handles": {"fw": {"status": "closed", "position": 9}, "fr": {"status": "closed", "position": 9}}, "active": ["fr"]}
  ],
  "output": [[], [], [], ["True"], [], ["one line"], []],
  "captions": [
    "`open` with mode `\"w\"` creates `foo.txt`, or empties it; `fw` refers to the open file object",
    "`write` hands the text to `fw`, where it waits in a buffer : the file on disk is still empty",
    "The block ends, so `with` closes `fw`, which first writes its buffer to the file",
    "`fw` still refers to the file object, now closed, so `fw.closed` is `True`",
    "The second `open` uses the default mode `\"r\"`; `fr` starts at the beginning of the file",
    "`read()` reads from the position to the end of the file, and the position moves along",
    "The second block ends and closes `fr`; the text stays in `foo.txt`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1|2|1|4|6|7|6}
with open("foo.txt", mode="w", encoding="utf-8") as fw:
    fw.write("one line\n")
# The file is closed here, even if write() raised.
print(fw.closed)  # True

with open("foo.txt", encoding="utf-8") as fr:
    print(fr.read(), end="")  # one line
```

<template #visual="{ step }">
<StatefulFile :run="run" :step="step" />
</template>
</DataStructuresRun>
