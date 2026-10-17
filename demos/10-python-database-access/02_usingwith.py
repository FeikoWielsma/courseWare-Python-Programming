import sqlite3
from contextlib import closing

con = sqlite3.connect("test.db")

with con:
    cur = con.cursor()
    cur.execute("SELECT SQLITE_VERSION()")

    data = cur.fetchone()

    print(f"SQLite version: {data}")

con.close()  # `with con:` commits or rolls back, it does not close

with closing(sqlite3.connect("test.db")) as con, con:
    cur = con.cursor()
    cur.execute("SELECT SQLITE_VERSION()")
    print(f"SQLite version: {cur.fetchone()}")
