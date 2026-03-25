import sqlite3

con = sqlite3.connect("cars.db")

with con:
    cur = con.cursor()

    cur.execute("PRAGMA table_info(Cars)")

    data = cur.fetchall()

    for d in data:
        print(d[0], d[1], d[2])

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")

    col_names = [cn[0] for cn in cur.description]

    rows = cur.fetchall()

    print("%s %-10s %s" % (col_names[0], col_names[1], col_names[2]))

    for row in rows:
        print("%2s %-10s %s" % row)
