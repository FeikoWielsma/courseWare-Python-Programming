---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Comprehensions
---

# Functional Programming

- Programming style that is focused on expressions :
  - Also called expression oriented programming
- Python has functions and features enabling functional approach :
  - `map, filter, reduce, lambda`
  - `list comprehension`
- `map(function, iterable) :`
  - Applies operation to each item and collects the result
- `filter(function, iterable)` :
  - Extracts each element in the sequence for which function returns True
- `reduce(function, iterable)` :
  - Reduces list to single value by combining elements via supplied function
  - In functools in Python 3.0
- `lambda` :
  - Small anonymous function consisting of single line

---

# Map and Filter

- Higher-order functions `map` and `filter` that operate on lists :

```python
def square(x):
    return x*x
def even(x):
    return x % 2 == 0
some_list = list(map(square, range(10,20)))
print (some_list)
```

- Output : `[100, 121, 144, 169, 196, 225, 256, 289, 324, 361]`

```python
some_list = list(filter(even, range(10,20)))
print (some_list)
```

- Output : `[10, 12, 14, 16, 18]`

```python
some_list = list(map(square, filter(even, range(10,20))))
print (some_list)
```

- Output : `[100, 144, 196, 256, 324]`
- More Pythonic are list comprehensions

> `demo01 · map_and_filter_functions`


---

# Reduce and Lambda

- `reduce` accepts iterator to process and returns single result :

```python
from functools import reduce
var1 = reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
print (var1) # 24
```

- Above code works as follows :
  - `reduce` passes current product along with next item from list to `lambda` function
  - Default first item in sequence initialized starting value
- Same functionality with `for` loop :

```python
li1 = [1, 2, 3, 4]
result = li1[0]
for x in li1[1:] :
     result = result * x
print (result)
```

> `demo02 · reduce_and_lambda`


---

# Built-ins that Take a Function

- `sorted` returns a new sorted list, `list.sort` rearranges in place :

```python
words = ["ticket", "to", "mars", "one", "way"]
sorted(words)                    # ['mars', 'one', 'ticket', 'to', 'way']
sorted(words, reverse=True)
```

- A `key` function decides the order, and `min` and `max` accept the same :

```python
sorted(words, key=len)           # ['to', 'one', 'way', 'mars', 'ticket']
max(words, key=len)              # 'ticket'
```

- `any` and `all` reduce a sequence of conditions to a single boolean :

```python
numbers = [4, 8, 15, 16, 23, 42]
any(n > 40 for n in numbers)     # True
all(n % 2 == 0 for n in numbers) # False
```

- Both stop as soon as the answer is known :
  - On an empty sequence `any` is `False` and `all` is `True`

> `demo03 · sorted_any_all`


---

# List Comprehensions

- Construct for creating new list based on existing lists :
  - Languages like Haskell, Erlang, Scala and Python have them
- Comprehension term :
  - Comes from math’s set comprehension notation to define sets in terms of other sets
- Powerful and popular feature in Python :
  - Generate new list by applying operation or function to every member of original list

```python
slist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (slist)
list_str = [str(x) for x in slist]
print (list_str)
```

- Output : `['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']`

```python
new_list = [x * 2 for x in slist]
print (new_list)
```

- Output : `[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]`

> `demo04 · list_comprehensions`


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
li_new = [elem*2 for elem in li]   # [6, 12, 4, 14]
```

- `if` statement acts as a filter and is optional :

```python
[x-10 for x in grades if x>0]
```

---

# Filtered List Comprehension

- Filter determines if expression is performed on list member :
  - For each element of list, checks if it satisfies the filter condition
- If filter condition returns False :
  - Element is omitted from the list before the list comprehension is evaluated
- Traditional syntax :

```python
slist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for x in slist:
    if (x % 2) == 0:
        new_list.append(str(x))
print (new_list) # ['2', '4', '6', '8', '10']
```

- Pythonic syntax using list comprehension :

```text
new_list = [str(x) for x in slist if (x % 2) == 0]
print (new_list) => ['2', '4', '6', '8', '10']
```

> `demo05 · comprehension_with_predicate`


---

# Syntactic Sugar

- List comprehensions are syntactic sugar for higher-order functions :

```python
[ expression for name in list ]
map( lambda name: expression, list )
```

- Example using higher order functions versus a list comprehension :

```python
lm = list(map(lambda x: 2*x+1, [10, 20, 30]))
print (lm) # [21, 41, 61]
lc = [2*x+1 for x in [10, 20, 30]]
print (lc) # [21, 41, 61]
```

- The same comparison combining `map` with `filter` :

```python
ls1 = list(map(lambda x: 2*x+1, filter(lambda x: x > 0, [10, 20, 30, -10])))
print (ls1) # [21, 41, 61]
ls2 = [2*x+1 for x in [10, 20, 30, -10] if x > 0]
print (ls2) # [21, 41, 61]
```

> `demo06 · syntactic_sugar`


---

# Nested List Comprehensions

- List comprehensions can easily be nested :
  - Take list as input and produce list as output
- In following inner comprehension produces : `[4, 3, 5, 2]`

```python
li = [3, 2, 4, 1]
[elem*2 for elem in [item+1 for item in li] ] #[8, 6, 10, 4]
```

- Another example is :

```python
list_a = ['A', 'B']
list_b = ['C', 'D']
list_c = [[x+y for x in list_a] for y in list_b]
print (list_c)
```

- Produces :

```text
[['AC', 'BC'], ['AD', 'BD']]
```

> `demo07 · nested_comprehensions`


---

# Comprehension Features

- If list contains elements of different types :
  - Expression must operate correctly on the types of all of list members.
- If elements of list are other containers :
  - Name can consist of container of names matching type and “shape” of list members

```python
list_d = [('a' , 1), ('b', 2), ('c', 7)]
list_e = [ n * 3 for (x, n) in list_d]
print (list_e) # [3, 6, 21]
```

- Containers are objects that contain references to other objects :
  - Lists, types, dictionaries
- Expression can also contain user-defined functions :

```python
def subtract(a, b):
     return a - b
oplist = [(6, 3), (1, 7), (5, 5)]
list_f = [subtract(y, x) for (x, y) in oplist]
print (list_f) # [-3, 6, 0]
```

> `demo08 · comprehension_features`


---

# Zip Function

- `zip(*iterables)` :
  - Makes an iterator that aggregates elements from each of the iterables
  - iterator stops when the shortest input iterable is exhausted
- Used to combine two lists in list of pairs :

```python
ls1 = [1,2,3]
ls2 = [4,5,6]
ls3 = list(zip(ls1,ls2))
print (ls3) # [(1, 4), (2, 5), (3, 6)]
```

- Original lists can also be restored using same function :

```python
b1, b2 = zip(*ls3)
print (b1)
print (b2)
```

> `demo09 · zip_function`


---

# Dictionary Construction with zip

- `zip` can be used to generate dictionaries :
  - When keys and values must be computed at runtime
- Dictionaries are traditionally created with literals or key assignments :

```python
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {}
dict2['a'] = 1; dict2['b'] = 2; dict2['c'] = 3
```

- Sometimes keys and values are only known at runtime :
  - Can then use `zip` to create lists and loop through them in parallel like this :

```python
dict3 = {}
for (k,v) in zip(keys, values):
     dict3[k] = v
print (dict3) # {'a': 1, 'b': 2, 'c': 3}
```

- Alternative is using constructor with :

```python
dict4 = dict(zip(keys, values))
```

> `demo10 · dictionary_with_zip`


---

# Dictionary Comprehensions

- Dictionary comprehension is like a list comprehension :
  - Constructs a dictionary instead of a list
- Dictionary comprehension makes dictionary from two lists :

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict5 = { k:v for (k,v) in zip(keys, values)}
print (dict5) # {'a': 1, 'b': 2, 'c': 3}
```

- Requires actually more code then constructor function :

```python
dict6 = dict(zip(keys, values))
print (dict6) # {'b': 2, 'c': 3, 'a': 1}
```

- Many more occasions to use dictionary comprehension :

```python
dict7 = {x: x**2 for x in [1,2,3,4,5]}
print (dict7) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
dict8 = {x.upper(): x*3 for x in 'abcd'}
print (dict8) #{'A': 'aaa', 'C': 'ccc', 'B': 'bbb', 'D': 'ddd'}
```

> `demo11 · dictionary_comprehension`


---

# Dictionary from Keys

- We can initialize dictionary from `keys` as follows :

```python
dict9 = dict.fromkeys(['a','b','c'], 0)
print (dict9) # {'a': 0, 'c': 0, 'b': 0}
```

- Can use dictionary comprehension to do the same thing :

```python
dict10 = {k: 0 for k in ['a','b','c']}
print (dict10) # {'a': 0, 'c': 0, 'b': 0}
```

- Generate dictionary by iterating each element :

```python
dict11 = dict.fromkeys('dictionary')
print (dict11) # {'d': None, 'o': None, 'i': None,
# 't': None, 'a': None, 'c': None, 'y': None, 'n': None, 'r': None}
```

- Now using comprehension :

```python
dict12 = {k: None for k in 'dictionary'}
print (dict12) # {'t': None, 'y': None, 'c': None,
# 'd': None, 'i': None, 'r': None, 'o': None, 'n': None, 'a': None}
```

> `demo12 · dictionary_from_keys`

---

# Set Comprehensions

- Sets have their own comprehension syntax as well :
  - Quite similar to the syntax for dictionary comprehensions
  - Difference is that sets just have values instead of `key:value` pairs
- Set comprehensions can take set as input :
  - Following set comprehension calculates squares of set of numbers from 0 to 9

```python
my_set = set(range(10))
print (my_set) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
my_set2 = {x ** 2 for x in my_set}
print (my_set2) # {0, 1, 4, 81, 64, 9, 16, 49, 25, 36}
```

- Set comprehensions can contain `if` clause to filter items :

```python
my_set3 = {x for x in my_set if x % 2 == 0}
print (my_set3) #{0, 8, 2, 4, 6}
```

- Set comprehensions do not have to take set as input :
  - They can take any sequence

```python
my_set4 = {2**x for x in range(10)}
print (my_set4) #{32, 1, 2, 4, 8, 64, 128, 256, 16, 512}
```

> `demo13 · set_comprehensions`


---

# Summary : Comprehensions

- List comprehension :
  - Generate new list by applying operation or function to every member of original list
- Syntax of a list comprehension may involve :
  - `for` loop, an `in` operation and an `if` statement
- If filter determines if expression is performed on list member :
  - For each element of list, checks if it satisfies the filter condition
- List comprehensions are syntactic sugar :
  - For higher-order functions like `map` and `filter`
- List comprehensions can easily be nested :
  - Take list as input and produce list as output
- Dictionary comprehension is like a list comprehension :
  - Constructs a dictionary instead of a list
- Set comprehensions have similar syntax as dictionaries :
  - Difference is that sets have values instead of `key:value` pairs

> `exercise07 · Comprehensions`
