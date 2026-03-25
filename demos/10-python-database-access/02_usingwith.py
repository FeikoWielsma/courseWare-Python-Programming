import sqlite3

con = sqlite3.connect("test.db")

with con:
    cur = con.cursor()
    cur.execute("SELECT SQLITE_VERSION()")

    data = cur.fetchone()

    print("SQLite version: %s" % data)
