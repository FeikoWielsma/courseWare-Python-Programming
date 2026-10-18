import re
import sqlite3
import sys
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
DB = Path(__file__).resolve().parents[2] / "data" / "books.db"
RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

SCHEMA = """
CREATE TABLE IF NOT EXISTS books (
    id           INTEGER PRIMARY KEY,
    title        TEXT    NOT NULL,
    price_gbp    REAL    NOT NULL,
    rating       INTEGER NOT NULL,
    availability TEXT    NOT NULL,
    category     TEXT    NOT NULL,
    url          TEXT    NOT NULL UNIQUE,
    first_seen   TEXT    NOT NULL,
    last_seen    TEXT    NOT NULL
);
"""

UPSERT = """
INSERT INTO books (title, price_gbp, rating, availability, category, url, first_seen, last_seen)
VALUES (:title, :price_gbp, :rating, :availability, :category, :url, :seen_at, :seen_at)
ON CONFLICT(url) DO UPDATE SET
    title        = excluded.title,
    price_gbp    = excluded.price_gbp,
    rating       = excluded.rating,
    availability = excluded.availability,
    last_seen    = excluded.last_seen
"""

# Fetch.
if "--live" in sys.argv:
    html = requests.get(URL, timeout=10).text
else:
    fixture = Path(__file__).resolve().parents[2] / "data" / "books-fixture.html"
    html = fixture.read_text(encoding="utf-8")
soup = BeautifulSoup(html, "lxml")

# Parse.
category = soup.select_one("ul.breadcrumb li.active").get_text(strip=True)
seen_at = datetime.now(UTC).isoformat(timespec="seconds")
books = []
for pod in soup.select("article.product_pod"):
    link = pod.select_one("h3 a")
    books.append(
        {
            "title": link["title"],
            "price_gbp": float(re.sub(r"[^\d.]", "", pod.select_one("p.price_color").text)),
            "rating": RATINGS[pod.select_one("p.star-rating")["class"][1]],
            "availability": pod.select_one("p.availability").get_text(strip=True),
            "category": category,
            "url": urljoin(URL, link["href"]),
            "seen_at": seen_at,
        }
    )

# Store. Running this twice changes last_seen and nothing else.
conn = sqlite3.connect(DB)
conn.executescript(SCHEMA)
before = conn.execute("SELECT COUNT(*) FROM books").fetchone()[0]
conn.executemany(UPSERT, books)
conn.commit()
after = conn.execute("SELECT COUNT(*) FROM books").fetchone()[0]

print(f"parsed {len(books)}, table went from {before} to {after} rows")

# Report.
query = """
SELECT rating, COUNT(*), ROUND(AVG(price_gbp), 2) FROM books GROUP BY rating ORDER BY rating
"""
for rating, count, average in conn.execute(query):
    print(f"{rating} stars {count:>3} books {average:>8.2f} average")

conn.close()
