import pandas as pd

heights = [ 59.0, 65.2, 62.9, 65.4, 63.7, 65.7, 64.1 ]
data = {'height': heights, 'sex': 'M'}
results = pd.DataFrame(data)

results.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
results.columns = ['height (in)', 'sex']

print(results)