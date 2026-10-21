<!-- appendix -->
# Exercise 12 : Type Hinting

Your game already carries type hints on collections and functions. Python itself does not enforce them. In this exercise you hand the hints to `mypy`, a tool that reads the whole package without running it and reports where the types do not fit. It helps you describe the marks of a guess precisely and makes callers handle a hint that may be missing.

Continue in your own `wordle` project, or start from `exercises/starters/12-type-hinting/`. The starter is the finished Exercise 11; this exercise hands out nothing. The solution is in `solutions/12-type-hinting/`. `mypy` runs in the terminal : keep it in the project folder, beside `pyproject.toml`.

Some steps give you the code, some a list of changes to make, and one only a signature and what it should do. Where you write the code yourself, the solution is hidden until you open it. Try the step first; the solution is there for when you are stuck, or to compare afterwards. This exercise is an appendix : do the steps in order.

---

### Step 1 : Run mypy

:::task
Install `mypy`, run it on the project and fix the one thing it reports.
:::

```text
wordle/
    pyproject.toml       <- uv add --dev records mypy here
    main.py
    wordle/
        game.py          <- annotate used_letters
```

`mypy` is a tool for checking the code while developing it. `uv add --dev` installs such a tool for this project and records it in `pyproject.toml`. Install it and run it on the package :

```bash
uv add --dev mypy
uv run mypy wordle main.py
```

```text
wordle\game.py:71: error: Need type annotation for "used_letters" (hint: "used_letters: set[<type>] = ...")  [var-annotated]
Found 1 error in 1 file (checked 8 source files)
```

Each message has a file, a line number, what is wrong and a code in brackets. The line number in your own project may differ. `used_letters = set()` is an empty set, and the checker cannot tell from that what it will hold. You know it holds letters. Tell it, with a hint on the variable, as you did for collections in *Typing Collections* :

```python
    used_letters: set[str] = set()
```

Run `uv run mypy wordle main.py` again :

```text
Success: no issues found in 8 source files
```

See *Checking with mypy* for the same run on a smaller program.

:::hint
The slide *Checking with mypy* shows installing and running the checker. *Annotating Collections*, in module 03, shows `set[str]` for a set of strings.
:::

### Step 2 : Say exactly what a mark is

:::task
Define a type `Mark` that allows only `"green"`, `"yellow"` and `"grey"`, and use it everywhere the code handles marks, until `mypy` reports no issues.
:::

```text
wordle/
    main.py
    wordle/
        scoring.py       <- define Mark, use it in score_guess
        game.py          <- use Mark in Game
        display.py       <- use Mark in render and colour_row
```

The marks that `score_guess` returns are declared as `list[str]`. That is true, but it is also true of `["gray", "blue", "yes"]`. The game only has three marks : `"green"`, `"yellow"` and `"grey"`. A type that lists exactly those can be checked.

In `wordle/scoring.py`, import `Literal` from `typing`, and give the three values a name below `WORD_LENGTH` :

```python
from typing import Literal

type Mark = Literal["green", "yellow", "grey"]
```

A `Literal` type is the type of those values and no others : a `str` accepts `"gray"` as happily as `"grey"`, but `Mark` does not, so a misspelt mark becomes a message from `mypy` instead of a game that quietly shows the wrong colour. See *Closed Sets with Literal*. The `type` line defines a name for it, so the rest of the code can say `Mark`.

Now change one thing only : the return type of `score_guess` becomes `list[Mark]`. Run `mypy` and read what it finds :

```text
wordle\scoring.py:46: error: Incompatible return value type (got "list[str]", expected "list[Literal['green', 'yellow', 'grey']]")  [return-value]
wordle\game.py:59: error: Argument 1 to "append" of "list" has incompatible type "tuple[str, list[Literal['green', 'yellow', 'grey']]]"; expected "tuple[str, list[str]]"  [arg-type]
wordle\game.py:60: error: Incompatible return value type (got "list[Literal['green', 'yellow', 'grey']]", expected "list[str]")  [return-value]
Found 3 errors in 2 files (checked 8 source files)
```

`mypy` also prints a few lines starting with `note:`, which are left out here. A single change has shown you every place the idea of a mark runs through. Work through them :

- in `score_guess`, the list `marks` starts as `["grey"] * WORD_LENGTH`; annotate it as `marks: list[Mark]`
- in `wordle/game.py`, import `Mark` from `wordle.scoring`, and use it in the annotation of `self.history` (`list[tuple[str, list[Mark]]]`) and in the return type of `Game.guess`
- run `mypy` again : now it flags the calls of `render` and `colour_row`, because their `marks` parameter still says `list[str]`. Give that parameter the type `list[Mark]` in `wordle/display.py`

Run `uv run mypy wordle main.py` until it reports `Success`.

To see what you gained, make a typing mistake on purpose. Create a file `mark_check.py` beside `main.py`, with a misspelt mark :

```python
from wordle.display import render

print(render("crane", ["green", "yelow", "grey", "grey", "grey"]))
```

Check it with `uv run mypy mark_check.py`. The checker finds the typo without running anything :

```text
mark_check.py:3: error: List item 1 has incompatible type "Literal['yelow']"; expected "Literal['green', 'yellow', 'grey']"  [list-item]
```

Read it from left to right : the file and line, then item 1 of the list (counting from 0, the second mark), then what it found, the text `'yelow'`, and what it expected, one of the three marks of `Mark`. Now run the file with `uv run python mark_check.py`. Python ignores annotations, so it finds the same mistake only when the line runs, as `KeyError: 'yelow'`. Delete `mark_check.py` afterwards.

:::hint
The slide *Closed Sets with Literal* defines a `Literal` type with `type` and uses it in a signature.
:::

:::hint
A `type` statement and a `Literal` need `from typing import Literal` and nothing else. Other modules import the alias like any name : `from wordle.scoring import Mark`.
:::

:::hint
`marks: list[Mark] = ["grey"] * WORD_LENGTH` is an annotation on the first assignment. Without it, the checker infers `list[str]` for the list and complains when you return it as `list[Mark]`.
:::

:::solution
In `wordle/scoring.py` :

```python
from typing import Literal

WORD_LENGTH = 5

type Mark = Literal["green", "yellow", "grey"]


def score_guess(secret: str, guess: str) -> list[Mark]:
    """Return Wordle marks while counting each secret letter only once."""
    marks: list[Mark] = ["grey"] * WORD_LENGTH
    ...
```

In `wordle/game.py` and `display.py`, import `Mark` with `from wordle.scoring import Mark` (`game.py` already imports from that module, so add `Mark` to its import) and replace `list[str]` by `list[Mark]` where it describes marks :

```python
        self.history: list[tuple[str, list[Mark]]] = []

    def guess(self, word: str) -> list[Mark]:

def render(guess: str, marks: list[Mark]) -> str:

def colour_row(guess: str, marks: list[Mark]) -> Text:
```
:::

### Step 3 : A hint that may not exist

:::task
Let `hint` return `None` when every letter of the secret has been tried, and let the `hint` command in `play` handle that case.
:::

```text
wordle/
    main.py
    wordle/
        hints.py         <- hint returns str | None
        game.py          <- handle None in case "hint"
```

`hint` returns a letter, and it promises one for any game. Ask for a hint when every letter of the secret has been tried and see what happens. Keep `secret = "crane"` in `main.py`, start the game, guess `nacre`, which has the same five letters in another order, and type `hint` :

```text
IndexError: list index out of range
```

The game stops with a traceback, and the type hints never warned about it, because `-> str` promised a letter that cannot exist : the list of untried letters is empty, so it has no item `[0]`. The honest signature says that the answer may be missing. Python writes "a `str` or `None`" as `str | None`. See *Optional Values*.

Here is the new signature of `hint` in `wordle/hints.py` :

```python
def hint(secret: str, used: set[str]) -> str | None:
    """Return the first letter of the secret that has not been tried yet, if any."""
```

Make it return `None` when no untried letter is left. Then run `uv run mypy wordle main.py`. The checker does not need to run the game to find the next problem : `play` calls `.upper()` on the result, and `None` has no `.upper()`.

```text
wordle\game.py:83: error: Item "None" of "str | None" has no attribute "upper"  [union-attr]
Found 1 error in 1 file (checked 8 source files)
```

That is the whole use of `| None` : the checker makes every caller deal with the case that there is no answer. Fix the `hint` command in `play` so that it prints `No hint left: you have tried every letter of the word.` when there is no letter, and the old message when there is one. Run `mypy` again until it reports `Success: no issues found in 8 source files`, then repeat the experiment with `nacre` :

```text
(N)(A)(C)(R)[E]
No hint left: you have tried every letter of the word.
```

The first line is the row for the guess `nacre`; the second is the answer to `hint`.

:::hint
The slide *Optional Values* writes `| None` for a value that may be absent, and tests `is None` before it uses the value.
:::

:::hint
Keep the list comprehension. Below it, `if not untried: return None`, then return the first item as before.
:::

:::hint
In `play`, keep the result in a variable first : `letter = hint(secret, used_letters)`. Then test `if letter is None:` and print the message, `else` print the old line using `letter.upper()`. After the test, the checker knows that `letter` is a `str`.
:::

:::output
```text
Success: no issues found in 8 source files
```
:::

:::solution
```python
def hint(secret: str, used: set[str]) -> str | None:
    """Return the first letter of the secret that has not been tried yet, if any."""
    untried = [letter for letter in secret if letter not in used]
    if not untried:
        return None
    return untried[0]
```

The `hint` command in `play` :

```python
            case "hint":
                letter = hint(secret, used_letters)
                if letter is None:
                    print("No hint left: you have tried every letter of the word.")
                else:
                    print(f"The word contains the letter {letter.upper()}.")
                continue
```

The finished project is in `solutions/12-type-hinting/`.
:::

---

### If time permits

Make `mypy` stricter. Add a `[tool.mypy]` section with `strict = true` to `pyproject.toml`, run `uv run mypy wordle main.py`, and fix what it reports. A project with this much annotation has little to fix : `summary` in `wordle/stats.py` returns a bare `dict`, and strict mode wants to know what is inside. There is no reference solution for this step.
