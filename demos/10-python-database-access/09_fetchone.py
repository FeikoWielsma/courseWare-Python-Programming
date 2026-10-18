import sqlite3

# Reads the films table; run 03_insertingdata.py or 04_preparedstatements.py first.
con = sqlite3.connect("watchlist.db")

with con:
    cur = con.cursor()
    cur.execute("SELECT id, title, minutes FROM films")

    while True:
        row = cur.fetchone()

        if row is None:
            break

        print(row[0], row[1], row[2])

con.close()
