# Exercise 7 : Comprehensions

Your game can judge a guess, but it cannot yet use the feedback to choose its next move. In this exercise you turn the same scoring function into a solver: it will rule out impossible answers and recommend a guess from the words that remain.

Continue in your own `wordle` project, or use `exercises/starters/07-comprehensions/`, the finished Exercise 6. Keep running commands beside `pyproject.toml`.

After editing a module, leave any open Python interpreter with `exit()`, start `uv run python` again, and repeat the imports before trying the changed code. An existing session keeps the previously imported definitions.

### Step 1 : Build a row from expressions

#### 1a

In `wordle/display.py`, start with this supplied version of `render`. It collects the pieces of the row in a list and joins them after the loop :

```python
def render(guess: str, marks: list[str]) -> str:
    symbols = {
        "green": lambda letter: f"[{letter}]",
        "yellow": lambda letter: f"({letter})",
        "grey": lambda letter: f" {letter} ",
    }
    pieces = []
    for letter, mark in zip(guess.upper(), marks, strict=True):
        pieces.append(symbols[mark](letter))
    return "".join(pieces)
```

For a green `A`, `symbols[mark]` selects the function that produces `[A]`; calling it with `letter` produces one piece of the row. `zip` pairs each letter with its mark.

Check the function in a fresh interpreter with `uv run python` :

```text
>>> from wordle.display import render
>>> render("react", ["yellow", "yellow", "green", "yellow", "grey"])
'(R)(E)[A](C) T '
```

The row must match Exercise 6's output before changing how it is built.

:::hint
The slide *Functions in Dictionaries*, in module 05, selects and calls a function through a dictionary. *Zip Function* pairs two sequences; `strict=True` rejects different lengths. *List Functions and Methods* shows `append`.
:::

#### 1b

Keep the supplied `symbols` dictionary. Replace the `pieces` list, its loop and the final return with a generator expression inside `join`. Fill in the expression that produces one row piece :

```python
    return "".join(... for letter, mark in zip(guess.upper(), marks, strict=True))
```

Save, restart the interpreter and repeat the same call. The result should be unchanged. The expression now supplies each piece directly to `join`.

:::hint
The slide *Generator Expressions* moves an expression and its `for` part inside a function call. Use the same `symbols[mark](letter)` call that was passed to `append` in 1a.
:::

:::solution
```python
def render(guess: str, marks: list[str]) -> str:
    """Draw green letters in brackets, yellow in parentheses and grey padded."""
    symbols = {
        "green": lambda letter: f"[{letter}]",
        "yellow": lambda letter: f"({letter})",
        "grey": lambda letter: f" {letter} ",
    }
    return "".join(symbols[mark](letter) for letter, mark in zip(guess.upper(), marks, strict=True))
```
:::

### Step 2 : Turn the scorer around

Imagine that a candidate word really is the secret. Would it give exactly the feedback you saw? If it would, the word is still possible. This reuses the duplicate-letter rules you already wrote, rather than inventing another set of rules for the solver.

Create `wordle/solver.py` with :

```python
from wordle.scoring import score_guess


def consistent(word: str, guess: str, marks: list[str]) -> bool:
    """Return whether word would produce the observed marks for guess."""
    return score_guess(word, guess) == marks
```

Try it in the interpreter. Keep the observed guess `slate` and its marks fixed. The candidate `crane` would produce those marks, but the candidate `trace` would not :

```text
>>> from wordle.scoring import score_guess
>>> from wordle.solver import consistent
>>> marks = score_guess("crane", "slate")
>>> consistent("crane", "slate", marks)
True
>>> consistent("trace", "slate", marks)
False
```

:::hint
The slide *return Statement* shows returning a comparison directly. Here `score_guess(word, guess)` must equal the observed `marks`; change the candidate `word` when checking another possible answer.
:::

The game remains playable while you build its solver.

### Step 3 : Keep every answer that fits

`history` contains pairs of a guess and its marks. A candidate must agree with every pair. Check one candidate first, then apply that check to a list of words.

#### 3a

Create a temporary file `solver_check.py` in the project root, beside `pyproject.toml`. Put this supplied walkthrough in it. Its history contains feedback from two guesses against CRANE :

```python
from wordle.scoring import score_guess
from wordle.solver import consistent

history = [
    ("slate", score_guess("crane", "slate")),
    ("react", score_guess("crane", "react")),
]
word = "crane"
matches = []
for guess, marks in history:
    matches.append(consistent(word, guess, marks))
print(matches)
print(all(matches))
```

Run it from the project root :

```bash
uv run python solver_check.py
```

```text
[True, True]
True
```

Change only `word` to `"trace"` and run it again :

```text
[False, False]
False
```

The observed guesses and their marks stay fixed. CRANE could have produced both rows; TRACE could not.

:::hint
The slide *Unpacking in for Loops* separates each history pair into `guess` and `marks`. *Generator Expressions* shows `all`: the candidate is kept only when every comparison is true.
:::

#### 3b

In `solver_check.py`, replace the `matches` list, its loop and the two print statements with one call. Keep `history` and `word`, and fill the expression that checks one history entry :

```python
print(all(... for guess, marks in history))
```

Run it once with `word = "crane"` and once with `word = "trace"`. The single result must match the last line of each run in 3a.

:::hint
The slide *Generator Expressions* uses `all` over generated conditions. Move the `consistent(word, guess, marks)` expression from 3a inside `all`.
:::

:::solution
```python
print(all(consistent(word, guess, marks) for guess, marks in history))
```
:::

#### 3c

Add `candidates` to `wordle/solver.py`. The outer comprehension visits each possible word; its condition is the whole-history check from 3b. Fill the remaining expression :

```python
def candidates(words: list[str], history: list[tuple[str, list[str]]]) -> list[str]:
    """Return words consistent with every guess and its marks."""
    return [
        word
        for word in words
        if all(... for guess, marks in history)
    ]
```

Keep the original order of `words`. An empty history rules out nothing: there is no observed feedback for a candidate to contradict.

In `solver_check.py`, add `candidates` to the import from `wordle.solver`. Replace the code from `word = ...` onwards with these checks, keeping the two-entry `history` above them :

```python
print(candidates(["crane", "slate", "trace"], history))
print(candidates(["crane", "slate", "trace"], []))
```

```text
['crane']
['crane', 'slate', 'trace']
```

:::hint
The slide *Filtered List Comprehension* shows `word for word in words if ...`. *Generator Expressions* shows that `all` is true for an empty sequence. Use the same `consistent` call as in 3b.
:::

:::solution
```python
def candidates(words: list[str], history: list[tuple[str, list[str]]]) -> list[str]:
    """Return words consistent with every guess and its marks."""
    return [
        word
        for word in words
        if all(consistent(word, guess, marks) for guess, marks in history)
    ]
```
:::

### Step 4 : Choose a useful next guess

Prefer a candidate whose distinct letters occur in many remaining words. Build this score in parts before passing it to `max`. It is a heuristic for useful information, not a guarantee of the fewest guesses.

#### 4a

Replace the contents of the temporary `solver_check.py` with this loop. CACAO repeats letters, but the set keeps each letter once :

```python
words = ["cacao", "crane"]
letters = set()
for word in words:
    for letter in word:
        letters.add(letter)
print(sorted(letters))
```

```text
['a', 'c', 'e', 'n', 'o', 'r']
```

Replace the empty set and both loops with a set comprehension. Complete this line and keep the final print as a check :

```python
letters = {... for word in words for letter in word}
```

:::hint
The slide *Flattening a List of Lists* puts an outer and inner loop into one comprehension, and *Set Comprehensions* uses braces to keep distinct values. The expression is the value that was passed to `add`.
:::

:::solution
```python
letters = {letter for word in words for letter in word}
```
:::

#### 4b

Count how many words contain each letter. Repeated occurrences within one word count only once. In `solver_check.py`, replace the `letters` assignment and its print with this check for one letter :

```python
print(["a" in word for word in words])
print(sum("a" in word for word in words))
```

```text
[True, True]
2
```

Both words contain `a`. Each true condition contributes `1`, so CACAO's second A does not add another count.

Now add `letter_counts` to `wordle/solver.py`. The set comprehension is the one from 4a; complete the expression that counts the words for each letter :

```python
def letter_counts(words: list[str]) -> dict[str, int]:
    """Count how many candidate words contain each letter."""
    letters = {letter for word in words for letter in word}
    return {letter: ... for letter in letters}
```

In `solver_check.py`, replace the two prints with these checks and add `from wordle.solver import letter_counts` at the top. Keep `words = ["cacao", "crane"]` :

```python
counts = letter_counts(words)
print(counts["a"])
print(counts["o"])
```

```text
2
1
```

:::hint
The slide *Dictionary Comprehensions* builds a value for each key, and *Generator Expressions* shows `sum` over generated values. Replace the fixed `"a"` in the supplied count with the dictionary's current `letter`.
:::

:::solution
```python
def letter_counts(words: list[str]) -> dict[str, int]:
    """Count how many candidate words contain each letter."""
    letters = {letter for word in words for letter in word}
    return {letter: sum(letter in word for word in words) for letter in letters}
```
:::

#### 4c

Score one proposed guess by adding the counts for its distinct letters. In `solver_check.py`, keep the import, `words` and `counts`, then replace the two prints with :

```python
word = "cacao"
score = 0
for letter in set(word):
    score += counts[letter]
print(score)
```

The result is `5`: C contributes `2`, A contributes `2`, and O contributes `1`. Change `word` to `"crane"` and run it again; the score is `7`.

Replace the counter and loop with a sum over a generator expression. Keep `print(score)` and check both words again :

```python
score = sum(... for letter in set(word))
```

:::hint
The slide *Generator Expressions* adds generated values with `sum`. The expression is the same `counts[letter]` that the loop added to `score`; keeping `set(word)` prevents repeated letters earning the same count twice.
:::

:::solution
```python
score = sum(counts[letter] for letter in set(word))
```
:::

#### 4d

Add `best_guess` to `wordle/solver.py`. Give `max` the score from 4c as its `key`: it compares those scores and returns the word with the largest one.

```python
def best_guess(words: list[str]) -> str:
    """Choose the word with the most frequently occurring distinct letters."""
    counts = letter_counts(words)
    return max(words, key=lambda word: ...)
```

For these functions, pass a non-empty list. During normal play the secret remains a candidate. On a tie, `max` chooses the first word with that score.

Add `best_guess` to the helper file's import and replace the checks after `words` with :

```python
print(best_guess(words))
```

```text
crane
```

:::hint
The slide *Built-ins that Take a Function* passes a `key` to `max`. *Lambda Functions*, in module 05, shows a small function written as an expression. The lambda's result is the sum from 4c, evaluated for the word that `max` passes to it.
:::

:::solution
```python
def best_guess(words: list[str]) -> str:
    """Choose the word with the most frequently occurring distinct letters."""
    counts = letter_counts(words)
    return max(words, key=lambda word: sum(counts[letter] for letter in set(word)))
```
:::

### Step 5 : Ask the game for help

Add `from wordle.solver import best_guess, candidates` to `wordle/game.py`. Initialise `history` as an empty list beside `used_letters` inside `play`. After scoring each valid guess, save `(guess, marks)` before rendering the row. Commands and rejected guesses must not enter the history.

Extend the existing `match guess` using this skeleton, keeping the existing `quit` and `letters` cases :

```python
match guess:
    case "hint":
        possible = ...
        print(...)  # number of candidates and the suggested word in upper case
        continue
```

Use the message format shown in the output below. Requesting a hint must not use a turn. After implementing it, keep `secret = "crane"` in `wordle/__main__.py`, run `uv run python -m wordle`, and enter `slate`, `hint`, then `crane`.

:::hint

This is Exercise 5's `play` with one more `case`; the slide *match Statement* shows the form, and *List Functions and Methods* has `append`.

:::

:::hint

Calculate the marks once, append the pair to `history`, and pass those same marks to `render`. The hint case calls `candidates(words, history)` first, then `best_guess(possible)`.

:::

:::output

Captured output with typed input omitted. Notice that the hint leaves the prompt at guess 2.

```text
Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.
Guess 1/6 :  S  L [A] T [E]
Guess 2/6 : 2 words left, try CRANE
Guess 2/6 : [C][R][A][N][E]
Got it in 2!
```

:::

:::solution

Add the history beside the existing initialisation :

```python
history = []
```

Add this case to the existing command handling :

```python
match guess:
    case "hint":
        possible = candidates(words, history)
        print(f"{len(possible)} words left, try {best_guess(possible).upper()}")
        continue
```

After `guess_count += 1` and `used_letters.update(guess)`, replace the old scoring-and-printing line with :

```python
marks = score_guess(secret, guess)
history.append((guess, marks))
print(render(guess, marks))
```

The complete integration is in `solutions/07-comprehensions/wordle/game.py`.

:::

Delete the temporary `solver_check.py` after checking the integrated game. The solver functions stay in `wordle/solver.py`.

Change the secret in `wordle/__main__.py` to another word in the list, then play a game and use `hint` after each guess. The suggestion comes from your scoring rules and the feedback recorded so far; the solver never reads the secret directly.

### If time permits

Write `solve(secret, words)` to play a whole game automatically. Start with an empty history, choose with `best_guess`, score the guess, append its feedback, and filter again until the guess is correct. Return the number of guesses used. Try the first 100 words as secrets and calculate the average. Keep this experiment separate from the interactive game.
