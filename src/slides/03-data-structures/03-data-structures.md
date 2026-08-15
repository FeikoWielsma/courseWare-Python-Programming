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
    - Objects may references to other objects and these other objects may be changed
  - Examples are Strings (Unicode items), Tuples, Bytes (bytes items)
- Mutable sequences :
  - Contain objects and content can be changed once created
  - Examples are Lists and Byte Arrays
- Operations that work on all sequences types :
  - Indexing, slicing, multiplying, and checking for membership
- Python has built-in functions for :
  - Finding the length of a sequence and its largest and smallest elements


---

# Lists

- Lists are mutable sequences and similar to arrays in C :
  - List contains items separated by commas and enclosed within square brackets `[]`
  - Difference with arrays in other languages is that list items can be of different data type
- Values are accessed using the index or slice operator `[ ]` and `[ : ]` :
  - Indexes start at 0, then upwards and with end-1
  - Lists can be sliced, concatenated and so on
- Lists respond to the `+` and * operators much like strings :
  - Meaning is concatenation and repetition
  - Except that result is a new list, not a string
- Lists respond to all sequence operations usable on strings :

```python
list1 = [ 'abcd', 786 , 2.23, 'john', True ]
print(list1) # Prints complete list
print(list1[0]) # Prints first element of the list
print(list1[1:3]) # Prints elements starting from 2nd to 4th
print(list1 * 2) # Prints list two times
print(list1[::-1]) # Prints complete list in reverse order
```

> `demo01 · lists`

---

# Accessing Lists

- Use index operator `[]` to access list at specific position :
  - On left-hand side of assignment operator for given element a value
  - On right-hand side of assignment operator for reading value of element

```python
li = ['physics', 'chemistry', 'biology', 'computer science']
print("Value available at index 2 : ")
print(li[2])
li[2] = 'mathematics'
print("New value available at index 2 : ")
print(li[2])
```

- Elements can be added to a list with `append()` :

```python
list2 = [1, 2, 3]
list2.append(4)
list2.append(5)
print(list2) # [1, 2, 3, 4, 5]
```

- Elements can be added to a list at a position with `insert(index, item)` :

```python
list2.insert(0,99)
print(list2) # [99, 1, 2, 3, 4, 5]
```

---

# Delete List Elements

- Remove a list element with `del` or `remove()`
- Use `del` statement if you know index of element to remove :

```python
li = ['physics', 'chemistry', 'biology', 'computer science']
del li[2]
print("After deleting value at index 2 : ")
print(li) # ['physics', 'chemistry', 'computer science']
```

- Use `remove()` if want to remove element by value :

```python
li.remove('physics')
print("After deleting value 'physics' ")
print(li) # ['chemistry', 'computer science']
```

- List itself can also be removed with `del` :

```python
del list1
list1.append(100) # gives NameError, name list1 not defined anymore
```

> `demo02 · updatinglists`


---

# Multidimensional Lists

- Multidimensional lists created by using other lists as elements :

```python
multilist = [['a', 'b', 'c'], [1, 2, 3, 4]]
# first dimension
print (multilist[0][0])   # a
print (multilist[0][2])   # c
# second dimension
print (multilist[1][0])   # 1
print (multilist[1][3])   # 4
# print (multilist[1][4]) # IndexError: list index out of range
```

- Delete from a multidimensional list :

```python
multilist = [['a', 'b', 'c'], [1, 2, 3, 4]]
del multilist[0][2]                # [['a', 'b'], [1, 2, 3, 4]]
multilist.remove(['a', 'b'])       # [[1, 2, 3, 4]]
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

- Assuming the following input list : `list1 = ['one','two','three']`

| Python Expression | Results | Description |
|---|---|---|
| `list1[2]` | `'three'` | Offsets start at zero |
| `list1[-2]` | `'two'` | Negative : count from the right |
| `list1[1:]` | `['two', 'three']` | Slicing fetches sections |

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
| `list.pop(obj=list[-1])` | Removes and returns last object or obj from list |
| `list.remove(obj)` | Removes object obj from list |
| `list.reverse()` | Reverses objects of list in place |
| `list.sort([key, reverse])` | Sorts the items of list in place |

> `demo05 · listmethods`

---

# Tuples

- Tuple is an immutable sequence of Python objects :
  - Consist of a number of values separated by commas
  - Tuples are sequences, just like lists, but tuples are faster because read-only
- Main differences between lists and tuples :
  - Lists are enclosed in brackets `[ ]` and their contents and size can be changed
  - Tuples are enclosed in parentheses `( )` and cannot be updated
- Create tuple by assigning comma-separated values to variable :
  - Best practice is to put these comma-separated values between parentheses
  - An empty tuple is written as two parentheses containing nothing
  - For a tuple containing a single value include a comma, otherwise it is a single value

```python
tup1 = ('physics', 'chemistry', 'biology', 'computer science')
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d" # not recommended
tup4 = ()                 # empty tuple
tup5 = (50,)              # single element tuple
```

> `demo06 · tuples`


---

# Accessing Tuples

- All of the general sequence operations can be applied on tuples :
  - Use square brackets for slicing along with index to obtain value, indices start at 0
  - Use the + and * operators for concatenation and repetition

```python
tup = (1, 2, 3, 4, 5, 6, 7 )
print(tup[0]) # 1
print(tup[1:5]) # [2, 3, 4, 5]
print(len(tup)) # 7
```

- Tuples are immutable and can be thought of as read-only lists :
  - Cannot update them or change values of tuple elements

```python
tuple[2] = 1000 # Invalid syntax with tuple
```

- Portions of existing tuples can be used to create new tuples :

```python
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print(tup3) # (12, 34.56, 'abc', 'xyz')
```
- Tuples can have other tuples or lists as elements

> `demo07 · tupleaccess`

---

# Delete Tuple Elements

- Removing individual tuple elements is not possible :
  - Another tuple with undesired elements discarded must be created
- Entire tuple can be removed with `del` statement :

```python
tup1 = ('physics', 'chemistry', 'biology', 'computer science')
print(tup) # ('physics', 'chemistry', 'biology', 'computer science')
del tup
print("After deleting tup : ")
print(tup)
```

- Result after deleting tup :

```text
Traceback (most recent call last):
  File "test.py", line 9, in <module>
     print(tup)
NameError: name 'tup' is not defined
```

- Error since after `del tup` tuple is gone

---

# Usage of Tuples

- Tuples have many uses :
  - Coordinate pairs, records from a database
- Any set of comma-separated objects default to tuples :
  - Event without identifying symbols like parentheses
- Tuples are faster than lists :
  - It is faster to loop through a tuple than through a list
- Tuples can make your code safer :
  - Allows you to “write-protect” data that does not need to be changed
- A tuple can have lists as items :
  - The items in the lists are mutable however
- Tuple can be destructured and contents assigned to variables :

```python
t = ('Albert', 'Einstein')
print(t) # ('Albert', 'Einstein')
v, s = t
print(v) # 'Albert'
print(s) # 'Einstein'
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

# Bytes and Byte Arrays

- Bytes object is an immutable array :
  - Items are 8-bit bytes, represented by integers in the range `0 <= x < 256`
- Bytes objects are constructed with :
  - Bytes literals like `b'abc'` or the built-in function `bytes()`
- Characters in string become Unicode values in bytes array :

```python
str = "ABCDE"
arr = bytes(str, 'utf-8') # string with encoding 'utf-8'
print(arr)
print(arr[0]) # 65
```

- Bytes objects can be decoded to strings via `decode() :`

```python
str2 = arr.decode("utf-8")
print (str2) # ABCD
```

- Bytearray object is mutable array created `bytearray()` constructor :
  - Has same interface as immutable bytes objects
- Extension modules `array` and `collections` :09_bytesandbytearrays
  - Provide additional mutable sequence examples

> `demo09 · bytesandbytesarrays`

---

# Sets

- Data type representing unordered collection with no duplicates :
  - Distinguish between mutable sets and immutable sets
- Mutable set created by `set()` constructor or by using curly braces `{ }` :

```python
s1 = {1, 1, 2, 2}
print(s1) # {1, 2}
```

- `set()` constructor expects one iterable object :

```python
s2 = set([3, 3, 4, 4])
print(s2) # {3, 4}
```

  - Can be modified afterwards by several methods like `add()`
  - Immutable set created by `frozenset()` constructor
- Supports mathematical operations like union and intersection :

```python
a = set('abracadabra')
b = set('alacazam')
print(a) # unique letters in a
                   # {'a', 'r', 'b', 'c', 'd'}
print(a - b) # letters in a but not in b
        # {'r', 'd', 'b'}
```

> `demo10 · setsandfrozensets`

---

# Dictionaries

- Dictionaries consist of pairs of keys and values :
  - Keys can be almost any immutable Python type but usually numbers or strings
  - Values can be any arbitrary Python object
- Python 's dictionaries are of hash table type :
  - Like associative arrays in Perl and PHP
  - Consist of key-value pairs separated by comma’s
- Dictionaries are enclosed by curly braces `{ }` :

```python
dict1 = {'Albert': 2341, 'Robert': 9102, 'Enrico': 3258}
print(dict1) #{'Albert': 2341, 'Robert': 9102, 'Enrico': 3258}
```

- Values can be assigned and accessed using square brackets `[]` :

```python
dict1['Werner'] = 3490
dict1[2] = "Data"
print(dict1) # {'Albert': 2341, 'Robert': 9102, 'Enrico': 3258, 'Werner': 3490, 2: 'Data'}
```

- Dictionaries have no concept of order among elements :
  - Elements are never "out of order“, they are simply unordered

---

# Accessing Values in Dictionary

- Keys are unique within a dictionary while values may be the same :
  - Values of a dictionary can be of any type
  - Keys must be of an immutable data type such as strings, numbers or tuples
- Use square brackets along with the key to obtain its value :

```python
print(dict1["Robert"]) # 9102
print(dict1[2]) # Data
```

- Dictionary can be updated by modifying an existing entry :

```python
dict1['Enrico'] = 9999
print(dict1['Enrico']) # 9999
```

- Dictionary entry can be deleted :

```python
del dict1['Albert']
print(dict1['Albert']) # KeyError
```

- Entire contents of dictionary is cleared with `clear()`
  - Entire dictionary can be deleted in single operation with del

> `demo11 · dictionaries`

---

# Properties of Dictionary Keys

- Dictionary values have no restrictions :
  - Can be any arbitrary Python object
  - Either standard objects or user-defined objects
- There two important points to about dictionary keys :
  - No duplicate keys allowed
  - Keys must be immutable
- In case duplicate keys are encountered during assignment :
  - Last assignment wins

```python
dict1 = {'Albert': 2341, 'Robert': 9102, 'Albert': 3258}
print (dict['Albert']) # Result : 3258
```

- Strings, numbers, or tuples can be dictionary keys :
  - But something like `['Name']` is not allowed since a list is mutable

```python
dict = {['Albert']: 2341, 'Robert': 9102}
print (dict[['Albert']])
```

- Result : `TypeError: list objects are unhashable`

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
| `dict.popitem()` | Remove and return arbitrary (key, value) pair from dictionary |
| `dict.items()` | Returns a list of dict's (key, value) tuple pairs |
| `dict.keys()` | Returns list of dictionary dict's keys |
| `dict.update(dict2)` | Adds dictionary dict2's key-values pairs to dict |
| `dict.values()` | Returns list of dictionary dict's values |

> `demo12 · dictionarymethods`

---

# Summary : Data Structures

- Sequences are most basic data structure :
  - Each element of a sequence is assigned a number, its position or index
  - First index is zero, the second index is one, and so forth
- Lists are mutable sequences :
  - Contain items separated by commas and enclosed within square brackets `[]`
  - Similar to arrays in C but list items can be of different data type
- Tuples are immutable sequences :
  - Enclosed in parenthesis ( ) instead of brackets
  - Consist of a number of values separated by commas
- Sets are unordered collections with no duplicates :
  - Support mathematical operations like union and intersection
  - Set is mutable and `frozenset` is immutable
- Dictionaries are comparable to associative arrays :
  - Pairs of keys and values separated by comma , and colon :
  - Enclosed by curly braces `{ },` values access with square brackets `[]`

> `exercise03 · Data Structures`
