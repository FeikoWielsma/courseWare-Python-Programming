import sqlite3
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

conn = sqlite3.connect(DATA / "pandas-demo.db")
books = pd.read_csv(DATA / "books-sample.csv")
summary = books.groupby("rating", as_index=False)["price_gbp"].mean()
summary.to_sql("rating_summary", conn, if_exists="replace", index=False)
conn.commit()
print(pd.read_sql("SELECT * FROM rating_summary", conn))
conn.close()
