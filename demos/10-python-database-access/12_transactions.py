import sqlite3
import sys

con = None
try:
    con = sqlite3.connect("friends.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Friends")
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT)")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")
    con.commit()  # without this line, close() discards the inserts

except sqlite3.Error as e:
    if con:
        con.rollback()

    print(f"Error: {e}")
    sys.exit(1)

finally:
    if con:
        con.close()

con = sqlite3.connect("friends.db")
print(con.execute("SELECT COUNT(*) FROM Friends").fetchone()[0], "friends saved")
con.close()
