import sqlite3

# Reads the Cars table; run 03_insertingdata.py or 04_preparedstatements.py first.
con = sqlite3.connect("cars.db")
con.row_factory = sqlite3.Row  # rows can now be read by column name

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        print(f"{row['Id']} {row['Name']} {row['Price']}")

    print(rows[0].keys())

con.close()
