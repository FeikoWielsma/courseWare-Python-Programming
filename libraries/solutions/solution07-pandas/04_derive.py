import sqlite3
from contextlib import closing
from pathlib import Path

import numpy as np
import pandas as pd

DATA: Path = Path(__file__).resolve().parents[2] / "data"
BOOKS_DB: Path = DATA / "books.db"
BOOKS_CSV: Path = DATA / "books-sample.csv"

# Fixed here on purpose. A report that quietly changes its numbers because a
# rate moved is a report nobody can reconcile against last month's copy.
RATE: float = 1.17


def load_books() -> pd.DataFrame:
    if BOOKS_DB.exists():
        with closing(sqlite3.connect(BOOKS_DB)) as conn:
            return pd.read_sql("SELECT * FROM books", conn)
    return pd.read_csv(BOOKS_CSV)


def with_prices(books: pd.DataFrame) -> pd.DataFrame:
    priced = books.copy()
    priced["price_eur"] = (priced["price_gbp"] * RATE).round(2)
    priced["band"] = np.where(
        priced["price_eur"] < 20.0,
        "budget",
        np.where(priced["price_eur"] < 45.0, "mid", "premium"),
    )
    return priced


def main() -> None:
    books = with_prices(load_books())

    print("the derived columns:")
    print(books[["title", "price_gbp", "price_eur", "band"]].head().to_string(index=False))

    print("\nbooks per band:")
    print(books["band"].value_counts())

    columns = ["title", "price_gbp", "price_eur", "band"]
    print("\nfive most expensive, by sort_values:")
    print(books.sort_values("price_eur", ascending=False)[columns].head(5).to_string(index=False))

    print("\nthe same five, by nlargest:")
    print(books.nlargest(5, "price_eur")[columns].to_string(index=False))


if __name__ == "__main__":
    main()
