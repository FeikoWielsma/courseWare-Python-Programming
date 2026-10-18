---
layout: default
title: A Lookup That May Find Nothing
pills: ["demo03 · optional"]
---

# A Lookup That May Find Nothing

<script setup>
const run = {
  "dict": {
    "name": "durations", "type": "dict[str, int]", "x": 0, "y": 0,
    "rows": [{"id": "imagine", "key": "'Imagine'", "value": "183"}, {"id": "echo", "key": "'Yesterday'", "value": "125"}]
  },
  "returns": {"x": 330, "y": 0, "label": "returns int | None", "lanes": [{"id": "int", "type": "int"}, {"id": "none", "type": "None"}]},
  "names": [{"id": "title", "x": 0, "y": 196}, {"id": "seconds", "x": 610, "y": 99}],
  "chips": [
    {"id": "title", "text": "'Wonderwall'"},
    {"id": "probe", "text": "'Wonderwall'", "enter": "title"},
    {"id": "result", "text": "None", "enter": "missing-value"}
  ],
  "places": {
    "title": {"x": 131, "y": 198},
    "missing-key": {"x": 13, "y": 128},
    "missing-value": {"x": 140, "y": 128},
    "lane-none": {"x": 451, "y": 101},
    "seconds": {"x": 757, "y": 101}
  },
  "states": [
    {"dict": false, "names": [], "chips": {}, "active": ["returns"]},
    {"dict": true, "names": [], "chips": {}, "active": ["dict"]},
    {"dict": true, "names": ["title"], "chips": {"title": "title"}, "active": ["title", "returns"], "mark": ["title"]},
    {"dict": true, "names": ["title"], "chips": {"title": "title", "probe": "missing-key", "result": "lane-none"}, "missing": {"key": "", "note": "not a key"}, "lane": "none", "active": ["dict", "title"], "mark": ["result"]},
    {"dict": true, "names": ["seconds"], "chips": {"result": "seconds"}, "lane": "none", "active": ["seconds"]},
    {"dict": true, "names": ["seconds"], "chips": {"result": "seconds"}, "lane": "none", "check": {"name": "seconds", "text": "is None → True"}, "active": ["seconds"], "mark": ["result"]},
    {"dict": true, "names": ["seconds"], "chips": {"result": "seconds"}, "lane": "none", "check": {"name": "seconds", "text": "is None → True"}, "active": []}
  ],
  "output": [[], [], [], [], [], [], ["Track not found"]],
  "captions": [
    "The definition binds `find_duration`; its annotation allows two kinds of result, an `int` or `None`",
    "`durations` maps each track title to its length in seconds",
    "The call passes `'Wonderwall'` as `title`, and the same dictionary as `durations`",
    "`.get(title)` finds no `'Wonderwall'` key, so it returns `None`, the second kind of result",
    "The call has ended; `seconds` refers to `None`, not to a number of seconds",
    "The guard tests for `None` before the value is used as a duration",
    "The `None` branch reports the missing track; the `else` branch would receive an `int`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="230px">

```python {1-2|5|6|2|6|7|8}
def find_duration(title: str, durations: dict[str, int]) -> int | None:
    return durations.get(title)


durations = {"Imagine": 183, "Yesterday": 125}
seconds = find_duration("Wonderwall", durations)
if seconds is None:
    print("Track not found")
else:
    print(f"Track length: {seconds} seconds")
```

<template #visual="{ step }">
<AppendixOptional :run="run" :step="step" />
</template>
</DataStructuresRun>
