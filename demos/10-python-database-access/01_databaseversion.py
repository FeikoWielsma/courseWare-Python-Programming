import sqlite3
import sys

con = None

try:
    con = sqlite3.connect("test.db")  # creates test.db if it does not exist

    cur = con.cursor()
    cur.execute("SELECT SQLITE_VERSION()")

    data = cur.fetchone()
    print(f"SQLite version: {data}")

except sqlite3.Error as e:
    print(f"Error: {e}")
    sys.exit(1)

finally:
    if con:
        con.close()
