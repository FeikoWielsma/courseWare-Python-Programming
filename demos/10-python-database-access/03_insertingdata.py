import sqlite3

# Creates watchlist.db and its films table, which the demos after this one read.
con = sqlite3.connect("watchlist.db")

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS films")
    cur.execute("""
        CREATE TABLE films(id INTEGER PRIMARY KEY, title TEXT, year INT,
                           minutes INT, watched INT DEFAULT 0, rating INT)
        """)
    cur.execute("INSERT INTO films(title, year, minutes) VALUES('Spirited Away', 2001, 125)")
    cur.execute("INSERT INTO films(title, year, minutes) VALUES('Amélie', 2001, 122)")
    cur.execute("INSERT INTO films(title, year, minutes) VALUES('Arrival', 2016, 116)")
    cur.execute("INSERT INTO films(title, year, minutes) VALUES('Paddington 2', 2017, 104)")
    cur.execute("INSERT INTO films(title, year, minutes) VALUES('Coco', 2017, 105)")
    cur.execute("INSERT INTO films(title, year, minutes) VALUES('Parasite', 2019, 132)")

con.close()
