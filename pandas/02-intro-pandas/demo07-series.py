import pandas as pd
file = 'AAPL.csv'
aapl = pd.read_csv(file)

low = aapl['Low']
print(type(low))

print(low.head())
lows = low.values

print(type(lows))
print(lows)