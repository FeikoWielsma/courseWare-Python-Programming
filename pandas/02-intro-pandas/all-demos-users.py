#step1 : read from csv

import pandas as pd
users = pd.read_csv('users.csv', index_col=0)
print(users)

#step2 : read from dictionary

import pandas as pd
data = {'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
        'city': ['Paris', 'Berlin', 'Paris', 'Berlin'],
         'visitors': [139, 237, 326, 456],
         'signups': [7, 12, 3, 5]}
users = pd.DataFrame(data)
print(users)

#step3 : read from lists

cities = ['Paris', 'Berlin', 'Paris', 'Berlin']
signups = [7, 12, 3, 5]
visitors = [139, 237, 326, 456]
weekdays = ['Sun', 'Sun', 'Mon', 'Mon']
list_labels = ['city', 'signups', 'visitors', 'weekday']
list_cols = [cities, signups, visitors, weekdays]
zipped = list(zip(list_labels, list_cols))
data = dict(zipped)
users = pd.DataFrame(data)
print(users)
users['fees'] = 0
print(users)

#step4 : broadcast from dictionary

heights = [ 59.0, 65.2, 62.9, 65.4, 63.7, 65.7, 64.1 ]
data = {'height': heights, 'sex': 'M'}
results = pd.DataFrame(data)
print(results)