# Exercise 7 : Comprehensions

Your game can judge a guess, but it cannot yet use the feedback to choose its next move. In this exercise you turn the same scoring function into a solver: it will rule out impossible answers and recommend a guess from the words that remain.

Continue in your own `wordle` project, or use `exercises/starters/07-comprehensions/`, the finished Exercise 6 with `tests/test_solver.py` added. If using your own project, copy that test file from `exercises/handouts/07-comprehensions/tests/`. Allow about 75 minutes. Keep running commands beside `pyproject.toml`.

### Step 1 : Build a row from expressions {★★}

In `wordle/display.py`, replace the loop with a joined sequence. Complete the call for each letter and mark :

```python
def render(guess: str, marks: list[str]) -> str:
    symbols = {
        "green": lambda letter: f"[{letter}]",
        "yellow": lambda letter: f"({letter})",
        "grey": lambda letter: f" {letter} ",
    }
    return "".join(... for letter, mark in zip(guess.upper(), marks, strict=True))
```

See *Zip Function*. `strict=True` rejects sequences of different lengths. Run the display test :

```bash
uv run pytest tests/test_display.py
```

:::hint

Call `symbols[mark]` with `letter`; `join` concatenates the results.

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

The expression inside `join` is a generator expression: it produces values as they are consumed, without building a separate list. You will use the same form inside `all` and `sum`; writing generators is covered further in Advanced Python.

### Step 2 : Turn the scorer around {★}

Imagine that a candidate word really is the secret. Would it give exactly the feedback you saw? If it would, the word is still possible. This reuses the duplicate-letter rules you already tested, rather than inventing another set of rules for the solver.

Create `wordle/solver.py` with :

```python
from wordle.scoring import score_guess


def consistent(word: str, guess: str, marks: list[str]) -> bool:
    """Return whether word would produce the observed marks for guess."""
    return score_guess(word, guess) == marks
```

Read `test_consistent_reuses_scoring_rules` in the handout. It scores `slate` against `crane`, then accepts that word-and-guess combination and rejects the same marks for the guess `raise`. The test file also imports the functions you will add in Steps 3 and 4, so it will not collect successfully yet. The game remains playable while you build its solver.

### Step 3 : Keep every answer that fits {★★★}

Add this function to `solver.py` :

```python
def candidates(words: list[str], history: list[tuple[str, list[str]]]) -> list[str]:
    """Return words consistent with every guess and its marks."""
```

`history` contains pairs of a guess and its marks. Keep a word only if it agrees with every pair, preserving the order of `words`. An empty history rules out nothing. See *Filtered List Comprehension*.

Run the given solver tests after implementing the remaining imported functions in Step 4 :

```bash
uv run pytest tests/test_solver.py
```

`test_candidates_match_all_history` is the test for this function. Read its concrete history and expected list before implementing it. For a quick check before Step 4, you can also import `candidates` directly in `uv run python` and evaluate the assertion from that test.

:::hint

Use an outer list comprehension over `words` and an `all(...)` condition over the pairs in `history`. `all` is true for an empty sequence, which gives the required empty-history behaviour automatically.

:::

:::output

After Step 4, the solver tests pass. In the full `uv run pytest` run, the final lines are as follows; timings vary.

```text
tests\test_solver.py ....                                                [100%]

============================== 8 passed in 0.04s ==============================
```

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

### Step 4 : Choose a useful next guess {★★}

Prefer an answer whose distinct letters occur in many remaining words. This heuristic favours useful information; it does not guarantee the fewest guesses.

Complete these functions in `solver.py`. Count words containing each letter; repeated occurrences in one word contribute only once.

```python
def letter_counts(words: list[str]) -> dict[str, int]:
    letters = {... for word in words for letter in word}
    return {letter: ... for letter in letters}


def best_guess(words: list[str]) -> str:
    counts = letter_counts(words)
    return max(words, key=lambda word: ...)
```

See *Dictionary Comprehensions*, *Set Comprehensions* and *Built-ins that Take a Function*. `best_guess` needs a non-empty list; during normal play the secret remains a candidate. On a tie, `max` chooses the first word with that score.

:::hint

For each letter, sum `letter in word` over the words. Booleans contribute 1 or 0. For a proposed guess, sum the counts for `set(word)` so repeating a letter does not inflate its score.

:::

:::solution

```python
def letter_counts(words: list[str]) -> dict[str, int]:
    """Count how many candidate words contain each letter."""
    letters = {letter for word in words for letter in word}
    return {letter: sum(letter in word for word in words) for letter in letters}
```

```python
def best_guess(words: list[str]) -> str:
    """Choose the word with the most frequently occurring distinct letters."""
    counts = letter_counts(words)
    return max(words, key=lambda word: sum(counts[letter] for letter in set(word)))
```

:::

Run `uv run pytest tests/test_solver.py`, then `uv run pytest`. The four new solver tests and all four earlier tests should pass. In particular, the `cacao` case checks that repeated letters are not counted as extra information.

### Step 5 : Ask the game for help {★★}

Add `from wordle.solver import best_guess, candidates` to `wordle/game.py`. Initialise `history` as an empty list beside `used_letters` inside `play`. After scoring each valid guess, save `(guess, marks)` before rendering the row. Commands and rejected guesses must not enter the history.

Extend the existing `match guess` using this skeleton, keeping the existing `quit` and `letters` cases :

```python
match guess:
    case "hint":
        possible = ...
        print(...)  # number of candidates and the suggested word in upper case
        continue
```

Use the message format shown in the output below. Requesting a hint must not use a turn. After implementing it, set `WORDLE_SECRET` to `crane` and run the game :

```powershell
$env:WORDLE_SECRET = "crane"
uv run python -m wordle
```

In Bash, use `WORDLE_SECRET=crane uv run python -m wordle`. Enter `slate`, `hint`, then `crane`.

:::hint

Calculate the marks once, append the pair to `history`, and pass those same marks to `render`. The hint case calls `candidates(words, history)` first, then `best_guess(possible)`.

:::

:::output

Captured output with typed input omitted. Notice that the hint leaves the prompt at guess 2.

```text
Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.
Guess 1/6 :  S  L [A] T [E]
Guess 2/6 : 15 words left, try GRACE
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

Remove the fixed-secret override with `Remove-Item Env:WORDLE_SECRET` in PowerShell, or `unset WORDLE_SECRET` if exported in Bash. Play a random game and use `hint` after each guess. The suggestion comes from your scoring rules and the feedback recorded so far; the solver never reads the secret directly.

### If time permits

Write `solve(secret, words)` to play a whole game automatically. Start with an empty history, choose with `best_guess`, score the guess, append its feedback, and filter again until the guess is correct. Return the number of guesses used. Try the first 100 words as secrets and calculate the average. Keep this experiment separate from the interactive game.
