import sqlite3
from contextlib import closing
from pathlib import Path

import pandas as pd

DATA: Path = Path(__file__).resolve().parents[2] / "data"
BOOKS_DB: Path = DATA / "books.db"
BOOKS_CSV: Path = DATA / "books-sample.csv"

RATE: float = 1.17


def load_books() -> pd.DataFrame:
    if BOOKS_DB.exists():
        with closing(sqlite3.connect(BOOKS_DB)) as conn:
            return pd.read_sql("SELECT * FROM books", conn)
    return pd.read_csv(BOOKS_CSV)


def summarise_by_rating(books: pd.DataFrame) -> pd.DataFrame:
    return (
        books.groupby("rating")
        .agg(
            titles=("title", "count"),
            mean_price=("price_eur", "mean"),
            cheapest=("price_eur", "min"),
            dearest=("price_eur", "max"),
        )
        .round(2)
        .reset_index()
    )


def main() -> None:
    books = load_books()
    books["price_eur"] = (books["price_gbp"] * RATE).round(2)

    per_rating = summarise_by_rating(books)
    print("one row per rating:")
    print(per_rating.to_string(index=False))

    print("\nsorted by mean price, to see whether a better rating costs more:")
    print(per_rating.sort_values("mean_price", ascending=False).to_string(index=False))

    # The grand totals are worth printing next to the groups, because a group
    # summary is only interesting relative to the whole.
    print("\nwhole catalogue:", len(books), "titles,", end=" ")
    print("mean price", round(books["price_eur"].mean(), 2), "EUR")


if __name__ == "__main__":
    main()
