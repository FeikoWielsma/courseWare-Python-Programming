import pandas as pd
file = 'AAPL.csv'
aapl = pd.read_csv(file)

aapl = aapl.set_index('Date')

print(aapl.head(6))
print(aapl.head(2))

print(aapl.tail())
print(aapl.tail(3))