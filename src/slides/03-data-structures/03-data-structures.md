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

- A playlist stores tracks in a chosen order :
  - Lists are mutable sequences
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
list1 = ["Thriller", "Imagine", "Yesterday", "Respect", "Hey Jude"]
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
<text x="410" y="196">playlist[1:3] gives [20, 30]</text>
</g>
</svg>


```python
playlist = ["Thriller", "Imagine", "Yesterday", "Hey Jude"]
print("Value available at index 2 : ")
print(playlist[2])
playlist[2] = "Jolene"
print("New value available at index 2 : ")
print(playlist[2])
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
playlist = ["Thriller", "Imagine", "Yesterday", "Hey Jude"]
del playlist[2]
print("After deleting value at index 2 : ")
print(playlist)  # ['Thriller', 'Imagine', 'Hey Jude']
```

- Use `remove()` if want to remove element by value :

```python
playlist.remove("Thriller")
print("After deleting value 'Thriller' ")
print(playlist)  # ['Imagine', 'Hey Jude']
```

- List itself can also be removed with `del` :

```python
del list1
list1.append(100)  # gives NameError, name list1 not defined anymore
```

> `demo02 · updatinglists`


---

# Multidimensional Lists

- A tiny image can store brightness values in rows and columns :
  - Each row is a list inside the outer list

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

- A music player can keep a stack of visited views :
  - `append` records the latest view; `pop` removes it when going back

```python
history = ["Library", "Album", "Track"]
history.append("Queue")
history.append("Artist")
print(history)  # ['Library', 'Album', 'Track', 'Queue', 'Artist']
print(history.pop())  # Artist
print(history)  # ['Library', 'Album', 'Track', 'Queue']
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

- A tuple stores a fixed sequence of values :
  - Each position can have a particular role, such as title and duration
  - Photo dimensions similarly pair width and height

```python
track = ("Imagine", 183)
dimensions = (1920, 1080)
titles = "Imagine", "Yesterday"  # The comma creates a tuple.
empty = ()
single = ("Imagine",)  # A one-item tuple needs the comma.
```

- Items cannot be replaced, inserted or removed from an existing tuple
- Commas create the tuple; parentheses usually make its boundaries clearer
- A tuple may contain mutable objects, whose own contents can still change

> `demo06 · tuples`

---

# Accessing Tuples

- Positions in this track record hold the title, artist and duration :

```python
track = ("Imagine", "John Lennon", 183)
print(track[0])  # Imagine
print(track[1:])  # ('John Lennon', 183)
print(len(track))  # 3
# track[2] = 240  # TypeError: tuple items cannot be assigned.
```

- Slicing and concatenation can create a different record :

```python
long_mix = track[:2] + (240,)
print(long_mix)  # ('Imagine', 'John Lennon', 240)
print(track)  # ('Imagine', 'John Lennon', 183)
```

- The original tuple remains unchanged

> `demo07 · tupleaccess`

---

# Delete Tuple Elements

- Individual items cannot be removed from an existing tuple
- A slice can create a shorter tuple :

```python
titles = ("Imagine", "Yesterday", "Respect")
shorter = titles[:-1]
print(shorter)  # ('Imagine', 'Yesterday')
```

- `del` removes a name binding, not items from a tuple :

```python
del titles
print(shorter)  # ('Imagine', 'Yesterday')
```

- Other names keep their objects available after a binding is removed

---

# Usage of Tuples

- Tuples have many uses :
  - Photo dimensions, track metadata and records from a database
- Any set of comma-separated objects default to tuples :
  - Even without parentheses around them
- Tuples can be dictionary keys and set members if every item is hashable
- Tuples can make your code safer :
  - Allows you to "write-protect" data that does not need to be changed
- A tuple can have lists as items :
  - The items in the lists are mutable however
- Tuple can be destructured and contents assigned to variables :

```python
selection = ("Imagine", "Toxic")
print(selection)  # ('Imagine', 'Toxic')
primary, backup = selection
print(primary)  # 'Imagine'
print(backup)  # 'Toxic'
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

- A set keeps each distinct value once :
  - Repeated artist names or track requests become single members

```python
artists = {"Queen", "Queen", "ABBA"}  # Duplicate names become one member.
print(sorted(artists))  # ['ABBA', 'Queen']
requests = ["Yesterday", "Yesterday", "Respect", "Respect"]
unique = set(requests)
unique.add("Imagine")
print(sorted(unique))  # ['Imagine', 'Respect', 'Yesterday']
print("Respect" in unique)  # True
```

- Sets have no sequence order; `sorted` gives predictable printed output
- An empty set is `set()`; `{}` creates an empty dictionary
- `frozenset(requests)` creates a set whose members cannot be changed

> `demo09 · setsandfrozensets`

---

# Set Operations

- Two fields of science show who worked in either field or in both :

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

- A dictionary can map a track title to its duration in seconds :
  - Entries consist of keys and values
  - Keys must be hashable; strings and numbers are common choices
  - Values can be any arbitrary Python object
- Dictionaries are hash tables :
  - Looking up a key is fast, however large the dictionary
- Dictionaries are enclosed by curly braces `{ }` :

```python
durations = {"Imagine": 183, "Yesterday": 125, "Respect": 149}
print(durations)  # {'Imagine': 183, 'Yesterday': 125, 'Respect': 149}
```

- Values can be assigned and accessed using square brackets `[]` :

```python
durations["Toxic"] = 199
durations["Thriller"] = 357
print(durations)
# {'Imagine': 183, 'Yesterday': 125, 'Respect': 149, 'Toxic': 199, 'Thriller': 357}
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
print(durations["Yesterday"])  # 125
print(durations["Thriller"])  # 357
```

- Dictionary can be updated by modifying an existing entry :

```python
durations["Respect"] = 147
print(durations["Respect"])  # 147
```

- Dictionary entry can be deleted :

```python
del durations["Imagine"]
print(durations["Imagine"])  # KeyError
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
track_lengths = {("Imagine", "John Lennon"): 183}
print(track_lengths[("Imagine", "John Lennon")])  # 183
```

- An immutable tuple can contain an unhashable list :

```python
hash(("Imagine", []))  # TypeError: unhashable type: 'list'
```

---

# Annotating Collections

- Each built-in collection is annotated with the type of what it holds :

```python
scores: list[int] = [10, 20, 30]
names: set[str] = {"Alice", "Bob"}
track_lengths: dict[str, int] = {"Imagine": 183, "Yesterday": 125}
```

- A dictionary takes two types, the key first and then the value
- A tuple is annotated position by position, because its length is fixed :

```python
point: tuple[int, int] = (3, 4)
track: tuple[str, int] = ("Imagine", 183)
```

- An ellipsis means any number of one type :

```python
readings: tuple[float, ...] = (1.5, 2.5, 3.5)
```

- Annotate where the collection is homogeneous, which most are :
  - Mixed element types are allowed, but a playlist of titles has the clearer
    annotation `list[str]`

---

# Dictionary Functions and Methods

| Function | Description |
|---|---|
| `len(dict)` | Gives the total length, or nr. of items, in the dictionary |
| `str(dict)` | Produces a printable string representation of a dictionary |
| `fromkeys()` | Create new dictionary with keys from seq, values set to value |
| `dict.clear()` | Removes all elements of dictionary dict |
| `dict.copy()` | Returns a shallow copy of dictionary dict |
| `dict.get(key, default)` | Returns the value for the key, or the default when the key is absent |
| `dict.popitem()` | Removes and returns the (key, value) pair added last |
| `dict.items()` | Returns a view of the dictionary's `(key, value)` pairs |
| `dict.keys()` | Returns a view of the dictionary's keys |
| `dict.update(dict2)` | Adds or replaces entries using the key-value pairs in `dict2` |
| `dict.values()` | Returns a view of the dictionary's values |

> `demo11 · dictionarymethods`

---

# Using Library Code

- A module is a file of Python code whose names can be imported
- The standard library supplies modules with Python :
  - `import math` makes its names available through `math.name`
  - `from math import sqrt` makes just `sqrt` available directly

```python
import math
from math import sqrt

print(math.sqrt(9))  # 3.0
print(sqrt(16))  # 4.0
```

- Imports run before the code that uses those names
- Standard-library modules need no `uv add` command

> `demo12 · library_imports`

---


# Choosing a Random Item

- `random.choice` returns one item from a nonempty sequence
- Repeated runs can choose different items
- A fixed value such as `track = "Imagine"` makes an example easier to check

```python
import random

tracks = ["Imagine", "Yesterday", "Respect"]
print(random.choice(tracks))
```

> `demo13 · random_choice`

---

# Summary : Data Structures

- Sequences are most basic data structure :
  - Each element of a sequence is assigned a number, its position or index
  - First index is zero, the second index is one, and so forth
- A playlist stores tracks in a chosen order :
  - Lists are mutable sequences
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
