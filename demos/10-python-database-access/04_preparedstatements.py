import sqlite3

# Creates cars.db and its Cars table as well, the same way as 03_insertingdata.py.
cars = (
    (1, "Audi", 52642),
    (2, "Mercedes", 57127),
    (3, "Skoda", 9000),
    (4, "Volvo", 29000),
    (5, "Bentley", 350000),
    (6, "Citroen", 21000),
    (7, "Hummer", 41400),
    (8, "Volkswagen", 21600),
)

con = sqlite3.connect("cars.db")

with con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)

con.close()
