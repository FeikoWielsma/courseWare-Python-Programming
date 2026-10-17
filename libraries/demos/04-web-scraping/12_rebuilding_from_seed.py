import sqlite3
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"
DB = DATA / "books.db"

# executescript runs a whole file of statements, which is what makes a plain
# .sql file a perfectly good backup of a small database.
conn = sqlite3.connect(DB)
conn.executescript((DATA / "books-seed.sql").read_text(encoding="utf-8"))
conn.commit()

print(conn.execute("SELECT COUNT(*) FROM books").fetchone()[0], "rows rebuilt in", DB)
print([row[1] for row in conn.execute("PRAGMA table_info(books)")])

conn.row_factory = sqlite3.Row
for row in conn.execute("SELECT * FROM books ORDER BY price_gbp DESC LIMIT 3"):
    print(f"{row['price_gbp']:>6.2f}  {row['rating']} stars  {row['title']}")

conn.close()
