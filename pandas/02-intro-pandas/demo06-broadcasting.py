import pandas as pd
file = 'AAPL.csv'
aapl = pd.read_csv(file)

aapl = aapl.set_index('Date')

import numpy as np

aapl.iloc[::3,-1] = np.nan

print(aapl.head(6))
aapl.info()