import pandas as pd
file = 'AAPL.csv'
aapl = pd.read_csv(file)

aapl = aapl.set_index('Date')
aapl.index

print(aapl.iloc[:5,:])
print(aapl.iloc[-5:,:])