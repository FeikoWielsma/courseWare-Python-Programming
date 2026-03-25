import pandas as pd
file = 'AAPL.csv'
aapl = pd.read_csv(file)

aapl = aapl.set_index('Date')

aapl.info()