import sqlite3

# Changes the films table; run 03_insertingdata.py or 04_preparedstatements.py first.
film_id = 3
rating = 5

con = sqlite3.connect("watchlist.db")

with con:
    cur = con.cursor()

    cur.execute("UPDATE films SET watched = 1, rating = ? WHERE id = ?", (rating, film_id))

    print(f"Number of rows updated: {cur.rowcount}")


title = "Howl's Moving Castle"

with con:
    cur = con.cursor()

    cur.execute(
        "INSERT INTO films(title, year, minutes) VALUES(:title, :year, :minutes)",
        {"title": title, "year": 2004, "minutes": 119},
    )
    cur.execute("SELECT id, title FROM films WHERE title = :title", {"title": title})

    row = cur.fetchone()
    print(row[0], row[1])

con.close()
