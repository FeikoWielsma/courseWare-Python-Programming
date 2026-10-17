import sqlite3

# Changes the Cars table; run 03_insertingdata.py or 04_preparedstatements.py first.
car_id = 1
new_price = 62300

con = sqlite3.connect("cars.db")

with con:
    cur = con.cursor()

    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (new_price, car_id))

    print(f"Number of rows updated: {cur.rowcount}")


car_id = 4

with con:
    cur = con.cursor()

    cur.execute("SELECT Name, Price FROM Cars WHERE Id=:id", {"id": car_id})

    row = cur.fetchone()
    print(row[0], row[1])

con.close()
