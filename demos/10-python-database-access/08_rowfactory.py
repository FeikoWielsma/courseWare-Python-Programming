import sqlite3

# Reads the films table; run 03_insertingdata.py or 04_preparedstatements.py first.
con = sqlite3.connect("watchlist.db")
con.row_factory = sqlite3.Row  # rows can now be read by column name

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM films")

    rows = cur.fetchall()

    for row in rows:
        print(f"{row['title']} ({row['year']}), {row['minutes']} min")

    print(rows[0].keys())

con.close()
