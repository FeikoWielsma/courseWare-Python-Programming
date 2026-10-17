from pathlib import Path

from sqlalchemy import create_engine, text

DATA = Path(__file__).resolve().parents[2] / "data"

# The URL is dialect://user:password@host/database. SQLite needs no server, so
# everything between the slashes is empty and the path is the file.
print("sqlite:///:memory:")
print(f"sqlite:///{DATA / 'library.db'}")
print("postgresql+psycopg://feiko@localhost/inventory")

# An engine is a factory and a connection pool. Make one per database, once,
# and keep it. It does not connect until something asks it to.
engine = create_engine(f"sqlite:///{DATA / 'library.db'}")
print(engine)
print(engine.dialect.name)

# begin() commits on the way out. connect() does not.
with engine.begin() as connection:
    connection.execute(text("CREATE TABLE note (body TEXT)"))
    connection.execute(text("INSERT INTO note VALUES ('written inside begin')"))

with engine.connect() as connection:
    print(connection.execute(text("SELECT body FROM note")).scalars().all())
