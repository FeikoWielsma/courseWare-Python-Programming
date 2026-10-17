import sqlite3
from contextlib import closing
from pathlib import Path

import pandas as pd

DATA: Path = Path(__file__).resolve().parents[2] / "data"
BOOKS_DB: Path = DATA / "books.db"
BOOKS_CSV: Path = DATA / "books-sample.csv"

COLUMNS: list[str] = ["title", "price_gbp", "rating", "availability"]


def load_books() -> pd.DataFrame:
    if BOOKS_DB.exists():
        with closing(sqlite3.connect(BOOKS_DB)) as conn:
            return pd.read_sql("SELECT * FROM books", conn)
    return pd.read_csv(BOOKS_CSV)


def main() -> None:
    books = load_books()

    # A mask is an ordinary value. Giving it a name costs nothing and makes the
    # combination below readable.
    well_rated = books["rating"] >= 4
    in_stock = books["availability"] == "In stock"
    affordable = books["price_gbp"] < 40.0

    print("well rated :", int(well_rated.sum()))
    print("in stock   :", int(in_stock.sum()))
    print("affordable :", int(affordable.sum()))

    # & rather than and, because and wants one true-or-false answer and a mask
    # has twenty. Each comparison needs its own parentheses.
    shortlist = books[well_rated & in_stock & affordable]
    print(f"\nall three at once, {len(shortlist)} rows:")
    print(shortlist[COLUMNS].to_string(index=False))

    print("\nisin replaces a chain of ORs:")
    print(books[books["rating"].isin([4, 5])][COLUMNS].head().to_string(index=False))

    print("\nbetween replaces two comparisons, and includes both ends:")
    print(books[books["price_gbp"].between(20.0, 40.0)][COLUMNS].to_string(index=False))


if __name__ == "__main__":
    main()
