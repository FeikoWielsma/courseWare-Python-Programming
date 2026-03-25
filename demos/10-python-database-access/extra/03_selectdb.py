import sqlite3

conn = sqlite3.connect("c:/tmp/example")

c = conn.cursor()

c.execute("select * from stocks order by price")

for row in c:
    print(row)
