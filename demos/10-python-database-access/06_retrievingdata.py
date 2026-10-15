import sqlite3

# Reads the Cars table; run 03_insertingdata.py or 04_preparedstatements.py first.
con = sqlite3.connect("cars.db")

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        print(row)

con.close()
