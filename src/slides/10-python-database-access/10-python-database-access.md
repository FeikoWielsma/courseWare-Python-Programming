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
- Influenced by ODBC, JDBC and Perl's DBI :
  - Modules available for most of the popular relational databases
- Standard is easy to implement and understand and this means :
  - More and higher quality database third party modules
  - More supported backends
- Python DB API 2.0 compatible modules :
  - Sqlite3 part of the standard library
  - MySQLdb (MySQL)
  - psycopg2 (PostgreSQL)
  - cx_Oracle (Oracle)
  - mxODBC (SQL Server, DB2, Sybase, Oracle, etc.)
  - mxODBC Connect (same as mxODBC, but more platforms)

---

# DB API Concepts

- DB API uses two main concepts for processing queries :
  - Connections and cursors
- Connection objects logically wrap a database connection :
  - Provide network/RPC access to the database
  - Provide means to handle database transactions
  - You can't execute statements on connection objects
- Example :

```python
db_connection = sqlite.connect('sample.db')
```

- Cursor objects used to manipulate and query the database :
  - Created on connections using the `conn.cursor()` method
  - Cursor objects provide ways to execute statements and access results
- Example :

```python
cursor = conn.cursor()
cursor.execute('create table testtable(id int, name varchar(254))')
```

---

# Check Database Version


```python
import sqlite3
import sys
con = None
try :
     con = sqlite3.connect('test.db')
     cur = con.cursor()
     cur.execute('SELECT SQLITE_VERSION()')
     data = cur.fetchone()
     print ("SQLite version: %s" % data)
except sqlite3.Error as e :
     print ("Error %s:" % e.args[0])
     sys.exit(1)
finally :
     if con:
          con.close()
```

> `demo01 · databaseversion`


---

# Using with

- By using the `with` statement the code is more compact :
  - Using `with` the Python interpreter automatically releases the resources
  - This also provides error handling

```python
import sqlite3
con = sqlite3.connect('test.db')
with con:
     cur = con.cursor()
     cur.execute('SELECT SQLITE_VERSION()')
     data = cur.fetchone()
     print ("SQLite version: %s" % data)
```

- Using the `with` statement :
  - Changes are automatically committed
  - Otherwise, we would have to commit them manually

> `demo02 · usingwith`


---

# Inserting Data

- Cursor objects provides a `cursor.execute()` method :
  - Execute SQL statements on a connection
- Method also accepts :
  - Sequence of parameters to customize the SQL statement

```python
import sqlite3
con = sqlite3.connect('cars.db')
with con :
  cur = con.cursor()
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
cars = ((1, 'Audi', 52642), (2, 'Mercedes', 57127), (3, 'Skoda', 9000),
        (4, 'Volvo', 29000), (5, 'Bentley', 350000), (6, 'Hummer', 41400),
        (7, 'Volkswagen', 21600))
con = sqlite3.connect('test.db')
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

```python
import sqlite3
con = sqlite3.connect(':memory:')
with con:
  cur = con.cursor()
  cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
  cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
  cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
  cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
  cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
  lid = cur.lastrowid
  print ("The last Id of the inserted row is %d" % lid)
```

> `demo05 · lastinsertedrowid`


---

# Retrieving Data

- Data retrieval is done with fetch functions like `fetchall()` :

```python
import sqlite3
con = sqlite3.connect('cars.db')
with con:
     cur = con.cursor()
     cur.execute("SELECT * FROM Cars")
     rows = cur.fetchall()
     for row in rows:
          print (row)
```

- `fetchall()` gets all records and returns a result set :
  - Actually the result set is a list of tuples
- Other `fetch*()` methods read data from result set :

```python
cursor.execute('select * from testtable')
first_row = cursor.fetchone()
next_10_rows = cursor.fetchmany(10)
all_remaining_rows = cursors.fetchall()
```

> `demo06 · retrievingdata`

---

# Fetching Rows

- Returning all data at a time may not be feasible :
  - It is also possible to fetch rows one by one with `fetchone()` :

```python
import sqlite3
con = lite.connect('test.db')
with con:
     cur = con.cursor()
     cur.execute("SELECT * FROM Cars")
     while True:
          row = cur.fetchone()
          if row == None:
              break
          print (row[0], row[1], row[2])
```

- `fetchone()` method returns next row from the table :
  - If there is no more data left, it returns `None`

> `demo07 · fetchone`


---

# Dictionary Cursor

- Default cursor returns data in a list of tuples :
  - When we use a dictionary cursor, the data is sent in the form of Python dictionaries
  - This way we can refer to the data by their column names

```python
import sqlite3
con = sqlite3.connect('cars.db')
with con:
     con.row_factory = sqlite3.Row
     cur = con.cursor()
     cur.execute("SELECT * FROM Cars")
     rows = cur.fetchall()
     for row in rows:
          print ("%s %s %s" % (row["Id"], row["Name"], row["Price"]))
```

> `demo08 · dictionarycursor`


---

# Parameterized Queries

- Passing data from Python to the database :
  - First discouraged option is quoting values and sending plain SQL to the database
  - Second option preferred using binding parameters in the SQL with place holders
- Python sqlite3 module supports two types of placeholders :
  - Question marks and named placeholders

```python
import sqlite3
uId = 1
uPrice = 62300
con = sqlite3.connect('test.db')
with con:
     cur = con.cursor()
     cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))
     con.commit()
     print ("Number of rows updated: %d" % cur.rowcount)
```

> `demo09 · parameterizedqueries`


---

# Metadata

- Metadata is information about the data in the database :
  - Contains information about the tables and columns like name and datatypes

```python
import sqlite3
con = sqlite3.connect('cars.db')
with con:
     cur = con.cursor()
     cur.execute('PRAGMA table_info(Cars)')
     data = cur.fetchall()
     for d in data:
          print (d[0], d[1], d[2])
```

- Metadata in SQLite can be obtained using `PRAGMA` command :
  - SQLite objects may have attributes, which are metadata
  - Obtain specific metatada from querying the SQLite system sqlite_master table

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
conn.commit()
```

- Undo all changes applied to the database on the connection :

```python
conn.rollback()
```

---

# Committing Data


```python
import sqlite3
import sys
try:# con = sqlite3.connect('friends.db', isolation_level=None) => autocommit
     con = sqlite3.connect('friends.db')
     cur = con.cursor()
     cur.execute("DROP TABLE IF EXISTS Friends")
     cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT)")
     cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
     cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
     cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
     cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")
     #con.commit() // data not written until commit is executed
except sqlite3.Error as e:
     if con:
          con.rollback()
     print ("Error %s:" % e.args[0])
     sys.exit(1)
finally:
```




```python
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
- Using `with` Python automatically releases the resources :
  - Changes are automatically committed
- DB API supports transactions if database supports them :

> `exercise · Python Database Access`

  - Via methods on the connection object
