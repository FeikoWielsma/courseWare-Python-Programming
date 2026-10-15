---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Python Database Access
---

# Python DB API

- Provides a standard interface from Python to databases :
  - Most Python database interfaces adhere to this standard
  - Each database has its own module highly consistent with others
- The standard is described in PEP 249 :
  - Modules are available for most of the popular relational databases
  - Code written for one database reads almost the same for another
- Python DB API 2.0 compatible modules :
  - `sqlite3` (SQLite), part of the standard library and used in this module
  - `psycopg` (PostgreSQL)
  - `mysqlclient` or `PyMySQL` (MySQL and MariaDB)
  - `oracledb` (Oracle)
  - `pyodbc` (any database with an ODBC driver, such as SQL Server and DB2)

---

# DB API Concepts

- DB API uses two main concepts for processing queries :
  - Connections and cursors
- Every script follows the same shape :

```mermaid
flowchart LR
  A[connect] --> B[cursor] --> C[execute] --> D[fetch] --> E[commit] --> F[close]
```

- Connection objects logically wrap a database connection :
  - Provide access to the database and handle transactions
- `sqlite3.connect()` opens a database file, and creates it if it does not exist
- Cursor objects used to manipulate and query the database :
  - Created on connections using the `conn.cursor()` method
  - Cursor objects provide ways to execute statements and access results

```python
con = sqlite3.connect("sample.db")
cur = con.cursor()
cur.execute("CREATE TABLE testtable(id int, name varchar(254))")
```

---

# Check Database Version


```python
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
```

> `demo01 · databaseversion`


---

# Using with

- A connection used in a `with` statement manages the transaction :
  - When the block ends normally, the changes are committed
  - When the block ends with an exception, the changes are rolled back

```python
import sqlite3
con = sqlite3.connect("test.db")
with con:
    cur = con.cursor()
    cur.execute("SELECT SQLITE_VERSION()")
    data = cur.fetchone()
    print(f"SQLite version: {data}")
con.close()  # `with con:` commits or rolls back, it does not close
```

- The connection stays open after the block :
  - Close it yourself with `con.close()` when you are done

> `demo02 · usingwith`


---

# Inserting Data

- Cursor objects provides a `cursor.execute()` method :
  - Execute SQL statements on a connection
- Method also accepts :
  - Sequence of parameters to customize the SQL statement

- This demo creates the `Cars` table that the later demos read :

```python
import sqlite3
con = sqlite3.connect("cars.db")
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
    cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
    cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
    cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
    cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
    cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
    cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
    cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
```

> `demo03 · insertingdata`


---

# Prepared Statements

- If same query must be repeated multiple times :
  - Can use parameterized queries with question marks or named parameters
  - Good for both performance and for security
- Can use `executemany()` method for prepared statements :

```python
import sqlite3
cars = (
    (1, "Audi", 52642),
    (2, "Mercedes", 57127),
    (3, "Skoda", 9000),
    (4, "Volvo", 29000),
    (5, "Bentley", 350000),
    (6, "Citroen", 21000),
    (7, "Hummer", 41400),
    (8, "Volkswagen", 21600),
)
con = sqlite3.connect("cars.db")
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
```

> `demo04 · preparedstatements`


---

# Last inserted row id

- Sometimes we need to determine the id of last inserted row :
  - In Python SQLite we use the `lastrowid` attribute of the cursor object
- The name `":memory:"` opens a database that lives only while the program runs :

```python
import sqlite3
con = sqlite3.connect(":memory:")
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT)")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")
    lid = cur.lastrowid
    print(f"The last Id of the inserted row is {lid}")
```

> `demo05 · lastinsertedrowid`


---

# Retrieving Data

- Data retrieval is done with fetch functions like `fetchall()` :
  - The `Cars` table comes from demo03 or demo04, so run one of them first

```python
import sqlite3
con = sqlite3.connect("cars.db")
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print(row)
```

- `fetchall()` gets all records and returns a result set :
  - Actually the result set is a list of tuples

```text
(1, 'Audi', 52642)
(2, 'Mercedes', 57127)
(3, 'Skoda', 9000)
```

- Other `fetch*()` methods read data from result set :

```python
first_row = cur.fetchone()
next_10_rows = cur.fetchmany(10)
all_remaining_rows = cur.fetchall()
```

> `demo06 · retrievingdata`

---

# Rows by Column Name

- A row is a tuple by default, so a column is read by its position :
  - `row[1]` works, but the reader has to know what the second column is
- Set `row_factory` on the connection to `sqlite3.Row` :
  - Every row can then be read by column name as well as by position

```python
import sqlite3
con = sqlite3.connect("cars.db")
con.row_factory = sqlite3.Row  # rows can now be read by column name
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print(f"{row['Id']} {row['Name']} {row['Price']}")
```

```text
1 Audi 52642
2 Mercedes 57127
```

> `demo07 · rowfactory`


---

# Fetching Rows

- Returning all data at a time may not be feasible :
  - It is also possible to fetch rows one by one with `fetchone()` :

```python
import sqlite3
con = sqlite3.connect("cars.db")
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
    while True:
        row = cur.fetchone()
        if row is None:
            break
        print(row[0], row[1], row[2])
```

- `fetchone()` method returns next row from the table :
  - If there is no more data left, it returns `None`

> `demo08 · fetchone`


---

# Parameterized Queries

- Passing data from Python to the database :
  - First discouraged option is quoting values and sending plain SQL to the database
  - Second option preferred using binding parameters in the SQL with place holders
- Python sqlite3 module supports two types of placeholders :
  - Question marks and named placeholders

```python
import sqlite3
car_id = 1
new_price = 62300
con = sqlite3.connect("cars.db")
with con:
    cur = con.cursor()
    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (new_price, car_id))
    print(f"Number of rows updated: {cur.rowcount}")
```

> `demo09 · parameterizedqueries`


---

# Metadata

- Metadata is information about the data in the database :
  - Contains information about the tables and columns like name and datatypes

```python
import sqlite3
con = sqlite3.connect("cars.db")
with con:
    cur = con.cursor()
    cur.execute("PRAGMA table_info(Cars)")
    data = cur.fetchall()
    for d in data:
        print(d[0], d[1], d[2])
```

```text
0 Id INT
1 Name TEXT
2 Price INT
```

- Metadata in SQLite can be obtained using `PRAGMA` command :
  - SQLite objects may have attributes, which are metadata
  - Obtain specific metadata from querying the SQLite system `sqlite_master` table

> `demo10 · metadata`


---

# Transactions

- Transactions logically wrap statements into blocks of execution :
  - Transactions are units of recovery
- Main benefit is that you can undo changes very easily :
  - Ensures data consistency at all times
  - Not all databases provide transactions !
- Transactions conform to ACID principles :
  - Atomicity, Consistency, Isolation, Durability
- DB API supports transactions if the database supports them :
  - Via methods on the connection object
- Write all changes of the last transaction block to the database :

```python
con.commit()
```

- Undo all changes applied to the database on the connection :

```python
con.rollback()
```

---

# Committing Data


```python
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
```

> `demo11 · transactions`

---

# Summary : Python Database Access

- Python DB API is standard interface from Python to databases :
  - Each database has its own module highly consistent with others
- DB API uses two main concepts for processing queries :
  - Connections and cursors
- Connection objects logically wrap a database connection :
  - Provide means to handle database transactions
- Cursor objects used to manipulate and query the database :
  - Created on connections using the `conn.cursor()` method
- If same query must be repeated multiple times :
  - Can use parameterized queries with question marks or named parameters
- A connection in a `with` statement commits or rolls back the transaction :
  - It does not close the connection; `con.close()` does that
- DB API supports transactions if database supports them :
  - Via methods on the connection object

> `exercise10 · Python Database Access`
