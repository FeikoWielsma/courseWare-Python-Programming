# Exercise 5 : Functions

Your Wordle works, but it is one long script from top to bottom. In this exercise you cut it into functions, and on the way you find and fix a bug that has been in the game since Exercise 2.

Continue in your own `wordle` project, or start from `exercises/starters/05-functions/`. The starter is the finished Exercise 4 plus the test file this exercise hands out.

Some steps give you the code, some a skeleton to complete, and some only the tests to pass. Where you write the code yourself, the solution is hidden until you open it. Try the step first; the solution is there for when you are stuck, or to compare afterwards.

---

### Step 1 : Find the bug

Play one round where you know the answer. The starter supports `WORDLE_SECRET`, an environment variable that overrides the random choice. In PowerShell, run :

```powershell
$env:WORDLE_SECRET = "crane"
uv run python wordle.py
```

In Bash, use `WORDLE_SECRET=crane uv run python wordle.py`. If your own script does not have the override yet, temporarily set `secret = "crane"`.

Enter `error`, then `crane`. Here is the captured output, with typed input omitted :

:::output

```text
Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.
Guess 1/6 : (E)[R](R) O (R)
Guess 2/6 : [C][R][A][N][E]
Got it in 2!
```

:::

CRANE has one R, and the green R in second place already uses it. The other two R's should be grey. Asking whether a letter occurs anywhere in the secret cannot tell one R from three. Keep the fixed secret until the end of the exercise.

### Step 2 : A main function

Before the scoring can be fixed it needs to be something you can call on its own, and before anything can be called on its own the script must stop running a whole game the moment it is loaded.

Move the code that reads the word list into a function, and the rest of the script into a function called `main`. Call `main` at the bottom, behind a guard :

```python
import os
import random
from pathlib import Path


def load_words(path: str = "words.txt") -> list[str]:
    """Read the word list, one word per line."""
    return Path(path).read_text(encoding="utf-8").split()


def main() -> None:
    words = load_words()
    secret = os.environ.get("WORDLE_SECRET", random.choice(words))
    ...  # the rest of the game, indented one level further


if __name__ == "__main__":
    main()
```

Run the game again with `uv run python wordle.py` and confirm it plays exactly as before.

The `if __name__ == "__main__":` line means : only start a game when this file is run, not when another file imports it. The test file you use in Step 4 imports `wordle`, and without the guard every test run would sit waiting for a guess. Module 6 explains how this works.

### Step 3 : Checking a guess

The game loop rejects a guess that is the wrong length or not in the word list. Give that check a name. Add `WORD_LENGTH = 5` beside the imports, then fill in the body. See *Annotating a Function* for the signature :

```python
def is_valid(guess: str, words: list[str]) -> bool:
    """A guess must be a known word of the right length."""
    return ...  # combine the length, letters-only and membership checks
```

Then replace the check in the game loop with a call to it :

```python
if not is_valid(guess, words):
    print("That is not a five-letter word I know.")
    continue
```

:::hint

A word made of letters only is something a string method can tell you. And a condition is already `True` or `False`, so it can be returned as it is; there is no need for `if ... : return True` followed by `return False`.

:::

:::solution

```python
WORD_LENGTH = 5


def is_valid(guess: str, words: list[str]) -> bool:
    """A guess must be a known word of the right length."""
    return len(guess) == WORD_LENGTH and guess.isalpha() and guess in words
```

`WORD_LENGTH` is a constant : a module-level name in capitals, which tells the reader it is not meant to change. Use it wherever the game says `5`.

:::

### Step 4 : Scoring a guess

This is the function the bug lives in. Here is its signature :

```python
def score_guess(secret: str, guess: str) -> list[str]:
    """Mark each letter of guess as "green", "yellow" or "grey"."""
```

The rules :

- a letter in the right place is `"green"`
- a letter that is in the secret, but somewhere else, is `"yellow"`
- anything else is `"grey"`
- each letter of the secret can colour **one** letter of the guess, and a green match uses it up first

The starter folder has a test file, `test_wordle.py`. If you are working in your own project, copy it in from `exercises/handouts/05-functions/`, and add `pytest` as a development dependency :

```bash
uv add --dev pytest
```

The handout imports `render` as well. Add this temporary definition so pytest can collect the tests; leave the existing game display in place until Step 5 :

```python
def render(guess: str, marks: list[str]) -> str:
    return ""
```

Run just the five scoring tests for now :

```bash
uv run pytest -k "not is_valid and not render"
```

Collection initially fails if `score_guess` is missing. Once it exists, pytest shows any failed assertions and their expected values. Implement it until all five scoring tests pass. The game still uses its old scoring until you connect the new functions in Step 5.

:::hint

The last rule is hard to get right in a single loop. Two loops make it easy. The first finds the greens, and keeps a list of the secret's letters that were not matched. The second goes over the remaining letters of the guess and marks one yellow only if its letter is still in that list, removing it when it does.

:::

:::output

The end of a passing run of the command above is shown below. Timings vary.

```text
collected 9 items / 4 deselected / 5 selected

test_wordle.py .....                                                     [100%]

======================= 5 passed, 4 deselected in 0.01s =======================
```

:::

:::solution

```python
def score_guess(secret: str, guess: str) -> list[str]:
    """Mark each letter of guess as "green", "yellow" or "grey".

    A letter is yellow only while the secret still has an unmatched copy of it,
    so one E in the secret cannot make two E's in the guess yellow.
    """
    marks = ["grey"] * WORD_LENGTH
    unmatched: list[str] = []

    # First pass : exact matches. Whatever the secret has left over is
    # available to be found elsewhere.
    for position, letter in enumerate(guess):
        if letter == secret[position]:
            marks[position] = "green"
        else:
            unmatched.append(secret[position])

    # Second pass : right letter, wrong place, each copy used at most once.
    for position, letter in enumerate(guess):
        if marks[position] != "green" and letter in unmatched:
            marks[position] = "yellow"
            unmatched.remove(letter)

    return marks
```

`["grey"] * WORD_LENGTH` builds a list of five `"grey"` strings, so every letter starts grey and only the two loops change that.

:::

### Step 5 : Drawing a row

The code that builds `[A]`, `(A)` and ` A ` now has the marks to work from instead of working them out itself. Move it into a function :

```python
def render(guess: str, marks: list[str]) -> str:
    """[A] is in the right place, (A) is in the word elsewhere, A is not in it."""
    row = ""
    for position, letter in enumerate(guess.upper()):
        ...
    return row
```

:::hint

A `match` on `marks[position]` reads well here.

:::

The game loop then shrinks to a single line where the scoring used to be :

```python
print(render(guess, score_guess(secret, guess)))
```

Run `uv run pytest` : `test_render_marks_each_letter` passes too.

:::solution

```python
def render(guess: str, marks: list[str]) -> str:
    """[A] is in the right place, (A) is in the word elsewhere, A is not in it."""
    row = ""
    for position, letter in enumerate(guess.upper()):
        match marks[position]:
            case "green":
                row += f"[{letter}]"
            case "yellow":
                row += f"({letter})"
            case _:
                row += f" {letter} "
    return row
```

:::

### Step 6 : One game, as a function

What is left in `main` is the game itself. Move it into a function that plays one game and reports whether it was won :

```python
def play(secret: str, words: list[str], max_guesses: int = 6) -> bool:
    """Play one game. Returns True when the word was found."""
    used_letters: set[str] = set()
    guess_count = 0
    ...  # move the loop here, returning True on a win and False otherwise
```

`max_guesses=8` allows an easier game; the default is six. See *Default Arguments*. Keep loading the words and choosing the secret in `main`, then call `play(secret, words)`. Without `WORDLE_SECRET`, the secret is random.

:::hint

Return `True` on a win, replacing the loop's `break` and `else`. In the `quit` case, keep only `break`; remove its old print so the secret is not shown twice. After the loop, reveal the secret and return `False`. Exercise 10 will use this result for statistics.

:::

:::solution

```python
def play(secret: str, words: list[str], max_guesses: int = 6) -> bool:
    """Play one game. Returns True when the word was found."""
    used_letters: set[str] = set()
    guess_count = 0

    while guess_count < max_guesses:
        guess = input(f"Guess {guess_count + 1}/{max_guesses} : ").strip().lower()

        match guess:
            case "quit":
                break
            case "letters":
                print("Tried :", " ".join(sorted(used_letters)))
                continue

        if not is_valid(guess, words):
            print("That is not a five-letter word I know.")
            continue

        guess_count += 1
        used_letters.update(guess)
        print(render(guess, score_guess(secret, guess)))

        if guess == secret:
            print(f"Got it in {guess_count}!")
            return True

    print(f"The word was {secret.upper()}.")
    return False
```

Replace `main` with :

```python
def main() -> None:
    words = load_words()
    print("Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.")
    secret = os.environ.get("WORDLE_SECRET", random.choice(words))
    play(secret, words)
```

The complete file is in `solutions/05-functions/wordle.py`.

:::

---

Run `uv run pytest` again; all nine tests should pass. Play with `error`, then `crane`, against the fixed secret. The captured output now shows only one coloured R :

:::output

```text
Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.
Guess 1/6 : (E)[R] R  O  R 
Guess 2/6 : [C][R][A][N][E]
Got it in 2!
```

:::

Remove the override with `Remove-Item Env:WORDLE_SECRET` in PowerShell, or `unset WORDLE_SECRET` if you exported it in Bash, and play a random game.

### If time permits

Add a hard mode, in which every guess must use what the earlier guesses revealed. A green letter must stay in its place, and a yellow letter must appear somewhere. Write

```python
def follows_hints(guess: str, history: list[tuple[str, list[str]]]) -> bool:
```

where `history` holds every earlier guess with its marks as `(guess, marks)` pairs, which `play` has to keep as a list. Add a parameter `hard: bool = False` to `play`, and reject a guess that breaks the rule when it is `True`. Try guesses that obey and break each rule. Exercise 8 will introduce writing your own tests. There is no reference solution for this step.
