import sqlite3

car_id = 1
new_price = 62300

con = sqlite3.connect("cars.db")

with con:
    cur = con.cursor()

    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (new_price, car_id))
    con.commit()

    print(f"Number of rows updated: {cur.rowcount}")


car_id = 4

with con:
    cur = con.cursor()

    cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id", {"Id": car_id})
    con.commit()

    row = cur.fetchone()
    print(row[0], row[1])
