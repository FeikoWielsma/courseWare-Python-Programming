import sqlite3
from contextlib import closing

con = sqlite3.connect("watchlist.db")

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS films(id INTEGER PRIMARY KEY, title TEXT)")
    cur.execute("SELECT COUNT(*) FROM films")

    print(f"Films on the watchlist: {cur.fetchone()[0]}")

con.close()  # `with con:` commits or rolls back, it does not close

with closing(sqlite3.connect("watchlist.db")) as con, con:
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM films")
    print(f"Films on the watchlist: {cur.fetchone()[0]}")
