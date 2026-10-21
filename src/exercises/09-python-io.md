# Exercise 9 : Python IO

Your game uses a small word list written directly in Python, and the moment a game ends the result is gone. In this exercise you clean a real word list, make the game find its data wherever it is started from, and keep a history of every game on disk.

Continue in your own `wordle` project, or start from `exercises/starters/09-python-io/`. The starter is the finished Exercise 8 plus this exercise's handouts : `raw-words.txt`, `allowed.txt` and `SOURCES.md`. If you continue in your own project, copy those three files in from `exercises/handouts/09-python-io/` to the project folder, beside `main.py`. The solution is in `solutions/09-python-io/`. Start a game by pressing Play on `main.py`.

Some steps give you the code, some a skeleton to complete, and some only a description of what to write. Where you write the code yourself, the solution is hidden until you open it. Try the step first; the solution is there for when you are stuck, or to compare afterwards.

---

### Step 1 : Clean a messy word list

:::task
Write `clean_words` in `wordle/words.py`. It turns the lines of a messy file into a clean, sorted list of five-letter words.
:::

```text
wordle/
    main.py
    raw-words.txt        the messy list, from the handouts
    wordle/
        words.py         <- add clean_words
```

`raw-words.txt` is what a word list looks like when it comes from the outside world : almost a thousand lines with some words in capitals, some duplicates, a few lines of the wrong length, a number, a word with an accent, and an empty line. Open it in the editor and scroll to the bottom to see for yourself.

Your game wants one word per line : lower case, five letters, ASCII letters only, no duplicates, in alphabetical order. Write a function in `wordle/words.py` that turns the lines of a file into such a list :

```python
def clean_words(lines: list[str]) -> list[str]:
    """Return unique lowercase five-letter ASCII words in sorted order."""
    kept = set()
    for line in lines:
        word = line.strip().lower()
        if ...:
            kept.add(word)
    return ...
```

Replace each `...` : the condition that keeps a word, and the sorted list that is returned. `str.isalpha()` is also `True` for letters with an accent, so a five-letter word such as `étage` would pass it; `str.isascii()` is `True` only when every character is plain ASCII, which rules it out.

Try the function in the interpreter, as in Exercise 8. Capitals, duplicates and empty lines disappear, and so do words of the wrong length, numbers and accents :

```python
clean_words(["Slate", "crane", "CRANE", ""])              # ['crane', 'slate']
clean_words(["cranes", "12345", "étage", " adieu "])      # ['adieu']
```

:::hint
The slide *Built-in String Methods*, in module 02, has `strip`, `lower` and `isalpha`, and *Set Operations*, in module 03, shows that a set keeps each value once and that `sorted` returns a list.
:::

:::hint
Strip the whitespace from each line before you look at it, then check its length, `isascii()` and `isalpha()`.
:::

:::hint
A set throws duplicates away. Add a cleaned word with `kept.add(word)` only when all three checks pass; return `sorted(kept)` after the loop.
:::

:::solution
```python
def clean_words(lines: list[str]) -> list[str]:
    """Return unique lowercase five-letter ASCII words in sorted order."""
    kept: set[str] = set()
    for line in lines:
        word = line.strip().lower()
        if len(word) == 5 and word.isascii() and word.isalpha():
            kept.add(word)
    return sorted(kept)
```

The loop cleans each line once, checks that cleaned word, and adds it to the set. `sorted(kept)` returns a list in alphabetical order, matching the skeleton above.
:::

### Step 2 : Write the clean list

:::task
In the interpreter, clean `raw-words.txt` once and write the result to `wordle/data/words.txt`. Copy `allowed.txt` and `SOURCES.md` into the same folder.
:::

```text
wordle/
    main.py
    raw-words.txt
    allowed.txt          from the handouts, copy into wordle/data/
    SOURCES.md           from the handouts, copy into wordle/data/
    wordle/
        data/            <- new folder
            words.txt    <- written by the interpreter
            allowed.txt
            SOURCES.md
```

Cleaning is done once, not every time the game starts, so use a throwaway session instead of a script. Start Python in the project folder and type this, line by line :

```bash
uv run python
```

```python
from pathlib import Path
from wordle.words import clean_words

lines = Path("raw-words.txt").read_text(encoding="utf-8").splitlines()
words = clean_words(lines)
len(lines), len(words)

Path("wordle/data").mkdir(exist_ok=True)
Path("wordle/data/words.txt").write_text("\n".join(words) + "\n", encoding="utf-8")
```

`splitlines()` cuts the text into a list with one line per item. The session answers with the number of lines read and the number of words kept. The last line returns the number of characters written. Leave Python with `exit()`.

```text
(981, 935)
5610
```

The folder `wordle/data/` is inside the package, next to the code that will read it. The existing loader still returns the practice list. Step 3 replaces it with a file reader.

Also copy the handed-out `allowed.txt` and `SOURCES.md` into `wordle/data/`. You use `allowed.txt` in Step 4; `SOURCES.md` records where the word lists come from.

:::hint
The slides *Reading Text Files*, *Creating and Removing Directories* and *Writing Text Files* show reading, making a folder and writing text with `Path`.
:::

### Step 3 : Find the file from the package

:::task
Let `load_words` read `wordle/data/words.txt`, wherever the game is started from. In `main.py`, print a message instead of a traceback when the file is missing.
:::

```text
wordle/
    main.py              <- catch FileNotFoundError
    wordle/
        words.py         <- load_words reads the file
        data/
            words.txt
```

Replace the practice-list function in `wordle/words.py` with a file reader. Add `from pathlib import Path` at the top of the module.

First try a path relative to the project folder :

```python
def load_words() -> list[str]:
    """Read the answer list from the project folder."""
    data_path = Path("wordle/data/words.txt")
    text = data_path.read_text(encoding="utf-8")
    return text.split()
```

Start `uv run python` in the project folder and check the new loader, then change the working directory :

```python
import os
from wordle.words import load_words

print(len(load_words()))  # 935
os.chdir("wordle")
load_words()
```

```text
FileNotFoundError: [Errno 2] No such file or directory: 'wordle/data/words.txt'
```

A relative path is resolved against the working directory. Leave Python with `exit()` before editing the loader. Build the path from the module's own location instead :

```python
def load_words() -> list[str]:
    """Read the package answer list, independent of the working directory."""
    data_path = Path(__file__).parent / "data" / "words.txt"
    return data_path.read_text(encoding="utf-8").split()
```

`Path(__file__).parent` is the folder containing `words.py`; `/` joins path parts. Start a fresh interpreter and repeat both checks. `len(load_words())` now returns `935` from either folder. Leave Python and press Play on `main.py`.

:::hint
The slide *Paths Relative to a Module* builds a path from `__file__`, and *Paths with pathlib* shows joining path parts with `/`. Save the changed loader before starting a new interpreter session.
:::

File loading adds a possible failure. Add this handler before the existing interruption handler in `main` of `main.py`. Step 4 adds the second file named in the message :

```python
    except FileNotFoundError:
        print(
            "A word list is missing. Restore wordle/data/words.txt "
            "and wordle/data/allowed.txt and try again."
        )
```

:::hint
The slide *Typed Exception Handling* shows an `except FileNotFoundError` clause. Temporarily rename `wordle/data/words.txt`, run the game and check the message, then restore the filename.
:::

### Step 4 : Two lists, answers and allowed guesses

:::task
Add `load_allowed` to `wordle/words.py`, and let `play` accept every word of `allowed.txt` as a guess.
:::

```text
wordle/
    main.py
    wordle/
        game.py          <- check guesses against the allowed words
        words.py         <- add load_allowed
        data/
            allowed.txt
```

You have been using one list for two jobs : the words the game can pick as a secret, and the words it accepts as a guess. A player should not be told that a perfectly good word is not a word, but the secret should be a word they have a fair chance of knowing. The real game uses two lists for this, and now your project does too :

- `wordle/data/words.txt` : the 935 common words the game picks its secret from, and the words the `letters` command counts letters in
- `wordle/data/allowed.txt` : 8 639 words the game accepts as a guess, including all of the answers

Add a second loader to `wordle/words.py`, next to `load_words` :

```python
def load_allowed() -> list[str]:
    """Read every allowed guess from the package data folder."""
    ...
```

Then change `play` in `wordle/game.py`. Load the allowed list once, at the top of the function, and check guesses against it, instead of against `words`. Everything else keeps using `words`.

Keep `secret = "crane"` in `main.py` and press Play. `crone` is a word the game used to reject, and it is accepted now :

```text
[C][R] O [N][E]
```

:::hint
The slide *Paths with pathlib* shows `/` joining the parts of a path. The body of `load_allowed` is `load_words` with another file name; you may copy it.
:::

:::hint
The change in `play` is two lines : `allowed_words = load_allowed()` before the loop, and `check_guess(guess, allowed_words)` in the `try` block. `most_common_first(..., words)` in the `letters` command keeps using `words`.
:::

:::solution
```python
def load_allowed() -> list[str]:
    """Read every allowed guess from the package data folder."""
    data_path = Path(__file__).parent / "data" / "allowed.txt"
    return data_path.read_text(encoding="utf-8").split()
```

In `wordle/game.py` add `from wordle.words import load_allowed` and change the start of `play` and the validation :

```python
def play(secret: str, words: list[str], max_guesses: int = 6) -> bool:
    """Play one game and return whether the player found the secret."""
    used_letters = set()
    guess_count = 0
    allowed_words = load_allowed()
    while guess_count < max_guesses:
        ...
        try:
            check_guess(guess, allowed_words)
        except InvalidGuess as error:
            print(error)
            continue
```
:::

### Step 5 : Keep a history file

:::task
Add `record_history` to `wordle/game.py` and call it when a game ends, so that `history.txt` gets one line per game.
:::

```text
wordle/
    main.py
    history.txt          <- written by record_history
    wordle/
        game.py          <- add history_path and record_history
```

A finished game should leave a line behind. One line per game, such as `crane,2,1`, holds the secret, the number of guesses used and `1` for a win or `0` for a loss. That is a CSV file, and the `csv` module knows how to write one. Read *The csv Module* first.

Put the history file in the project folder, next to the `wordle/` package, and for the same reason as in Step 3 do not let it depend on the working directory. This function is given, add it to `wordle/game.py` together with `from pathlib import Path` and `import csv` at the top :

```python
def history_path() -> Path:
    """Return the history file beside the project package."""
    return Path(__file__).resolve().parents[1] / "history.txt"
```

`Path(__file__).resolve()` is the full path of `game.py`; `parents[0]` is the `wordle/` folder and `parents[1]` is the project folder. Now write the function that adds a line :

```python
def record_history(secret: str, guesses: int, won: bool) -> None:
    """Append one finished game to the CSV history file."""
    with history_path().open(..., encoding="utf-8", newline="") as history_file:
        ...
```

Open the file for **appending** with `"a"`, so earlier games stay. See *File Open Modes* and *Using with*. Inside the `with`, give `csv.writer` the row `[secret, guesses, int(won)]`. Then call `record_history` in `play` : once with `True` just before the `return True` of a win, and once with `False` after the loop, before the final `return False`. A game you give up with `quit` counts as lost.

Play two games with `secret = "crane"` in `main.py` : guess `slate` and then `crane` in the first, and `slate` followed by `quit` in the second. Open `history.txt`:

```text
crane,2,1
crane,1,0
```

:::hint
The slide *The csv Module* writes rows with `csv.writer` inside a `with` block, and *File Open Modes* lists `a` for appending.
:::

:::hint
`csv.writer(history_file).writerow([...])` writes one row and adds the line ending itself. `newline=""` stops Python from adding its own line ending on top of the one the `csv` module writes.
:::

:::hint
`won` is a `bool`. `int(True)` is `1` and `int(False)` is `0`, which makes the file easy for other tools to read.
:::

:::solution
```python
def record_history(secret: str, guesses: int, won: bool) -> None:
    """Append one finished game to the CSV history file."""
    with history_path().open("a", encoding="utf-8", newline="") as history_file:
        csv.writer(history_file).writerow([secret, guesses, int(won)])
```

The calls in `play`:

```python
        if guess == secret:
            print(f"Got it in {guess_count}!")
            record_history(secret, guess_count, True)
            return True
    print(f"The word was {secret.upper()}.")
    record_history(secret, guess_count, False)
    return False
```
:::

### Step 6 : A stats command

:::task
Add a `stats` command to `play` that reads `history.txt` and prints how many games were played and won.
:::

```text
wordle/
    main.py              <- list 'stats' in the welcome message
    history.txt
    wordle/
        game.py          <- add case "stats" and print_stats
```

Reading the file back is the other half. Add a new command to `play`, next to `quit`, `letters` and `hint`, so that typing `stats` prints how many games were played and how many were won :

```python
            case "stats":
                print_stats()
                continue
```

The function is given, because Exercise 10 replaces it with a database query. Add it to `wordle/game.py` :

```python
def print_stats() -> None:
    """Read the CSV history and print game and win totals."""
    path = history_path()
    if not path.exists():
        print("Games played: 0; won: 0.")
        return
    with path.open(encoding="utf-8", newline="") as history_file:
        rows = list(csv.reader(history_file))
    wins = sum(row[2] == "1" for row in rows)
    print(f"Games played: {len(rows)}; won: {wins}.")
```

Read it line by line :

- The `return` on its own line leaves the function early when there is no history file yet, so the rest does not need an `else`.
- Every field read from a CSV file is a string, so the wins are the rows whose third column equals `"1"`, not the number `1`.
- `sum(...)` over conditions counts how many are true, because `True` is `1`.

Also change the welcome line in `main.py` so it lists the commands the game now knows :

```python
        print(
            "Guess the five-letter word. Type 'quit', 'letters', "
            "'hint' or 'stats'."
        )
```

The game is playable again, with a memory. After the two games of Step 5, type `stats` at the first prompt of a new game :

:::hint
The slide *Reading CSV Rows by Name* explains reading CSV data, and *Generator Expressions*, in module 07, shows summing conditions. Keep `print_stats` outside `play`, beside the other functions.
:::

```text
Games played: 2; won: 1.
```

The complete project is in `solutions/09-python-io/`.

### If time permits

Add a `last` command that prints the final five games from `history.txt`, newest first, one per line in the form `CRANE : won in 2` or `CRANE : lost`. Slicing and `reversed()` do the work. There is no reference solution for this step.
