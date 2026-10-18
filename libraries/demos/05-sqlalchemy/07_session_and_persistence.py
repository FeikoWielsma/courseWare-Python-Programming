from sqlalchemy import Float, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    price_gbp: Mapped[float] = mapped_column(Float)
    rating: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"Book(id={self.id}, title={self.title!r})"


engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

with Session(engine) as session:
    first = Book(title="Sharp Objects", price_gbp=47.82, rating=4)
    second = Book(title="In a Dark, Dark Wood", price_gbp=19.63, rating=1)
    session.add_all([first, second])
    print(first.id, second.id)

    session.flush()
    print(first.id, second.id)

    # Flush assigns ids inside the transaction; commit makes the writes permanent.
    session.commit()
    print(first.id, second.id)

    # The session tracks what it loaded. Changing an attribute is enough; there is
    # no UPDATE to write.
    first.price_gbp = 41.99
    print(session.dirty)
    session.commit()
    print(session.get(Book, first.id).price_gbp)
