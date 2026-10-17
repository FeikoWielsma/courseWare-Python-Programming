import sqlite3
from contextlib import closing
from pathlib import Path

from scrape_books import PAGE_URLS, fetch_pages, parse_books, store

DB_PATH: Path = Path(__file__).resolve().parents[2] / "data" / "exercise-books.db"


def most_expensive(conn: sqlite3.Connection, limit: int = 5) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT title, price_gbp FROM books ORDER BY price_gbp DESC LIMIT ?", (limit,)
    ).fetchall()


def per_rating(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT rating, COUNT(*) AS books, ROUND(AVG(price_gbp), 2) AS average "
        "FROM books GROUP BY rating ORDER BY rating"
    ).fetchall()


def cheaper_than(conn: sqlite3.Connection, price: float) -> int:
    # The threshold is a parameter, not something formatted into the SQL text.
    return conn.execute("SELECT COUNT(*) FROM books WHERE price_gbp < ?", (price,)).fetchone()[0]


def build_if_missing() -> None:
    # Running this file on its own should work, so scrape the first page here
    # rather than demanding that scrape_books.py was run first.
    if DB_PATH.exists():
        return
    url, html = fetch_pages(PAGE_URLS[:1])[0]
    books = parse_books(html, url)
    store(DB_PATH, books)
    print(f"Built {DB_PATH.name} from {url}, {len(books)} rows")


def main() -> int:
    build_if_missing()

    with closing(sqlite3.connect(DB_PATH)) as conn:
        # Rows behave as dictionaries as well as tuples, which pays for itself
        # the moment a query returns more than two columns.
        conn.row_factory = sqlite3.Row

        print("The five most expensive :")
        for row in most_expensive(conn):
            print(f"  {row['price_gbp']:>6.2f}  {row['title']}")

        print(f"\n{'Stars':<7}{'Books':>7}{'Average price':>16}")
        for row in per_rating(conn):
            print(f"{row['rating']:<7}{row['books']:>7}{row['average']:>16.2f}")

        print(f"\nBooks under 20.00 : {cheaper_than(conn, 20.0)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
