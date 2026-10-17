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
    books = load_books()

    print("books.info():")
    books.info()

    print("\nbooks.describe():")
    print(books.describe().round(2).to_string())

    # An empty column here would mean the scrape failed on that field, so this
    # is the check worth doing before trusting any of the numbers above.
    print("\nmissing values per column:")
    print(books.isna().sum())

    print("\ncategories:")
    print(books["category"].value_counts())

    print("\nratings:")
    print(books["rating"].value_counts().sort_index())

    # The dtypes were inferred from the database, not declared here.
    print("\nprice_gbp dtype:", books["price_gbp"].dtype)
    print("rating    dtype:", books["rating"].dtype)


if __name__ == "__main__":
    main()
