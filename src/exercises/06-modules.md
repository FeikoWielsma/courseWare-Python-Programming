# Exercise 6 : Modules

The scoring can now be tested on its own, but loading words, drawing rows and running the game still share one file. Split those responsibilities into a package so the solver in the next exercise has a clear place to live.

Continue in your own `wordle` project, or use `exercises/starters/06-modules/`, the finished Exercise 5 plus this exercise's handouts. Allow about 45 minutes. Run commands from the project root, beside `pyproject.toml` and `words.txt`, not from inside the new package directory.

### Step 1 : Start a package {★}

Create a directory named `wordle` inside your project and an empty `wordle/__init__.py`. That file marks the directory as a package; see *Packages in Python*. Copy `load_words` into `wordle/words.py` with its import :

```python
from pathlib import Path


def load_words(path: str = "words.txt") -> list[str]:
    """Read the word list, one word per line."""
    return Path(path).read_text(encoding="utf-8").split()
```

Keep the original `wordle.py` intact for this step so `uv run python wordle.py` still plays a game. In the next step you will finish the package and remove that old file. Leave `words.txt` beside `pyproject.toml`; moving the loader does not change the working directory.

### Step 2 : Give each module one job {★★}

Move the existing functions into the following files. Keep their signatures and bodies; this is a change of organisation, not of scoring rules.

| File | What belongs there |
| --- | --- |
| `wordle/scoring.py` | `WORD_LENGTH`, `is_valid`, `score_guess` |
| `wordle/display.py` | `render` |
| `wordle/game.py` | `play` |
| `wordle/__main__.py` | `main` and the `if __name__ == "__main__":` guard |

Fill the import slots at the top of `game.py` :

```python
from wordle.display import ...
from wordle.scoring import ...

# Move play here, keeping its body and annotations.
```

Use this skeleton in `__main__.py` :

```python
import os
import random

from wordle.game import ...
from wordle.words import ...


def main() -> None:
    words = ...
    ...  # keep the welcome message and call play with the chosen secret


if __name__ == "__main__":
    main()
```

Delete the old `wordle.py` once the package is complete. Check it with `uv run python -m wordle`.

:::hint

`game.py` needs the renderer and both scoring functions. Neither of those modules imports the game. See *from...import Statement*.

:::

:::solution

The complete moved functions are in `solutions/06-modules/wordle/`. The functions retain their Exercise 5 behaviour. These are the imports in `game.py` :

```python
from wordle.display import render
from wordle.scoring import is_valid, score_guess
```

`__main__.py` contains :

```python
import os
import random

from wordle.game import play
from wordle.words import load_words


def main() -> None:
    """Load the words and play one game."""
    words = load_words()
    print("Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.")
    play(os.environ.get("WORDLE_SECRET", random.choice(words)), words)


if __name__ == "__main__":
    main()
```

:::

### Step 3 : Run the package {★}

Run from the project root :

```bash
uv run python -m wordle
```

The `-m` option asks Python to locate a module or package. For a package, Python runs `wordle/__main__.py`. The guard moved with the entry point; importing `wordle.scoring` does not start a game.

For a repeatable check in PowerShell, run :

```powershell
$env:WORDLE_SECRET = "crane"
uv run python -m wordle
```

In Bash, use `WORDLE_SECRET=crane uv run python -m wordle`. Enter `slate`, then `crane`. Captured output, with typed input omitted :

:::output

```text
Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.
Guess 1/6 :  S  L [A] T [E]
Guess 2/6 : [C][R][A][N][E]
Got it in 2!
```

:::

### Step 4 : Test the new boundaries {★★}

The old `test_wordle.py` imports from the single-file version. Remove that test file and use `tests/test_scoring.py` and `tests/test_display.py` from `exercises/handouts/06-modules/`. They are already present in the starter. The handouts regroup the earlier checks into four tests; the smaller count is intentional.

Before inspecting their imports, fill these two import lines yourself, one for each test file :

```python
# tests/test_scoring.py
from wordle.scoring import ...
```

```python
# tests/test_display.py
from wordle.display import ...
```

Add this section to `pyproject.toml` so pytest can import the local package from the project root :

```toml
[tool.pytest.ini_options]
pythonpath = ['.']
```

Run `uv run pytest` and fix any import errors before changing function bodies.

:::hint

Import each function from the module that defines it, not from `wordle` itself. An empty `__init__.py` does not automatically import the other modules. Check that the old `test_wordle.py` has gone.

:::

:::output

The final line from a passing run is shown below; timings vary.

```text
============================== 4 passed in 0.07s ==============================
```

:::

:::solution

The scoring tests import :

```python
from wordle.scoring import is_valid, score_guess
```

The display test imports :

```python
from wordle.display import render
```

Your project now has this shape, apart from environment and lock files :

```text
wordle/
    pyproject.toml
    words.txt
    wordle/
        __init__.py
        __main__.py
        words.py
        scoring.py
        display.py
        game.py
    tests/
        test_scoring.py
        test_display.py
```

:::

Remove the fixed-secret override with `Remove-Item Env:WORDLE_SECRET` in PowerShell, or `unset WORDLE_SECRET` if exported in Bash. Play another game with `uv run python -m wordle`. Its behaviour should be the same as Exercise 5, with the duplicate-letter fix intact.

### If time permits

Try colour as an optional display experiment. Install `rich` with `uv add rich`, then use its printing support to colour a row when displaying it. Keep the text returned by `render` unchanged so the existing display test still passes. See *Installing Packages* for dependencies.

The following exercises and reference solutions continue with the text markers; colour is not required to proceed.
