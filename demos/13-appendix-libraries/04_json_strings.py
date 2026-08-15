"""Converting between Python objects and JSON text."""

import json

book = {
    "title": "Fluent Python",
    "pages": 1012,
    "in_print": True,
    "tags": ["python", "reference"],
    "sequel": None,
}

# dumps writes a string. indent and sort_keys are for humans reading it.
text = json.dumps(book, indent=2, sort_keys=True)
print(text)

# loads reads a string back into Python objects.
restored = json.loads(text)
print(type(restored).__name__, restored["pages"], restored["sequel"])
