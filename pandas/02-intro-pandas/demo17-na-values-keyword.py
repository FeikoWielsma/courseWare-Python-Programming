import pandas as pd

filepath = 'ISSN_D_tot.csv'

col_names = ['year', 'month', 'day', 'dec_date', 'sunspots', 'definite']
sunspots = pd.read_csv(filepath, header=None, names = col_names, na_values=' -1')
print(sunspots.iloc[10:20, :])