# Exercise 9 : Python IO

Your game plays well, but it lives on borrowed data and it has no memory. The word list is a file you typed by hand, it is only found when you start the game from the right folder, and the moment a game ends the result is gone. In this exercise you clean a real word list, make the game find its data wherever it is started from, and keep a history of every game on disk.

Continue in your own `wordle` project, or start from `exercises/starters/09-python-io/`. The starter is the finished Exercise 8 plus this exercise's handouts : `raw-words.txt`, `allowed.txt` and `tests/test_words.py`. If you continue in your own project, copy those three files in from `exercises/handouts/09-python-io/`.

Every step is marked with how much help it gives :

- ★ the code is given; type it in and read it
- ★★ a skeleton is given; you fill in the body
- ★★★ only the signature and the tests are given

Steps marked ★★ have a solution that is hidden until you open it. Try the step first; the solution is there for when you are stuck, or to compare afterwards. Allow about 45 minutes.

---

### Step 1 : Clean a messy word list {★★}

`raw-words.txt` is what a word list looks like when it comes from the outside world : almost a thousand lines with some words in capitals, some duplicates, a few lines of the wrong length, a number, a word with an accent, and an empty line. Open it in the editor and scroll to the bottom to see for yourself.

Your game wants one word per line : lower case, five letters, ASCII letters only, no duplicates, in alphabetical order. Write a function in `wordle/words.py` that turns the lines of a file into such a list :

```python
def clean_words(lines: list[str]) -> list[str]:
    """Return unique lowercase five-letter ASCII words in sorted order."""
    ...
```

The handout `tests/test_words.py` checks it. Run `uv run pytest tests/test_words.py` and see it fail, because `clean_words` does not exist yet. Write the function until it passes. Read the slide *Reading Text Files* if you want to see how lines come out of a file.

:::hint
Strip the whitespace from each line before you look at it. `str.isalpha()` is also `True` for letters with an accent, so a five-letter word such as `étage` would pass it. `str.isascii()` rules it out.
:::

:::hint
A set throws duplicates away and `sorted(...)` turns it back into a list. A set comprehension can hold the whole filter : `{line.strip().lower() for line in lines if ...}`.
:::

:::output
```text
.                                                                        [100%]
1 passed in 0.01s
```
:::

:::solution
```python
def clean_words(lines: list[str]) -> list[str]:
    """Return unique lowercase five-letter ASCII words in sorted order."""
    return sorted(
        {
            line.strip().lower()
            for line in lines
            if len(line.strip()) == 5
            and line.strip().isascii()
            and line.strip().isalpha()
        }
    )
```

The condition strips each line three times, which is easy to read and fast enough for a thousand lines.
:::

### Step 2 : Write the clean list {★}

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

The session answers with the number of lines read and the number of words kept. The last line returns the number of characters written. Leave Python with `exit()`.

```text
(981, 935)
5610
```

The folder `wordle/data/` is inside the package, next to the code that reads it. Data that belongs to the program travels with the program. Now `wordle/data/words.txt` is the answer list, and the old `words.txt` in the project folder is no longer needed : delete it, so that nothing can keep using it by accident. It held the same 935 words.

Also copy the handed-out `allowed.txt` into `wordle/data/`. You use it in Step 4.

### Step 3 : Find the file from the package {★}

Your `load_words` still opens `words.txt` as a path relative to wherever the program was started. Try what that means. Start Python in the project folder again and import the function first, because after the change of folder Python can no longer find the `wordle` package. Then change the working directory :

```python
import os
from wordle.words import load_words

os.chdir("tests")
load_words()
```

```text
FileNotFoundError: [Errno 2] No such file or directory: 'words.txt'
```

A relative path is resolved against the working directory, and the working directory belongs to whoever starts the program, not to the program. The same holds for a game started from a shortcut, from a test runner or from an editor in another folder.

The fix is to ask the module where it lives. Every module knows its own file name in `__file__`, and `pathlib` turns that into a folder you can build a path from. Replace `load_words` in `wordle/words.py`:

```python
def load_words() -> list[str]:
    """Read the package answer list, independent of the working directory."""
    data_path = Path(__file__).parent / "data" / "words.txt"
    return data_path.read_text(encoding="utf-8").split()
```

`Path(__file__).parent` is the `wordle/` folder, and the `/` operator joins path parts. See *Paths with pathlib*. The `path` parameter is gone, because the function no longer needs to be told where the file is. Repeat the experiment in the new session; it now returns the list from any working directory :

```text
935
```

Run `uv run python -m wordle` and check that the game still starts. A game started now no longer depends on a `words.txt` in the project folder.

### Step 4 : Two lists, answers and allowed guesses {★★}

You have been using one list for two jobs : the words the game can pick as a secret, and the words it accepts as a guess. A player should not be told that a perfectly good word is not a word, but the secret should be a word they have a fair chance of knowing. The real game uses two lists for this, and now your project does too :

- `wordle/data/words.txt` : the 935 common words the game picks its secret from, and the words the `hint` command searches
- `wordle/data/allowed.txt` : 8 639 words the game accepts as a guess, including all of the answers

Add a second loader to `wordle/words.py`, next to `load_words` :

```python
def load_allowed() -> list[str]:
    """Read every allowed guess from the package data folder."""
    ...
```

Then change `play` in `wordle/game.py`. Load the allowed list once, at the top of the function, and check guesses against it, instead of against `words`. Everything else keeps using `words`.

Play with `WORDLE_SECRET=crane` set. This is the environment variable that `main` has read since Exercise 5, and it fixes the secret word. In a bash shell, put it in front of the command : `WORDLE_SECRET=crane uv run python -m wordle`. In PowerShell, set it once with `$env:WORDLE_SECRET = "crane"` and then run the command as usual. `crone` is a word the game used to reject, and it is accepted now :

```text
[C][R] O [N][E]
```

:::hint
The body of `load_allowed` is `load_words` with another file name. You may copy it.
:::

:::hint
The change in `play` is two lines : `allowed_words = load_allowed()` before the loop, and `check_guess(guess, allowed_words)` in the `try` block. `candidates(words, history)` for the `hint` command stays as it is.
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
    history = []
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

### Step 5 : Keep a history file {★★}

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
    ...
```

Open the file for **appending** with `"a"`, so earlier games stay. See *File Open Modes* and *Using with*. Open it with `newline=""` and give `csv.writer` the row `[secret, guesses, int(won)]`. Then call `record_history` in `play` : once with `True` just before the `return True` of a win, and once with `False` after the loop, before the final `return False`. A game you give up with `quit` counts as lost.

Play two games with `WORDLE_SECRET=crane` : guess `slate` and then `crane` in the first, and `slate` followed by `quit` in the second. Open `history.txt`:

```text
crane,2,1
crane,1,0
```

:::hint
`csv.writer(history_file).writerow([...])` writes one row and adds the line ending itself. Open the file in `"a"` mode with `encoding="utf-8"` as well, to be explicit about the text encoding.
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

### Step 6 : A stats command {★★}

Reading the file back is the other half. Add a new command to `play`, next to `quit`, `letters` and `hint`, so that typing `stats` prints how many games were played and how many were won :

```python
            case "stats":
                print_stats()
                continue
```

Write `print_stats` in `wordle/game.py` :

```python
def print_stats() -> None:
    """Read the CSV history and print game and win totals."""
    path = history_path()
    if not path.exists():
        ...
    with path.open(encoding="utf-8", newline="") as history_file:
        rows = list(csv.reader(history_file))
    ...
```

Print `Games played: 0; won: 0.` when there is no history file yet. Otherwise count the rows, and count the rows whose third column is `"1"`. Every field read from a CSV file is a string, so compare with `"1"` and not with the number `1`. Also change the welcome line in `wordle/__main__.py` so it lists the commands the game now knows :

```python
        print(
            "Guess the five-letter word. Type 'quit', 'letters', "
            "'hint' or 'stats'."
        )
```

The game is playable again, with a memory. After the two games of Step 5, type `stats` at the first prompt of a new game :

```text
Games played: 2; won: 1.
```

:::hint
Return early from the `if` when the file is missing, the way a guard clause does, so the rest of the function does not have to be indented in an `else`.
:::

:::hint
`sum(...)` over a generator expression of conditions counts how many are true, because `True` is `1` : `sum(row[2] == "1" for row in rows)`.
:::

:::solution
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

The `return` on its own line leaves the function early. The complete project is in `solutions/09-python-io/`.
:::

### If time permits

Add a `last` command that prints the final five games from `history.txt`, newest first, one per line in the form `CRANE : won in 2` or `CRANE : lost`. Slicing and `reversed()` do the work. There is no reference solution for this step.
