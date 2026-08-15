import sqlite3

u_id = 1
u_price = 62300

con = sqlite3.connect("Cars.db")

with con:
    cur = con.cursor()

    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (u_price, u_id))
    con.commit()

    print(f"Number of rows updated: {cur.rowcount}")


u_id = 4

with con:
    cur = con.cursor()

    cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id", {"Id": u_id})
    con.commit()

    row = cur.fetchone()
    print(row[0], row[1])
