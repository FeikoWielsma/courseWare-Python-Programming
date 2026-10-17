from pathlib import Path

from sqlalchemy import Float, Integer, MetaData, String, create_engine, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATA = Path(__file__).resolve().parents[2] / "data"
DB = DATA / "books.db"
SEED = DATA / "books-seed.sql"


def ensure_database() -> None:
    if DB.exists():
        return
    import sqlite3

    with sqlite3.connect(DB) as connection:
        connection.executescript(SEED.read_text(encoding="utf-8"))


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    price_gbp: Mapped[float] = mapped_column(Float)
    rating: Mapped[int] = mapped_column(Integer)
    category: Mapped[str] = mapped_column(String(60))

    def __repr__(self) -> str:
        return f"Book({self.title!r}, {self.price_gbp:.2f}, {self.rating}*)"


def step1(engine) -> None:  # noqa: ANN001 - the Engine type is not the lesson here
    metadata = MetaData()
    metadata.reflect(bind=engine)
    print("tables  :", list(metadata.tables))
    books = metadata.tables["books"]
    print("columns :", [column.name for column in books.columns])
    with engine.connect() as connection:
        print("rows    :", connection.execute(select(func.count()).select_from(books)).scalar_one())


def step2(session: Session) -> None:
    print()
    print("first three, as objects :")
    for book in session.scalars(select(Book).limit(3)):
        print("  ", book)


def step3(session: Session) -> None:
    print()
    print("rated 5, dearest first :")
    best = select(Book).where(Book.rating == 5).order_by(Book.price_gbp.desc())
    for book in session.scalars(best):
        print("  ", book)

    dear = select(func.count()).select_from(Book).where(Book.price_gbp > 30)
    print()
    print("costing more than 30 :", session.execute(dear).scalar_one())

    print()
    print("rating  count   mean price")
    by_rating = (
        select(Book.rating, func.count(), func.avg(Book.price_gbp))
        .group_by(Book.rating)
        .order_by(Book.rating)
    )
    for rating, count, mean in session.execute(by_rating):
        print(f"  {rating}       {count}       {mean:.2f}")


def main() -> None:
    ensure_database()
    engine = create_engine(f"sqlite:///{DB}")
    step1(engine)
    with Session(engine) as session:
        step2(session)
        step3(session)


if __name__ == "__main__":
    main()
