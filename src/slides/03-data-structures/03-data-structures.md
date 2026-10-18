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
list1 = ["Intro", "Orbit", "Echo", "Pulse", "Outro"]
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
playlist = ["Intro", "Orbit", "Echo", "Outro"]
print("Value available at index 2 : ")
print(playlist[2])
playlist[2] = "Remix"
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
playlist = ["Intro", "Orbit", "Echo", "Outro"]
del playlist[2]
print("After deleting value at index 2 : ")
print(playlist)  # ['Intro', 'Orbit', 'Outro']
```

- Use `remove()` if want to remove element by value :

```python
playlist.remove("Intro")
print("After deleting value 'Intro' ")
print(playlist)  # ['Orbit', 'Outro']
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
track = ("Orbit", 222)
dimensions = (1920, 1080)
titles = "Orbit", "Echo"  # The comma creates a tuple.
empty = ()
single = ("Orbit",)  # A one-item tuple needs the comma.
```

- Items cannot be replaced, inserted or removed from an existing tuple
- Commas create the tuple; parentheses usually make its boundaries clearer
- A tuple may contain mutable objects, whose own contents can still change

> `demo06 · tuples`

---

# Accessing Tuples

- Positions in this track record hold the title, artist and duration :

```python
track = ("Orbit", "Nova", 222)
print(track[0])  # Orbit
print(track[1:])  # ('Nova', 222)
print(len(track))  # 3
# track[2] = 240  # TypeError: tuple items cannot be assigned.
```

- Slicing and concatenation can create a different record :

```python
long_mix = track[:2] + (240,)
print(long_mix)  # ('Orbit', 'Nova', 240)
print(track)  # ('Orbit', 'Nova', 222)
```

- The original tuple remains unchanged

> `demo07 · tupleaccess`

---

# Delete Tuple Elements

- Individual items cannot be removed from an existing tuple
- A slice can create a shorter tuple :

```python
titles = ("Orbit", "Echo", "Pulse")
shorter = titles[:-1]
print(shorter)  # ('Orbit', 'Echo')
```

- `del` removes a name binding, not items from a tuple :

```python
del titles
print(shorter)  # ('Orbit', 'Echo')
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
selection = ("Orbit", "Nova")
print(selection)  # ('Orbit', 'Nova')
primary, backup = selection
print(primary)  # 'Orbit'
print(backup)  # 'Nova'
```

> `demo08 · destructurewithtuples`


---

# Unpacking in for Loops

- A `for` loop unpacks each item the same way, and the unpacking can nest :

```python
rows = [(1,), (2,)]
for (number,) in rows:
    print(number)  # 1, then 2

records = [(1, ("Orbit", "Nova"))]
for number, (title, artist) in records:
    print(number, title, artist)  # 1 Orbit Nova
```

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
artists = {"Nova", "Nova", "Echo"}  # Duplicate names become one member.
print(sorted(artists))  # ['Echo', 'Nova']
requests = ["Echo", "Echo", "Pulse", "Pulse"]
unique = set(requests)
unique.add("Orbit")
print(sorted(unique))  # ['Echo', 'Orbit', 'Pulse']
print("Pulse" in unique)  # True
```

- Sets have no sequence order; `sorted` gives predictable printed output
- An empty set is `set()`; `{}` creates an empty dictionary
- `frozenset(requests)` creates a set whose members cannot be changed

> `demo09 · setsandfrozensets`

---

# Set Operations

- Two festival lineups show which artists play either day or both days :

```python
day_one = {"Nova", "Echo", "Pulse", "Orbit"}
day_two = {"Pulse", "Muse", "Vega"}
print("Pulse" in day_two)  # True
print(sorted(day_one | day_two))  # union, in either set
print(sorted(day_one & day_two))  # intersection, in both
print(sorted(day_one - day_two))  # difference, in day_one only
print(sorted(day_one ^ day_two))  # in one of the two, not both
```

```text
True
['Echo', 'Muse', 'Nova', 'Orbit', 'Pulse', 'Vega']
['Pulse']
['Echo', 'Nova', 'Orbit']
['Echo', 'Muse', 'Nova', 'Orbit', 'Vega']
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
  - Consist of key-value pairs separated by commas
- Dictionaries are enclosed by curly braces `{ }` :

```python
durations = {"Orbit": 222, "Echo": 185, "Pulse": 204}
print(durations)  # {'Orbit': 222, 'Echo': 185, 'Pulse': 204}
```

- Values can be assigned and accessed using square brackets `[]` :

```python
durations["Nova"] = 196
durations["Intro"] = 90
print(durations)  # {'Orbit': 222, 'Echo': 185, 'Pulse': 204, 'Nova': 196, 'Intro': 90}
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
print(durations["Echo"])  # 185
print(durations["Intro"])  # 90
```

- Dictionary can be updated by modifying an existing entry :

```python
durations["Pulse"] = 210
print(durations["Pulse"])  # 210
```

- Dictionary entry can be deleted :

```python
del durations["Orbit"]
print(durations["Orbit"])  # KeyError
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
track_lengths = {("Orbit", "Nova"): 222}
print(track_lengths[("Orbit", "Nova")])  # 222
```

- An immutable tuple can contain an unhashable list :

```python
hash(("Orbit", []))  # TypeError: unhashable type: 'list'
```

---

# Annotating Collections

- Each built-in collection is annotated with the type of what it holds :

```python
scores: list[int] = [10, 20, 30]
names: set[str] = {"Alice", "Bob"}
track_lengths: dict[str, int] = {"Orbit": 222, "Echo": 185}
```

- A dictionary takes two types, the key first and then the value
- A tuple is annotated position by position, because its length is fixed :

```python
point: tuple[int, int] = (3, 4)
track: tuple[str, int] = ("Orbit", 222)
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
| `dict.get(key)` | For key key, returns value or default if key not in dictionary |
| `dict.popitem()` | Removes and returns the (key, value) pair added last |
| `dict.items()` | Returns a view of dict'backup (key, value) tuple pairs |
| `dict.keys()` | Returns a view of dictionary dict'backup keys |
| `dict.update(dict2)` | Adds dictionary dict2'backup key-values pairs to dict |
| `dict.values()` | Returns a view of dictionary dict'backup values |

> `demo11 · dictionarymethods`

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
