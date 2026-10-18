---
layout: default
title: Moving the File Position
pills: ["demo09 · file_positions"]
---

# Moving the File Position

<script setup>
const run = {
  "file": {"name": "positions.bin"},
  "cells": ["A", "B", "C", "D", "E"],
  "handles": [{"id": "fw", "mode": "wb"}, {"id": "fr", "mode": "rb"}],
  "states": [
    {"disk": 5, "buffer": null, "handles": {"fw": {"status": "closed"}}, "active": ["fw"]},
    {"disk": 5, "buffer": null, "handles": {"fw": {"status": "closed"}, "fr": {"status": "open", "position": 0, "label": "fr at 0"}}, "active": ["fr"]},
    {"disk": 5, "buffer": null, "handles": {"fw": {"status": "closed"}, "fr": {"status": "open", "position": 2, "label": "fr at 2"}}, "read": {"from": 0, "to": 2}, "active": ["fr"]},
    {"disk": 5, "buffer": null, "handles": {"fw": {"status": "closed"}, "fr": {"status": "open", "position": 2, "label": "fr at 2"}}, "active": ["fr"]},
    {"disk": 5, "buffer": null, "handles": {"fw": {"status": "closed"}, "fr": {"status": "open", "position": 0, "label": "fr at 0"}}, "active": ["fr"]},
    {"disk": 5, "buffer": null, "handles": {"fw": {"status": "closed"}, "fr": {"status": "open", "position": 2, "label": "fr at 2"}}, "read": {"from": 0, "to": 2}, "active": ["fr"]},
    {"disk": 5, "buffer": null, "handles": {"fw": {"status": "closed"}, "fr": {"status": "closed", "position": 2, "label": "fr at 2"}}, "active": ["fr"]}
  ],
  "output": [[], [], ["b'AB'"], ["2"], [], ["b'AB'"], []],
  "captions": [
    "The first block writes five bytes to `positions.bin` and closes `fw`",
    "`fr` opens the file for reading bytes; its position is 0, before the first byte",
    "`read(2)` returns the two bytes after the position and moves it to 2",
    "`tell()` reports the position, a count of bytes from the start",
    "`seek(0)` moves the position back to the start; nothing is read",
    "So the next `read(2)` returns the same two bytes again",
    "The block ends and closes `fr`; the file still holds all five bytes"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1-2|4|5|6|7|8|4}
with open("positions.bin", "wb") as fw:
    fw.write(b"ABCDE")

with open("positions.bin", "rb") as fr:
    print(fr.read(2))  # b'AB'
    print(fr.tell())  # 2
    fr.seek(0)
    print(fr.read(2))  # b'AB'
```

<template #visual="{ step }">
<StatefulFile :run="run" :step="step" />
</template>
</DataStructuresRun>
