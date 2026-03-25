import pandas as pd

filepath = 'ISSN_D_tot.csv'

col_names = ['year', 'month', 'day', 'dec_date', 'sunspots', 'definite']
sunspots = pd.read_csv(filepath, header=None, names = col_names,
                       na_values={'sunspots':[' -1']}, parse_dates=[[0, 1, 2]])

sunspots.index = sunspots['year_month_day']
sunspots.index.name = 'date'
sunspots.info()
print(sunspots.iloc[10:20, :])