# Exercise 3 : Data Structures

So far the game knows one word, `crane`, and forgets every guess the moment it has printed it. A real game picks its secret from a list of words, and keeps track of what each guess has ruled out. In this exercise you load the word list and use lists, sets, tuples and dictionaries to answer questions about a guess.

Continue in your own `wordle` project, or start from `exercises/starters/03-data-structures/`, which is the finished Exercise 2 with the word list. This exercise starts a new script in `wordle.py`; Exercise 2's table is not needed again. Run the program after every step with :

```bash
uv run python wordle.py
```

Some steps give you the code, some a skeleton to complete, and some only a description of what to write. Where you write the code yourself, the solution is hidden until you open it. Try the step first; the solution is there for when you are stuck, or to compare afterwards.

---

### Step 1 : The word list

Replace the contents of `wordle.py` with :

```python
import random
from pathlib import Path

words = Path("words.txt").read_text(encoding="utf-8").split()
guess = input("Your guess: ").strip().lower()
random.seed(0)
secret = random.choice(words)

print(f"There are {len(words)} words. The first ten are {words[:10]}.")
print(f"Crane is in the word list: {'crane' in words}.")
print(f"Example secret: {secret.upper()}.")
```

The line that reads the file is an incantation for now : it reads `words.txt` into one string, and `.split()` cuts that string into a list wherever there is white space, which in this file means at every line break. Exercise 9 takes it apart.

`words` is a list of strings, so `len`, slicing and `in` work on it just as they did on a single string. `random.choice` picks one item of a list at random. `random.seed(0)` makes the random choices the same on every run, which is why everybody gets the same example secret below. Remove that line and run the program twice to see the secret change, then put it back so your output matches the rest of this exercise.

Run it and type `crane` :

```text
Your guess: crane
There are 935 words. The first ten are ['abbey', 'abide', 'abled', 'abort', 'about', 'above', 'abuse', 'acorn', 'actor', 'acute'].
Crane is in the word list: True.
Example secret: TRUST.
```

### Step 2 : What a guess rules out

`set("crane")` is the set of letters in a word : each letter once, in no particular order. Two sets can be combined with operators, which is exactly what the game needs to describe a guess. Work out three sets of letters, each sorted into a list for printing :

- the letters the guess and the secret have in common
- the letters of the guess that are not in the secret, which the guess has ruled out
- the letters of the alphabet that the guess has not tried

```python
import string  # at the top of the file, with the other imports

common = sorted(...)
ruled_out_letters = sorted(...)
not_tried = sorted(...)
print(f"Letters in common: {common}")
print(f"Letters ruled out: {ruled_out_letters}")
print(f"Letters not tried: {not_tried}")
```

`string.ascii_lowercase` is the string `"abcdefghijklmnopqrstuvwxyz"`, the alphabet the third set starts from.

:::hint
The slide *Set Operations* shows the operators : `&` gives the items that are in both sets, and `-` gives the items of the first set that are not in the second.
:::

:::hint
Make a set of `string.ascii_lowercase` the same way as of a word. `sorted` accepts a set and returns a list, which is why the result prints in alphabetical order.
:::

:::output
```text
Letters in common: ['r']
Letters ruled out: ['a', 'c', 'e', 'n']
Letters not tried: ['b', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```
:::

:::solution
```python
common = sorted(set(guess) & set(secret))
ruled_out_letters = sorted(set(guess) - set(secret))
not_tried = sorted(set(string.ascii_lowercase) - set(guess))
print(f"Letters in common: {common}")
print(f"Letters ruled out: {ruled_out_letters}")
print(f"Letters not tried: {not_tried}")
```
:::

### Step 3 : A history of guesses

A game has more than one guess, and they come in order. Keep them in a list called `history` : start it empty, then append a first guess, `"slate"`, and the guess the player typed.

Then record a guess together with what it ruled out as a pair, the tuple `(guess, ruled_out_letters)`, in a variable called `ruled_out`. Print both :

```python
history = ...
...
ruled_out = ...
print(f"History: {history}")
print(f"Guess and ruled-out letters: {ruled_out}")
```

A tuple cannot be changed once it is made. See that for yourself : add the line `ruled_out[0] = "wrong"` below the tuple, run the program, and read the last line of the error. It is a `TypeError` that says a `tuple` does not support item assignment. Then turn the line into a comment, so the program runs again and the reader can still see what you tried.

:::hint
`demo01 · lists` starts with an empty list, the slide *List Functions and Methods* has `append`, and *Tuples* shows how a tuple is written.
:::

:::hint
`[]` is an empty list, and `append` adds one item at the end. A tuple is written as values separated by commas, usually in brackets.
:::

:::output
```text
History: ['slate', 'crane']
Guess and ruled-out letters: ('crane', ['a', 'c', 'e', 'n'])
```
:::

:::solution
```python
history = []
history.append("slate")
history.append(guess)
ruled_out = (guess, ruled_out_letters)
# Uncomment this line to see why tuple items cannot be reassigned.
# ruled_out[0] = "wrong"
print(f"History: {history}")
print(f"Guess and ruled-out letters: {ruled_out}")
```

The tuple itself cannot change, but the list inside it still can : `ruled_out[1].append("z")` is allowed. A tuple fixes which objects it holds, not what happens inside them.
:::

### Step 4 : Statistics

A game keeps statistics : how many games were played and how many were won. A dictionary holds them by name. Create `stats` with the keys `"played"` and `"won"`, both starting at 0. Then record this game : one more played, and one more won if the guess was the secret.

Print the dictionary, and also the current streak, which `stats` does not have yet :

```python
stats = ...
...
print(f"Stats: {stats}; streak: {stats.get('streak', 0)}")
```

`stats["streak"]` would stop the program with a `KeyError`, because the key does not exist. `get` returns the second argument instead. The slide *Dictionary Functions and Methods* lists `get`.

:::hint
The slide *Dictionaries* shows a dictionary written out with its keys and values, and *Accessing Values in Dictionary* changes the value under a key.
:::

:::hint
`stats["played"] += 1` adds one to the value stored under `"played"`.
:::

:::hint
There is no `if` yet, and you do not need one. `guess == secret` is `True` or `False`, and as the slide *Type Conversions* says, a Boolean behaves like 0 and 1 : `int(True)` is 1 while `int(False)` is 0.
:::

:::output
```text
Your guess: crane
There are 935 words. The first ten are ['abbey', 'abide', 'abled', 'abort', 'about', 'above', 'abuse', 'acorn', 'actor', 'acute'].
Crane is in the word list: True.
Example secret: TRUST.
Letters in common: ['r']
Letters ruled out: ['a', 'c', 'e', 'n']
Letters not tried: ['b', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
History: ['slate', 'crane']
Guess and ruled-out letters: ('crane', ['a', 'c', 'e', 'n'])
Stats: {'played': 1, 'won': 0}; streak: 0
```
:::

:::solution
```python
stats = {"played": 0, "won": 0}
stats["played"] += 1
stats["won"] += int(guess == secret)
print(f"Stats: {stats}; streak: {stats.get('streak', 0)}")
```

The complete file is in `solutions/03-data-structures/wordle.py`.
:::

### If time permits

Two more questions about the word list :

- Print the first ten words of the list sorted in reverse order, and then the first ten sorted by their last letter. `sorted` takes a `key`, a small function that says what to sort by : `sorted(words, key=lambda word: word[-1])`. Module 05 explains `lambda`.
- How many words start with each vowel? Without a loop this takes a trick : join the words into one long string with a space in front of every word, then `count` how often `" a"`, `" e"` and so on occur in it. Check one of your answers by looking at the word list.

There is no reference solution for this step.
