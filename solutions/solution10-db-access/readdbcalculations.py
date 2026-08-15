import sqlite3

con = sqlite3.connect('calculations.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Calculations")
    rows = cur.fetchall()

    for row in rows:
        print(row)
