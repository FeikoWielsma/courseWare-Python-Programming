import sqlite3

# Reads the films table; run 03_insertingdata.py or 04_preparedstatements.py first.
con = sqlite3.connect("watchlist.db")

with con:
    cur = con.cursor()
    cur.execute("SELECT id, title, year FROM films")

    rows = cur.fetchall()

    for row in rows:
        print(row)

con.close()
