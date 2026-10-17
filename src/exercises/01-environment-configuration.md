# Exercise 1 : Python Intro

Before you can write a game you need somewhere to write it. This exercise installs Python, the `uv` project manager, the `ruff` linter and an editor that understands Python, and creates the project you build a Wordle game in for the rest of the course.

There is no starter for this exercise : it is where your own `wordle` project begins. From Exercise 2 on, every exercise also has a starter folder for when you fall behind.

Every step in this exercise gives you the commands : the point is to see each tool work once.

---

### Step 1 : Install uv

`uv` is the project manager the course uses. It can install Python itself, so it is the only thing you install by hand. On Windows, run this in PowerShell :

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

On macOS or Linux, run this in a terminal :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen the terminal afterwards so that `uv` is on your `PATH`, then confirm that it works :

```bash
uv --version
```

The documentation is at `https://docs.astral.sh/uv/`.

### Step 2 : Install Python

Let `uv` fetch the interpreter the course uses :

```bash
uv python install 3.14
```

This needs no administrator rights and leaves any Python already on the machine alone. Confirm it with `uv python list`, which shows every interpreter `uv` can see.

### Step 3 : Install an editor

Install Visual Studio Code from `https://code.visualstudio.com`, then add two extensions from the Extensions panel, the square icon on the left :

- `Python`, published by Microsoft
- `Ruff`, published by Astral

Any editor works, but the course demonstrates VS Code and the slides assume it. The slide *Editor Setup* lists what the two extensions do for you.

### Step 4 : Create the wordle project

You write your own code this week in a project of your own, the same way you would at work. From the folder where you keep your work, run :

```bash
uv init wordle
cd wordle
```

`uv init` writes a `pyproject.toml`, a `.python-version`, a `README.md` and a placeholder `main.py`, and makes the folder a git repository; the slide *Creating a Project* explains each of them. Run the placeholder :

```bash
uv run python main.py
```

The first run creates the project's own environment in `.venv`, then prints :

```text
Hello from wordle!
```

Open the `wordle` folder in VS Code. Then open the Command Palette, run `Python: Select Interpreter`, and choose the interpreter in `.venv`. The editor now uses the same Python as `uv run`.

### Step 5 : See the linter work

A linter reads code without running it and reports what looks wrong. Add `ruff` to the project as a development tool, one the project needs while you write it but not when it runs :

```bash
uv add --dev ruff
```

`uv` records it in `pyproject.toml` under `[dependency-groups]`, so anybody who works on the project gets the same tool. The test runner `pytest` arrives the same way in Exercise 5. Run `ruff` over the project :

```bash
uv run ruff check .
```

There is nothing wrong yet, so it reports :

```text
All checks passed!
```

Now write something with a mistake in it. Create `hello.py` in the project :

```python
import json


def greet(name: str) -> str:
    return f"Hello, {name}"


print(greet("Python"))
```

Run it with `uv run python hello.py`. It prints `Hello, Python`, so Python itself has no complaint. Run `uv run ruff check .` again. This time `ruff` reports the import nobody uses :

```text
F401 [*] `json` imported but unused
 --> hello.py:1:8
  |
1 | import json
  |        ^^^^
help: Remove unused import: `json`
  |
  - import json
1 |
  |

Found 1 error.
[*] 1 fixable with `--fix`.
```

`F401` is the rule, and the arrow points at the file, line and column. VS Code underlines the same line, because the Ruff extension runs the same checks as you type. The `[*]` means the fix is safe to make automatically, so let `ruff` make it :

```bash
uv run ruff check . --fix
```

It reports `Found 1 error (1 fixed, 0 remaining).`, and the import has gone from `hello.py`. The slide *Linting with ruff* has the other commands. You can delete `hello.py` now; the game does not need it.

### Step 6 : The word list

A word game needs words. Copy `words.txt` from `exercises/handouts/01-environment-configuration/` into the `wordle` folder, next to `pyproject.toml`.

Rename `main.py` to `wordle.py`, which is the name the game has from here on, and replace its contents with :

```python
from pathlib import Path


def main() -> None:
    """Print the number of characters in the word list."""
    words = Path("words.txt").read_text(encoding="utf-8")
    print(f"The word list contains {len(words)} characters.")


if __name__ == "__main__":
    main()
```

`Path("words.txt").read_text(...)` reads the whole file into one string, and `len` counts its characters. The rest of the file is the same shape as the `main.py` that `uv init` wrote; module 05 explains `def` and module 06 explains the last two lines. Run it :

```bash
uv run python wordle.py
```

It prints :

```text
The word list contains 5610 characters.
```

The file holds one five-letter word per line, so every word takes six characters including its line break. How many words are in the list? Exercise 3 counts them properly.

### If time permits

The course folder has a file that is written badly on purpose, `demos/01-pythonintro/03_ruff_findings.py`. Copy it into your `wordle` project and run `uv run ruff check 03_ruff_findings.py`. Read every finding, and decide why `ruff` objects before you read the comment in the file that explains it.

Then copy `ruff.toml` from the course folder into the project as well, and run the same command again. The course's configuration switches on more rules than the default set, so `ruff` now finds more. Which rules did it add, and would you want them in your own projects? Delete both files when you are done.
