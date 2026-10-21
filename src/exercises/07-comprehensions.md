# Exercise 7 : Comprehensions

Your game works, but the screen is plain. The rows have no colour, `letters` only lists what you have tried, and a player who is stuck gets no help. In this exercise you make the screen friendlier, one small function at a time : coloured rows, the letters you have not tried yet, and a `hint` command that reveals a letter of the secret. Each function is a comprehension of one or two lines. An optional last step orders the untried letters so that the most useful ones come first.

Continue in your own `wordle` project, or use `exercises/starters/07-comprehensions/`, the finished Exercise 6. The solution is in `solutions/07-comprehensions/`. Start a game by opening `main.py` and pressing Play.

At the start your project looks like this. `wordle/` is the folder you have open in VS Code; the `wordle/` inside it is the package :

```text
wordle/
    pyproject.toml
    main.py              start a game here
    wordle/
        __init__.py
        display.py
        game.py
        scoring.py
        words.py
```

Some steps try a function on its own in the interpreter, as in Exercise 6. Open the terminal in VS Code, check that it is in the project folder beside `pyproject.toml`, and start it with `uv run python`. The interpreter keeps the version of a file that it imported first : after you save a change, leave it with `exit()`, start it again and repeat the import.

### Step 1 : A row in one expression

:::task
In `wordle/display.py`, build the row of `render` with a generator expression inside `"".join(...)`. The row it returns stays the same.
:::

```text
wordle/
    main.py
    wordle/
        display.py       <- change render
```

#### 1a

Keep the docstring at the top of `wordle/display.py` and replace the rest of the file with this version. It does the same as your `render`, but it looks up the piece for each letter in a dictionary instead of using `match` :

```python
SYMBOLS = {
    "green": lambda letter: f"[{letter}]",
    "yellow": lambda letter: f"({letter})",
    "grey": lambda letter: f" {letter} ",
}


def render(guess: str, marks: list[str]) -> str:
    """Draw green letters in brackets, yellow in parentheses and grey padded."""
    pieces = []
    for letter, mark in zip(guess.upper(), marks, strict=True):
        pieces.append(SYMBOLS[mark](letter))
    return "".join(pieces)
```

Each value in `SYMBOLS` is a small function written as a lambda. `SYMBOLS["green"]` is the function for a green letter, and calling it with `"A"` gives `"[A]"`. `zip` pairs each letter with its mark. Try both in the interpreter :

```text
>>> from wordle.display import SYMBOLS, render
>>> SYMBOLS["green"]("A")
'[A]'
>>> SYMBOLS["yellow"]("B")
'(B)'
>>> render("react", ["yellow", "yellow", "green", "yellow", "grey"])
'(R)(E)[A](C) T '
```

The row must match Exercise 6 before you change how it is built.

:::hint
The slide *Lambda Functions*, in module 05, shows a small function written as an expression, and *Functions in Dictionaries* selects and calls a function through a dictionary. *Zip Function*, in module 07, pairs two sequences; `strict=True` rejects lists of different lengths.
:::

#### 1b

Replace the `pieces` list, its loop and the final `return` with one `return`. Fill in the expression that makes one piece of the row :

```python
    return "".join(... for letter, mark in zip(guess.upper(), marks, strict=True))
```

Save, restart the interpreter and repeat the `render` call. The result is the same row.

:::hint
The slide *Generator Expressions* puts an expression and its `for` part inside a function call. The expression is the `SYMBOLS[mark](letter)` that the loop passed to `append`.
:::

:::solution
```python
def render(guess: str, marks: list[str]) -> str:
    """Draw green letters in brackets, yellow in parentheses and grey padded."""
    return "".join(SYMBOLS[mark](letter) for letter, mark in zip(guess.upper(), marks, strict=True))
```
:::

### Step 2 : Colour

:::task
Install `rich`, add a function `colour_row` to `wordle/display.py`, and let `play` in `wordle/game.py` print each row in colour.
:::

```text
wordle/
    pyproject.toml       <- uv add records rich here
    main.py
    wordle/
        display.py       <- add COLOURS and colour_row
        game.py          <- print the row with rich
```

#### 2a

In the terminal, in the project folder, install the package :

```bash
uv add rich
```

`pyproject.toml` now lists `rich` under `dependencies`. If pressing Play on `main.py` later reports `No module named 'rich'`, VS Code is using another Python : press Ctrl+Shift+P, choose `Python: Select Interpreter` and pick the one in `.venv`.

:::hint
The slide *Installing Packages*, in module 06, shows `uv add` and what it records.
:::

#### 2b

Add the import at the top of `wordle/display.py`, below the docstring, and the dictionary of colours below `SYMBOLS` :

```python
from rich.text import Text
```

```python
COLOURS = {
    "green": "bold white on green",
    "yellow": "bold black on yellow",
    "grey": "white on grey35",
}
```

Then add `colour_row` at the end of the file. It makes the same pieces as `render`, but each piece is a `Text` with the colour of its mark. Fill in the text and the style of one piece :

```python
def colour_row(guess: str, marks: list[str]) -> Text:
    """Draw the same row as render, with a background colour for each mark."""
    return Text("").join(
        Text(..., style=...)
        for letter, mark in zip(guess.upper(), marks, strict=True)
    )
```

Restart the interpreter and print a row with a `Console` :

```text
>>> from rich.console import Console
>>> from wordle.display import colour_row
>>> Console().print(colour_row("react", ["yellow", "yellow", "green", "yellow", "grey"]))
(R)(E)[A](C) T
```

In the terminal the letters have a yellow, green or grey background.

:::hint
The slide *Colour Output with rich*, in module 06, makes a `Text` with a style and joins styled pieces with `Text(" ").join`. Here the separator is `Text("")`, nothing, just as `""` is in `render`.
:::

:::hint
The text of a piece is the same `SYMBOLS[mark](letter)` as in `render`. Its style is the colour of the mark : `COLOURS[mark]`.
:::

:::solution
```python
def colour_row(guess: str, marks: list[str]) -> Text:
    """Draw the same row as render, with a background colour for each mark."""
    return Text("").join(
        Text(SYMBOLS[mark](letter), style=COLOURS[mark])
        for letter, mark in zip(guess.upper(), marks, strict=True)
    )
```
:::

#### 2c

In `wordle/game.py`, import the console and the new function, and make one console below the imports :

```python
from rich.console import Console

from wordle.display import colour_row
from wordle.scoring import is_valid, score_guess

console = Console()
```

`render` is no longer used in this file, so its import goes. In `play`, the row is printed with `print(render(...))`. Print it with `console.print(colour_row(...))` instead, with the same two arguments. Press Play on `main.py`, enter `slate`, then `crane`.

:::output

Captured output with typed input omitted. In the terminal each letter also has its colour.

```text
Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.
Guess 1/6 :  S  L [A] T [E]
Guess 2/6 : [C][R][A][N][E]
Got it in 2!
```

:::

:::hint
The slide *Colour Output with rich* prints a `Text` with `console.print`. A plain `print` would show the text without colour.
:::

:::solution
```python
        console.print(colour_row(guess, score_guess(secret, guess)))
```
:::

### Step 3 : Letters you have not tried

:::task
Create `wordle/hints.py` with a function `letters_left`, and let the `letters` command also print the letters that have not been tried.
:::

```text
wordle/
    main.py
    wordle/
        game.py          <- extend the letters command
        hints.py         <- new
```

#### 3a

Create `wordle/hints.py` with this loop version :

```python
"""Help the player choose the next guess."""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def letters_left(used: set[str]) -> list[str]:
    """Return the letters of the alphabet that have not been tried yet."""
    left = []
    for letter in ALPHABET:
        if letter not in used:
            left.append(letter)
    return left
```

Try it with the letters of `slate` :

```text
>>> from wordle.hints import letters_left
>>> " ".join(letters_left({"s", "l", "a", "t", "e"}))
'b c d f g h i j k m n o p q r u v w x y z'
```

#### 3b

Replace the list, the loop and the `return` with a filtered list comprehension. Fill in both parts :

```python
    return [... for letter in ALPHABET if ...]
```

Restart the interpreter and repeat the call. The result is the same.

:::hint
The slide *Filtered List Comprehension* keeps only the items that pass the `if`. The expression is the value that the loop appended, and the condition is the one of the loop's `if`.
:::

:::solution
```python
def letters_left(used: set[str]) -> list[str]:
    """Return the letters of the alphabet that have not been tried yet."""
    return [letter for letter in ALPHABET if letter not in used]
```
:::

#### 3c

In `wordle/game.py`, add `from wordle.hints import letters_left` to the imports. In the `letters` case of `play`, keep the line that prints the letters tried and add a second line below it :

```python
                print("Not tried :", " ".join(letters_left(used_letters)))
```

Press Play on `main.py`, enter `slate`, then `letters`, then `quit`. The `letters` command prints :

:::output

```text
Tried : a e l s t
Not tried : b c d f g h i j k m n o p q r u v w x y z
```

:::

### Step 4 : A hint

:::task
Add a function `hint` to `wordle/hints.py`, and a `hint` command to `play` that tells the player one letter of the secret they have not tried yet.
:::

```text
wordle/
    main.py              <- mention 'hint' in the welcome message
    wordle/
        game.py          <- add case "hint"
        hints.py         <- add hint
```

#### 4a

Write `hint` in `wordle/hints.py`. It returns the first letter of `secret` that is not in `used` :

```python
def hint(secret: str, used: set[str]) -> str:
    """Return the first letter of the secret that has not been tried yet."""
```

```text
>>> from wordle.hints import hint
>>> hint("crane", {"s", "l", "a", "t", "e"})
'c'
>>> hint("crane", {"c", "r"})
'a'
```

:::hint
This is `letters_left` again, with the letters of `secret` instead of `ALPHABET`. The slide *Filtered List Comprehension* shows the form.
:::

:::hint
Keep the untried letters in a list, `untried = [...]`, and return its first item, `untried[0]`.
:::

:::solution
```python
def hint(secret: str, used: set[str]) -> str:
    """Return the first letter of the secret that has not been tried yet."""
    untried = [letter for letter in secret if letter not in used]
    return untried[0]
```
:::

#### 4b

In `wordle/game.py`, import `hint` too, so that the line reads `from wordle.hints import hint, letters_left`. Add a case to the `match guess` in `play`, below the `letters` case. Like `letters`, it must not use a turn :

```python
            case "hint":
                print(f"The word contains the letter {...}.")
                continue
```

In `main.py`, change the welcome message to `"Guess the five-letter word. Type 'quit', 'letters' or 'hint'."`. Keep `secret = "crane"`, press Play and enter `slate`, `hint`, then `crane` :

:::output

Captured output with typed input omitted. The hint leaves the prompt at guess 2.

```text
Guess the five-letter word. Type 'quit', 'letters' or 'hint'.
Guess 1/6 :  S  L [A] T [E]
Guess 2/6 : The word contains the letter C.
Guess 2/6 : [C][R][A][N][E]
Got it in 2!
```

:::

:::hint
The slide *match Statement*, in module 04, shows the form; the `letters` case already ends with `continue`. Inside the braces, call `hint(secret, used_letters)` and add `.upper()`.
:::

:::solution
```python
            case "hint":
                print(f"The word contains the letter {hint(secret, used_letters).upper()}.")
                continue
```

The complete game is in `solutions/07-comprehensions/wordle/game.py`.
:::

Change the secret in `main.py` to another word in the list and play a game with `letters` and `hint`, then restore `"crane"`. Ask for a hint while the word still has a letter you have not tried; Exercise 12 deals with the other case.

### Step 5 : The most useful letters first (optional)

:::task
Add `letter_counts` and `most_common_first` to `wordle/hints.py`, so that `letters` lists the untried letters that occur most in the word list first.
:::

```text
wordle/
    main.py
    wordle/
        game.py          <- use most_common_first
        hints.py         <- add two functions
```

A letter that occurs in many words is a good letter to try next. Count each letter first, then sort by that count. This step is extra practice with a dictionary comprehension and a lambda; Exercise 8 starts from the game without it.

#### 5a

Join the words into one string and count a letter in it. Try this in the interpreter :

```text
>>> words = ["crane", "geese", "slate"]
>>> text = "".join(words)
>>> text
'cranegeeseslate'
>>> text.count("e")
5
>>> text.count("z")
0
```

Add `letter_counts` to `wordle/hints.py`. It returns a dictionary with every letter of the alphabet as a key and its count in the text as the value. Fill in the key and the value :

```python
def letter_counts(words: list[str]) -> dict[str, int]:
    """Count how often each letter of the alphabet occurs in the words."""
    text = "".join(words)
    return {...: ... for letter in ALPHABET}
```

```text
>>> from wordle.hints import letter_counts
>>> counts = letter_counts(["crane", "geese", "slate"])
>>> counts["e"]
5
>>> counts["c"]
1
```

:::hint
The slide *Dictionary Comprehensions* writes `key: value` before the `for`. *Built-in String Methods*, in module 02, lists `count`. The key is the letter, the value is `text.count(letter)`.
:::

:::solution
```python
def letter_counts(words: list[str]) -> dict[str, int]:
    """Count how often each letter of the alphabet occurs in the words."""
    text = "".join(words)
    return {letter: text.count(letter) for letter in ALPHABET}
```
:::

#### 5b

`sorted` can order the letters by their counts. A lambda tells it which value to compare : for each letter, its count. Keep `counts` from 5a and try :

```text
>>> sorted(["c", "e", "z"], key=lambda letter: counts[letter])
['z', 'c', 'e']
>>> sorted(["c", "e", "z"], key=lambda letter: counts[letter], reverse=True)
['e', 'c', 'z']
```

Now write `most_common_first` in `wordle/hints.py` yourself. It counts the letters of `words` and returns `letters` sorted with the highest count first :

```python
def most_common_first(letters: list[str], words: list[str]) -> list[str]:
    """Sort the letters so that the ones used most in the words come first."""
```

```text
>>> from wordle.hints import most_common_first
>>> most_common_first(["c", "e", "z"], ["crane", "geese", "slate"])
['e', 'c', 'z']
```

:::hint
The slide *A lambda as the Key* sorts titles by their play counts with `reverse=True`. Here the play counts are the letter counts.
:::

:::hint
Two lines : `counts = letter_counts(words)`, then `return sorted(...)` with the same `key` and `reverse` as in the interpreter.
:::

:::solution
```python
def most_common_first(letters: list[str], words: list[str]) -> list[str]:
    """Sort the letters so that the ones used most in the words come first."""
    counts = letter_counts(words)
    return sorted(letters, key=lambda letter: counts[letter], reverse=True)
```
:::

#### 5c

In `wordle/game.py`, import `most_common_first` as well. In the `letters` case, replace the line from 3c with these two lines :

```python
                left = most_common_first(letters_left(used_letters), words)
                print("Not tried, most common first :", " ".join(left))
```

`words` is the word list that `play` already receives. Press Play on `main.py`, enter `slate`, then `letters`, then `quit`. The `letters` command prints :

:::output

```text
Tried : a e l s t
Not tried, most common first : r o c g h p d i n k m u w y b f j q v x z
```

:::

Of the letters not tried, R and O occur most often in the practice words, so they come first. Letters that do not occur at all stay in alphabetical order at the end, because `sorted` keeps the original order of equal values.

### If time permits

- Colour the `letters` list : show the untried letters in green and the tried ones in grey, with `Text(" ").join(...)` and a `Text` for each letter of `ALPHABET`. Pick the style with `"green" if letter in left else "grey50"`.
- Suggest a whole word. Score a word by adding the counts of its distinct letters, `sum(counts[letter] for letter in set(word))`, and let `max(words, key=lambda word: ...)` pick the word with the highest score. Try it for the practice words after a few guesses.
