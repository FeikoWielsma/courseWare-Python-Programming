import sqlite3
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"
DB = DATA / "books.db"

# The scraping module writes this file; rebuild it from the seed if that
# module has not been run yet.
if not DB.exists():
    sqlite3.connect(DB).executescript((DATA / "books-seed.sql").read_text(encoding="utf-8"))

conn = sqlite3.connect(DB)

# sqlite_master is the catalogue. Asking it first is how you find out what a
# database you did not write actually contains.
print(pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'", conn))

books = pd.read_sql("SELECT * FROM books", conn)
print(books.shape)
print(list(books.columns))
print(books[["title", "price_gbp", "rating", "category"]].head(4).to_string())

# Values go in as parameters, never as string formatting, exactly as they would
# from any other database client.
query = "SELECT title, price_gbp, rating FROM books WHERE price_gbp > ? ORDER BY price_gbp DESC"
print(pd.read_sql(query, conn, params=(45.0,)).to_string())

conn.close()

# Once it is a DataFrame the database is out of the picture.
print(books.groupby("rating")["price_gbp"].agg(["count", "mean"]).round(2))
