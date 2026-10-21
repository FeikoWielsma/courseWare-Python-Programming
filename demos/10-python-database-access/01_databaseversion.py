import sqlite3

con = sqlite3.connect("watchlist.db")  # creates watchlist.db if it does not exist
cur = con.cursor()
cur.execute("SELECT sqlite_version()")
print(f"SQLite version: {cur.fetchone()[0]}")
# SQLite also creates the cursor through the connection shortcut.
cur = con.execute("SELECT sqlite_version()")
print(cur.fetchone()[0])
version = con.execute("SELECT sqlite_version()").fetchone()[0]
con.close()
