import re
import sqlite3
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
DB = Path(__file__).resolve().parents[2] / "data" / "books.db"
RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

# The url is the natural key : one page, one book, whatever the title says.
# UNIQUE on it is what makes the upsert in the next demo possible.
SCHEMA = """
DROP TABLE IF EXISTS books;
CREATE TABLE books (
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

INSERT = """
INSERT INTO books (title, price_gbp, rating, availability, category, url, first_seen, last_seen)
VALUES (:title, :price_gbp, :rating, :availability, :category, :url, :seen_at, :seen_at)
"""

soup = BeautifulSoup(requests.get(URL, timeout=10).text, "lxml")
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

conn = sqlite3.connect(DB)
conn.executescript(SCHEMA)
# Named placeholders take the dictionaries exactly as they already are.
conn.executemany(INSERT, books)
conn.commit()

print(conn.execute("SELECT COUNT(*) FROM books").fetchone()[0], "rows in", DB)

for title, price in conn.execute("SELECT title, price_gbp FROM books ORDER BY price_gbp DESC"):
    print(f"{price:>6.2f}  {title}")

wanted = "The Bachelor Girl's Guide to Murder (Herringford and Watts Mysteries #1)"

# Never do this. Written out once so the failure is a memory, not a warning.
try:
    conn.execute(f"SELECT COUNT(*) FROM books WHERE title = '{wanted}'")
except sqlite3.OperationalError as error:
    print("formatted    :", error)

found = conn.execute("SELECT COUNT(*) FROM books WHERE title = ?", (wanted,)).fetchone()[0]
print("parameterised:", found)

conn.close()
