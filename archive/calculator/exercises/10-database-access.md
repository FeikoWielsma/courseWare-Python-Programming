# Exercise 10 : Python Database Access

In this exercise the file logging is replaced by a SQLite database.

---

### Step 1

Create a project or directory named `exercise10` and a Python module `calculator10.py`. Copy the contents of `calculator9.py` from the previous exercise to `calculator10.py`. Also copy the `calcu` package. You will replace the file access code with database access code.

Before entering the while loop in which the user is asked to choose the type of calculation, use the following code to create a database `calculations.db` and a table `Calculations` :

```python
con = sqlite3.connect("calculations.db")
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Calculations")
    cur.execute("CREATE TABLE Calculations (Id VARCHAR(10), Nr1 INT, Nr2 INT, Result DECIMAL)")
```

Next consider the Faculty calculation type and replace the code where data is written to the file with code that writes data to the database :

```python
with con:
    cur = con.cursor()
    cur.execute(
        "INSERT INTO Calculations ('Id', 'Nr1', 'Nr2', 'Result') VALUES(?,?,?,?)",
        (calc_action, x, 0, faculty(x)),
    )
```

In this exercise we will not consider the Sum and Average calculation types; just remove the code that writes their data to the file. We will however consider the Add, Subtract, Divide and Multiply calculation types. For these replace the file access code with the following database access code, for instance for the Add calculation type :

```python
with con:
    cur = con.cursor()
    cur.execute(
        "INSERT INTO Calculations ('Id', 'Nr1', 'Nr2', 'Result') VALUES(?,?,?,?)",
        (calc_action, f1, f2, add(f1, f2)),
    )
```

Next insert some records in the database, observe the existence of the `calculations.db` file in the directory of the script and use the SQLiteStudio Database Viewer to connect to SQLite and examine the contents of the database.

Also make a script to read the database records back in and display them in the console.
