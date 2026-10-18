import json

playlist = {"name": "Night drive", "tracks": ["Imagine", "Yesterday"], "cover": None}
text = json.dumps(playlist, indent=2, sort_keys=True)
restored = json.loads(text)
print(text)
print(restored == playlist)
