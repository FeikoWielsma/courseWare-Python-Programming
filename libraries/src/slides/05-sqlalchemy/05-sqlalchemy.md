---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: SQLAlchemy
language: python
---

# SQLAlchemy

- The scraping module talked to SQLite with `sqlite3` :
  - Which is the driver, and drivers are database-specific
- SQLAlchemy sits above the driver :
  - One way of working, whichever database is underneath
- It has two halves, and both are useful :
  - `Core`, which builds SQL out of Python objects
  - The `ORM`, which maps rows onto classes
- Nothing here replaces knowing SQL :
  - It repays knowing SQL, which is the point


---

# sqlite3 and SQLAlchemy

- The same call, against a different database :
  - Change the URL, not the program
- Parameters have names instead of positions
- Rows can come back as objects rather than tuples
- The query is a value you can build up, print and reuse

```python
found = connection.execute(
    text("SELECT title, price FROM book WHERE price > :floor"), {"floor": 25}
)
print("sqlalchemy :", found.all())
```

> `demo01 · why_a_layer`


---

# Engine and URL

- An engine is a factory and a connection pool :
  - Make one per database, once, and keep it
  - It does not open a connection until something asks
- The URL says everything about where the data lives :

```text
dialect+driver://user:password@host/database

sqlite:///:memory:
sqlite:///data/library.db
postgresql+psycopg://feiko@localhost/inventory
```

- SQLite needs no server, so the middle of the URL is empty

> `demo02 · engine_and_connection`


---

# begin and connect

- `engine.begin()` opens a transaction :
  - Commits when the module ends, rolls back if it raises
- `engine.connect()` gives you a connection and nothing else :
  - Anything written is discarded unless you commit it yourself
- Prefer `begin()` for anything that writes

```python
with engine.begin() as connection:
    connection.execute(text("INSERT INTO note VALUES ('kept')"))

with engine.connect() as connection:
    rows = connection.execute(text("SELECT body FROM note")).scalars().all()
```


---

# Bound Parameters

- The parameter is sent separately from the statement :
  - The database never parses the value as SQL
- Named, so there are no question marks to count
- The scraping module uses the same separation of SQL and values

```python
statement = text("SELECT title FROM book WHERE rating >= :floor")
connection.execute(statement, {"floor": 3})
```

- A formatted query breaks on ordinary data long before it is attacked :

```text
SELECT rating FROM book WHERE title = 'The Widow's Tale'
```

> `demo03 · parameters`


---

# Table Definitions

- Core describes a table as a Python object :
  - Columns, types, constraints, all as values
- `MetaData` is the catalogue every table registers in
- `create_all()` issues `CREATE TABLE` for whatever is missing

```python
book = Table(
    "book",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(200), nullable=False),
    Column("price_gbp", Float, nullable=False),
)
```

> `demo04 · describing_a_table`


---

# Core Queries

- `select()` returns something you can hold, print and add to :
  - `.where()`, `.order_by()`, `.limit()` each return a new query
- Column access is `table.c.name`
- Printing the query shows the SQL it will send

```python
statement = select(book.c.title, book.c.price_gbp).where(book.c.rating >= 4)
print(statement)

with engine.connect() as connection:
    for title, price in connection.execute(statement):
        print(f"{title:<24} {price:>6.2f}")
```

> `demo05 · core_insert_and_select`


---

# Declarative Models

- The ORM maps a class onto a table :
  - One class, one table, one instance per row
- Every model inherits from a `DeclarativeBase` :
  - Which is block one doing real work
- `Mapped[int]` is an ordinary annotation, so editors understand it

```python
class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    price_gbp: Mapped[float] = mapped_column(Float)
```

> `demo06 · declarative_model`


---

# Session

- A `Session` is a unit of work, not a connection :
  - Add objects to it, then commit once
- Generated ids become available when inserts are flushed
- The session tracks what it loaded :
  - Change an attribute and there is no `UPDATE` to write

- `flush()` sends pending writes inside the current transaction
- `commit()` makes the transaction permanent

```python
with Session(engine) as session:
    session.add_all([first, second])
    session.flush()
    session.commit()

    first.price_gbp = 41.99
    session.commit()
```

> `demo07 · session_and_persistence`



---

# ORM Queries

- The same `select()`, but the rows are objects
- `scalars()` unwraps a one-column result into the thing itself
- Comparisons build SQL rather than returning a boolean :
  - `Book.rating >= 4` is a fragment of a `WHERE` clause

```python
for found in session.scalars(select(Book).where(Book.rating >= 4)):
    print(found)
```

```python
for rating, count, mean in session.execute(
    select(Book.rating, func.count(), func.avg(Book.price_gbp)).group_by(Book.rating)
):
    print(f"{rating}* {count:>3} {mean:>8.2f}")
```

> `demo08 · orm_queries`


---

# Relationships

- A foreign key becomes an attribute on both sides :
  - `category.books` is a list, `book.category` is an object
- `back_populates` names the attribute pointing the other way
- Appending to the list is what creates the link :
  - No ids written by hand, and the insert order is worked out

```python
class Category(Base):
    books: Mapped[list[Book]] = relationship(back_populates="category")

mystery.books.append(Book(title="Sharp Objects"))
session.add(mystery)
```

> `demo09 · relationships`


---

# Joins and Relationships

<div class="two-col">
<div>

- As a join :
  - One query
  - Explicit, and familiar
  - What the database does anyway

```python
joined = select(Book.title, Category.name).join(Book.category)
print(joined)
for title, category in session.execute(joined):
    print(f"{title:<18} {category}")

for found in session.scalars(select(Book)):
    print(f"{found.title:<18} {found.category.name}")
```

</div>
<div>

- As an attribute :
  - Reads better
  - Issues a query per object
  - Easy to do by accident



</div>
</div>

> `demo10 · joins`


---

# Reflection

- Reflection reads the schema out of an existing database :
  - Rather than describing it in Python first
- Which is most databases, most of the time

```python
metadata = MetaData()
metadata.reflect(bind=engine)

books = metadata.tables["books"]
print([column.name for column in books.columns])
```

- The demo points at the database the scraping module filled in

> `demo11 · reading_the_scraped_db`


---

# SQLAlchemy and Pandas

- `read_sql` takes an engine anywhere it takes a connection :
  - So the portable half comes along for free
- The grouping can happen in either place :
  - In the database, or in the DataFrame afterwards
- For twenty rows it makes no difference :
  - For twenty million, let the database do it

```python
engine = create_engine(f"sqlite:///{DB}")
frame = pd.read_sql("SELECT title, price_gbp, rating FROM books", engine)
```

> `demo12 · with_pandas`


---

# text, Core and ORM

- `text()` when the SQL is the clearest way to say it :
  - Or when it is already written and correct
- `Core` when the query is assembled from parts, or must be portable
- The `ORM` when rows are things the program keeps hold of and changes
- These are not levels, and not a progression :
  - Plenty of good programs use all three in one file

> `demo13 · core_or_orm`


---

# Summary : SQLAlchemy

- SQLAlchemy sits above the driver, not above SQL
- An engine is made once and carries the URL :
  - Use `begin()` for anything that writes
- Core builds queries as objects you can print and compose
- The ORM maps a class onto a table, with a `Session` as the unit of work
- Relationships turn a foreign key into an attribute on both sides
- Reflection reads a schema somebody else designed
- An engine drops straight into `pandas.read_sql`
