import pandas as pd
file = 'AAPL.csv'
aapl = pd.read_csv(file, parse_dates=['Date'])
print(type(aapl))

print(aapl.shape)
print(aapl.columns)

print(aapl.index)
aapl = aapl.set_index('Date')
print(aapl.index)

print(type(aapl.index))
#print(aapl)