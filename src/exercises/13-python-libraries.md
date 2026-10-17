<!-- appendix -->
# Exercise 13 : Python Libraries

Your Wordle plays well, but it is still a game for one person, one sitting and one list of rules. The standard library has what it takes to change that without installing anything : `datetime` gives everybody the same word on the same day, `json` lets a game wait until you come back, `re` checks input with a pattern, and `sys.argv` turns options on and off from the command line. The third-party test runner `pytest`, which you add in Step 3, lets you check your own work. Each step uses one of them.

Continue in your own `wordle` project, or start from `exercises/starters/13-python-libraries/`. The starter is the finished Exercise 12; this exercise hands out nothing. Keep running commands beside `pyproject.toml`.

The steps are small and separate, one library each. Do Steps 1 to 3 in order, because they build up `main` and the options of the game. Step 4 (`json`) and Step 5 (`re`) can then be done in either order. Step 6 and Step 7 (`pytest`) come last, because they test what the earlier steps wrote; Step 3 sets `pytest` up.

Some steps give you the code, some a skeleton to complete, and some only a signature and the test it must pass. Where you write the code yourself, the solution is hidden until you open it. Try the step first; the solution is there for when you are stuck, or to compare afterwards. This exercise is an appendix : pick the libraries you want.

---

### Step 1 : The daily word

Everybody who plays today should get the same word, and tomorrow a different one. No server is needed for that : count the days since a fixed starting date, and use the count to pick from the word list. See *The datetime Module* and *Date Arithmetic with timedelta*.

Try it in a Python session first, with a fixed date so that your result is the same as the one below :

```bash
uv run python
```

```python
from datetime import date
from wordle.words import load_words

words = load_words()
today = date(2026, 10, 17)
day_number = (today - date(2026, 1, 1)).days
print(day_number, words[day_number % len(words)], len(words))
```

```text
289 drill 935
```

Subtracting two dates gives a `timedelta`, and its `.days` is a whole number. The `%` operator is the remainder after division : after 935 days the count has passed the end of the word list, and the remainder starts again at the first word. Day 289 of 2026 is the word `drill`.

Now give the game an option. In `wordle/__main__.py` add `import sys` and `from datetime import date` at the top, and let `main` choose the secret itself :

```python
        words = load_words()
        if "--daily" in sys.argv[1:]:
            day_number = (date.today() - date(2026, 1, 1)).days
            secret = words[day_number % len(words)]
        else:
            secret = os.environ.get("WORDLE_SECRET", random.choice(words))
        print(
            "Guess the five-letter word. Type 'quit', 'letters', "
            "'hint' or 'stats'."
        )
        guesses, won = play(secret, words)
```

The lines that record the game stay as they are. `sys.argv` is the list of words typed on the command line; Step 2 looks at it properly. Start the game twice with `uv run python -m wordle --daily`, type `quit` each time and compare the word it reveals. It is the same word both times.

### Step 2 : Options from the command line

`sys.argv` holds what was typed after the program name. Look at it :

```bash
uv run python -c "import sys; print(sys.argv)" --easy
```

```text
['-c', '--easy']
```

The first item is the program, the rest are the options. Read *Command-Line Arguments with sys.argv*. Reading them by hand is fine for a few flags; `argparse` is the standard answer when there are many, and is named at the end of this exercise.

Give the game two more options : `--easy` gives the player ten guesses instead of six, and `--hard` switches on hard mode, which Step 3 builds. Rewrite the part of `main` from Step 1 so that it reads the options once :

```python
        words = load_words()
        options = set(sys.argv[1:])
        if "--daily" in options:
            day_number = (date.today() - date(2026, 1, 1)).days
            secret = words[day_number % len(words)]
        else:
            secret = os.environ.get("WORDLE_SECRET", random.choice(words))
        max_guesses = ...
        hard = ...
```

Fill in `max_guesses` (`10` with `--easy`, otherwise `6`) and `hard` (a `bool`). Then pass both to `play`, as `guesses, won = play(secret, words, max_guesses, hard)`. `play` has the `max_guesses` parameter already; give it the new one, which does nothing yet :

```python
def play(secret: str, words: list[str], max_guesses: int = 6, hard: bool = False) -> tuple[int, bool]:
```

Run `uv run python -m wordle --easy`. The prompt now reads `Guess 1/10`. A guess limit of 10 is allowed by the property you wrote in Exercise 11, and 11 would not be.

:::hint
Exercise 10 gave a conditional expression for the win percentage, and the slide *Logical, Membership, Identity Operators*, in module 02, shows `in` giving `True` or `False`.
:::

:::hint
A conditional expression fits on one line : `10 if "--easy" in options else 6`. A membership test is already a `bool`, so `hard = "--hard" in options` needs no `if`.
:::

:::solution
```python
        words = load_words()
        options = set(sys.argv[1:])
        if "--daily" in options:
            day_number = (date.today() - date(2026, 1, 1)).days
            secret = words[day_number % len(words)]
        else:
            secret = os.environ.get("WORDLE_SECRET", random.choice(words))
        max_guesses = 10 if "--easy" in options else 6
        hard = "--hard" in options
        print(
            "Guess the five-letter word. Type 'quit', 'letters', "
            "'hint' or 'stats'."
        )
        guesses, won = play(secret, words, max_guesses, hard)
```
:::

### Step 3 : Hard mode

In hard mode, every guess must use what the earlier guesses revealed. Write the rule as a function in `wordle/game.py`, above `play` :

```python
def follows_hints(guess: str, history: list[tuple[str, list[Mark]]]) -> bool:
    """Return whether guess keeps green letters and includes yellow ones."""
```

For every earlier guess and its marks :

- a letter that was green must be in the same place in the new guess
- a letter that was yellow must be somewhere in the new guess

This is the first function of this exercise that gets a test. `pytest` is a development tool, like `ruff`, so add it the same way; see *Testing with pytest* :

```bash
uv add --dev pytest
```

The tests live in a folder of their own, `tests/`, and import the `wordle` package from the project folder. Tell `pytest` to look there by adding this section to `pyproject.toml` :

```toml
[tool.pytest.ini_options]
pythonpath = ['.']
```

Create `tests/test_ex13.py` for the tests of this exercise, and put this first one in it :

```python
"""The Exercise 13 tests written from scratch."""

from wordle.game import follows_hints
from wordle.scoring import Mark


def test_follows_hints_keeps_green_letters_and_uses_yellow_letters() -> None:
    history: list[tuple[str, list[Mark]]] = [
        ("crane", ["green", "grey", "yellow", "grey", "grey"])
    ]
    assert follows_hints("caper", history)
    assert not follows_hints("paper", history)
    assert not follows_hints("clink", history)
```

The history says that after `crane`, the C was in the right place, and the A was in the word but not in the third place. `caper` obeys both. `paper` moves the C, and `clink` leaves out the A. Run `uv run pytest` and make the test pass. If you wrote a `follows_hints` in the last step of Exercise 5, compare it with this one.

Then use it in `play`. When `hard` is true and there is a history, a guess that does not follow the hints is refused with `That guess does not follow the revealed hints.` and does not count. Do the check after the word is known to be valid, because the function indexes into the guess and a word of three letters would break it. Play with `uv run python -m wordle --hard`, with `WORDLE_SECRET=crane` set : guess `slate`, then `trick`.

:::hint
The slide *Zip Function*, in module 07, pairs two sequences, and *Iterating with enumerate*, in module 04, adds the position.
:::

:::hint
Loop over the history with `for previous, marks in history`. Then loop over the positions with `enumerate(zip(previous, marks, strict=True))`, which gives `position, (letter, mark)`. A `return False` the moment a rule breaks, and a `return True` after the loops.
:::

:::hint
Each rule is one condition that says when it is broken : `mark == "green" and guess[position] != letter` for the green rule, and `mark == "yellow" and letter not in guess` for the yellow rule.
:::

:::output
The end of a passing run; timings vary.

```text
tests\test_ex13.py .                                                     [100%]

============================== 1 passed in 0.03s ==============================
```
:::

:::solution
```python
def follows_hints(guess: str, history: list[tuple[str, list[Mark]]]) -> bool:
    """Return whether guess keeps green letters and includes yellow ones."""
    for previous, marks in history:
        for position, (letter, mark) in enumerate(zip(previous, marks, strict=True)):
            if mark == "green" and guess[position] != letter:
                return False
            if mark == "yellow" and letter not in guess:
                return False
    return True
```

In `play`, inside the `try` block, after `check_guess`:

```python
            check_guess(guess, allowed_words)
            if hard and game.history and not follows_hints(guess, game.history):
                print("That guess does not follow the revealed hints.")
                continue
            marks = game.guess(guess)
```
:::

### Step 4 : Save and resume

A game should survive being interrupted. `json` turns lists, dictionaries, strings and numbers into text and back again; see *The json Module*. Save the secret, the guesses and the game's settings (the guess limit and hard mode) after every guess, and load them when the game starts. The settings matter : a game that was started with `--easy` must still have ten guesses when it is resumed without the flag. Create `wordle/storage.py`. The path of the save file is given, built from the module's own location as in Exercise 9 :

```python
"""Save and restore an unfinished game in JSON format."""

import json
from pathlib import Path

from wordle.scoring import Mark

SAVE_PATH = Path(__file__).resolve().parents[1] / "save.json"
```

Write three functions with these signatures :

```python
def save_game(
    secret: str, history: list[tuple[str, list[Mark]]], max_guesses: int, hard: bool
) -> None:
    """Write the secret, the scored guesses and the game's settings to the save file."""


def load_saved_game() -> tuple[str, list[tuple[str, list[Mark]]], int, bool] | None:
    """Read a saved game, returning None when no save exists."""


def clear_saved_game() -> None:
    """Remove the save after a game is complete."""
```

Save a dictionary with the keys `"secret"`, `"history"`, `"max_guesses"` and `"hard"`, written with `json.dumps(data, indent=2)` so that you can read it. JSON has no tuples : the `(word, marks)` pairs are written as lists, and `load_saved_game` must turn them back into tuples, and return the secret, the history, the guess limit and the hard flag, in that order. See *Reading and Writing JSON Files* and *JSON and Python Types*.

Then connect the module to the game. This part is given.

In `wordle/game.py`, import the functions with `from wordle.storage import clear_saved_game, save_game`, and let `play` start from a history:

```python
def play(secret: str, words: list[str], max_guesses: int = 6, hard: bool = False,
         history: list[tuple[str, list[Mark]]] | None = None) -> tuple[int, bool]:
```

```python
    game = Game(secret, allowed_words, max_guesses)
    if history:
        game.history.extend(history)
        print(game)
    used_letters: set[str] = set()
    used_letters.update(letter for word, _ in game.history for letter in word)
```

The `print(game)` shows the restored board before the first prompt, so that a player who comes back sees where the game stood; it uses the `__str__` of Exercise 11. Save after each printed row, with `save_game(game.secret, game.history, game.max_guesses, hard)`, and call `clear_saved_game()` once the loop has ended, so that a finished game leaves no save behind.

In `wordle/__main__.py`, add `from wordle.storage import load_saved_game`, and put the saved game first, before the options decide on a new one :

```python
        words = load_words()
        options = set(sys.argv[1:])
        saved = load_saved_game()
        if saved is not None:
            secret, history, max_guesses, hard = saved
            print("Resuming your saved game.")
        else:
            history = []
            if "--daily" in options:
                day_number = (date.today() - date(2026, 1, 1)).days
                secret = words[day_number % len(words)]
            else:
                secret = os.environ.get("WORDLE_SECRET", random.choice(words))
            max_guesses = 10 if "--easy" in options else 6
            hard = "--hard" in options
```

The limit and the hard flag now come from the save when there is one, and from the options only for a new game. Then call `guesses, won = play(secret, words, max_guesses, hard, history)`.

Play with `WORDLE_SECRET=crane`, guess `slate` and then stop the game with Ctrl+C. Open `save.json` :

```json
{
  "secret": "crane",
  "history": [
    [
      "slate",
      [
        "grey",
        "grey",
        "green",
        "grey",
        "green"
      ]
    ]
  ],
  "max_guesses": 6,
  "hard": false
}
```

Start the game again, without any option. It announces the saved game, draws the board so far, continues at guess 2 with the same settings as before, and removes the save file when the game is finished :

```text
Resuming your saved game.
Guess the five-letter word. Type 'quit', 'letters', 'hint' or 'stats'.
 S  L [A] T [E]
Guess 2/6 :
```

Try the same with `--easy`, and stop after a guess : the resumed game still says `Guess 2/10`.

A game that ends with `quit` is over and is cleared too. Only an interruption leaves a save behind.

:::hint
The slide *The json Module* turns a dictionary into text with `json.dumps` and back with `json.loads`, and *Renaming and Deleting Files*, in module 09, removes a file with `unlink`.
:::

:::hint
`SAVE_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")` writes the file. `json.loads(SAVE_PATH.read_text(encoding="utf-8"))` reads it back as dictionaries and lists.
:::

:::hint
Return `None` when `SAVE_PATH.exists()` is false. `SAVE_PATH.unlink(missing_ok=True)` removes a file, and does not complain if there is none.
:::

:::solution
```python
def save_game(
    secret: str, history: list[tuple[str, list[Mark]]], max_guesses: int, hard: bool
) -> None:
    """Write the secret, the scored guesses and the game's settings to the save file."""
    data = {"secret": secret, "history": history, "max_guesses": max_guesses, "hard": hard}
    SAVE_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


def load_saved_game() -> tuple[str, list[tuple[str, list[Mark]]], int, bool] | None:
    """Read a saved game, returning None when no save exists."""
    if not SAVE_PATH.exists():
        return None
    data = json.loads(SAVE_PATH.read_text(encoding="utf-8"))
    history = [(word, marks) for word, marks in data["history"]]
    return data["secret"], history, data["max_guesses"], data["hard"]


def clear_saved_game() -> None:
    """Remove the save after a game is complete."""
    SAVE_PATH.unlink(missing_ok=True)
```
:::

### Step 5 : Check input with a pattern

`check_guess` uses `guess.isalpha()` to see that a guess is made of letters. It accepts more than the game can use, such as letters with an accent. Try it :

```python
from wordle.scoring import check_guess
from wordle.words import load_allowed

check_guess("éclat", load_allowed())
```

```text
wordle.scoring.InvalidGuess: That word is not in the word list.
```

`éclat` passed the letters test and was only stopped by the word list. A regular expression says exactly what is allowed : five characters, each one of `a` to `z`. Replace the test in `check_guess` with `re.fullmatch`, which succeeds only if the whole string matches the pattern. Add `import re` to `wordle/scoring.py`, and keep the check on the length before it :

```python
    if not re.fullmatch(..., guess):
        raise InvalidGuess("A guess must contain letters only.")
```

See *Regular Expressions with re* and *Matching and Searching*. Run the session again; the same word is now refused for the right reason :

```text
wordle.scoring.InvalidGuess: A guess must contain letters only.
```

Run `uv run pytest`; the hard-mode test of Step 3 still passes.

:::hint
The slide *Matching and Searching* uses `re.fullmatch` with a character class, `[a-z]+`.
:::

:::hint
`[a-z]` is one lower-case letter and `{5}` repeats the previous item five times. Write the pattern as a raw string, `r"[a-z]{5}"`, as you would a path, so that backslashes in later patterns mean what they say.
:::

:::solution
```python
import re
...
    if not re.fullmatch(r"[a-z]{5}", guess):
        raise InvalidGuess("A guess must contain letters only.")
```
:::

### Step 6 : Write your own tests

In Step 3 the test was given. Tests of this kind are small : a function whose name starts with `test_`, and a plain `assert`. See *Testing with pytest*. You wrote this exercise's functions yourself, so write the tests too. Add two to `tests/test_ex13.py`, which Step 3 created. Their imports go at the top of the file, next to the ones that are there, and the tests go at the bottom :

```python
import pytest
from wordle.scoring import InvalidGuess, check_guess
from wordle.solver import best_guess
```

```python
def test_best_guess_returns_none_for_no_candidates() -> None:
    ...


def test_check_guess_rejects_capital_letters() -> None:
    ...
```

The first is one `assert` : with no candidates, `best_guess` returns `None` (the `str | None` of Exercise 12). Compare with `is None`. The second needs the test to expect an exception, which is what `pytest.raises` is for :

```python
    with pytest.raises(InvalidGuess, match="letters only"):
        ...
```

Anything raised inside the `with` block must be an `InvalidGuess` whose message contains `letters only`, or the test fails. The pattern of Step 5 refuses capital letters. See *Exceptions and Parametrized Tests*. Read a failure before you move on : change an expected value in one test on purpose, run `uv run pytest tests/test_ex13.py`, read what pytest shows next to the failing `assert`, and change it back. See *Reading a Test Failure*.

:::hint
The slide *Testing with pytest* shows a test that is one `assert`, and *Exceptions and Parametrized Tests* puts the call that must fail inside `with pytest.raises(...)`.
:::

:::hint
`assert best_guess([]) is None`. The second test calls `check_guess("CRANE", ["crane"])` inside the `with` block; the length is fine, so the pattern is what fails.
:::

:::solution
```python
def test_best_guess_returns_none_for_no_candidates() -> None:
    assert best_guess([]) is None


def test_check_guess_rejects_capital_letters() -> None:
    with pytest.raises(InvalidGuess, match="letters only"):
        check_guess("CRANE", ["crane"])
```
:::

### Step 7 : One test, several cases

Testing `clean_words` from Exercise 9 on several inputs means repeating a test function, or looping inside it, where the first failure hides the rest. `pytest.mark.parametrize` runs one test function once per value and reports each separately. Add this to `tests/test_ex13.py`, with `from wordle.words import clean_words` at the top :

```python
@pytest.mark.parametrize("line", ["crane", "slate", "raise"])
def test_clean_words_keeps_lowercase_five_letter_words(line: str) -> None:
    assert clean_words([line, line.upper()]) == [line]
```

The decorator names the parameter and lists the values; pytest calls the function with each. The test checks that cleaning a word and its capitalised copy leaves exactly one lower-case word. Run it with `-v` to see each case :

```bash
uv run pytest tests/test_ex13.py -v
```

```text
tests/test_ex13.py::test_follows_hints_keeps_green_letters_and_uses_yellow_letters PASSED [ 16%]
tests/test_ex13.py::test_best_guess_returns_none_for_no_candidates PASSED [ 33%]
tests/test_ex13.py::test_check_guess_rejects_capital_letters PASSED      [ 50%]
tests/test_ex13.py::test_clean_words_keeps_lowercase_five_letter_words[crane] PASSED [ 66%]
tests/test_ex13.py::test_clean_words_keeps_lowercase_five_letter_words[slate] PASSED [ 83%]
tests/test_ex13.py::test_clean_words_keeps_lowercase_five_letter_words[raise] PASSED [100%]
```

Three cases, three lines. Finish with `uv run pytest` for the whole project, and `uv run mypy wordle` to check that the new modules are typed too.

---

### If time permits

- Replace the hand-made option parsing in `main` with `argparse`, which also provides `--help` for free. Look it up in the standard library documentation. There is no reference solution for this step.
- Use `datetime` once more : store the date with the daily word in `save.json`, so that a saved daily game from yesterday is not resumed today.
