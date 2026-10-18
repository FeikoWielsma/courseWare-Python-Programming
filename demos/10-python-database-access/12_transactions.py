import sqlite3

# Changes the films table; run 03_insertingdata.py or 04_preparedstatements.py first.


def save_ratings(ratings: list[tuple[int, int]]) -> None:
    con = sqlite3.connect("watchlist.db")
    try:
        cur = con.cursor()
        for film_id, stars in ratings:
            if not 1 <= stars <= 5:
                raise ValueError(f"rating must be 1 to 5, got {stars}")
            cur.execute("UPDATE films SET watched = 1, rating = ? WHERE id = ?", (stars, film_id))
        con.commit()  # without this line, close() discards the updates
    except (sqlite3.Error, ValueError) as e:
        con.rollback()  # undoes every update of this batch
        print(f"Error: {e}")
    finally:
        con.close()


save_ratings([(2, 3), (6, 9)])  # 9 is refused, so the rating of film 2 is undone too
save_ratings([(1, 4), (6, 5)])

con = sqlite3.connect("watchlist.db")
for row in con.execute("SELECT title, watched, rating FROM films WHERE id IN (1, 2, 6)"):
    print(row)
con.close()
