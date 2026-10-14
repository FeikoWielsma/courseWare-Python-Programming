# Exercise 5 : Functions

Your Wordle works, but it is one long script from top to bottom. In this exercise you cut it into functions, and on the way you find and fix a bug that has been in the game since Exercise 2.

Continue in your own `wordle` project, or start from `exercises/starters/05-functions/`. The starter is the finished Exercise 4 plus the test file this exercise hands out.

Every step is marked with how much help it gives :

- ★ the code is given; type it in and read it
- ★★ a skeleton is given; you fill in the body
- ★★★ only the signature and the tests are given

Steps marked ★★ and ★★★ have a reference solution on the page after them. Try the step first; the solution is there for when you are stuck, or to compare afterwards.

---

### Step 1 ★ : Find the bug

Play one round where you already know the answer. Change the line that picks the secret word to a fixed word for a moment :

```python
secret = "crane"
```

Then guess `error`. Your game prints something like :

```text
(E)[R](R) O (R)
```

CRANE has one R, and it is already accounted for by the green R in second place. The other two R's should be grey. The scoring code only asks "is this letter anywhere in the secret?", and that question cannot tell one R from three.

Keep `crane` for now; you will need a known word again in Step 4. Put `random.choice(words)` back in Step 6.

### Step 2 ★ : A main function

Before the scoring can be fixed it needs to be something you can call on its own, and before anything can be called on its own the script must stop running a whole game the moment it is loaded.

Move the code that reads the word list into a function, and the rest of the script into a function called `main`. Call `main` at the bottom, behind a guard :

```python
import random
from pathlib import Path


def load_words(path: str = "words.txt") -> list[str]:
    """Read the word list, one word per line."""
    return Path(path).read_text(encoding="utf-8").split()


def main() -> None:
    words = load_words()
    secret = "crane"
    ...  # the rest of the game, indented one level further


if __name__ == "__main__":
    main()
```

Run the game again with `uv run python wordle.py` and confirm it plays exactly as before.

The `if __name__ == "__main__":` line means : only start a game when this file is run, not when another file imports it. The test file you use in Step 4 imports `wordle`, and without the guard every test run would sit waiting for a guess. Module 6 explains how this works.

### Step 3 ★★ : Checking a guess

The game loop rejects a guess that is the wrong length or not in the word list. Give that check a name. Fill in the body :

```python
def is_valid(guess: str, words: list[str]) -> bool:
    """A guess must be a known word of the right length."""
    ...
```

Then replace the check in the game loop with a call to it :

```python
if not is_valid(guess, words):
    print("That is not a five-letter word I know.")
    continue
```

Two hints. A word made of letters only is something a string method can tell you. And a condition is already `True` or `False`, so it can be returned as it is; there is no need for `if ... : return True` followed by `return False`.

<details open>
<summary>Reference solution</summary>

```python
WORD_LENGTH = 5


def is_valid(guess: str, words: list[str]) -> bool:
    """A guess must be a known word of the right length."""
    return len(guess) == WORD_LENGTH and guess.isalpha() and guess in words
```

`WORD_LENGTH` is a constant : a module-level name in capitals, which tells the reader it is not meant to change. Use it wherever the game says `5`.

</details>

### Step 4 ★★★ : Scoring a guess

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

Run the tests :

```bash
uv run pytest
```

They fail, because `score_guess` does not exist yet. Read the report : pytest names each failing test and shows what it expected next to what it got. Write `score_guess` until the five scoring tests pass. Then run the game and guess `error` against `crane` again.

If you are stuck : the last rule is hard to get right in a single loop. Two loops make it easy. The first finds the greens, and keeps a list of the secret's letters that were *not* matched. The second goes over the remaining letters of the guess and marks one yellow only if its letter is still in that list, removing it when it does.

<details open>
<summary>Reference solution</summary>

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

</details>

### Step 5 ★★ : Drawing a row

The code that builds `[A]`, `(A)` and ` A ` now has the marks to work from instead of working them out itself. Move it into a function :

```python
def render(guess: str, marks: list[str]) -> str:
    """[A] is in the right place, (A) is in the word elsewhere, A is not in it."""
    row = ""
    for position, letter in enumerate(guess.upper()):
        ...
    return row
```

A `match` on `marks[position]` reads well here. The game loop then shrinks to a single line where the scoring used to be :

```python
print(render(guess, score_guess(secret, guess)))
```

Run `uv run pytest` : `test_render_marks_each_letter` passes too.

<details open>
<summary>Reference solution</summary>

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

</details>

### Step 6 ★★ : One game, as a function

What is left in `main` is the game itself. Move it into a function that plays one game and reports whether it was won :

```python
def play(secret: str, words: list[str], max_guesses: int = 6) -> bool:
    """Play one game. Returns True when the word was found."""
    ...
```

`max_guesses` has a default, so `play(secret, words)` is a normal game and `play(secret, words, max_guesses=8)` is an easy one. `main` becomes short :

```python
def main() -> None:
    words = load_words()
    print("Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.")
    play(random.choice(words), words)
```

This is the moment to put `random.choice(words)` back.

Inside `play`, a `return True` the moment the word is found replaces the `break` and the `else:` on the loop. Nothing uses the result yet. Exercise 10 will, when it keeps your statistics.

<details open>
<summary>Reference solution</summary>

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

The complete file is in `solutions/05-functions/wordle.py`.

</details>

---

**If time permits** ★★★ : add a hard mode, in which every guess must use what the previous guess revealed. A green letter must stay in its place, and a yellow letter must appear somewhere. Write

```python
def follows_hints(guess: str, previous: str, marks: list[str]) -> bool:
```

add a parameter `hard: bool = False` to `play`, and reject a guess that breaks the rule when it is `True`. Write a test or two for `follows_hints` in `test_wordle.py` first, in the same style as the ones you were given. There is no reference solution for this step.
