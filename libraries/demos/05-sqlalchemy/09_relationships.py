from sqlalchemy import ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(60))

    # The other side of the foreign key, as a list of objects.
    books: Mapped[list[Book]] = relationship(back_populates="category")

    def __repr__(self) -> str:
        return f"Category({self.name!r})"


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))

    category: Mapped[Category] = relationship(back_populates="books")

    def __repr__(self) -> str:
        return f"Book({self.title!r})"


engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

with Session(engine) as session:
    # No ids, no foreign keys written by hand. Appending to the list creates the
    # link, and the INSERT order is worked out for you.
    mystery = Category(name="Mystery")
    mystery.books.append(Book(title="Sharp Objects"))
    mystery.books.append(Book(title="A Fatal Winter"))
    session.add(mystery)
    session.commit()

    found = session.scalars(select(Category)).one()
    print(found)
    print(found.books)

    # The same link read from the other end.
    one_book = session.scalars(select(Book).where(Book.title == "Sharp Objects")).one()
    print(one_book)
    print(one_book.category)
    print(one_book.category_id)
