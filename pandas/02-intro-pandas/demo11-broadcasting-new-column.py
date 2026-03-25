import pandas as pd

cities = ['Paris', 'Berlin', 'Paris', 'Berlin']
signups = [7, 12, 3, 5]
visitors = [139, 237, 326, 456]
weekdays = ['Sun', 'Sun', 'Mon', 'Mon']
list_labels = ['city', 'signups', 'visitors', 'weekday']

list_cols = [cities, signups, visitors, weekdays]
zipped = list(zip(list_labels, list_cols))

data = dict(zipped)

users = pd.DataFrame(data)

users['fees'] = 0
print(users)