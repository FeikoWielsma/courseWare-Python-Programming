# Exercise 5 : Functions

Your Wordle works, but it is one long script from top to bottom. In this exercise you cut it into functions, and on the way you find and fix a bug that has been in the game since Exercise 2.

Continue in your own `wordle` project, or start from `exercises/starters/05-functions/`. The starter is the finished Exercise 4.

Some steps give you the code and some give you a skeleton to complete. The scoring function is built in two passes, with a check after each one. Where you write the code yourself, the solution is hidden until you open it. Try the step first; the solution is there for when you are stuck, or to compare afterwards.

---

### Step 1 : Find the bug

Keep `secret = "crane"` and run `uv run python wordle.py`.

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

Move the word list into a function that returns it, and the rest of the script into a function called `main`. Call `main` at the bottom, behind a guard :

```python
def load_words() -> list[str]:
    """Return the small practice word list."""
    return [
        "hello", "crane", "react", "paper", "slate", "error", "house", "ghost",
        "world", "money", "speed", "geese", "trace", "grace", "raise", "trick",
    ]


def main() -> None:
    words = load_words()
    secret = "crane"
    ...  # the rest of the game, indented one level further


if __name__ == "__main__":
    main()
```

Run the game again with `uv run python wordle.py` and confirm it plays exactly as before.

The `if __name__ == "__main__":` line means : only start a game when this file is run, not when another file imports it. The slide *Running and Importing a File* shows the guard. In Step 4 you import `wordle` into the interactive interpreter to try a function on its own, and without the guard the import would start a game and sit waiting for a guess.

:::hint

The slide *Function Syntax* shows the shape : everything indented under the `def` line is the body of the function. *return Statement* shows how `load_words` hands its list back.

:::

### Step 3 : Checking a guess

The game loop rejects a guess that is the wrong length or not in the word list. Give that check a name. Add `WORD_LENGTH = 5` above the functions, then fill in the body. See *Annotating a Function* for the signature :

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

The slide *Built-in String Methods*, in module 02, lists a method that tells whether a string holds only letters. *return Statement* shows how a function passes a value back to its caller.

:::

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

Each letter of the secret can colour one letter of the guess. A letter in the right place is green and uses its matching secret letter first. Only the secret letters left over can make other guess letters yellow. Any guess letter that cannot use one of those remaining letters stays grey.

Keep the current game loop unchanged during this step. Build and check `score_guess` on its own; Step 5 connects it to the game.

#### 4a

Add this first version above `main`. It starts every position grey, marks exact matches green, and collects the unused secret letters. The first pass is given :

```python
def score_guess(secret: str, guess: str) -> list[str]:
    """Mark each letter of guess as "green", "yellow" or "grey".

    A letter is yellow only while the secret still has an unmatched copy of it,
    so one E in the secret cannot make two E's in the guess yellow.
    """
    marks = ["grey"] * WORD_LENGTH
    unmatched: list[str] = []

    for position, letter in enumerate(guess):
        if letter == secret[position]:
            marks[position] = "green"
        else:
            unmatched.append(secret[position])

    return marks
```

Start the interactive interpreter with `uv run python`, then import and call the function :

```text
>>> from wordle import score_guess
>>> score_guess("crane", "error")
['grey', 'green', 'grey', 'grey', 'grey']
```

Only the R at position `1` is green. That match has used CRANE's only R. At the end of this pass, `unmatched` contains `['c', 'a', 'n', 'e']`: these are the secret letters available for yellow matches.

:::hint
The slide *List Operations* builds a list by repetition, and *Iterating with enumerate* supplies a position and letter. *List Functions and Methods* shows `append`. Follow one position at a time through the supplied first loop.
:::

#### 4b

Insert a second loop immediately before `return marks`. Fill its condition and its final statement :

```python
    for position, letter in enumerate(guess):
        if ...:
            marks[position] = "yellow"
            ...
```

A letter can become yellow only when its position is not already green and the letter is still in `unmatched`. After marking it yellow, remove one copy of that letter from `unmatched`, so it cannot colour another position.

For ERROR against CRANE, the first E can use the remaining E and becomes yellow. The green R stays green. There is no R left for either of the later R's, so both stay grey.

:::hint
The slide *Logical, Membership, Identity Operators* combines conditions with `and` and checks membership with `in`. *List Functions and Methods* shows `remove`, which removes one matching item.
:::

:::hint
The condition combines `marks[position] != "green"` with `letter in unmatched`. After setting the mark, call `unmatched.remove(letter)`.
:::

Leave the interpreter with `exit()` and restart it after saving the change. Repeat the import before checking these three calls :

```text
>>> from wordle import score_guess
>>> score_guess("crane", "error")
['yellow', 'green', 'grey', 'grey', 'grey']
>>> score_guess("crane", "react")
['yellow', 'yellow', 'green', 'yellow', 'grey']
>>> score_guess("speed", "geese")
['grey', 'yellow', 'green', 'yellow', 'grey']
```

The last example checks repeated E's: SPEED has two, so GEESE can colour two of its three E's. The game still uses its old scoring until Step 5.

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

Your Exercise 4 code built this row already. The slide *match Statement* shows a `case` for each literal value and the wildcard `case _` for the rest.

:::

:::hint

A `match` on `marks[position]` reads well here.

:::

The game loop then shrinks to a single line where the scoring used to be :

```python
print(render(guess, score_guess(secret, guess)))
```

In the interpreter, `render("react", ["yellow", "yellow", "green", "yellow", "grey"])` now returns `'(R)(E)[A](C) T '`.

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

`max_guesses=8` allows an easier game; the default is six. See *Default Arguments*. Keep loading the words and choosing the secret in `main`, then call `play(secret, words)`. Keep `secret = "crane"` for repeatable checks.

:::hint

The slide *return Statement* shows that `return` exits the function at once, so a `return` inside the loop ends the loop as well.

:::

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
    secret = "crane"
    play(secret, words)
```

The complete file is in `solutions/05-functions/wordle.py`.

:::

---

Play with `error`, then `crane`, against the fixed secret. The captured output now shows only one coloured R :

:::output

```text
Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.
Guess 1/6 : (E)[R] R  O  R 
Guess 2/6 : [C][R][A][N][E]
Got it in 2!
```

:::

Change the `secret` variable in `main` to another word from the list and play again. Restore `"crane"` for the following checks.

### If time permits

Add a hard mode, in which every guess must use what the earlier guesses revealed. A green letter must stay in its place, and a yellow letter must appear somewhere. Write

```python
def follows_hints(guess: str, history: list[tuple[str, list[str]]]) -> bool:
```

where `history` holds every earlier guess with its marks as `(guess, marks)` pairs, which `play` has to keep as a list. Add a parameter `hard: bool = False` to `play`, and reject a guess that breaks the rule when it is `True`. Try guesses that obey and break each rule. There is no reference solution for this step.
