import sqlite3

import pandas as pd

con1 = sqlite3.connect("cars.db")

carsdf = pd.read_sql_query("SELECT * FROM Cars", con1)

print(type(carsdf))

con2 = sqlite3.connect("calculations.db")

calcudf = pd.read_sql_query("SELECT * FROM Calculations", con2)

print(type(calcudf))
