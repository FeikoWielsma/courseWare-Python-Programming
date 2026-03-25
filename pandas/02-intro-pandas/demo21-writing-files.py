import pandas as pd

filepath = 'ISSN_D_tot.csv'

col_names = ['year', 'month', 'day', 'dec_date', 'sunspots', 'definite']
sunspots = pd.read_csv(filepath, header=None, names = col_names,
                       na_values={'sunspots':[' -1']}, parse_dates=[[0, 1, 2]])

sunspots.index = sunspots['year_month_day']
sunspots.index.name = 'date'

cols = ['sunspots', 'definite']
sunspots = sunspots[cols]

print("writing files")
out_csv = 'sunspots.csv'
sunspots.to_csv(out_csv)
out_tsv = 'sunspots.tsv'
sunspots.to_csv(out_tsv, sep='\t')
out_xlsx = 'sunspots.xlsx'
sunspots.to_excel(out_xlsx)