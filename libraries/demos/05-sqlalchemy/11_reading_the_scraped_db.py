import sqlite3
from pathlib import Path

from sqlalchemy import MetaData, create_engine, select

DB = Path(__file__).resolve().parents[2] / "data" / "books.db"

# The scraping module writes this file; rebuild it from the seed if that
# module has not been run yet.
if not DB.exists():
    sqlite3.connect(DB).executescript((DB.parent / "books-seed.sql").read_text(encoding="utf-8"))

engine = create_engine(f"sqlite:///{DB}")

# Reflection reads the schema out of the database, so nothing is declared here.
metadata = MetaData()
metadata.reflect(bind=engine)
print(list(metadata.tables))

books = metadata.tables["books"]
print([column.name for column in books.columns])

statement = (
    select(books.c.title, books.c.price_gbp, books.c.rating)
    .where(books.c.rating >= 4)
    .order_by(books.c.price_gbp.desc())
    .limit(5)
)
with engine.connect() as connection:
    for title, price, rating in connection.execute(statement):
        print(f"{rating}*  {price:>6.2f}  {title}")
