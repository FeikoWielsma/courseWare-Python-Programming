import sqlite3

# Reads the films table; run 03_insertingdata.py or 04_preparedstatements.py first.
con = sqlite3.connect("watchlist.db")

with con:
    cur = con.cursor()

    cur.execute("PRAGMA table_info(films)")

    data = cur.fetchall()

    for d in data:
        print(d[0], d[1], d[2])

with con:
    cur = con.cursor()
    cur.execute("SELECT id, title, year FROM films")

    col_names = [cn[0] for cn in cur.description]

    rows = cur.fetchall()

    print(f"{col_names[0]:>2} {col_names[1]:<20} {col_names[2]}")

    for row in rows:
        print(f"{row[0]:>2} {row[1]:<20} {row[2]}")

con.close()
