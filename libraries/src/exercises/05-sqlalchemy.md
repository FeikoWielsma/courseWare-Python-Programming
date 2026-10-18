# Exercise 5 : SQLAlchemy

In this exercise you point SQLAlchemy at the database the scraping module filled in, describe its table as a Python class, and then build a small catalogue of your own with a relationship in it. Everything you write goes into `data/exercise-library.db`, so the scraped `data/books.db` is only ever read and cannot be damaged.

Start from `exercises/starters/05-sqlalchemy/`. Run from `libraries/`, so relative data paths resolve.

---

### Step 1 : Connect to something that already exists

:::hint
The slide *Engine and URL* shows the operation used in this step.
:::

Make a file `library.py`. Create an engine pointing at the scraped database and ask it what is in there. This step exists to prove the environment works :

```python
from pathlib import Path
from sqlalchemy import MetaData, create_engine

DATA = Path(__file__).resolve().parent / "data"
engine = create_engine(f"sqlite:///{DATA / 'books.db'}")

metadata = MetaData()
metadata.reflect(bind=engine)
print(list(metadata.tables))
```

You should see `['books']`. Now print the column names of that table, and then the number of rows in it. If `data/books.db` does not exist, run `uv run demos/04-web-scraping/12_rebuilding_from_seed.py` first, which builds it from the checked-in seed without touching the network.

---

### Step 2 : Describe the table as a class

:::hint
The slide *Declarative Models* shows the operation used in this step.
:::

Reflection is convenient, but it gives you tuples. Write a `Book` model that matches the table you just inspected, so that queries hand back objects instead :

```python
class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    # add price_gbp, rating and category
```

Give it a `__repr__` so that printing one is readable. Then open a `Session` and print the first three books.

You do not need `create_all()` here; the table already exists and your class is describing it, not creating it.

---

### Step 3 : Ask it questions

:::hint
The slide *Session* shows the operation used in this step.
:::

Using `select()` and the session, answer each of these. Print the answer with a line saying what it is :

- Every book rated 5, ordered by price, most expensive first.
- The number of books costing more than £30.
- The average price at each rating, as a small table.

For the last one you want `func.count()` and `func.avg()`, and `group_by`. Compare what you write with the SQL you would have written by hand; they should look similar enough to be reassuring.

---

### Step 4 : Your own database, with two tables

:::hint
The slide *ORM Queries* shows the operation used in this step.
:::

Now build something of your own in `data/exercise-library.db`. Two models :

- `Shelf`, with an `id` and a `name`.
- `Volume`, with an `id`, a `title`, and a foreign key to `Shelf`.

Wire them together with a relationship in both directions :

```python
class Shelf(Base):
    __tablename__ = "shelf"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(60))
    volumes: Mapped[list[Volume]] = relationship(back_populates="shelf")
```

Call `Base.metadata.create_all(engine)` against the new database, then create two shelves with a few volumes each. Add only the shelves to the session, not the volumes, and check that the volumes are saved anyway.

---

### Step 5 : Read it back both ways

:::hint
The slide *Relationships* shows the operation used in this step.
:::

Print every shelf with the titles on it, using the relationship attribute. Then print the same information again as a single query with an explicit `join`.

Both should produce the same lines. Satisfy yourself about which one issued how many queries; passing `echo=True` to `create_engine` will show you every statement as it is sent, which is the quickest way to see the difference.

---

### Step 6 : Change something

:::hint
The slide *Relationships* shows the operation used in this step.
:::

Move one volume from one shelf to the other by assigning to its `shelf` attribute, then commit. Print both shelves again to confirm it moved.

Notice that you did not write an `UPDATE` statement, and that you did not touch the foreign key column yourself.

---

### Step 7 : Optional, hand it to pandas

Load your `volume` table into a DataFrame with `pandas.read_sql`, passing the engine rather than a connection. Group it by shelf and count the rows.

Then do the same aggregation in SQL instead, and compare. Which one you would reach for in real work depends on how big the table is and on what you want to do next, and it is worth having an opinion about both.
