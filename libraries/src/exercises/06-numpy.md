# Exercise 6 : Listening Habits with NumPy

Analyse a fictional week of listening. `data/plays-hourly.csv` has one row per
day and one numeric column per hour. Counts are made up, not from work or a
streaming account. A high-count hour is called a "binge hour" for this report;
the label is a teaching category, not a health judgement.

Run commands from `libraries/`. Create your scripts in `work/numpy_listening/`.
The complete solution is in `solutions/solution06-numpy/`. Each script reloads
the CSV so it can run independently.

### Step 1 : Load the grid

Create `01_load.py`. Read the numeric columns, excluding the header and day labels:

```python
from pathlib import Path

import numpy as np

DATA = Path("data")
plays = np.loadtxt(DATA / "plays-hourly.csv", delimiter=",", skiprows=1,
                   usecols=range(1, 25), dtype=np.int64)
```

Print the shape, dtype, size and `plays[:2, :6]`. The shape is `(7, 24)` and
the array contains 168 counts.

:::hint
The slide *Reading a CSV* and demo `csv_into_array` show `loadtxt` and `usecols`.
:::

### Step 2 : Summarise each day

Create `02_per_day.py`. Compute each day's mean, minimum and maximum. Print
the results beside `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat` and `Sun`.
Find the day with the highest mean using `np.argmax`.

:::hint
The slide *axis Argument* shows that removing the hours with `axis=1` leaves
one result per day. *Aggregations* shows `argmax`.
:::

### Step 3 : Summarise each hour

Create `03_per_hour.py`. Compute the mean count per hour across the week.
Print the busiest and quietest hour with their means. Print each hour's mean
beside a bar of `#` characters. Use a loop to format the results; compute
the means with an array operation.

:::hint
The slide *axis Argument* shows that `axis=0` removes days and leaves hours.
The result has shape `(24,)`.
:::

### Step 4 : Find binge hours

Create `04_alerts.py`. Build a mask for counts above 10. Print the number of
matching cells, then print each matching day, hour and count.
Also print which days have at least one such hour and count the cells above
6 and at most 10.

:::hint
The slide *Boolean Masking* shows masks and `nonzero`. *axis Argument* explains
how an `any(axis=1)` reduction gives one boolean per day.
:::

### Step 5 : Compare with the baseline

Create `05_baseline.py`. Calculate the median for each hour across the week,
then subtract those medians from the grid. Find the day and hour with the
largest positive deviation. Print its deviation.

Make an independent copy of the counts and cap every value above 10 at 10.
Print the maximum of both arrays to prove that the original was preserved.

:::hint
The slides *Broadcasting* and *Aggregations* show compatible shapes, median
and `unravel_index`. *Views and Copies* shows an independent copy.
:::

### If time permits

Create `06_bands.py`. Label counts above 10 as `binge`, counts above 6 as
`regular`, and the rest as `quiet`. Count each label overall and count binge
hours per day. Save the 24 hourly means with `savetxt`.

:::hint
The slide *np.where* shows nested conditions. *Reading a CSV* shows `savetxt`.
:::
