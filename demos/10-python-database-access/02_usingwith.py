import sqlite3

con = sqlite3.connect("test.db")

with con:
    cur = con.cursor()
    cur.execute("SELECT SQLITE_VERSION()")

    data = cur.fetchone()

    print(f"SQLite version: {data}")
