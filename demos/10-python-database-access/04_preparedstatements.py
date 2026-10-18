import sqlite3

# Creates watchlist.db and its films table as well, the same way as 03_insertingdata.py.
films = (
    ("Spirited Away", 2001, 125),
    ("Amélie", 2001, 122),
    ("Arrival", 2016, 116),
    ("Paddington 2", 2017, 104),
    ("Coco", 2017, 105),
    ("Parasite", 2019, 132),
)

con = sqlite3.connect("watchlist.db")

with con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS films")
    cur.execute("""
        CREATE TABLE films(id INTEGER PRIMARY KEY, title TEXT, year INT,
                           minutes INT, watched INT DEFAULT 0, rating INT)
        """)
    cur.executemany("INSERT INTO films(title, year, minutes) VALUES(?, ?, ?)", films)

con.close()
