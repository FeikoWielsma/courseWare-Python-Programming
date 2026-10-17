from sqlalchemy import (
    Column,
    Float,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    insert,
    select,
)

metadata = MetaData()
book = Table(
    "book",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(200), nullable=False),
    Column("price_gbp", Float, nullable=False),
    Column("rating", Integer, nullable=False),
)

ROWS = [
    {"title": "Sharp Objects", "price_gbp": 47.82, "rating": 4},
    {"title": "In a Dark, Dark Wood", "price_gbp": 19.63, "rating": 1},
    {"title": "The Past Never Ends", "price_gbp": 56.50, "rating": 4},
]

engine = create_engine("sqlite:///:memory:")
metadata.create_all(engine)

with engine.begin() as connection:
    connection.execute(insert(book), ROWS)

# A select() is an object. Print it to see what will actually be sent.
"select title, price_gbp from book where rating >= 4"
statement = select(book.c.title, book.c.price_gbp).where(book.c.rating >= 4)
print(statement)

with engine.connect() as connection:
    for title, price in connection.execute(statement):
        print(f"{title:<24} {price:>6.2f}")

    dearest = select(book.c.title).order_by(book.c.price_gbp.desc()).limit(1)
    print(connection.execute(dearest).scalar_one())
