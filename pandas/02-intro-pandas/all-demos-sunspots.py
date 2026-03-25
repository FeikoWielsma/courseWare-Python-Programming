#step1 : read csv
import pandas as pd
filepath = 'ISSN_D_tot.csv'
sunspots = pd.read_csv(filepath)
print(sunspots.info())
print(sunspots.iloc[10:20, :])

#step2 : read csv with header=None
sunspots = pd.read_csv(filepath, header=None)
print(sunspots.iloc[10:20, :])

#step3 : read csv with col_names
col_names = ['year', 'month', 'day', 'dec_date', 'sunspots', 'definite']
sunspots = pd.read_csv(filepath, header=None, names = col_names)
print(sunspots.iloc[10:20, :])

#step3 : read csv with na_values
sunspots = pd.read_csv(filepath, header=None, names = col_names, na_values=' -1')
print(sunspots.iloc[10:20, :])

#step4 : read csv with na_values and parse_dates and setting index
sunspots = pd.read_csv(filepath, header=None, names = col_names, 
                       na_values={'sunspots':[' -1']}, parse_dates=[[0, 1, 2]])
print(sunspots.info())
sunspots.index = sunspots['year_month_day']
sunspots.index.name = 'date'
print(sunspots.info())
print(sunspots.iloc[10:20, :])

#step5 remove redundant data
cols = ['sunspots', 'definite']
sunspots = sunspots[cols]
print(sunspots.iloc[10:20, :])

#step6 print to file
out_csv = 'sunspots.csv'
sunspots.to_csv(out_csv)
out_tsv = 'sunspots.tsv'
sunspots.to_csv(out_tsv, sep='\t')
out_xlsx = 'sunspots.xlsx'
sunspots.to_excel(out_xlsx)