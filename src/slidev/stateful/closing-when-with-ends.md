---
layout: default
title: with Closes the File
pills: ["demo02 · usingwith"]
---

# with Closes the File

<script setup>
const run = {
  "file": {"name": "last_played.txt"},
  "cells": ["S", "o", " ", "W", "h", "a", "t", "\n"],
  "handles": [{"id": "fw", "mode": "w"}, {"id": "fr", "mode": "r"}],
  "states": [
    {"disk": 0, "buffer": null, "handles": {"fw": {"status": "open", "position": 0}}, "active": ["fw"]},
    {"disk": 0, "buffer": {"handle": "fw", "count": 8}, "handles": {"fw": {"status": "open", "position": 8}}, "active": ["fw"]},
    {"disk": 8, "buffer": null, "handles": {"fw": {"status": "closed", "position": 8}}, "active": ["fw"]},
    {"disk": 8, "buffer": null, "handles": {"fw": {"status": "closed", "position": 8}}, "active": ["fw"]},
    {"disk": 8, "buffer": null, "handles": {"fw": {"status": "closed", "position": 8}, "fr": {"status": "open", "position": 0}}, "active": ["fr"]},
    {"disk": 8, "buffer": null, "handles": {"fw": {"status": "closed", "position": 8}, "fr": {"status": "open", "position": 8}}, "read": {"from": 0, "to": 8}, "active": ["fr"]},
    {"disk": 8, "buffer": null, "handles": {"fw": {"status": "closed", "position": 8}, "fr": {"status": "closed", "position": 8}}, "active": ["fr"]}
  ],
  "output": [[], [], [], ["True"], [], ["So What"], []],
  "captions": [
    "`open` with mode `\"w\"` creates `last_played.txt`, or empties it; `fw` refers to the open file object",
    "`write` hands the track title to `fw`, where it waits in a buffer : the file on disk is still empty",
    "The block ends, so `with` closes `fw`, which first writes its buffer to the file",
    "`fw` still refers to the file object, now closed, so `fw.closed` is `True`",
    "The second `open` uses the default mode `\"r\"`; `fr` starts at the beginning of the file",
    "`read()` reads from the position to the end of the file, and the position moves along",
    "The second block ends and closes `fr`; the title stays in `last_played.txt` for the next run"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1|2|1|4|6|7|6}
with open("last_played.txt", mode="w", encoding="utf-8") as fw:
    fw.write("So What\n")
# The file is closed here, even if write() raised.
print(fw.closed)  # True

with open("last_played.txt", encoding="utf-8") as fr:
    print(fr.read(), end="")  # So What
```

<template #visual="{ step }">
<StatefulFile :run="run" :step="step" />
</template>
</DataStructuresRun>
