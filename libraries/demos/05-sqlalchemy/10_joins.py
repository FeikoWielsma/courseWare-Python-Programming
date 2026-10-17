from sqlalchemy import ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(60))
    books: Mapped[list[Book]] = relationship(back_populates="category")


class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped[Category] = relationship(back_populates="books")


engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all(
        [
            Category(name="Mystery", books=[Book(title="Sharp Objects")]),
            Category(name="Poetry", books=[Book(title="Selected Poems")]),
        ]
    )
    session.commit()

    # Written as a join, which is what the database does either way.
    joined = select(Book.title, Category.name).join(Book.category)
    print(joined)
    for title, category in session.execute(joined):
        print(f"{title:<18} {category}")

    # Written as attribute access, which reads better and issues the same query
    # lazily, one category at a time, when you touch .category.
    for found in session.scalars(select(Book)):
        print(f"{found.title:<18} {found.category.name}")
