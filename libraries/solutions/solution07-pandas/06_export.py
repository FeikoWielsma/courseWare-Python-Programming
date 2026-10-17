import sqlite3
from contextlib import closing
from pathlib import Path

import numpy as np
import pandas as pd

DATA: Path = Path(__file__).resolve().parents[2] / "data"
BOOKS_DB: Path = DATA / "books.db"
BOOKS_CSV: Path = DATA / "books-sample.csv"

RATE: float = 1.17
WORKBOOK: Path = DATA / "book-report.xlsx"


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

    shortlist: pd.DataFrame = books[
        (books["rating"] >= 4) & (books["availability"] == "In stock")
    ].sort_values("price_eur", ascending=False)[
        ["title", "category", "rating", "price_gbp", "price_eur", "band"]
    ]

    per_rating: pd.DataFrame = (
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

    # index=False on both: the row numbers are pandas' business, not the
    # reader's, and they only get in the way in a spreadsheet.
    with pd.ExcelWriter(WORKBOOK, engine="openpyxl") as workbook:
        shortlist.to_excel(workbook, sheet_name="shortlist", index=False)
        per_rating.to_excel(workbook, sheet_name="by rating", index=False)

    csv_path = DATA / "book-report.csv"
    shortlist.to_csv(csv_path, index=False)

    print("wrote", WORKBOOK)
    print("sheets:", pd.ExcelFile(WORKBOOK).sheet_names)
    print("wrote", csv_path.name, f"({len(shortlist)} rows)")

    print("\nreading the workbook back to prove it is really a spreadsheet:")
    print(pd.read_excel(WORKBOOK, sheet_name="by rating").to_string(index=False))


if __name__ == "__main__":
    main()
