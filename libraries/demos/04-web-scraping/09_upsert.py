import sqlite3
from datetime import UTC, datetime, timedelta

SCHEMA = """
CREATE TABLE books (
    id         INTEGER PRIMARY KEY,
    title      TEXT NOT NULL,
    price_gbp  REAL NOT NULL,
    url        TEXT NOT NULL UNIQUE,
    first_seen TEXT NOT NULL,
    last_seen  TEXT NOT NULL
);
"""

# The conflict target names the UNIQUE column. first_seen is left alone on
# purpose: it is the one column an upsert must never touch.
UPSERT = """
INSERT INTO books (title, price_gbp, url, first_seen, last_seen)
VALUES (:title, :price_gbp, :url, :seen_at, :seen_at)
ON CONFLICT(url) DO UPDATE SET
    title     = excluded.title,
    price_gbp = excluded.price_gbp,
    last_seen = excluded.last_seen
"""

BOOKS = [
    {"title": "Sharp Objects", "price_gbp": 47.82, "url": "https://example.com/sharp-objects"},
    {"title": "The Widow", "price_gbp": 27.26, "url": "https://example.com/the-widow"},
    {"title": "Most Wanted", "price_gbp": 35.28, "url": "https://example.com/most-wanted"},
]

monday = datetime(2026, 3, 2, 9, 0, tzinfo=UTC)
next_monday = monday + timedelta(days=7)

conn = sqlite3.connect(":memory:")
conn.executescript(SCHEMA)

conn.executemany(UPSERT, [book | {"seen_at": monday.isoformat()} for book in BOOKS])
for row in conn.execute("SELECT id, title, price_gbp, first_seen, last_seen FROM books"):
    print(row)

# A week later the price has moved, and the same run happens again unchanged.
moved = [
    book | {"price_gbp": 39.99} if book["title"] == "Sharp Objects" else book for book in BOOKS
]
conn.executemany(UPSERT, [book | {"seen_at": next_monday.isoformat()} for book in moved])

print()
for row in conn.execute("SELECT id, title, price_gbp, first_seen, last_seen FROM books"):
    print(row)

print(conn.execute("SELECT COUNT(*) FROM books").fetchone()[0], "rows, not 6")
conn.close()
