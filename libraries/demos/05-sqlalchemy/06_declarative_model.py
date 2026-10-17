from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "book"

    # Mapped[int] is a real annotation, so a checker and an editor both
    # understand the attribute.
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    price_gbp: Mapped[float] = mapped_column(Float)
    rating: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, price_gbp={self.price_gbp!r})"


my_book = Book()
my_book.title = "Hoi"
print(Book.__mro__[1].__name__)
print(Book.__tablename__)
print([column.name for column in Book.__table__.columns])

# An unsaved instance is an ordinary Python object. Nothing has touched a
# database yet, and its id is still None.
draft = Book(title="Sharp Objects", price_gbp=47.82, rating=4)
print(draft)
print(draft.id)
