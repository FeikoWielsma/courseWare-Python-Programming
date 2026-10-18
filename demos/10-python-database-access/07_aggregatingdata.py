import sqlite3

# Run demo03 or demo04 first to create the films table.
con = sqlite3.connect("watchlist.db")
try:
    cur = con.cursor()
    cur.execute("""
        SELECT year, COUNT(*), COALESCE(SUM(minutes), 0)
        FROM films WHERE year >= ?
        GROUP BY year ORDER BY SUM(minutes) DESC
        """, (2010,))
    for row in cur.fetchall():
        print(row)
finally:
    con.close()
