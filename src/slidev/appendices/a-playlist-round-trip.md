---
layout: default
title: A Playlist Round Trip
pills: ["demo04 · json_strings"]
---

# A Playlist Round Trip

<script setup>
const run = {
  "dicts": [{"id": "playlist", "label": "playlist", "type": "dict", "x": 0}, {"id": "restored", "label": "restored", "type": "dict", "x": 560}],
  "rows": {
    "playlist": [
      {"id": "name", "key": "'name'", "value": "'Night drive'"},
      {"id": "tracks", "key": "'tracks'", "items": ["'Imagine'", "'Yesterday'"]},
      {"id": "cover", "key": "'cover'", "value": "None"}
    ],
    "restored": [
      {"id": "cover", "key": "'cover'", "value": "None", "from": "cover"},
      {"id": "name", "key": "'name'", "value": "'Night drive'", "from": "name"},
      {"id": "tracks", "key": "'tracks'", "items": ["'Imagine'", "'Yesterday'"], "from": "tracks"}
    ]
  },
  "text": {
    "x": 290, "width": 240, "label": "text", "type": "str",
    "lines": [
      {"id": "open", "text": "{"},
      {"id": "cover", "text": "  \"cover\": null,", "hi": "null", "from": "playlist.cover"},
      {"id": "name", "text": "  \"name\": \"Night drive\",", "from": "playlist.name"},
      {"id": "tracks", "text": "  \"tracks\": [", "from": "playlist.tracks"},
      {"id": "imagine", "text": "    \"Imagine\",", "from": "playlist.tracks.0"},
      {"id": "echo", "text": "    \"Yesterday\"", "from": "playlist.tracks.1"},
      {"id": "tracks-end", "text": "  ]", "from": "playlist.tracks"},
      {"id": "close", "text": "}"}
    ]
  },
  "states": [
    {"show": ["playlist"], "active": ["playlist"]},
    {"show": ["playlist", "text"], "active": ["playlist", "text"], "mark": {"playlist.cover": "change", "text.cover": "change"}},
    {"show": ["playlist", "text", "restored"], "active": ["text", "restored"], "mark": {"text.cover": "change", "restored.cover": "change"}},
    {"show": ["playlist", "text", "restored"], "active": ["text"], "mark": {"text": "select"}},
    {
      "show": ["playlist", "text", "restored"], "active": ["playlist", "restored"], "pairs": ["name", "tracks", "cover"],
      "mark": {"playlist.name": "select", "playlist.tracks": "select", "playlist.cover": "select", "restored.cover": "select", "restored.name": "select", "restored.tracks": "select"}
    }
  ],
  "output": [
    [],
    [],
    [],
    ["{", "  \"cover\": null,", "  \"name\": \"Night drive\",", "  \"tracks\": [", "    \"Imagine\",", "    \"Yesterday\"", "  ]", "}"],
    ["True"]
  ],
  "captions": [
    "`playlist` holds a name, a list of tracks in play order and `None` for a missing cover",
    "`dumps` writes one string: `sort_keys` puts `cover` first, `None` becomes `null`, the tracks keep their order",
    "`loads` builds a new dictionary from the text; `null` comes back as `None`, keys in the order of the text",
    "`print(text)` shows the JSON exactly as `dumps` wrote it",
    "`==` pairs the entries by key, whatever their order, and compares the lists item by item: `True`"
  ]
}
</script>

<DataStructuresRun :run="run" layout="stack" output-width="280px">

```python {1-3|4|5|6|7}
import json

playlist = {"name": "Night drive", "tracks": ["Imagine", "Yesterday"], "cover": None}
text = json.dumps(playlist, indent=2, sort_keys=True)
restored = json.loads(text)
print(text)
print(restored == playlist)
```

<template #visual="{ step }">
<AppendixJson :run="run" :step="step" />
</template>
</DataStructuresRun>
