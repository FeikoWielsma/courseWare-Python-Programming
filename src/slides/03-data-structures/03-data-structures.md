---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Data Structures
---

# Sequences

- Most basic data structure in Python is the sequence :
  - Each element of a sequence is assigned a number, its position or index
  - First index is zero, the second index is one, and so forth
  - Python distinguishes sequences on the basis of mutability
- Immutable sequences :
  - Contain objects and content cannot change once created :
    - Objects may reference other objects, and those other objects may change
  - Examples are strings, tuples and bytes, which the IO module covers
- Mutable sequences :
  - Contain objects and content can be changed once created
  - The list is the example used everywhere
- Operations that work on all sequences types :
  - Indexing, slicing, multiplying, and checking for membership
- Python has built-in functions for :
  - Finding the length of a sequence and its largest and smallest elements


---

# Lists

- Lists are mutable sequences :
  - List contains items separated by commas and enclosed within square brackets `[]`
  - The items of one list can be of different data types
- Values are accessed using the index or slice operator `[ ]` and `[ : ]` :
  - Indexes start at 0, then upwards and with end-1
  - Lists can be sliced, concatenated and so on
- Lists respond to the `+` and * operators much like strings :
  - Meaning is concatenation and repetition
  - Except that result is a new list, not a string
- Lists respond to all sequence operations usable on strings :

```python
list1 = ["abcd", 786, 2.23, "john", True]
print(list1)  # Prints complete list
print(list1[0])  # Prints first element of the list
print(list1[1:3])  # Prints the 2nd and 3rd elements
print(list1 * 2)  # Prints list two times
print(list1[::-1])  # Prints complete list in reverse order
```

> `demo01 · lists`

---

# Accessing Lists

- Use index operator `[]` to access list at specific position :
  - Counting runs from `0` at the front and from `-1` at the back
  - A slice runs up to but not including its second index

<svg viewBox="0 0 960 200" width="100%" style="width:100%;height:auto;display:block;margin:6px 0 4px" role="img" aria-label="A five element list with its positive indexes, negative indexes and the extent of the slice one to three">
<g fill="currentColor" font-size="17" opacity="0.75">
<text x="20" y="42">index</text>
<text x="20" y="88">value</text>
<text x="20" y="140">from the end</text>
</g>
<g fill="none" stroke="currentColor" stroke-width="2">
<rect x="150" y="56" width="130" height="48"/>
<rect x="280" y="56" width="130" height="48"/>
<rect x="410" y="56" width="130" height="48"/>
<rect x="540" y="56" width="130" height="48"/>
<rect x="670" y="56" width="130" height="48"/>
</g>
<g fill="currentColor" font-size="21" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" text-anchor="middle">
<text x="215" y="88">10</text>
<text x="345" y="88">20</text>
<text x="475" y="88">30</text>
<text x="605" y="88">40</text>
<text x="735" y="88">50</text>
</g>
<g fill="currentColor" font-size="19" text-anchor="middle">
<text x="215" y="42">0</text>
<text x="345" y="42">1</text>
<text x="475" y="42">2</text>
<text x="605" y="42">3</text>
<text x="735" y="42">4</text>
</g>
<g fill="currentColor" font-size="19" text-anchor="middle" opacity="0.75">
<text x="215" y="140">-5</text>
<text x="345" y="140">-4</text>
<text x="475" y="140">-3</text>
<text x="605" y="140">-2</text>
<text x="735" y="140">-1</text>
</g>
<g fill="none" stroke="currentColor" stroke-width="2">
<path d="M 280 158 L 280 176 L 540 176 L 540 158"/>
</g>
<g fill="currentColor" font-size="19" text-anchor="middle">
<text x="410" y="196">li[1:3] gives [20, 30]</text>
</g>
</svg>


```python
li = ["physics", "chemistry", "biology", "computer science"]
print("Value available at index 2 : ")
print(li[2])
li[2] = "mathematics"
print("New value available at index 2 : ")
print(li[2])
```

- Elements can be added to a list with `append()` :

```python
list2 = [1, 2, 3]
list2.append(4)
list2.append(5)
print(list2)  # [1, 2, 3, 4, 5]
```

- Elements can be added to a list at a position with `insert(index, item)` :

```python
list2.insert(0, 99)
print(list2)  # [99, 1, 2, 3, 4, 5]
```

---

# Delete List Elements

- Remove a list element with `del` or `remove()`
- Use `del` statement if you know index of element to remove :

```python
li = ["physics", "chemistry", "biology", "computer science"]
del li[2]
print("After deleting value at index 2 : ")
print(li)  # ['physics', 'chemistry', 'computer science']
```

- Use `remove()` if want to remove element by value :

```python
li.remove("physics")
print("After deleting value 'physics' ")
print(li)  # ['chemistry', 'computer science']
```

- List itself can also be removed with `del` :

```python
del list1
list1.append(100)  # gives NameError, name list1 not defined anymore
```

> `demo02 · updatinglists`


---

# Multidimensional Lists

- A list can hold other lists, which gives a grid of rows and columns :

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
]
print(grid[0])  # [1, 2, 3], the first row
print(grid[1][2])  # 6, row 1, column 2
print(len(grid), len(grid[0]))  # 2 3, rows and columns
```

- Each row is an ordinary list, so it can be changed in place or added to :

```python
grid[0][0] = 10
print(grid)  # [[10, 2, 3], [4, 5, 6]]
grid.append([7, 8, 9])
print(grid)  # [[10, 2, 3], [4, 5, 6], [7, 8, 9]]
```

- Repeating a row with `*` repeats one list object, not a copy of it :

```python
shared = [[0] * 3] * 2
shared[0][0] = 1
print(shared)  # [[1, 0, 0], [1, 0, 0]], both rows are one list
```

> `demo03 · multidimensionallists`

---

# List Operations

| Python Expression | Results | Description |
|---|---|---|
| `len([1,2,3])` | `3` | Length |
| `[1,2,3]+[4,5,6]` | `[1,2,3,4,5,6]` | Concatenation |
| `['go']*3` | `['go','go','go']` | Repetition |
| `3 in [1,2,3]` | `True` | Membership |
| `for x in [1,2,3]: print(x)` | `1 2 3` | Iteration |

- A list also works as a stack : `append` puts an item on top, `pop` takes the top one off

```python
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)  # [3, 4, 5, 6, 7]
print(stack.pop())  # 7
print(stack)  # [3, 4, 5, 6]
```

> `demo04 · listsasstacks`

---

# List Functions and Methods

| Function | Description |
|---|---|
| `len(list)` | Gives the total length of the list |
| `max(list)` / `min(list)` | Returns item from the list with max or min value |
| `list(seq)` | Converts a tuple into list |
| `list.append(obj)` | Appends object obj to list |
| `list.count(obj)` | Returns count of how many times obj occurs in list |
| `list.extend(seq)` | Appends the contents of seq to list |
| `list.index(obj)` | Returns the lowest index in list that obj appears |
| `list.insert(index, obj)` | Inserts object obj into list at offset index |
| `list.pop(index=-1)` | Removes and returns the item at an index; default is last |
| `list.remove(obj)` | Removes object obj from list |
| `list.reverse()` | Reverses objects of list in place |
| `list.sort(key=None, reverse=False)` | Sorts in place; options are keyword-only |

> `demo05 · listmethods`

---

# Tuples

- Tuple is an immutable sequence of Python objects :
  - Consist of a number of values separated by commas
  - Tuples are sequences, just like lists, but cannot be changed once created
- Main differences between lists and tuples :
  - Lists are enclosed in brackets `[ ]` and their contents and size can be changed
  - Tuples are enclosed in parentheses `( )` and cannot be updated
- Create tuple by assigning comma-separated values to variable :
  - Best practice is to put these comma-separated values between parentheses
  - An empty tuple is written as two parentheses containing nothing
  - For a tuple containing a single value include a comma, otherwise it is a single value

```python
tup1 = ("physics", "chemistry", "biology", "computer science")
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"  # not recommended
tup4 = ()                  # empty tuple
tup5 = (50,)               # single element tuple
```

> `demo06 · tuples`


---

# Accessing Tuples

- All of the general sequence operations can be applied on tuples :
  - Use square brackets for slicing along with index to obtain value, indices start at 0
  - Use the + and * operators for concatenation and repetition

```python
tup = (1, 2, 3, 4, 5, 6, 7)
print(tup[0])  # 1
print(tup[1:5])  # (2, 3, 4, 5)
print(len(tup))  # 7
```

- Tuples are immutable and can be thought of as read-only lists :
  - Cannot update them or change values of tuple elements

```python
tup[2] = 1000  # TypeError: 'tuple' object does not support item assignment
```

- Portions of existing tuples can be used to create new tuples :

```python
tup1 = (12, 34.56)
tup2 = ("abc", "xyz")
tup3 = tup1 + tup2
print(tup3)  # (12, 34.56, 'abc', 'xyz')
```
- Tuples can have other tuples or lists as elements

> `demo07 · tupleaccess`

---

# Delete Tuple Elements

- Removing individual tuple elements is not possible :
  - Another tuple with undesired elements discarded must be created
- Entire tuple can be removed with `del` statement :

```python
tup = ("physics", "chemistry", "biology", "computer science")
print(tup)  # ('physics', 'chemistry', 'biology', 'computer science')
del tup
print("After deleting tup : ")
print(tup)
```

- Result after deleting tup :

```text
Traceback (most recent call last):
  File "C:\course-work\tuples.py", line 5, in <module>
    print(tup)
          ^^^
NameError: name 'tup' is not defined
```

- After `del tup`, the name is no longer bound; other references may keep the tuple alive

---

# Usage of Tuples

- Tuples have many uses :
  - Coordinate pairs, records from a database
- Any set of comma-separated objects default to tuples :
  - Even without parentheses around them
- Tuples can be dictionary keys and set members if every item is hashable
- Tuples can make your code safer :
  - Allows you to "write-protect" data that does not need to be changed
- A tuple can have lists as items :
  - The items in the lists are mutable however
- Tuple can be destructured and contents assigned to variables :

```python
t = ("Albert", "Einstein")
print(t)  # ('Albert', 'Einstein')
v, s = t
print(v)  # 'Albert'
print(s)  # 'Einstein'
```

- A `for` loop unpacks each item the same way, and the unpacking can nest :

```python
rows = [(1,), (2,)]
for (number,) in rows:
    print(number)  # 1, then 2

records = [(1, ("Albert", "Einstein"))]
for number, (first, last) in records:
    print(number, first, last)  # 1 Albert Einstein
```

> `demo08 · destructurewithtuples`


---

# Tuple Functions

- Only functions and methods that do not modify tuple available

| Function | Description |
|---|---|
| `len(tuple)` | Gives the total length of the tuple |
| `max(tuple)` | Returns item from the tuple with max value |
| `min(tuple)` | Returns item from the tuple with min value |
| `tuple(seq)` | Converts a list into tuple |
| `tup.index(i)` | Index of the first occurrence of i in tup |
| `tup.count(i)` | Total number of occurrences of i in tup |

---

# Sets

- A set is an unordered collection with no duplicates :
  - Created with curly braces `{ }` or with the `set()` constructor
  - `set()` takes one iterable, such as a list, and keeps each value once

```python
s1 = {1, 1, 2, 2}
print(s1)  # {1, 2}
numbers = [3, 3, 4, 4]
s2 = set(numbers)
print(s2)  # {3, 4}
s2.add(5)
print(s2)  # {3, 4, 5}
print(4 in s2)  # True, a fast membership test
```

- An empty set is written `set()`, because `{}` is an empty dictionary
- A `frozenset` is a set that cannot be changed after it is created :

```python
frozen = frozenset(numbers)
print(frozen)  # frozenset({3, 4})
```

> `demo09 · setsandfrozensets`

---

# Set Operations

- Sets support the operations of set theory, each written as an operator :

```python
physics = {"Einstein", "Bohr", "Curie", "Fermi"}
chemistry = {"Curie", "Rutherford", "Pauling"}
print("Curie" in chemistry)  # True
print(sorted(physics | chemistry))  # union, in either set
print(sorted(physics & chemistry))  # intersection, in both
print(sorted(physics - chemistry))  # difference, in physics only
print(sorted(physics ^ chemistry))  # in one of the two, not both
```

```text
True
['Bohr', 'Curie', 'Einstein', 'Fermi', 'Pauling', 'Rutherford']
['Curie']
['Bohr', 'Einstein', 'Fermi']
['Bohr', 'Einstein', 'Fermi', 'Pauling', 'Rutherford']
```

- A set has no order, so `sorted()` turns it into a list to print it predictably
- Each operator has a method form that accepts any iterable :
  - `union()`, `intersection()`, `difference()` and `symmetric_difference()`

---

# Dictionaries

- Dictionaries consist of pairs of keys and values :
  - Keys must be hashable; strings and numbers are common choices
  - Values can be any arbitrary Python object
- Dictionaries are hash tables :
  - Looking up a key is fast, however large the dictionary
  - Consist of key-value pairs separated by commas
- Dictionaries are enclosed by curly braces `{ }` :

```python
dict1 = {"Albert": 2341, "Robert": 9102, "Enrico": 3258}
print(dict1)  # {'Albert': 2341, 'Robert': 9102, 'Enrico': 3258}
```

- Values can be assigned and accessed using square brackets `[]` :

```python
dict1["Werner"] = 3490
dict1[2] = "Data"
print(dict1)  # {'Albert': 2341, 'Robert': 9102, 'Enrico': 3258, 'Werner': 3490, 2: 'Data'}
```

- Dictionaries remember insertion order :
  - Keys come out in the order in which they were first added

---

# Accessing Values in Dictionary

- Keys are unique within a dictionary while values may be the same :
  - Values of a dictionary can be of any type
  - Keys must be hashable; a tuple qualifies only if all its items are hashable
- Use square brackets along with the key to obtain its value :

```python
print(dict1["Robert"])  # 9102
print(dict1[2])  # Data
```

- Dictionary can be updated by modifying an existing entry :

```python
dict1["Enrico"] = 9999
print(dict1["Enrico"])  # 9999
```

- Dictionary entry can be deleted :

```python
del dict1["Albert"]
print(dict1["Albert"])  # KeyError
```

- Entire contents of dictionary is cleared with `clear()` :
  - Entire dictionary can be deleted in single operation with del

> `demo10 · dictionaries`

---

# Properties of Dictionary Keys

- Keys must be hashable :
  - Their hash stays stable, and equal keys must have equal hashes
  - Strings and numbers qualify; lists and dictionaries do not
  - A tuple is hashable only when every item is hashable
- Values can be any object; assigning an equal key replaces its value

```python
extensions = {("Albert", "Einstein"): 2341}
print(extensions[("Albert", "Einstein")])  # 2341
```

- An immutable tuple can contain an unhashable list :

```python
hash(("Albert", []))  # TypeError: unhashable type: 'list'
```

---

# Annotating Collections

- Each built-in collection is annotated with the type of what it holds :

```python
scores: list[int] = [10, 20, 30]
names: set[str] = {"Alice", "Bob"}
extensions: dict[str, int] = {"Albert": 2341, "Robert": 9102}
```

- A dictionary takes two types, the key first and then the value
- A tuple is annotated position by position, because its length is fixed :

```python
point: tuple[int, int] = (3, 4)
row: tuple[str, int, float] = ("Audi", 2019, 52643.0)
```

- An ellipsis means any number of one type :

```python
readings: tuple[float, ...] = (1.5, 2.5, 3.5)
```

- Annotate where the collection is homogeneous, which most are :
  - A deliberately mixed list such as `['abcd', 786, 2.23]` has no single
    element type, and is better left bare than annotated `list[object]`

---

# Dictionary Functions and Methods

| Function | Description |
|---|---|
| `len(dict)` | Gives the total length, or nr. of items, in the dictionary |
| `str(dict)` | Produces a printable string representation of a dictionary |
| `fromkeys()` | Create new dictionary with keys from seq, values set to value |
| `dict.clear()` | Removes all elements of dictionary dict |
| `dict.copy()` | Returns a shallow copy of dictionary dict |
| `dict.get(key)` | For key key, returns value or default if key not in dictionary |
| `dict.popitem()` | Removes and returns the (key, value) pair added last |
| `dict.items()` | Returns a view of dict's (key, value) tuple pairs |
| `dict.keys()` | Returns a view of dictionary dict's keys |
| `dict.update(dict2)` | Adds dictionary dict2's key-values pairs to dict |
| `dict.values()` | Returns a view of dictionary dict's values |

> `demo11 · dictionarymethods`

---

# Summary : Data Structures

- Sequences are most basic data structure :
  - Each element of a sequence is assigned a number, its position or index
  - First index is zero, the second index is one, and so forth
- Lists are mutable sequences :
  - Contain items separated by commas and enclosed within square brackets `[]`
  - Items can be of different data types, and lists can hold other lists
- Tuples are immutable sequences :
  - Enclosed in parenthesis ( ) instead of brackets
  - Consist of a number of values separated by commas
- Sets are unordered collections with no duplicates :
  - Fast membership tests, and union, intersection and difference
  - Set is mutable and `frozenset` is immutable
- Dictionaries map keys to values, in insertion order :
  - Pairs of keys and values, separated by a comma and a colon
  - Enclosed by curly braces `{ }`, values accessed with square brackets `[]`

> `exercise03 · Data Structures`
