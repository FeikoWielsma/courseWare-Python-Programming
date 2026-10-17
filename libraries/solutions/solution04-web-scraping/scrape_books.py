import re
import sqlite3
import time
from contextlib import closing
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

DATA: Path = Path(__file__).resolve().parents[2] / "data"
DB_PATH: Path = DATA / "exercise-books.db"

SITE: str = "https://books.toscrape.com"
# Step 7 : both pages of the Mystery category, twenty books and then twelve.
PAGE_URLS: list[str] = [
    f"{SITE}/catalogue/category/books/mystery_3/index.html",
    f"{SITE}/catalogue/category/books/mystery_3/page-2.html",
]
AGENT: str = "SpiralTrain-Day4-Exercise/1.0 (training exercise; you@example.com)"

RATINGS: dict[str, int] = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

SCHEMA: str = """
CREATE TABLE IF NOT EXISTS books (
    id        INTEGER PRIMARY KEY,
    title     TEXT    NOT NULL,
    price_gbp REAL    NOT NULL,
    rating    INTEGER NOT NULL,
    url       TEXT    NOT NULL UNIQUE,
    last_seen TEXT    NOT NULL
);
"""

# Step 6 : the upsert is what makes the script safe to run a second time.
UPSERT: str = """
INSERT INTO books (title, price_gbp, rating, url, last_seen)
VALUES (:title, :price_gbp, :rating, :url, :seen_at)
ON CONFLICT(url) DO UPDATE SET
    title     = excluded.title,
    price_gbp = excluded.price_gbp,
    rating    = excluded.rating,
    last_seen = excluded.last_seen
"""

type Book = dict[str, str | float | int]


def fetch_pages(urls: list[str], delay: float = 2.0) -> list[tuple[str, str]]:
    # One Session reuses the connection and carries the User-Agent on every
    # request, so the site's access log says who you are.
    session = requests.Session()
    session.headers["User-Agent"] = AGENT

    pages: list[tuple[str, str]] = []
    for index, url in enumerate(urls):
        if index:
            # The delay goes between requests, not before the first one.
            time.sleep(delay)
        response = session.get(url, timeout=10)
        response.raise_for_status()
        pages.append((url, response.text))
    return pages


def parse_books(html: str, page_url: str) -> list[Book]:
    soup = BeautifulSoup(html, "lxml")
    books: list[Book] = []
    for pod in soup.select("article.product_pod"):
        link = pod.select_one("h3 a")
        stars = pod.select_one("p.star-rating")["class"]
        books.append(
            {
                "title": link["title"],
                # The price text carries a currency sign, so keep the number only.
                "price_gbp": float(re.sub(r"[^\d.]", "", pod.select_one("p.price_color").text)),
                "rating": next((RATINGS[name] for name in stars if name in RATINGS), 0),
                "availability": pod.select_one("p.availability").get_text(strip=True),
                # A relative link is worthless once it is out of the page it came from.
                "url": urljoin(page_url, link["href"]),
            }
        )
    return books


def store(db_path: Path, books: list[Book]) -> int:
    seen_at = datetime.now(UTC).isoformat(timespec="seconds")
    with closing(sqlite3.connect(db_path)) as conn:
        conn.executescript(SCHEMA)
        # The extracted records carry one key the table does not want; the named
        # placeholders simply ignore availability, so no repackaging is needed.
        conn.executemany(UPSERT, [book | {"seen_at": seen_at} for book in books])
        conn.commit()
        return conn.execute("SELECT COUNT(*) FROM books").fetchone()[0]


def main() -> int:
    books: list[Book] = []
    for url, html in fetch_pages(PAGE_URLS):
        found = parse_books(html, url)
        print(f"Parsed {len(found):>3} books from {url}")
        books.extend(found)

    print("\nFirst three records :")
    for book in books[:3]:
        print(f"  {book}")

    total = store(DB_PATH, books)
    print(f"\nStored {len(books)} records, the table now holds {total} rows")
    print(f"Database : {DB_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
