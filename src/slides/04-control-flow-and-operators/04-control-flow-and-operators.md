---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Control Flow
---

# Control Flow Constructs

- Statements run one after the other unless a control flow construct intervenes :
  - Branching constructs choose which block runs
  - Iteration constructs repeat a block
- Branching statements :
  - `if`, `if...else` and `elif`
  - `match`, which compares one value against a series of patterns
- Iteration statements :
  - `while`, which repeats as long as a condition holds
  - `for`, which takes each item of a sequence in turn
- Statements that steer a loop or fill a gap :
  - `break`, `continue`, a loop's `else`, and `pass`

---

# if Statement

- `if` tests an expression and runs a block only when it is true :
  - The expression is often a comparison, such as `count > 0`
  - The block is skipped when the expression is false
- Syntax `if` statement :

```python
if expression:
    statement(s)
```

- Expression is evaluated first :
  - If it is true, the indented block runs
  - Otherwise execution continues with the statement after the block

```mermaid
flowchart LR
  A[statement before] --> B{expression}
  B -- True --> C[indented block]
  B -- False --> D[block is skipped]
  C --> E[statement after]
  D --> E
```

- Values other than `True` and `False` can also be tested :
  - `0`, `""`, empty collections and `None` count as false, everything else as true
- Grouping statements :
  - Statements indented by the same amount form one block
  - Python uses indentation, four spaces by convention, as its way of grouping

---

# if Example

```python
var1 = 100
if var1:
    print("1 - Got a true expression value")
    print(var1)

var2 = 0
if var2:
    print("2 - Got a true expression value")
    print(var2)
print("Good bye!")
```

- Result :

```text
1 - Got a true expression value
100
Good bye!
```

- In case `if` has only one line it may go on same line :

```python
if expression == 1: print("Value of expression is 1")
```

> `demo01 · if`

---

# else Statement

- Is combined with an `if` statement :
  - Contains the block that runs when the `if` expression is false
- `else` is optional :
  - At most one `else` can follow an `if`, and it comes last
- Syntax `if...else` statement :

```python
if expression:
    statement(s)
else:
    statement(s)
```

- Example reading input with `input` and testing it with `endswith` :

```python
name = input("What is your name? ")
if name.endswith("Gumby"):
    print("Hello, Mr. Gumby")
else:
    print("Hello, stranger")
```

> `demo02 · else`


---

# elif Statement

- Tests several expressions in turn :
  - The block of the first expression that is true runs, and the rest are skipped
- `elif` is optional :
  - Any number of `elif` branches may follow an `if`
- Syntax of the `if...elif` statement :

```text
if expression1:
    statement(s)
elif expression2:
    statement(s)
elif expression3:
    statement(s)
else:
    statement(s)
```

- Where a chain of `elif` tests one value, `match` often reads better :
  - Covered at the end of this module

> `demo03 · elif`


---

# Nested if...elif...else

- An `if` statement can sit inside the block of another :
  - The inner condition is only tested once the outer one is true
- Syntax nested `if...elif...else` :

```text
if expression1:
    statement(s)
    if expression2:
        statement(s)
    elif expression3:
        statement(s)
    else:
        statement(s)
elif expression4:
    statement(s)
else:
    statement(s)
```

- Each level of nesting adds four spaces :
  - More than two levels usually reads better as `and`, or as a function

> `demo04 · nested_if`


---

# while Loop

- Repeats a block for as long as an expression is true :
  - The expression is tested before every pass, including the first

```python
while expression:
    statement(s)
```

- The loop ends when the expression is false :
  - Execution continues with the statement after the loop

```mermaid
flowchart LR
  A[before the loop] --> B{expression}
  B -- True --> C[loop body]
  C --> B
  B -- False --> D[statement after the loop]
```

- If the expression never becomes false, the loop never ends :
  - Sometimes that is the intent, as in a server or a game that waits for input
  - Such a loop is written `while True:` and left with `break`, covered below
- A body that must run at least once is written the same way :
  - `while True:`, then the body, then `if done:` with `break` under it

> `demo05 · while`


---

# Infinite while Loop

```python
while True:  # the condition never becomes false
    num = input("Enter a number: ")
    print("You entered:", num)
print("Good bye!")  # never reached
```

- Result :

```text
Enter a number: 20
You entered: 20
Enter a number: 3
You entered: 3
Enter a number: Traceback (most recent call last):
  File "06_infinitewhile.py", line 2, in <module>
    num = input("Enter a number: ")
KeyboardInterrupt
```

- A loop written this way continues until interrupted :
  - Press Ctrl+C to stop the program

> `demo06 · infinitewhile`


---

# for Loop

- Repeats a block for each item of a sequence :
  - Iterates over any sequence or iterable, such as a list, a string or a range
- Syntax :

```python
for var in sequence:
    statement(s)
```

- How a `for` loop works :
  - Each item is assigned to variable `var` in turn
  - The block runs once per item until the sequence is exhausted

```mermaid
flowchart LR
  A[sequence] --> B{items left}
  B -- yes --> C[assign next item to var]
  C --> D[loop body]
  D --> B
  B -- no --> E[statement after the loop]
```

```python
words = ["one", "way", "ticket", "to", "mars"]
for word in words:
    print(word, end=" ")
print()
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in list1:
    print(number)
```

> `demo07 · for`


---

# Iterating by Sequence Index

- A sequence can be walked by index, using `len()` and `range()` :

```python
planets = ["venus", "mars", "jupiter"]
for index in range(len(planets)):
    print("Current planet :", planets[index])
```

- This works, and is what a loop over positions looks like in many languages :
  - `len()` gives the number of elements, `range()` the sequence of positions
  - It is worth recognising, because you will meet it in other people's code
- In Python it is rarely what you want :
  - The index is only used to look the element back up again
  - A `range` that drifts out of step with the sequence is a common bug
- When the element is all you need, iterate the sequence itself :

```python
for planet in planets:
    print("Current planet :", planet)
```

---

# Iterating with enumerate

- When the index is genuinely needed, `enumerate` yields both :

```python
for index, planet in enumerate(planets):
    print(index, planet)
```

```text
0 venus
1 mars
2 jupiter
```

- The two can never fall out of step, because they come from one call
- Counting starts at zero unless a `start` is given :

```python
for number, planet in enumerate(planets, start=1):
    print(number, planet)
```

- The pattern generalises :
  - `enumerate(seq)` for position and element
  - `zip(a, b)` for two sequences walked in step, covered in Comprehensions
  - `dict.items()` for a dictionary's keys and values together

> `demo08 · loopbyindex`


---

# break and continue Statements

- `break` leaves the loop immediately :
  - Execution continues with the statement after the loop
- `continue` skips the rest of the current iteration :
  - Control moves directly to the next pass of the loop
- Both statements work inside `while` and `for` loops

```python
for letter in "Python":
    if letter == "h":
        continue
    print("Current Letter :", letter)  # letter 'h' is not printed
print("After first loop!")
for letter in "Programming":
    if letter == "i":
        break
    print("Current Letter :", letter)  # loop stops on letter 'i'
print("After second loop!")
```

> `demo09 · breakandcontinue`


---

# Loop with else Combination

- An `else` clause can be attached to a loop :
  - In a `for` loop, the `else` block runs when the sequence is exhausted
  - In a `while` loop, the `else` block runs when the condition becomes false
  - In both cases, the `else` block is skipped if the loop was left via `break`
- In the following example :
  - The loop searches for a perfect square downwards from 99
  - When 81 is found, `break` leaves the loop and skips the `else` block

```python
from math import sqrt
for n in range(99, 80, -1):
    root = sqrt(n)
    print(root)
    print(int(root))
    if root == int(root):
        print(f"Perfect square is {n}")
        break
else:
    print("Didn't find it!")
```

> `demo10 · for_else`

---

# pass Statement

- Used when Python's syntax requires a statement but no action is needed :
  - A null operation; nothing happens when it executes
  - Commonly used as a placeholder in stubs or empty branches
- When a code block is under construction :
  - `pass` keeps the file syntactically valid until code is written

```python
for letter in "Python":
    if letter == "h":
        pass
        print("This is pass block")
    print("Current Letter :", letter)
print("Good bye!")
```

> `demo11 · passstatement`


---

# match Statement

- Python 3.10 added structural pattern matching, `match` and `case` :
  - It compares a value against a series of patterns and runs the first that fits
  - Older Python has no such statement, which is why chains of `elif` are common

```python
match command.split():
    case ["quit"]:  # a literal pattern
        return "leaving"
    case ["go", direction]:  # captures the second word
        return f"walking {direction}"
    case ["take" | "get", item] if item != "moon":  # or-pattern with a guard
        return f"picking up the {item}"
    case _:  # the wildcard, matched last
        return "I do not understand"
```

- It matches the shape of the data as well as its value :
  - A pattern can bind names out of a sequence, as `direction` and `item` do
  - `case _` is the catch-all, and belongs last
- There is no fall through between cases, so a case needs no `break` to end it; a `break` inside a case still leaves the loop around the `match`

> `demo12 · matchstatement`

---

# Summary : Control Flow

- Branching statements choose which code runs :
  - `if`, `if...else` and `elif` test conditions in turn
  - `match` compares data against a series of patterns
- Iteration statements repeat a block of code :
  - `while` repeats as long as a condition holds
  - `for` iterates over each item of a sequence
- Statements that steer a loop :
  - `break` exits the loop early
  - `continue` skips to the next iteration
  - An `else` clause runs when the loop finishes without a `break`
- The `pass` statement is a no-op placeholder where a statement is required

> `exercise04 · Control Flow`
