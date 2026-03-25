import sqlite3
import sys

try:
    con = sqlite3.connect("friends.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Friends")
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT)")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")

    # con.commit()
except sqlite3.Error as e:
    if con:
        con.rollback()

    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()
