import sqlite3

# Run demo03 or demo04 first to create the Cars table.
con = sqlite3.connect("cars.db")
try:
    cur = con.cursor()
    cur.execute("""
        SELECT Name, COUNT(*), COALESCE(SUM(Price), 0)
        FROM Cars WHERE Price >= ?
        GROUP BY Name ORDER BY SUM(Price) DESC
        """, (50000,))
    for row in cur.fetchall():
        print(row)
finally:
    con.close()
