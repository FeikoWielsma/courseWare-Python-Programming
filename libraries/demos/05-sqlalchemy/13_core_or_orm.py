import sqlite3
from pathlib import Path

from sqlalchemy import MetaData, create_engine, func, select, text

DB = Path(__file__).resolve().parents[2] / "data" / "books.db"

# The scraping module writes this file; rebuild it from the seed if that
# module has not been run yet.
if not DB.exists():
    sqlite3.connect(DB).executescript((DB.parent / "books-seed.sql").read_text(encoding="utf-8"))

engine = create_engine(f"sqlite:///{DB}")
metadata = MetaData()
metadata.reflect(bind=engine)
books = metadata.tables["books"]

with engine.connect() as connection:
    # Raw SQL through text(). Nothing is abstracted, and you can paste the string
    # into any database client to check it.
    rows = connection.execute(
        text("SELECT rating, COUNT(*) FROM books GROUP BY rating ORDER BY rating")
    ).all()
    print("text() :", [tuple(row) for row in rows])

    # Core. The query is an object, so it can be built up in pieces and the column
    # names are checked where you write them, not at runtime.
    statement = (
        select(books.c.rating, func.count()).group_by(books.c.rating).order_by(books.c.rating)
    )
    print("core   :", [tuple(row) for row in connection.execute(statement)])
