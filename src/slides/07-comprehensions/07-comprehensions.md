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
numbers: list[int] = [1, 2, 3, 4, 5]
doubled = [number * 2 for number in numbers]
print(doubled)  # [2, 4, 6, 8, 10]
labels = [str(number) for number in numbers]
print(labels)  # ['1', '2', '3', '4', '5']
```



> `demo01 · list_comprehensions`

---

# Syntax List Comprehensions

- Syntax of a list comprehension may involve :
  - `for` loop, an `in` operation and an `if` statement
- Python's notation is `[ expression for name in list ]` :

<svg viewBox="0 0 960 210" width="100%" style="width:100%;height:auto;display:block;margin:6px 0 4px" role="img" aria-label="The three parts of a list comprehension: the expression, the name bound to each item and the source sequence">
<g fill="currentColor" font-size="23" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
<text x="194" y="46" textLength="14" lengthAdjust="spacingAndGlyphs">[</text>
<text x="214" y="46" textLength="84" lengthAdjust="spacingAndGlyphs">elem*2</text>
<text x="312" y="46" textLength="42" lengthAdjust="spacingAndGlyphs">for</text>
<text x="368" y="46" textLength="56" lengthAdjust="spacingAndGlyphs">elem</text>
<text x="438" y="46" textLength="28" lengthAdjust="spacingAndGlyphs">in</text>
<text x="480" y="46" textLength="28" lengthAdjust="spacingAndGlyphs">li</text>
<text x="514" y="46" textLength="14" lengthAdjust="spacingAndGlyphs">]</text>
</g>
<g fill="none" stroke="currentColor" stroke-width="2">
<rect x="210" y="24" width="92" height="30" rx="3"/>
<rect x="364" y="24" width="64" height="30" rx="3"/>
<rect x="476" y="24" width="34" height="30" rx="3"/>
</g>
<g fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.7">
<path d="M 494 54 L 494 100 L 554 100"/>
<path d="M 396 54 L 396 140 L 554 140"/>
<path d="M 256 54 L 256 180 L 554 180"/>
</g>
<g fill="currentColor" font-size="19">
<text x="566" y="106">the source sequence</text>
<text x="566" y="146">the name bound to each item</text>
<text x="566" y="186">the expression, evaluated per item</text>
</g>
</svg>

- Reads as the loop that would otherwise be written out in full :

```python
li = [3, 6, 2, 7]
li_new = [elem * 2 for elem in li]  # [6, 12, 4, 14]
```

- `if` statement acts as a filter and is optional :

```python
grades = [12, 0, 18]
print([x - 10 for x in grades if x > 0])  # [2, 8]
```

---

# Filtered List Comprehension

- An optional `if` keeps only the items that satisfy its condition.
- These two forms produce the same list :

```python
numbers = [1, 2, 3, 4, 5, 6]
labels = []
for number in numbers:
    if number % 2 == 0:
        labels.append(str(number))
print(labels)  # ['2', '4', '6']

labels = [str(number) for number in numbers if number % 2 == 0]
print(labels)  # ['2', '4', '6']
```



> `demo02 · comprehension_with_predicate`

---

# Nested List Comprehensions

- The inner comprehension creates one row; the outer one creates the rows.
- Keep nesting short enough to read at a glance.

```python
list_a = ["A", "B"]
list_b = ["C", "D"]
rows = [[x + y for x in list_a] for y in list_b]
print(rows)  # [['AC', 'BC'], ['AD', 'BD']]
```

- A comprehension can also have two `for` clauses, and the second runs for each item of the first :

```python
words = ["one", "two"]
letters = [letter for word in words for letter in word]
print(letters)  # ['o', 'n', 'e', 't', 'w', 'o']
```



> `demo03 · nested_comprehensions`

---

# Comprehension Features

- Unpack each tuple into names inside the `for` part.
- The expression can call a function.

```python
def subtract(a: int, b: int) -> int:
    return a - b


pairs = [(6, 3), (1, 7), (5, 5)]
differences = [subtract(y, x) for x, y in pairs]
print(differences)  # [-3, 6, 0]
```



> `demo04 · comprehension_features`

---

# Zip Function

- `zip` pairs items from its input iterables.
- By default it stops when the shortest input runs out.
- `strict=True` raises a `ValueError` when the inputs differ in length, instead of stopping early :

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]
pairs = list(zip(keys, values))
print(pairs)  # [('a', 1), ('b', 2), ('c', 3)]
checked = list(zip(keys, values, strict=True))  # the lengths match, so no error
print(checked)  # [('a', 1), ('b', 2), ('c', 3)]
```



> `demo05 · zip_function`

---

# Dictionary Construction with zip

- Pass pairs of keys and values to `dict` to build a dictionary.

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]
counts = dict(zip(keys, values))
print(counts)  # {'a': 1, 'b': 2, 'c': 3}
```



> `demo06 · dictionary_with_zip`

---

# Dictionary Comprehensions

- Use `key: value` to compute each dictionary entry.
- Add an `if` to keep only some entries.

```python
squares = {number: number**2 for number in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
counts = {"a": 2, "b": 0, "c": 3}
positive = {key.upper(): value for key, value in counts.items() if value > 0}
print(positive)  # {'A': 2, 'C': 3}
```



> `demo07 · dictionary_comprehension`

---

# Dictionary from Keys

- `dict.fromkeys` gives every key the same value.
- Use a comprehension when each key needs its own mutable value.

```python
counts = dict.fromkeys(["a", "b", "c"], 0)
print(counts)  # {'a': 0, 'b': 0, 'c': 0}
groups: dict[str, list[int]] = {key: [] for key in ["a", "b", "c"]}
groups["a"].append(1)
print(groups)  # {'a': [1], 'b': [], 'c': []}
```

- Avoid `dict.fromkeys(keys, [])` : every key would share the same list.

> `demo08 · dictionary_from_keys`

---

# Set Comprehensions

- A set comprehension uses braces around an expression.
- Duplicate results disappear; sets have no defined display order.

```python
numbers = [1, 2, 2, 3, 4]
squares = {number**2 for number in numbers}
print(sorted(squares))  # [1, 4, 9, 16]
even_squares = {number**2 for number in numbers if number % 2 == 0}
print(sorted(even_squares))  # [4, 16]
```



> `demo09 · set_comprehensions`

---

# Generator Expressions

- A generator expression supplies values as they are needed, without building a list.
- As the only argument of a call, it needs no extra parentheses.

```python
numbers = [4, 8, 15, 16, 23, 42]
print(sum(n * n for n in numbers))  # 2854
print(any(n > 40 for n in numbers))  # True
print(all(n % 2 == 0 for n in numbers))  # False
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
