---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: NumPy
language: python
---

# NumPy Arrays

- NumPy adds one thing to Python, the array :
  - A fixed-size block of numbers, all of the same type
- Everything else in the library exists to build or work on that array :
  - Arithmetic, statistics, sorting, reshaping, reading and writing
- An operation applies to the whole array at once :
  - No loop is written, and no loop runs in Python
- It is the foundation the rest of the numeric stack sits on :
  - Pandas, SciPy, scikit-learn and matplotlib all speak arrays
- The usual import, and it is always spelled this way :

```python
import numpy as np

celsius = np.array([25.3, 24.8, 26.9, 23.9])
print(celsius * 9 / 5 + 32)          # every reading converted
```

> `demo01 · first_array`


---

# Memory Use

- A Python list of numbers is a list of pointers :
  - Each pointer leads to a separate integer object with its own header
- A NumPy array is one contiguous block of raw numbers :
  - No per-element object, no per-element pointer
- The difference is not marginal :

```text
1,000,000 integers
  as a Python list :   36,000,056 bytes
  as a NumPy array :    8,000,000 bytes
```

- One Python integer costs 28 bytes, one array element costs 8
- Contiguous also means the processor can prefetch it :
  - Which is the reason the next slide comes out the way it does

> `demo02 · memory_footprint`


---

# Speed

- Multiply two sequences together and total the result, the Python way :

```python
total = 0.0
for i in range(COUNT):
    total += left_list[i] * right_list[i]
```

- The same arithmetic with arrays is `float((left * right).sum())`
- Two million multiplications, timed :

```text
Python loop      0.086 s
NumPy arrays     0.008 s
```

- The loop still happens, in compiled C rather than in Python

> `demo03 · speed_comparison`


---

# Creating Arrays

- From data you already have :
  - `np.array([3, 1, 4])`, `np.array([[1, 2], [3, 4]])`
- From a rule, when the values are regular :
  - `np.arange(0, 10, 2)` steps like `range`, and stops one short
  - `np.linspace(0.0, 1.0, 5)` asks for a count, and includes both ends
- From a shape, when the values come later :
  - `np.zeros((2, 4))`, `np.ones(3, dtype=int)`, `np.full(4, 7.5)`
- A shape is a tuple, so a two-dimensional shape needs the inner brackets :

```python
np.zeros(3)            # shape (3,)
np.zeros((3, 1))       # shape (3, 1), a column
```

> `demo04 · making_arrays`


---

# Array Data Types

- Every array has a single element type, its `dtype` :
  - Chosen once when the array is created, and fixed for its lifetime
- NumPy picks the narrowest type that holds everything given :

```python
np.array([1, 2, 3]).dtype        # int64
np.array([1.0, 2, 3]).dtype      # float64, one float promotes the lot
```

- Ask for a type and it is enforced, not negotiated :

```python
np.array([1.7, 2.9, -3.4], dtype=np.int32)   # [ 1  2 -3], truncated
```

- The common types are `int32`, `int64`, `float32`, `float64` and `bool`
- `astype` converts, and always makes a new array

> `demo05 · dtypes`


---

# Shape and Dimensions

- `shape` is a tuple giving the size along each dimension :
  - `ndim` is how many dimensions, `size` is the total element count
- Shape reads outermost first, so a table is rows then columns :

```python
table = np.array([[3.4, 8.7, 9.9],
                  [1.1, -7.8, -0.7]])
print(table.ndim)      # 2
print(table.shape)     # (2, 3), two rows of three columns
print(table.size)      # 6, the product of the shape
```

- One dimension is a row of values, two is a table, three is a stack of tables
- Almost every NumPy error message is about a shape :
  - Reading the two shapes in the message is usually the whole diagnosis

> `demo06 · shape_and_ndim`


---

# Reshape and Transpose

- `reshape` gives the same numbers a different shape :
  - The element count has to come out the same
- `-1` means work the remaining dimension out for me :

```python
readings = np.arange(12)
table = readings.reshape(3, 4)      # 3 rows of 4
print(readings.reshape(-1, 2).shape)  # (6, 2)
```

- `.T` transposes, turning rows into columns :

```python
print(table.T.shape)                # (4, 3)
```

- Neither call moves a single number :
  - Both hand back another way of looking at the same block of memory

> `demo07 · reshape_and_transpose`


---

# Indexing and Slicing

- Indexing works as it does on a list :
  - `row[0]`, `row[-1]`, `row[2:5]`, `row[::2]`, and the stop is excluded
- In two dimensions the indices go inside one pair of brackets :

```python
table[1, 2]        # row 1, column 2, a single value
table[0]           # a whole row
table[:, 1]        # a whole column, the colon means "all of them"
table[1:, 2:]      # a sub-table, from row 1 and column 2 on
```

- A slice can also go on the left of an assignment :

```python
table[0] = 0       # the whole first row, in one statement
```

- The colon means every position along that dimension

> `demo08 · indexing_and_slicing`


---

# Views and Copies

- Slicing a list gives a copy, slicing an array gives a view :
  - A view is a window onto the original numbers, not a duplicate of them

```python
readings = np.arange(10) * 10
window = readings[1:4]
window[0] = 999
print(readings)     # [0 999 20 30 ...], the original changed
```

- `.copy()` is the explicit way to detach, and the only reliable one :

```python
window = readings[1:4].copy()      # now edits stay local
```

- Two ways to check which one is in your hands :
  - `np.shares_memory(window, readings)` and `window.base`
- Indexing with a list of positions copies, slicing does not

> `demo09 · views_and_copies`


---

# Vectorised Arithmetic

- An operator between an array and a number applies to every element :

```python
traffic = np.array([1_200, 3_400, 900, 15_800])
print(traffic / 1024)          # every value in kilobytes
```

- An operator between two arrays of the same shape works elementwise :

```python
limits = np.array([2_000, 2_000, 2_000, 10_000])
print(limits - traffic)        # headroom, per interface
```

- The named functions behave the same way over the whole array :
  - `np.sqrt`, `np.log10`, `np.abs`, `np.round`, and the rest
- A comparison is arithmetic too, and returns an array of `True` and `False`
- This is the habit to build : say what to compute, not how to iterate

> `demo10 · vectorised_arithmetic`


---

# Boolean Masking

- A comparison over an array gives a mask, which is itself an array :

```python
latency = np.array([12.1, 9.8, 210.5, 11.2, 480.0])
mask = latency > 100.0         # [False False True False True]
```

- Indexing with the mask keeps the elements where it is `True` :

```python
print(latency[mask])           # [210.5 480. ]
print(mask.sum())              # 2, because True counts as one
```

- Conditions combine with `&` and `|`, and each one needs its own brackets :

```python
(latency > 12.0) & (latency < 100.0)
```

- The mask also works on the left of an assignment

> `demo11 · boolean_masking`


---

# np.where

- `np.where` is an if-else evaluated for every element at once :

```python
disk = np.array([41, 88, 96, 12, 73, 91])
print(np.where(disk > 90, 0, 90 - disk))    # headroom, floored at zero
print(np.where(disk > 90, "FULL", "ok"))    # a label per reading
```

- Either branch can be an array or a single value, in any combination
- Nesting gives more than two outcomes, and three is the readable limit :

```python
np.where(disk > 90, "critical", np.where(disk > 70, "warning", "fine"))
```

- With a single argument it answers "where", giving positions :
  - `np.where(disk > 90)` and `np.nonzero(disk > 90)` are the same call
- `np.clip(disk, 0, 90)` is the common case, already named

> `demo12 · np_where`


---

# Broadcasting

- Broadcasting lets arrays of different shapes work together :
  - Line the shapes up from the right, then compare them
- Two dimensions are compatible when they are equal, or when one is `1` :
  - A size-one dimension is stretched, and nothing is copied to do it

```text
   (3, 4)  with  (4,)     ->  (3, 4)   one row applied to every row
   (3, 1)  with  (4,)     ->  (3, 4)   a column against a row
   (3, 4)  with  (3,)     ->  refused, nothing lines up
```

- Reshaping to `(3, 1)` is how a per-row value is applied to whole rows :

```python
load - baseline.reshape(3, 1)      # each server minus its own baseline
```

> `demo13 · broadcasting`


---

# Aggregations

- A reduction turns a whole array into one number :

```python
print(latency.sum(), latency.mean())
print(latency.min(), latency.max(), latency.std())
```

- `argmin` and `argmax` give the position rather than the value :
  - Which probe, which hour, which server, and usually the useful answer
- Boolean reductions answer yes or no across the array :
  - `mask.any()`, `mask.all()`, and `mask.sum()` for the count
- A mean is a poor summary of anything skewed :
  - `np.median` and `np.percentile(latency, 95)` say more, and lie less
- Every reduction exists as a method and as a function, either is fine

> `demo14 · aggregations`


---

# axis Argument

- Every reduction takes an `axis`, and it names the dimension that disappears
- With no `axis` at all, every dimension goes and one number comes back :

```text
LOAD = [[  1,   2,   3,   4],      axis 0 runs down the rows
        [ 10,  20,  30,  40],      axis 1 runs along the columns
        [100, 200, 300, 400]]      shape (3, 4)

LOAD.sum()        ->  1110                 shape ()
LOAD.sum(axis=0)  ->  [111 222 333 444]    shape (4,), one per column
LOAD.sum(axis=1)  ->  [  10  100 1000]     shape (3,), one per row
```

- `axis=0` removes the rows, so a per-column answer survives
- `keepdims=True` leaves the collapsed dimension as size one, ready to broadcast

> `demo15 · the_axis_argument`


---

# Random Numbers

- Make a generator, then ask it for what is needed :

```python
rng = np.random.default_rng(seed=42)

print(rng.random(4))                  # uniform, 0 to 1
print(rng.integers(1, 7, size=8))     # eight dice
print(rng.normal(100.0, 15.0, 4))     # mean 100, deviation 15
```

- Every call takes a `size`, and a shape works as well as a count
- `rng.choice` samples from data already in hand, with or without replacement
- A seed makes the run repeatable, which is what a demo or a test needs
- The older `np.random.seed` and `np.random.rand` still exist :
  - They share one hidden global generator, and are not what to write now

> `demo16 · random_numbers`


---

# Reading a CSV

- `np.loadtxt` reads a rectangle of numbers, and wants it to be tidy :

```python
load = np.loadtxt(CSV, delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5))
print(load.shape)                  # (24, 5), hours by servers
print(load.mean(axis=0))           # mean per server
```

- `skiprows` steps over a header, `usecols` drops columns that are not numbers
- `np.savetxt` writes one back out, and `np.save` stores the exact bytes
- `np.genfromtxt` copes with gaps and missing values, at some cost in speed
- When the columns have names and different types, this stops being the tool :
  - That is a table rather than an array, and the next module reads it properly

> `demo17 · csv_into_array`


---

# Summary : NumPy

- Reach for it when the data is a rectangle of numbers of one type :
  - Measurements, samples, pixels, matrices, counters over time
- Three habits to carry forward :
  - Say what to compute, rather than how to loop over it
  - Print `.shape` whenever something is not behaving
  - Write `.copy()` when a slice is about to be modified
- Reach for Pandas instead when the columns have names and types
- The rest of the numeric stack is built on this one object :
  - SciPy, scikit-learn, matplotlib and Pandas all take arrays and give them back
