# Exercise 5 : NumPy

In this exercise you take a day of CPU readings off five servers and answer questions about them with arrays instead of loops. The data is already in the repository as `data/server-load.csv` : twenty-four hourly readings for `web01`, `web02`, `web03`, `db01` and `cache01`, as a percentage. By the end you will have found the busiest server, the busiest hour, and the one host that misbehaves in the middle of the night.

Work in a folder `numpy_load/`, one file per step, and keep the files as you go. Every answer in this exercise is one or two lines. If you find yourself writing a `for` loop over an array, stop and look for the expression instead.

---

### Step 1 : Load the file

Create `01_load.py`.

Read the CSV into an array. The first row is a header and the first column is the hour, so neither is a number you want in the array :

```python
from pathlib import Path

import numpy as np

DATA = Path(__file__).resolve().parents[2] / "data"

load = np.loadtxt(DATA / "server-load.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5))
```

Print `load.shape`, `load.dtype` and `load.size`. You should see `(24, 5)` : twenty-four rows of hours, five columns of servers. Print the first two rows as well, so you can see real numbers on the screen.

That is the whole of step one. If it printed `(24, 5)`, your environment works and the rest of the exercise will run.

---

### Step 2 : Summarise each server

Create `02_per_server.py` and load the array again.

Each column is one server, so a per-server answer means collapsing the hours. That is `axis=0` : the rows are the dimension that disappears.

Compute the mean, the minimum and the maximum for each of the five servers, and print them next to their names :

```python
SERVERS = ["web01", "web02", "web03", "db01", "cache01"]

means = load.mean(axis=0)
for name, mean in zip(SERVERS, means, strict=True):
    ...
```

Then find the busiest server. `np.argmax` gives you a position rather than a value, and `SERVERS[position]` turns that position back into a name.

Check your answer against the shapes : `load.mean(axis=0)` must have shape `(5,)`. If you got `(24,)`, you used the other axis.

---

### Step 3 : Summarise each hour

Create `03_per_hour.py`.

Now collapse the other way. A per-hour answer keeps the rows and loses the servers, which is `axis=1`.

Compute the mean load per hour, then print :

1. The busiest hour of the day, and its mean.
2. The quietest hour, and its mean.
3. The total load per hour, so you can see the shape of the working day.

The hour number is the row number, because the rows are in order from 00:00, so `np.argmax` gives you the hour directly.

> If you are not sure which axis you want, print the shape of the result. One number per hour means twenty-four numbers.

---

### Step 4 : Find the readings that matter

Create `04_alerts.py`.

Build a boolean mask of every reading above 80 percent :

```python
busy = load > 80.0
```

Print how many readings are over the line, using `busy.sum()`. Then use `np.nonzero(busy)` to get the positions. It returns one array per dimension, so unpack it into two names :

```python
hours, servers = np.nonzero(busy)
```

Loop over those two arrays together and print one line per alert, naming the server and the hour, for example `db01 at 02:00 -> 93.3 %`. This is the one loop in the exercise you are allowed to write, because you are formatting text rather than computing numbers.

Then answer the same question a second way : which servers ever go over 80 percent at all? `busy.any(axis=0)` gives you one `True` or `False` per server, which you can use to index the server names once you have made them an array.

---

### Step 5 : Compare each server to its own baseline

Create `05_baseline.py`.

A raw percentage is not very interesting; the interesting question is how far each reading is from normal *for that server*. `cache01` sitting at 10 percent is fine, `cache01` at 40 percent would not be.

Take the median of each server, then subtract it from that server's column. The medians come out as shape `(5,)` and the array is `(24, 5)`, so they line up from the right and broadcast across every row with no reshaping needed :

```python
baseline = np.median(load, axis=0)
deviation = load - baseline
```

Print the shape of `baseline`, and the largest deviation for each server. Then find the single worst deviation in the whole table. `np.argmax` on a two-dimensional array gives you a position into the flattened array, so use `np.unravel_index` to turn it back into a row and a column :

```python
hour, server = np.unravel_index(np.argmax(deviation), deviation.shape)
```

Finally, make a copy of `load` and clip every reading in the copy to a ceiling of 90 percent, without disturbing the original :

```python
capped = load.copy()
capped[capped > 90.0] = 90.0
```

Print the maximum of both arrays to prove the original survived. Leave the `.copy()` out and run it again to see what happens when you forget.

---

### Optional : band every reading

Create `06_bands.py` if you have time.

Use `np.where` to turn the whole table into labels in one expression : `critical` above 90, `warning` above 60, and `fine` otherwise. Nesting one `np.where` inside another gives you the three bands.

Then count how many readings fall into each band. Comparing the label array against a string gives you a mask, and a mask sums to a count :

```python
labels = np.where(load > 90.0, "critical", np.where(load > 60.0, "warning", "fine"))
print("critical :", (labels == "critical").sum())
```

For a last flourish, print a per-server count of warnings by summing that mask along `axis=0`, and write the hourly means out to a new CSV in `data/` with `np.savetxt`.
