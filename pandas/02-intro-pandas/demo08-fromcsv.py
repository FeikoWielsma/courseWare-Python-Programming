#step1 : read from csv

import pandas as pd
users = pd.read_csv('users.csv', index_col=0)
#users = pd.read_csv('users.csv')
print(users)