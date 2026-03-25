import pandas as pd

filepath = 'ISSN_D_tot.csv'
sunspots = pd.read_csv(filepath)
sunspots.info()
print(sunspots.iloc[10:20, :])