import json
from pathlib import Path

playlist = {"name": "Night drive", "tracks": ["Imagine", "Yesterday"], "cover": None}
path = Path("playlist.json")

with path.open("w", encoding="utf-8") as file:
    json.dump(playlist, file, indent=2)

with path.open(encoding="utf-8") as file:
    restored = json.load(file)
print(restored["tracks"])
