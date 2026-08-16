"""Solution to Exercise 13, step 2 : json."""

import json
from datetime import date
from pathlib import Path

books: list[dict] = [
    {"title": "Fluent Python", "pages": 1012, "tags": ["python", "reference"]},
    {"title": "The Pragmatic Programmer", "pages": 352, "tags": ["craft"]},
    {"title": "Python Crash Course", "pages": 544, "tags": ["python", "beginner"]},
]

path = Path("books.json")
with path.open("w", encoding="utf-8") as f:
    json.dump(books, f, indent=2)

with path.open(encoding="utf-8") as f:
    restored = json.load(f)

for book in restored:
    if book["pages"] > 500:
        print(f"{book['title']} has {book['pages']} pages")

# A date is not one of the types JSON knows, so json.dump raises
#   TypeError: Object of type date is not JSON serializable
# Converting it to a string first is the fix the exercise asks for.
books[0]["published"] = date(2022, 3, 1).isoformat()
with path.open("w", encoding="utf-8") as f:
    json.dump(books, f, indent=2)
print("written with a published date")

path.unlink()
