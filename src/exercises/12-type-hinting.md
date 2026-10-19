<!-- appendix -->
# Exercise 12 : Type Hinting

Your game already carries type hints on collections and functions. Python itself does not enforce them. In this exercise you hand the hints to `mypy`, a tool that reads the whole package without running it and reports where the types do not fit. It helps you describe the marks of a guess precisely and makes callers handle a solver result that may be missing.

Continue in your own `wordle` project, or start from `exercises/starters/12-type-hinting/`. The starter is the finished Exercise 11; this exercise hands out nothing. Keep running commands beside `pyproject.toml`.

Some steps give you the code, some a list of changes to make, and one only a signature and what it should do. Where you write the code yourself, the solution is hidden until you open it. Try the step first; the solution is there for when you are stuck, or to compare afterwards. This exercise is an appendix : do the steps in order.

---

### Step 1 : Run mypy

`mypy` is a tool for checking the code while developing it. `uv add --dev` installs such a tool for this project and records it in `pyproject.toml`. Install it and run it on the package :

```bash
uv add --dev mypy
uv run mypy wordle
```

```text
wordle\game.py:65: error: Need type annotation for "used_letters" (hint: "used_letters: set[<type>] = ...")  [var-annotated]
Found 1 error in 1 file (checked 8 source files)
```

Each message has a file, a line number, what is wrong and a code in brackets. The line number in your own project may differ. `used_letters = set()` is an empty set, and the checker cannot tell from that what it will hold. You know it holds letters. Tell it, with a hint on the variable, as you did for collections in *Typing Collections* :

```python
    used_letters: set[str] = set()
```

Run `uv run mypy wordle` again :

```text
Success: no issues found in 8 source files
```

See *Checking with mypy* for the same run on a smaller program.

:::hint
The slide *Checking with mypy* shows installing and running the checker. *Annotating Collections*, in module 03, shows `set[str]` for a set of strings.
:::

### Step 2 : Say exactly what a mark is

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
wordle\game.py:53: error: Argument 1 to "append" of "list" has incompatible type "tuple[str, list[Literal['green', 'yellow', 'grey']]]"; expected "tuple[str, list[str]]"  [arg-type]
wordle\game.py:54: error: Incompatible return value type (got "list[Literal['green', 'yellow', 'grey']]", expected "list[str]")  [return-value]
Found 3 errors in 2 files (checked 8 source files)
```

`mypy` also prints a few lines starting with `note:`, which are left out here. A single change has shown you every place the idea of a mark runs through. Work through them :

- in `score_guess`, the list `marks` starts as `["grey"] * WORD_LENGTH`; annotate it as `marks: list[Mark]`
- in `wordle/game.py`, import `Mark` from `wordle.scoring`, and use it in the annotation of `self.history` (`list[tuple[str, list[Mark]]]`) and in the return type of `Game.guess`
- the same two spots in `wordle/solver.py` (`consistent` and `candidates`) and the `marks` parameter of `render` in `wordle/display.py` are not flagged, but they describe marks too, so give them `Mark` as well

Run `uv run mypy wordle` until it reports `Success`. To see what you gained, misspell a mark in `score_guess` : change `"yellow"` into `"yelow"`, run `mypy`, and put it back. The first line of its report points at the assignment :

```text
wordle\scoring.py:44: error: No overload variant of "__setitem__" of "list" matches argument types "int", "str"  [call-overload]
```

The message is not friendly, but the file and line are right. Play a game as well : Python ignores annotations, so it plays as before.

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

In `wordle/game.py`, `solver.py` and `display.py`, import `Mark` with `from wordle.scoring import Mark` (`game.py` already imports from that module, so add `Mark` to its import) and replace `list[str]` by `list[Mark]` where it describes marks :

```python
        self.history: list[tuple[str, list[Mark]]] = []

    def guess(self, word: str) -> list[Mark]:

def consistent(word: str, guess: str, marks: list[Mark]) -> bool:

def candidates(words: list[str], history: list[tuple[str, list[Mark]]]) -> list[str]:

def render(guess: str, marks: list[Mark]) -> str:
```
:::

### Step 3 : A hint that may not exist

`best_guess` returns a word, and it returns it for any list you give it. Ask for a hint when no word is left and see what happens. This can only happen when the secret is a word the game accepts as a guess but never picks, so start the game after changing `secret = "crane"` to `secret = "crone"` in `wordle/__main__.py`, guess `crane`, and type `hint` :

```text
ValueError: max() iterable argument is empty
```

The game stops with a traceback, and the type hints never warned about it, because `-> str` promised a word that cannot exist. The honest signature says that the answer may be missing. Python writes "a `str` or `None`" as `str | None`. See *Optional Values*.

Here is the new signature of `best_guess` in `wordle/solver.py` :

```python
def best_guess(words: list[str]) -> str | None:
    """Choose the word with the most frequently occurring distinct letters."""
```

Make it return `None` for an empty list. Then run `uv run mypy wordle`. The checker does not need to run the game to find the next problem : `play` calls `.upper()` on the result, and `None` has no `.upper()`.

```text
wordle\game.py:76: error: Item "None" of "str | None" has no attribute "upper"  [union-attr]
Found 1 error in 1 file (checked 8 source files)
```

That is the whole use of `| None` : the checker makes every caller deal with the case that there is no answer. Fix the `hint` command in `play` so that it prints `No candidate words remain.` when there is no suggestion, and the old message when there is one. Run `mypy` again until it reports `Success: no issues found in 8 source files`, then repeat the experiment with `crone` :

```text
[C][R] A [N][E]
No candidate words remain.
```

The first line is the row for the guess `crane`; the second is the answer to `hint`. Restore `secret = "crane"` after this check.

:::hint
The slide *Optional Values* writes `| None` for a value that may be absent, and tests `is None` before it uses the value.
:::

:::hint
`if not words: return None` at the top of `best_guess` is enough. The rest of the function stays as it is.
:::

:::hint
In `play`, keep the result in a variable first : `suggestion = best_guess(possible)`. Then test `if suggestion is None:` and print the message, `else` print the old line using `suggestion.upper()`. After the test, the checker knows that `suggestion` is a `str`.
:::

:::output
```text
Success: no issues found in 8 source files
```
:::

:::solution
```python
def best_guess(words: list[str]) -> str | None:
    """Choose the word with the most frequently occurring distinct letters."""
    if not words:
        return None
    counts = letter_counts(words)
    return max(words, key=lambda word: sum(counts[letter] for letter in set(word)))
```

The `hint` command in `play` :

```python
            case "hint":
                possible = candidates(words, game.history)
                suggestion = best_guess(possible)
                if suggestion is None:
                    print("No candidate words remain.")
                else:
                    print(f"{len(possible)} words left, try {suggestion.upper()}")
                continue
```

The finished project is in `solutions/12-type-hinting/`.
:::

---

### If time permits

Make `mypy` stricter. Add a `[tool.mypy]` section with `strict = true` to `pyproject.toml`, run `uv run mypy wordle`, and fix what it reports. A project with this much annotation has little to fix : `summary` in `wordle/stats.py` returns a bare `dict`, and strict mode wants to know what is inside. There is no reference solution for this step.
