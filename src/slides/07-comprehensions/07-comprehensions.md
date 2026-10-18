---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Comprehensions
---

# List Comprehensions

- A comprehension builds a new list by evaluating an expression for each item.
- Read the `for` part first, then the expression on its left.

```python
filenames: list[str] = ["cover", "stage", "crowd"]
photo_files = [f"{name}.jpg" for name in filenames]
print(photo_files)  # ['cover.jpg', 'stage.jpg', 'crowd.jpg']
```



> `demo01 · list_comprehensions`

---

# Syntax List Comprehensions

- A comprehension has the form `[expression for name in source]`.
- `source` supplies the items; `name` receives one item at a time.
- `expression` computes the value added to the new list.

```python
filenames: list[str] = ["cover", "stage", "crowd"]
photo_files = []
for name in filenames:
    photo_files.append(f"{name}.jpg")
print(photo_files)  # ['cover.jpg', 'stage.jpg', 'crowd.jpg']

photo_files = [f"{name}.jpg" for name in filenames]
print(photo_files)  # ['cover.jpg', 'stage.jpg', 'crowd.jpg']
```

- Both forms create a new list and leave `filenames` unchanged.

---

# Filtered List Comprehension

- An optional `if` keeps only the items that satisfy its condition.
- These two forms produce the same list :

```python
filenames = ["cover.jpg", "notes.txt", "stage.jpg"]
photo_files = []
for name in filenames:
    if name.endswith(".jpg"):
        photo_files.append(name)
print(photo_files)  # ['cover.jpg', 'stage.jpg']

photo_files = [name for name in filenames if name.endswith(".jpg")]
print(photo_files)  # ['cover.jpg', 'stage.jpg']
```



> `demo02 · comprehension_with_predicate`

---

# Nested List Comprehensions

- A nested comprehension builds a list of lists, preserving the row structure.

```python
photo_sizes = [[18.2, 19.6], [20.1, 21.8]]
rounded = [[round(value) for value in row] for row in photo_sizes]
print(rounded)  # [[18, 20], [20, 22]]
```

- Each row holds the photo sizes in megabytes from one album.
- The inner comprehension rounds the photo sizes in one row.
- The outer comprehension repeats that operation for every row.
- Use an ordinary loop when the nesting needs more explanation.

> `demo03 · nested_comprehensions`

---

# Flattening a List of Lists

- Two `for` clauses collect all the photo_sizes into one list.
- Their order is the same as in the equivalent nested loops.

```python
photo_sizes = [[18.2, 19.6], [20.1, 21.8]]
flat = []
for row in photo_sizes:
    for value in row:
        flat.append(value)
print(flat)  # [18.2, 19.6, 20.1, 21.8]

flat = [value for row in photo_sizes for value in row]
print(flat)  # [18.2, 19.6, 20.1, 21.8]
```

- The result can be used to calculate a minimum or maximum across all albums.

---

# Comprehension Features

- Unpack each track into a title and duration inside the `for` part
- The expression can call a function :

```python
def format_duration(seconds: int) -> str:
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}:{remainder:02d}"


tracks = [("Imagine", 183), ("Yesterday", 125), ("Respect", 149)]
labels = [f"{title} [{format_duration(seconds)}]" for title, seconds in tracks]
print(labels)
```

```text
['Imagine [3:03]', 'Yesterday [2:05]', 'Respect [2:29]']
```

> `demo04 · comprehension_features`

---

# Zip Function

- `zip` pairs each track title with its duration :
  - It stops when the shortest input runs out by default
  - `strict=True` raises `ValueError` if their lengths differ

```python
titles = ["Imagine", "Yesterday", "Respect"]
lengths = [183, 125, 149]
pairs = list(zip(titles, lengths))
print(pairs)
checked = list(zip(titles, lengths, strict=True))
print(checked)
```

```text
[('Imagine', 183), ('Yesterday', 125), ('Respect', 149)]
[('Imagine', 183), ('Yesterday', 125), ('Respect', 149)]
```

> `demo05 · zip_function`

---

# Dictionary Construction with zip

- `dict` builds a lookup from pairs of keys and values :

```python
titles = ["Imagine", "Yesterday", "Respect"]
lengths = [183, 125, 149]
durations = dict(zip(titles, lengths))
print(durations)
```

```text
{'Imagine': 183, 'Yesterday': 125, 'Respect': 149}
```

> `demo06 · dictionary_with_zip`

---

# Dictionary Comprehensions

- `key: value` computes each dictionary entry
- An optional `if` keeps only matching tracks :

```python
durations = {"Imagine": 183, "Yesterday": 125, "Respect": 149}
short_tracks = {title: seconds for title, seconds in durations.items() if seconds < 150}
print(short_tracks)  # {'Yesterday': 125, 'Respect': 149}
minutes = {title: round(seconds / 60, 2) for title, seconds in durations.items()}
print(minutes)  # {'Imagine': 3.05, 'Yesterday': 2.08, 'Respect': 2.48}
```

> `demo07 · dictionary_comprehension`

---

# Dictionary from Keys

- `dict.fromkeys` gives each key the same value
- A comprehension gives each playlist its own mutable track list :

```python
albums = ["Night drive", "Warm-up"]
play_counts = dict.fromkeys(albums, 0)
print(play_counts)
playlists: dict[str, list[str]] = {name: [] for name in albums}
playlists["Night drive"].append("Imagine")
print(playlists)
```

```text
{'Night drive': 0, 'Warm-up': 0}
{'Night drive': ['Imagine'], 'Warm-up': []}
```

- `dict.fromkeys(albums, [])` would make every album share one list

> `demo08 · dictionary_from_keys`

---

# Set Comprehensions

- A set comprehension keeps each result once :
  - Titles that differ only in spacing and case can become one value

```python
titles = [" Imagine ", "Yesterday", "imagine", "Respect "]
unique = {title.strip().lower() for title in titles}
print(sorted(unique))  # ['imagine', 'respect', 'yesterday']

files = ["cover.jpg", "notes.txt", "cover.jpg", "stage.jpg"]
unique_photos = {name for name in files if name.endswith(".jpg")}
print(sorted(unique_photos))  # ['cover.jpg', 'stage.jpg']
```

- Sets have no display order; `sorted` makes printed output predictable

> `demo09 · set_comprehensions`

---

# Generator Expressions

- A generator expression supplies values without building a new list :
  - These photo sizes are checked and totalled as they are consumed

```python
sizes_mb = [12, 8, 25]
print(sum(size for size in sizes_mb if size >= 10))  # 37
print(any(size > 20 for size in sizes_mb))  # True
print(all(size <= 20 for size in sizes_mb))  # False
print(any([]), all([]))  # False True
```

- `any` and `all` stop as soon as the answer is known
- As the only argument of a call, the expression needs no extra parentheses
- Generator functions and `yield` belong to Advanced Python

> `demo10 · generator_expressions`

---

# Built-ins that Take a Function

- A `key` function selects the value used for ordering :
  - Track titles can be sorted alphabetically or by title length

```python
titles = ["Bohemian Rhapsody", "Yesterday", "Imagine"]
print(sorted(titles))  # ['Bohemian Rhapsody', 'Imagine', 'Yesterday']
print(sorted(titles, key=len))  # ['Imagine', 'Yesterday', 'Bohemian Rhapsody']
print(min(titles, key=len), max(titles, key=len))  # Imagine Bohemian Rhapsody
```

- `sorted` returns a new list; `list.sort` changes a list in place
- `min` and `max` also accept a key function

> `demo11 · sorted_by_key`

---

# Recognising map and filter

- `map` transforms each item; `filter` keeps matching items
- Both return iterators; `list` collects the results :

```python
def clean_filename(name: str) -> str:
    return name.strip().lower()


def is_photo(name: str) -> bool:
    return name.endswith(".jpg")


files = ["  COVER.JPG ", "STAGE.JPG", "NOTES.TXT"]
cleaned = list(map(clean_filename, files))
photos = list(filter(is_photo, cleaned))
print(photos)  # ['cover.jpg', 'stage.jpg']
print([name for name in cleaned if is_photo(name)])
```

- These forms also occur in existing code

> `demo12 · map_and_filter_functions`

---

# Comprehensions and map

- A comprehension can express the same filename transformation as `map` :

```python
files = ["COVER.JPG", "STAGE.JPG"]
mapped = list(map(lambda name: name.lower(), files))
print(mapped)  # ['cover.jpg', 'stage.jpg']
comprehended = [name.lower() for name in files]
print(comprehended)  # ['cover.jpg', 'stage.jpg']
```

- Choose the form that makes the operation clear

> `demo13 · syntactic_sugar`

---

# Recognising reduce

- `functools.reduce` combines items into one running result :
  - Each step adds the next track's duration to the accumulated duration

```python
from functools import reduce

lengths = [183, 125, 149]
total = reduce(lambda running, seconds: running + seconds, lengths)
print(total)  # 457
print(sum(lengths))  # 457
```

- Prefer `sum` when it names the operation directly

> `demo14 · reduce_and_lambda`

---

# Summary : Comprehensions

- Build lists, dictionaries and sets with comprehensions.
- Use an optional `if` to filter the input.
- Keep nested comprehensions simple.
- Feed generator expressions into `sum`, `any` and `all`.
- Pass a `key` function to `sorted`, `min` and `max`.
- Recognise `map`, `filter` and `reduce` when reading other code.

> `exercise07 · Comprehensions`
