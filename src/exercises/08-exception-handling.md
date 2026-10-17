# Exercise 8 : Exception Handling

The game gives the same rejection for every bad guess, and a missing word list or an interrupted input ends in a traceback. Give each failure a useful response, then write your first tests to check those responses at the validation boundary.

Continue in your own `wordle` project, or use `exercises/starters/08-exception-handling/`, the finished Exercise 7 plus this exercise's handouts. If continuing your own project, copy `tests/test_scoring.py` from `exercises/handouts/08-exception-handling/`, replacing the earlier version and retaining your other tests. Read the handout's `README.txt`: the exception tests are deliberately not provided. You write them in Step 5. Allow about 60 minutes.

### Step 1 : Name an invalid guess

Add this class below `WORD_LENGTH` in `wordle/scoring.py` :

```python
class InvalidGuess(ValueError):  # noqa: N818  # Contracted name from plan section 4.
    """Raised when a guess is not an allowed five-letter word."""
```

This creates a specific `ValueError` the game can catch. See *User Defined Exceptions*; Module 11 covers classes in detail. The `noqa` comment permits the course's exception name instead of Ruff's preferred `Error` suffix.

Next, make the validator raise this exception with a reason.

### Step 2 : Explain why a guess is invalid

Add `check_guess` to `scoring.py`. Check length, letters, then membership. Valid guesses return normally; invalid ones raise `InvalidGuess`. See *Raising Exceptions*.

```python
def check_guess(guess: str, words: list[str]) -> None:
    if ...:
        raise InvalidGuess("A guess must have five letters.")
    if ...:
        raise InvalidGuess("A guess must contain letters only.")
    if ...:
        raise InvalidGuess("That word is not in the word list.")
```

Keep `is_valid` so the earlier tests and the current game still work, but make it a wrapper around the new validator :

```python
def is_valid(guess: str, words: list[str]) -> bool:
    try:
        ...  # call the validator
    except InvalidGuess:
        ...  # report failure as a boolean
    return True
```

Run `uv run pytest`. The eight existing tests should still pass. They do not yet check the exception reasons; you will add that coverage yourself.

:::hint

Compare `len(guess)` with `WORD_LENGTH`, use `guess.isalpha()`, and then test membership in `words`. Inside the wrapper, catch only `InvalidGuess` and return `False`; unrelated programming errors should remain visible.

:::

:::solution

```python
def check_guess(guess: str, words: list[str]) -> None:
    """Raise InvalidGuess with a reason when guess cannot be played."""
    if len(guess) != WORD_LENGTH:
        raise InvalidGuess("A guess must have five letters.")
    if not guess.isalpha():
        raise InvalidGuess("A guess must contain letters only.")
    if guess not in words:
        raise InvalidGuess("That word is not in the word list.")
```

```python
def is_valid(guess: str, words: list[str]) -> bool:
    """Return whether guess is valid, for compatibility with Exercise 6."""
    try:
        check_guess(guess, words)
    except InvalidGuess:
        return False
    return True
```

:::

### Step 3 : Recover without spending a turn

In `wordle/game.py`, replace the scoring import with :

```python
from wordle.scoring import InvalidGuess, check_guess, score_guess
```

Replace `if not is_valid(...)` after command handling, before updating the guess count or history :

```python
try:
    ...  # validate the guess
except InvalidGuess as error:
    ...  # display the reason
    continue
```

:::hint

Call `check_guess(guess, words)`; catch and print `InvalidGuess`. See *Typed Exception Handling*.

:::

:::solution

```python
try:
    check_guess(guess, words)
except InvalidGuess as error:
    print(error)
    continue
```

:::

### Step 4 : Stop cleanly when play cannot continue

In `wordle/__main__.py`, wrap loading the words and playing the game in handlers for a missing file and interrupted input. Keep `os`, `random`, `play` and `load_words` imported, and keep the existing guard below `main`.

```python
def main() -> None:
    try:
        ...  # load words, print the welcome message and play
    except FileNotFoundError:
        ...  # explain how to restore the word list
    except (KeyboardInterrupt, EOFError):
        ...  # print a newline followed by a friendly stopping message
```

For a missing file, print `The word list is missing. Restore words.txt and try again.` For interrupted input, print `\nGame stopped.` Try Ctrl+C while the game waits for a guess. End-of-input is Ctrl+D on Unix terminals, or Ctrl+Z followed by Enter on Windows. To test the missing-file case, temporarily rename `words.txt`, run the game, and restore the filename immediately afterwards.

:::hint

The game can recover from one bad guess, so that handler belongs inside `play`. Missing data or interrupted input ends the session, so those handlers belong in `main`. A tuple lets one handler catch either interruption type.

:::

:::solution

```python
def main() -> None:
    """Load the words and play one game."""
    try:
        words = load_words()
        print(
            "Guess the five-letter word. Type 'quit' to give up, "
            "'letters' for the letters tried."
        )
        play(os.environ.get("WORDLE_SECRET", random.choice(words)), words)
    except FileNotFoundError:
        print("The word list is missing. Restore words.txt and try again.")
    except (KeyboardInterrupt, EOFError):
        print("\nGame stopped.")
```

:::

### Step 5 : Write your first exception tests

Create `tests/test_exceptions.py`. So far you have run tests written for you. Now you will specify the three ways a guess can be rejected.

Import `pytest`, and import `InvalidGuess` and `check_guess` from `wordle.scoring`. Set `WORDS = ["crane", "slate"]`. Write these test functions :

```python
def test_wrong_length_has_a_specific_reason() -> None:
    ...


def test_non_letters_have_a_specific_reason() -> None:
    ...


def test_unknown_words_have_a_specific_reason() -> None:
    ...
```

Use `cran`, `cr4ne` and `zzzzz`, respectively. Check both the exception type and a distinctive part of its message. `pytest.raises` is a context manager: the indented call must raise the expected exception. If no exception occurs, or the type or message is wrong, the test fails. The `match=` argument checks a regular-expression match within the message; use the simple phrases `five letters`, `letters only` and `not in the word list` here.

Run your new file, then all tests :

```bash
uv run pytest tests/test_exceptions.py
uv run pytest
```

:::hint

Use a `with pytest.raises(InvalidGuess, match="..."):` block around each call to `check_guess`. Choose a five-character input for the letters-only test, otherwise the earlier length check will reject it for a different reason.

:::

:::output

With these three tests added, the end of a complete run looks like this. Timings vary.

```text
tests\test_display.py .                                                  [  9%]
tests\test_exceptions.py ...                                             [ 36%]
tests\test_scoring.py ...                                                [ 63%]
tests\test_solver.py ....                                                [100%]

============================= 11 passed in 0.05s ==============================
```

:::

:::solution

```python
import pytest
from wordle.scoring import InvalidGuess, check_guess

WORDS = ["crane", "slate"]


def test_wrong_length_has_a_specific_reason() -> None:
    with pytest.raises(InvalidGuess, match="five letters"):
        check_guess("cran", WORDS)


def test_non_letters_have_a_specific_reason() -> None:
    with pytest.raises(InvalidGuess, match="letters only"):
        check_guess("cr4ne", WORDS)


def test_unknown_words_have_a_specific_reason() -> None:
    with pytest.raises(InvalidGuess, match="not in the word list"):
        check_guess("zzzzz", WORDS)
```

:::

Finally, set `WORDLE_SECRET` to `crane` and play again :

```powershell
$env:WORDLE_SECRET = "crane"
uv run python -m wordle
```

In Bash, use `WORDLE_SECRET=crane uv run python -m wordle`. Enter `cran`, `cr4ne`, `zzzzz`, then `crane`. Captured output, with typed input omitted :

:::output

```text
Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.
Guess 1/6 : A guess must have five letters.
Guess 1/6 : A guess must contain letters only.
Guess 1/6 : That word is not in the word list.
Guess 1/6 : [C][R][A][N][E]
Got it in 1!
```

:::

All three invalid guesses leave the first turn available. Remove the override with `Remove-Item Env:WORDLE_SECRET` in PowerShell, or `unset WORDLE_SECRET` if exported in Bash, and play a random game. The solver's `hint` command should still work.

### If time permits

Add tests for a valid guess returning `None`, for a too-long guess, and for an input that fails more than one rule. Decide which reason should take priority and check that the implementation follows that decision. Keep the game playable and rerun all tests after each change.
