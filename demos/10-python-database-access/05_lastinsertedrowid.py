import sqlite3

con = sqlite3.connect(":memory:")  # a database that lives only while the program runs

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE films(id INTEGER PRIMARY KEY, title TEXT)")
    cur.execute("INSERT INTO films(title) VALUES('Spirited Away')")
    cur.execute("INSERT INTO films(title) VALUES('Arrival')")
    cur.execute("INSERT INTO films(title) VALUES('Paddington 2')")

    film_id = cur.lastrowid
    print(f"Paddington 2 was added with id {film_id}")

con.close()
