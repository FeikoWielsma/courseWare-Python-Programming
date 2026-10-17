import sqlite3
from contextlib import closing
from pathlib import Path

import matplotlib

# Chosen before pyplot is imported, so this script writes a file rather than
# waiting for someone to close a window. That is what makes it safe in cron.
matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

DATA: Path = Path(__file__).resolve().parents[2] / "data"
BOOKS_DB: Path = DATA / "books.db"
BOOKS_CSV: Path = DATA / "books-sample.csv"

RATE: float = 1.17
CHART: Path = DATA / "book-report-chart.png"


def load_books() -> pd.DataFrame:
    if BOOKS_DB.exists():
        with closing(sqlite3.connect(BOOKS_DB)) as conn:
            return pd.read_sql("SELECT * FROM books", conn)
    return pd.read_csv(BOOKS_CSV)


def summarise_by_rating(books: pd.DataFrame) -> pd.DataFrame:
    return (
        books.groupby("rating")
        .agg(titles=("title", "count"), mean_price=("price_eur", "mean"))
        .round(2)
        .reset_index()
    )


def main() -> None:
    books = load_books()
    books["price_eur"] = (books["price_gbp"] * RATE).round(2)
    per_rating = summarise_by_rating(books)

    axes = per_rating.plot(kind="bar", x="rating", y="mean_price", legend=False)
    axes.set_title("Mean price by star rating")
    axes.set_xlabel("stars")
    axes.set_ylabel("EUR")
    figure = axes.get_figure()
    figure.tight_layout()
    figure.savefig(CHART, dpi=120)
    plt.close(figure)
    print("wrote", CHART.name, f"({CHART.stat().st_size} bytes)")

    words = pd.DataFrame(
        {
            "rating": [1, 2, 3, 4, 5],
            "verdict": ["poor", "weak", "fair", "good", "excellent"],
        }
    )
    print("\nthe summary joined onto the lookup:")
    print(per_rating.merge(words, on="rating").to_string(index=False))

    # Drop a row from the lookup and the inner join silently loses a rating.
    gappy = words[words["rating"] != 3]
    checked = per_rating.merge(gappy, on="rating", how="left", indicator=True)
    print("\nwith a gap in the lookup, how='left' and indicator=True:")
    print(checked.to_string(index=False))
    print("\nrows by origin:")
    print(checked["_merge"].value_counts())


if __name__ == "__main__":
    main()
