from sqlalchemy import Column, Float, Integer, MetaData, String, Table, create_engine
from sqlalchemy.schema import CreateTable

metadata = MetaData()

book = Table(
    "book",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(200), nullable=False),
    Column("price_gbp", Float, nullable=False),
    Column("rating", Integer, nullable=False),
)

engine = create_engine("sqlite:///:memory:")
# Issues the CREATE TABLE for anything in the catalogue that is missing.
metadata.create_all(engine)

print(book.name)
print([column.name for column in book.columns])
print([column.name for column in book.primary_key])

# The Python object knows its own SQL.
print(CreateTable(book).compile(engine))
