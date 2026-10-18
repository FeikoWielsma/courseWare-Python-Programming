---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: NumPy
language: python
---

# NumPy Arrays

- An array holds values of one dtype in a regular shape
- Arithmetic applies to every element without a Python loop
- `np.sin` can compute samples of an audio tone

```python
times = np.arange(8) / 8000
samples = np.sin(2 * np.pi * 440 * times)
print(samples.round(3))
print(samples * 0.5)
```

> `demo01 · first_array`

---

# Memory Use

- A Python list holds references to Python objects
- A numeric array stores the numbers in a contiguous buffer
- `nbytes` measures the array buffer; `getsizeof` measures Python objects

```python
count = 60 * 44100
samples = [math.sin(2 * math.pi * 440 * i / 44100) for i in range(count)]
tone = np.array(samples)
list_bytes = sys.getsizeof(samples) + sum(sys.getsizeof(x) for x in samples)
print(f"list: {list_bytes:,} bytes")
print(f"array: {tone.nbytes:,} bytes")
```

> `demo02 · memory_footprint`

---

# Speed

- NumPy evaluates array arithmetic in compiled code
- A Python loop evaluates one sample at a time
- Compare equivalent results before comparing elapsed time

```python
count = 60 * 44100
start = time.perf_counter()
samples = [math.sin(2 * math.pi * 440 * i / 44100) for i in range(count)]
print(f"Python: {time.perf_counter() - start:.3f} s")
start = time.perf_counter()
times = np.arange(count) / 44100
tone = np.sin(2 * np.pi * 440 * times)
print(f"NumPy: {time.perf_counter() - start:.3f} s")
print(np.allclose(samples, tone))
```

> `demo03 · speed_comparison`

---

# Creating Arrays

- `array` converts an existing sequence
- `arange` selects a step; `linspace` selects a sample count
- `zeros`, `ones` and `full` fill a given shape

```python
print(np.array([183, 126, 146]))
print(np.arange(0, 8, 2))
print(np.linspace(0.0, 1.0, 5))
print(np.zeros((2, 4)))
print(np.ones(3, dtype=int))
print(np.full(3, 0.5))
```

> `demo04 · making_arrays`

---

# Array Data Types

- `dtype` determines the representation of each element
- Request a dtype at construction or convert with `astype`
- Integer conversions discard fractional parts; narrow integers have limits

```python
samples = np.array([0.1, 0.5, -0.4], dtype=np.float32)
print(samples.dtype)
print(samples.astype(np.int16))
print(np.iinfo(np.int16).min, np.iinfo(np.int16).max)
counts = np.array([183, 126, 146], dtype=np.int64)
print(counts.dtype, counts.itemsize)
```

> `demo05 · dtypes`

---

# Shape and Dimensions

- An RGB image has height, width and colour-channel dimensions
- `.shape` gives each dimension's length; `.ndim` counts dimensions
- `.size` counts all elements

```python
print(photo.shape)
print(photo.ndim)
print(photo.size)
print(photo[0, 0].shape)
```

> `demo06 · shape_and_ndim`

---

# Reshaping and Transposing

- `reshape` changes dimensions while preserving the element count
- `-1` asks NumPy to calculate one dimension
- `transpose` rearranges axes; `.T` reverses them

```python
pixels = photo.reshape(-1, 3)
print(pixels.shape)
print(np.shares_memory(pixels, photo))
print(photo.transpose(1, 0, 2).shape)
print(pixels.T.shape)
```

> `demo07 · reshape_and_transpose`

---

# Indexing and Slicing

- Give one index or slice per dimension, separated by commas
- A slice excludes its stop position
- A negative step reverses an axis

```python
print(photo[24, 32])
crop = photo[12:36, 16:48]
print(crop.shape)
flipped = photo[::-1]
print(np.array_equal(flipped[0], photo[-1]))
print(photo[:, :, 0].shape)
```

> `demo08 · indexing_and_slicing`

---

# Views and Copies

- Basic slicing returns a view of the same buffer
- Writing through a view also changes the original
- `.copy()` makes an independent buffer; advanced indexing also copies

```python
crop = photo[12:36, 16:48]
detached = crop.copy()
crop[0, 0] = [1.0, 0.0, 0.0]
print(photo[12, 16])
print(detached[0, 0])
print(np.shares_memory(crop, photo))
print(np.shares_memory(detached, photo))
print(np.shares_memory(photo[[0, 1]], photo))
```

> `demo09 · views_and_copies`

---

# Vectorised Arithmetic

- A scalar applies to every element
- Matching shapes combine element by element
- Functions such as `sqrt`, `sin` and `log10` also accept arrays

```python
times = np.arange(8) / 8000
tone = np.sin(2 * np.pi * 440 * times)
quiet = tone * 0.5
print(quiet.round(3))
print(np.sqrt(tone ** 2).round(3))
print((tone - quiet).round(3))
```

> `demo10 · vectorised_arithmetic`

---

# Boolean Masking

- A comparison creates an array of booleans
- Indexing with a mask keeps matching values
- `&` and `|` combine conditions; each comparison needs parentheses

```python
tone = np.array([0.0, 0.2, 0.9, -0.8, 0.0, -0.1])
silent = np.abs(tone) < 0.05
print(tone[silent])
print(silent.sum(), silent.any(), silent.all())
print(np.nonzero(silent)[0])
print(tone[(tone > -0.5) & (tone < 0.5)])
```

> `demo11 · boolean_masking`

---

# np.where

- `where(condition, yes, no)` chooses a value for each element
- Each branch can be an array or a scalar
- Nesting a second `where` supports three outcomes

```python
tone = np.array([-0.9, -0.2, 0.0, 0.4, 0.9])
clipped = np.where(tone > 0.5, 0.5, np.where(tone < -0.5, -0.5, tone))
print(clipped)
print(np.where(np.abs(tone) < 0.05, "silence", "sound"))
print(np.where(tone > 0.5)[0])
```

> `demo12 · np_where`

---

# Broadcasting

- Shapes align from the right
- Dimensions must be equal or one of them must be `1`
- Three channel factors apply to every pixel in an RGB photo

```python
factors = np.array([1.1, 1.0, 0.9])
corrected = np.clip(photo * factors, 0.0, 1.0)
print(photo.shape, factors.shape, corrected.shape)
print(np.broadcast_shapes((48, 64, 3), (3,)))
print(np.broadcast_shapes((3, 1), (4,)))
```

> `demo13 · broadcasting`

---

# Aggregations

- Reductions produce totals, averages or extreme values
- `argmax` gives a position; `unravel_index` converts it to coordinates
- Median and percentiles describe the distribution

```python
print(plays.sum(), plays.mean().round(2))
print(plays.min(), plays.max(), plays.std().round(2))
print(np.median(plays), np.percentile(plays, 95))
day, hour = np.unravel_index(np.argmax(plays), plays.shape)
print(f"peak: day {day}, hour {hour:02d}")
```

> `demo14 · aggregations`

---

# axis Argument

- `axis` names the dimension removed by the reduction
- A days-by-hours grid reduces to hours with `axis=0`
- `axis=1` removes the hours and leaves a value per day
- `keepdims=True` retains the reduced dimension with length one

```python
plays = np.array([[1, 2, 3, 4], [2, 0, 1, 3], [0, 1, 2, 1]])
print(plays.sum())
print(plays.sum(axis=0))
print(plays.sum(axis=1))
print(plays.sum(axis=1, keepdims=True).shape)
```

> `demo15 · the_axis_argument`

---

# Random Numbers

- `default_rng(seed)` produces reproducible pseudorandom draws
- `choice` samples existing values; `permutation` returns a shuffled copy
- `shuffle` changes its input in place

```python
rng = np.random.default_rng(7)
titles = np.array(["Imagine", "Yesterday", "Respect", "Toxic"])
print(rng.permutation(titles))
print(rng.choice(titles, size=2, replace=False))
print(rng.integers(0, 10, size=4))
print(rng.random(3).round(2))
print(rng.normal(0.0, 0.1, size=3).round(2))
rng.shuffle(titles)
print(titles)
```

> `demo16 · random_numbers`

---

# Reading a CSV

- `loadtxt` reads regular numeric data
- `skiprows` excludes the header; `usecols` excludes the day labels
- `savetxt` writes an array back to a file

```python
print(plays.shape)
print(plays.sum(axis=0))
print(plays.sum(axis=1))
print(int(np.argmax(plays.sum(axis=0))))
np.savetxt(DATA / "plays-hourly-mean.csv", plays.mean(axis=0),
           delimiter=",", fmt="%.2f")
```

> `demo17 · csv_into_array`

---

# Summary : NumPy

- Arrays have a dtype and a regular shape
- Slices usually share memory; copies own independent buffers
- Arithmetic, masks and `where` operate on whole arrays
- Broadcasting aligns compatible dimensions from the right
- Reductions remove the selected axes; seeded generators repeat their draws
