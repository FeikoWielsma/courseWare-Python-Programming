---
layout: default
title: Moving the File Position
pills: ["demo13 · file_positions"]
---

# Moving the File Position

<script setup>
const run = {
  "file": {"name": "trilobyte.jpg"},
  "cells": ["ff", "d8", "ff", "e0", "00", "10", "J", "F", "I", "F", "..."],
  "handles": [{"id": "photo", "mode": "rb"}],
  "states": [
    {"disk": 11, "buffer": null, "handles": {"photo": {"status": "open", "position": 0, "label": "photo at 0"}}, "active": ["photo"]},
    {"disk": 11, "buffer": null, "handles": {"photo": {"status": "open", "position": 2, "label": "photo at 2"}}, "read": {"from": 0, "to": 2}, "active": ["photo"]},
    {"disk": 11, "buffer": null, "handles": {"photo": {"status": "open", "position": 2, "label": "photo at 2"}}, "active": ["photo"]},
    {"disk": 11, "buffer": null, "handles": {"photo": {"status": "open", "position": 6, "label": "photo at 6"}}, "active": ["photo"]},
    {"disk": 11, "buffer": null, "handles": {"photo": {"status": "open", "position": 10, "label": "photo at 10"}}, "read": {"from": 6, "to": 10}, "active": ["photo"]},
    {"disk": 11, "buffer": null, "handles": {"photo": {"status": "open", "position": 0, "label": "photo at 0"}}, "active": ["photo"]},
    {"disk": 11, "buffer": null, "handles": {"photo": {"status": "open", "position": 2, "label": "photo at 2"}}, "read": {"from": 0, "to": 2}, "active": ["photo"]},
    {"disk": 11, "buffer": null, "handles": {"photo": {"status": "closed", "position": 2, "label": "photo at 2"}}, "active": ["photo"]}
  ],
  "output": [[], ["ffd8"], ["2"], [], ["b'JFIF'"], [], ["ffd8"], []],
  "captions": [
    "`photo` opens the JPEG for reading bytes; its position is 0, before the first of the ten bytes drawn",
    "`read(2)` returns the two bytes after the position and moves it to 2; `hex()` shows them",
    "`tell()` reports the position, a count of bytes from the start",
    "`seek(6)` moves the position to byte 6 without reading anything",
    "`read(4)` returns the four bytes `JFIF`, which name the photo's format",
    "`seek(0)` moves the position back to the start",
    "So the next `read(2)` returns the first two bytes again",
    "The block ends and closes `photo`; the photo itself is unchanged"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="300px">

```python {1|2|3|4|5|6|7|1}
with open("trilobyte.jpg", "rb") as photo:
    print(photo.read(2).hex())  # ffd8
    print(photo.tell())  # 2
    photo.seek(6)
    print(photo.read(4))  # b'JFIF'
    photo.seek(0)
    print(photo.read(2).hex())  # ffd8
```

<template #visual="{ step }">
<StatefulFile :run="run" :step="step" />
</template>
</DataStructuresRun>
