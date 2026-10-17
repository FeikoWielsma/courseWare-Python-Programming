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
filenames: list[str] = ["sales", "stock", "prices"]
csv_files = [f"{name}.csv" for name in filenames]
print(csv_files)  # ['sales.csv', 'stock.csv', 'prices.csv']
```



> `demo01 · list_comprehensions`

---

# Syntax List Comprehensions

- A comprehension has the form `[expression for name in source]`.
- `source` supplies the items; `name` receives one item at a time.
- `expression` computes the value added to the new list.

```python
filenames: list[str] = ["sales", "stock", "prices"]
csv_files = []
for name in filenames:
    csv_files.append(f"{name}.csv")
print(csv_files)  # ['sales.csv', 'stock.csv', 'prices.csv']

csv_files = [f"{name}.csv" for name in filenames]
print(csv_files)  # ['sales.csv', 'stock.csv', 'prices.csv']
```

- Both forms create a new list and leave `filenames` unchanged.

---

# Filtered List Comprehension

- An optional `if` keeps only the items that satisfy its condition.
- These two forms produce the same list :

```python
filenames = ["sales.csv", "notes.txt", "stock.csv"]
csv_files = []
for name in filenames:
    if name.endswith(".csv"):
        csv_files.append(name)
print(csv_files)  # ['sales.csv', 'stock.csv']

csv_files = [name for name in filenames if name.endswith(".csv")]
print(csv_files)  # ['sales.csv', 'stock.csv']
```



> `demo02 · comprehension_with_predicate`

---

# Nested List Comprehensions

- A nested comprehension builds a list of lists, preserving the row structure.

```python
readings = [[18.2, 19.6], [20.1, 21.8]]
rounded = [[round(value) for value in row] for row in readings]
print(rounded)  # [[18, 20], [20, 22]]
```

- Each row holds the temperature readings from one location.
- The inner comprehension rounds the readings in one row.
- The outer comprehension repeats that operation for every row.
- Use an ordinary loop when the nesting needs more explanation.

> `demo03 · nested_comprehensions`

---

# Flattening a List of Lists

- Two `for` clauses collect all the readings into one list.
- Their order is the same as in the equivalent nested loops.

```python
readings = [[18.2, 19.6], [20.1, 21.8]]
flat = []
for row in readings:
    for value in row:
        flat.append(value)
print(flat)  # [18.2, 19.6, 20.1, 21.8]

flat = [value for row in readings for value in row]
print(flat)  # [18.2, 19.6, 20.1, 21.8]
```

- The result can be used to calculate a minimum or maximum across all locations.

---

# Comprehension Features

- Unpack each tuple into names inside the `for` part.
- The expression can call a function.

```python
def line_total(price: float, quantity: int) -> float:
    return round(price * quantity, 2)


items = [(12.50, 2), (4.00, 3), (7.25, 1)]
totals = [line_total(price, quantity) for price, quantity in items]
print(totals)  # [25.0, 12.0, 7.25]
```



> `demo04 · comprehension_features`

---

# Zip Function

- `zip` pairs items from its input iterables.
- By default it stops when the shortest input runs out.
- `strict=True` raises a `ValueError` when the inputs differ in length, instead of stopping early :

```python
products = ["tea", "coffee", "cocoa"]
quantities = [12, 8, 5]
pairs = list(zip(products, quantities))
print(pairs)  # [('tea', 12), ('coffee', 8), ('cocoa', 5)]
checked = list(zip(products, quantities, strict=True))
print(checked)  # [('tea', 12), ('coffee', 8), ('cocoa', 5)]
```



> `demo05 · zip_function`

---

# Dictionary Construction with zip

- Pass pairs of keys and values to `dict` to build a dictionary.

```python
products = ["tea", "coffee", "cocoa"]
quantities = [12, 8, 5]
stock = dict(zip(products, quantities))
print(stock)  # {'tea': 12, 'coffee': 8, 'cocoa': 5}
```



> `demo06 · dictionary_with_zip`

---

# Dictionary Comprehensions

- Use `key: value` to compute each dictionary entry.
- Add an `if` to keep only some entries.

```python
stock = {"tea": 12, "coffee": 0, "cocoa": 5}
available = {name: count for name, count in stock.items() if count > 0}
print(available)  # {'tea': 12, 'cocoa': 5}
prices = {"tea": 2.0, "coffee": 4.0}
with_tax = {name: round(price * 1.21, 2) for name, price in prices.items()}
print(with_tax)  # {'tea': 2.42, 'coffee': 4.84}
```



> `demo07 · dictionary_comprehension`

---

# Dictionary from Keys

- `dict.fromkeys` gives every key the same value.
- Use a comprehension when each key needs its own mutable value.

```python
sites = ["AMS", "RTM"]
counts = dict.fromkeys(sites, 0)
print(counts)  # {'AMS': 0, 'RTM': 0}
groups: dict[str, list[str]] = {site: [] for site in sites}
groups["AMS"].append("web01")
print(groups)  # {'AMS': ['web01'], 'RTM': []}
```

- Avoid `dict.fromkeys(keys, [])` : every key would share the same list.

> `demo08 · dictionary_from_keys`

---

# Set Comprehensions

- A set comprehension uses braces around an expression.
- Duplicate results disappear; sets have no defined display order.

```python
names = [" Sales ", "Stock", "sales", "Prices "]
unique = {name.strip().lower() for name in names}
print(sorted(unique))  # ['prices', 'sales', 'stock']

csv_files = ["sales.csv", "notes.txt", "sales.csv", "stock.csv"]
unique_csv = {name for name in csv_files if name.endswith(".csv")}
print(sorted(unique_csv))  # ['sales.csv', 'stock.csv']
```



> `demo09 · set_comprehensions`

---

# Generator Expressions

- A generator expression supplies values as they are needed, without building a list.
- As the only argument of a call, it needs no extra parentheses.

```python
sizes_mb = [120, 80, 250]
print(sum(size for size in sizes_mb if size >= 100))  # 370
print(any(size > 200 for size in sizes_mb))  # True
print(all(size <= 200 for size in sizes_mb))  # False
print(any([]), all([]))  # False True
```

- `any` and `all` stop as soon as the answer is known.
- Generator functions, `yield` and generators in depth belong to Advanced Python.

> `demo10 · generator_expressions`

---

# Built-ins that Take a Function

- `sorted` returns a new list; `list.sort` changes a list in place.
- A `key` function computes the comparison value for each item.
- `min` and `max` accept a `key` function too.

```python
words = ["ticket", "to", "mars", "one", "way"]
print(sorted(words))  # ['mars', 'one', 'ticket', 'to', 'way']
print(sorted(words, key=len))  # ['to', 'one', 'way', 'mars', 'ticket']
print(min(words, key=len), max(words, key=len))  # to ticket
```



> `demo11 · sorted_by_key`

---

# Recognising map and filter

- You will encounter these function-based forms in other people's code.
- `map` applies a function; `filter` keeps items for which a function returns true.
- Both return iterators; `list` collects their results.

```python
def square(x: int) -> int:
    return x * x


def even(x: int) -> bool:
    return x % 2 == 0


print(list(map(square, range(1, 6))))  # [1, 4, 9, 16, 25]
print(list(filter(even, range(1, 6))))  # [2, 4]
print([square(x) for x in range(1, 6) if even(x)])  # [4, 16]
```



> `demo12 · map_and_filter_functions`

---

# Comprehensions and map

- A comprehension often reads more directly than a combination of `map` and `filter`.
- Recognise both forms; choose the one that makes the operation clear.

```python
mapped = list(map(lambda x: 2 * x + 1, [10, 20, 30]))
print(mapped)  # [21, 41, 61]
comprehended = [2 * x + 1 for x in [10, 20, 30]]
print(comprehended)  # [21, 41, 61]
```



> `demo13 · syntactic_sugar`

---

# Recognising reduce

- `functools.reduce` combines items into one result.
- Here each step multiplies the running result by the next number.

```python
from functools import reduce

product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)  # 24

result = 1
for number in [1, 2, 3, 4]:
    result *= number
print(result)  # 24
```

- Prefer a named built-in such as `sum` when it expresses the operation directly.

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
