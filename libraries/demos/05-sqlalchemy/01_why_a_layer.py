import sqlite3

from sqlalchemy import create_engine, text

ROWS = [("Sharp Objects", 47.82), ("In a Dark Wood", 19.63)]

# sqlite3 speaks one dialect, uses ? placeholders, and hands back tuples.
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE book (title TEXT, price REAL)")
conn.executemany("INSERT INTO book VALUES (?, ?)", ROWS)
found = conn.execute("SELECT title, price FROM book WHERE price > ?", (25,))
print("sqlite3    :", found.fetchall())

# Named parameters, and the same lines would work against PostgreSQL.
engine = create_engine("sqlite:///:memory:")
with engine.begin() as connection:
    connection.execute(text("CREATE TABLE book (title TEXT, price REAL)"))
    connection.execute(
        text("INSERT INTO book VALUES (:title, :price)"),
        [{"title": title, "price": price} for title, price in ROWS],
    )
    found = connection.execute(
        text("SELECT title, price FROM book WHERE price > :floor"), {"floor": 25}
    )
    print("sqlalchemy :", found.all())
