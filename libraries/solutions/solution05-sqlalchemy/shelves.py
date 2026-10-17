from pathlib import Path

import pandas as pd
from sqlalchemy import ForeignKey, Integer, String, create_engine, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

DATA = Path(__file__).resolve().parents[2] / "data"
DB = DATA / "exercise-library.db"


class Base(DeclarativeBase):
    pass


class Shelf(Base):
    __tablename__ = "shelf"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(60))
    volumes: Mapped[list[Volume]] = relationship(back_populates="shelf")

    def __repr__(self) -> str:
        return f"Shelf({self.name!r})"


class Volume(Base):
    __tablename__ = "volume"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    shelf_id: Mapped[int] = mapped_column(ForeignKey("shelf.id"))
    shelf: Mapped[Shelf] = relationship(back_populates="volumes")

    def __repr__(self) -> str:
        return f"Volume({self.title!r})"


def build(session: Session) -> None:
    session.add_all(
        [
            Shelf(
                name="Crime",
                volumes=[Volume(title="Sharp Objects"), Volume(title="A Fatal Winter")],
            ),
            Shelf(
                name="Reference",
                volumes=[Volume(title="The SQL Standard"), Volume(title="Unix in a Nutshell")],
            ),
        ]
    )
    session.commit()


def read_both_ways(session: Session) -> None:
    print("through the relationship :")
    for shelf in session.scalars(select(Shelf).order_by(Shelf.name)):
        for volume in shelf.volumes:
            print(f"  {shelf.name:<12} {volume.title}")

    print()
    print("as one join :")
    joined = select(Shelf.name, Volume.title).join(Shelf.volumes).order_by(Shelf.name, Volume.title)
    for name, title in session.execute(joined):
        print(f"  {name:<12} {title}")


def move_one(session: Session) -> None:
    reference = session.scalars(select(Shelf).where(Shelf.name == "Reference")).one()
    moving = session.scalars(select(Volume).where(Volume.title == "A Fatal Winter")).one()

    print()
    print(f"moving {moving.title!r} from {moving.shelf.name!r} to {reference.name!r}")
    moving.shelf = reference
    session.commit()

    for shelf in session.scalars(select(Shelf).order_by(Shelf.name)):
        print(f"  {shelf.name:<12} {[volume.title for volume in shelf.volumes]}")


def with_pandas(engine) -> None:  # noqa: ANN001 - the Engine type is not the lesson here
    print()
    frame = pd.read_sql("SELECT id, title, shelf_id FROM volume", engine)
    print("counted in pandas :")
    print(frame.groupby("shelf_id")["title"].count().to_string())

    print()
    print("counted in SQL :")
    with Session(engine) as session:
        counted = select(Shelf.name, func.count(Volume.id)).join(Shelf.volumes).group_by(Shelf.name)
        for name, count in session.execute(counted):
            print(f"  {name:<12} {count}")


def main() -> None:
    # Start from nothing so the solution is re-runnable.
    DB.unlink(missing_ok=True)
    engine = create_engine(f"sqlite:///{DB}")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        build(session)
        read_both_ways(session)
        move_one(session)
    with_pandas(engine)


if __name__ == "__main__":
    main()
