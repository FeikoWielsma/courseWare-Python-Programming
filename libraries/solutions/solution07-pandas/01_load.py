import sqlite3
from contextlib import closing
from pathlib import Path

import pandas as pd

DATA: Path = Path(__file__).resolve().parents[2] / "data"
BOOKS_DB: Path = DATA / "books.db"
BOOKS_CSV: Path = DATA / "books-sample.csv"


def load_books() -> pd.DataFrame:
    if BOOKS_DB.exists():
        with closing(sqlite3.connect(BOOKS_DB)) as conn:
            return pd.read_sql("SELECT * FROM books", conn)
    return pd.read_csv(BOOKS_CSV)


def main() -> None:
    if BOOKS_DB.exists():
        with closing(sqlite3.connect(BOOKS_DB)) as conn:
            tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'", conn)
        print("tables in", BOOKS_DB.name)
        print(tables)
    else:
        print(BOOKS_DB.name, "is not here yet, reading", BOOKS_CSV.name, "instead")

    books = load_books()
    print("\nshape   :", books.shape)
    print("columns :", list(books.columns))
    print("\nfirst five rows:")
    print(books[["title", "price_gbp", "rating", "category"]].head())


if __name__ == "__main__":
    main()
