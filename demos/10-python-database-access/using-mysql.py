import mysql.connector

import pandas as pd

# https://pypi.org/project/mysql-connector-python/
# pip install mysql-connector-python

con = mysql.connector.connect(
    user="root", password="", host="127.0.0.1", database="cars", port="3306"
)
# with con:

cur = con.cursor()
cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")  # -*- coding: utf-8 -*-

cur.execute("SELECT * FROM Cars")

rows = cur.fetchall()
print(type(rows))

for row in rows:
    print(row)

df = pd.read_sql_query("SELECT * FROM Cars", con)
