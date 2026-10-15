import sqlite3

# Reads the Cars table; run 03_insertingdata.py or 04_preparedstatements.py first.
con = sqlite3.connect("cars.db")

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")

    while True:
        row = cur.fetchone()

        if row is None:
            break

        print(row[0], row[1], row[2])

con.close()
