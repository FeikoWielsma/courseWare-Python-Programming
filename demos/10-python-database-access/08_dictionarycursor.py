import sqlite3

con = sqlite3.connect("cars.db")

with con:
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        print("%s %s %s" % (row["Id"], row["Name"], row["Price"]))
