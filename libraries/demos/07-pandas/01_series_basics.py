import pandas as pd

durations = pd.Series([183, 126, 146],
                      index=["Imagine", "Yesterday", "Respect"])
print(durations["Imagine"])
print(durations / 60)
print(durations > 180)
print(durations.index.tolist())
print(durations.to_numpy())
