import pandas as pd

#step1 : read from dictionary

import pandas as pd
data = {'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
        'city': ['Paris', 'Berlin', 'Paris', 'Berlin'],
         'visitors': [139, 237, 326, 456],
         'signups': [7, 12, 3, 5]}
users = pd.DataFrame(data)
print(users)