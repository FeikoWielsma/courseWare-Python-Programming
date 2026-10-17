import sqlite3
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

DB = Path(__file__).resolve().parents[2] / "data" / "books.db"

# The scraping module writes this file; rebuild it from the seed if that
# module has not been run yet.
if not DB.exists():
    sqlite3.connect(DB).executescript((DB.parent / "books-seed.sql").read_text(encoding="utf-8"))

# pandas takes an engine anywhere it takes a connection, and the engine is the
# portable half : the same line works against PostgreSQL.
engine = create_engine(f"sqlite:///{DB}")

frame = pd.read_sql("SELECT title, price_gbp, rating FROM books", engine)
print(frame.shape)
print(frame.head(3).to_string(index=False))

# The database does the grouping, or pandas does. For twenty rows it makes no
# difference; for twenty million, let the database do it.
in_pandas = frame.groupby("rating")["price_gbp"].mean().round(2)
in_sql = pd.read_sql(
    "SELECT rating, ROUND(AVG(price_gbp), 2) AS price_gbp FROM books GROUP BY rating",
    engine,
    index_col="rating",
)["price_gbp"]

print(pd.DataFrame({"in pandas": in_pandas, "in SQL": in_sql}).to_string())
