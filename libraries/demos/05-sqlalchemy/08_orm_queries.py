from sqlalchemy import Float, Integer, String, create_engine, func, select
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
        return f"Book({self.title!r}, {self.price_gbp}, {self.rating}*)"


ROWS = [
    {"title": "Sharp Objects", "price_gbp": 47.82, "rating": 4},
    {"title": "In a Dark, Dark Wood", "price_gbp": 19.63, "rating": 1},
    {"title": "The Past Never Ends", "price_gbp": 56.50, "rating": 4},
    {"title": "A Fatal Winter", "price_gbp": 22.60, "rating": 5},
]

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all([Book(**row) for row in ROWS])
    session.commit()

    # scalars() unwraps the one-column-per-row tuple into the object itself.
    for found in session.scalars(select(Book).where(Book.rating >= 4)):
        print(found)

    # The comparison builds SQL rather than returning True or False, which is the
    # one genuinely surprising thing about the ORM.
    print(type(Book.rating >= 4).__name__)
    print(Book.rating >= 4)

    for rating, count, mean in session.execute(
        select(Book.rating, func.count(), func.avg(Book.price_gbp)).group_by(Book.rating)
    ):
        print(f"{rating}* {count:>3} {mean:>8.2f}")
