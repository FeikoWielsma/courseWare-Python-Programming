import sqlite3

con = sqlite3.connect("cars.db")

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")

    while True:
        row = cur.fetchone()

        if row == None:
            break

        print(row[0], row[1], row[2])
