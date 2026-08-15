# Exercise 1 : Python Tooling

This exercise takes about fifteen minutes and leaves you with a working Python 3.14, the `uv` project manager, the `ruff` linter and an editor that understands Python. Everything you do in the rest of the course runs in the project you build here.

---

### Step 1 : Install uv

`uv` is the project manager the course uses, and it can install Python itself, so it is the only thing you install by hand. On Windows, run this in PowerShell :

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

On macOS or Linux, run this in a terminal :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen the terminal afterwards so that `uv` is on your `PATH`, then confirm it works with `uv --version`.

See also : https://docs.astral.sh/uv/

### Step 2 : Install Python

Let `uv` fetch the interpreter the course uses :

```bash
uv python install 3.14
```

This needs no administrator rights and leaves any Python already on the machine alone. Confirm it with `uv python list`.

---

### Step 3 : Install an editor

Install Visual Studio Code from `https://code.visualstudio.com`, then add two extensions from the Extensions panel, the square icon on the left :

- `Python`, published by Microsoft
- `Ruff`, published by Astral

Any editor works, but the course demonstrates VS Code and the slides assume it.

See also : https://docs.astral.sh/ruff/

### Step 4 : Create your course project

You write your own code this week in a project of your own, the same way you would at work. From the folder where you keep your work :

```bash
uv init course-work
cd course-work
```

Open that folder in VS Code, then use the Command Palette, `Python: Select Interpreter`, and choose the interpreter in `.venv`.

---

### Step 5 : Confirm the toolchain runs

Run each of these from inside `course-work` :

```bash
uv --version
uv run python --version      # prints Python 3.14.x
uv run ruff --version
```

Then write a first script. Create `hello.py` in the project :

```python
def greet(name):
    return f"Hello, {name}"


print(greet("Python"))
```

Run it with `uv run python hello.py`. You should see `Hello, Python`.

### Step 6 : See the linter work

Run the linter over your project :

```bash
uv run ruff check .
```

It should report nothing. Now break something on purpose. Add an unused import at the top of `hello.py` :

```python
import json
```

Run `uv run ruff check .` again. It reports `F401 'json' imported but unused`. Notice that VS Code underlines the same line. Remove the import, or let the linter do it for you :

```bash
uv run ruff check . --fix
```

**If time permits** : look at `demos/00a-python-tooling/02_ruff_findings.py`, which is written badly on purpose. Run `uv run ruff check` over it and read every finding before you look at the comments explaining them.
