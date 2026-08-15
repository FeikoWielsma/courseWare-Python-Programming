"""dump and load work on a file object rather than a string."""

import json
from pathlib import Path

book = {"title": "Fluent Python", "pages": 1012}
path = Path("book.json")

# dump writes to an open file, no s on the end.
with path.open("w", encoding="utf-8") as f:
    json.dump(book, f, indent=2)

with path.open(encoding="utf-8") as f:
    restored = json.load(f)

print(restored)
path.unlink()  # tidy up after the demo
