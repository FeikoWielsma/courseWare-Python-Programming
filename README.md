# Python Programming (PRG400)

Welcome. This bundle contains everything you need for the course : the slides,
the lab exercises, runnable example code, reference solutions and some
background reading. This page explains what is here and how to run it.

This repository is refreshed automatically after every change to the course
material, so a `git pull` always gives you the latest version.

## What is in this bundle

- **`slides/`** : the animated course presentation. From the course folder, run
  `python slides/serve.py`, then open <http://localhost:4188/slidev/>. Arrow keys
  or scrolling move through the steps; going back reverses them.
- **`PRG400-Python-Programming.pdf`** : the slides as a PDF, showing the completed
  examples. **`PRG400-Python-Programming-Marp.html`** and **`-Marp.pdf`** are the
  static fallback deck; the HTML opens directly from disk.
- **`PRG400-Python-Programming-Exercises.pdf`** : the lab guide, one exercise per
  module.
- **`site/index.html`** : the same exercises as a small website that opens from
  disk. Each step has hints and its solution behind a click, you can tick steps
  off as you go, and there is a quiz for the end of the course.
- **`demos/`** : the runnable example programs shown on the slides, one folder
  per module (for example `demos/05-functions/`). A slide that shows a demo names
  it at the bottom, for example `demo10 · overwritingreferences`, which is the
  file `demos/05-functions/10_overwritingreferences.py`.
- Type annotations appear from module 2 onwards, and
  **`demos/12-appendix-type-hinting/`** gathers them up in the appendix.
- **The exercises build one project, a Wordle game**, from Exercise 2 to the end.
  Some steps give you the code, some a skeleton to complete, and some only the
  signature and expected output, with the solution behind a click.
- **`solutions/`** : the finished game as it stands at the end of each exercise,
  one folder per exercise. Try the exercise first.
- **`exercises/starters/`** : if you fell behind, start an exercise from its
  starter folder instead of your own code. The starter for an exercise is the
  solution of the one before, plus anything that exercise hands out.
- **`exercises/handouts/`** : files an exercise hands out, such as the word lists
  and data files.
- **`appendices/`** : the appendix decks and their exercises.
- **`reference/`** : background reading, none of it required. The official
  Python 3.14 documentation as PDFs, articles on single topics, books,
  cheatsheets, and material on GUI work, notebooks and packaging. It has its
  own `README.md` describing what is where.

## Following the course online : GitHub Codespaces

If you join remotely, or cannot install software on your machine, you can do
the whole course in your browser. You need a free GitHub account; it includes
60 hours a month of Codespaces, which is more than the course uses.

1. Open <https://codespaces.new/FeikoWielsma/Python-Programming-Student> and
   click **Create codespace**. The first start takes a few minutes.
2. You get VS Code in the browser with Python 3.14, uv and the Python and Ruff
   extensions already installed, and this bundle already opened. Skip the
   installation steps below and continue at **Creating your own project**,
   using the **Terminal** menu to open a terminal.
3. Your work is kept inside the codespace between days. Reopen it from
   <https://github.com/codespaces>. A codespace stops itself after 30 minutes
   of inactivity; that is harmless, your files stay.

The tkinter GUI demos need a desktop and do not open a window in a codespace.
To view the animated slides in Codespaces, run `python slides/serve.py` in the
terminal, then open **Course slides** on port **4188** in the **Ports** panel.

## Setting up Python

1. Install [**uv**](https://docs.astral.sh/uv/), the Python project manager. It
   can install Python itself, so it is the only thing you install by hand.
   - Windows (PowerShell) :

     ```powershell
     powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
     ```

   - macOS or Linux :

     ```bash
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```

   Close and reopen your terminal afterwards, then check it with `uv --version`.

2. Install the interpreter the course uses :

   ```bash
   uv python install 3.14
   ```

   This needs no administrator rights and leaves any Python already on the
   machine alone.

3. Install [**VS Code**](https://code.visualstudio.com) with the Microsoft
   **Python** extension. Exercise 1 explains how to open a folder, create a
   Python file, save it and run it. The optional *Python Tooling and Reference*
   appendix covers Ruff and the more detailed project settings.

## Creating your own project

You build your own project for the code you write this week, the same way you
would at work. The bundle deliberately ships no `pyproject.toml`, you create one :

```bash
uv init --bare --python 3.14 wordle
cd wordle
```

This creates the `wordle` folder and a `pyproject.toml` with the project's Python
requirement. Exercise 1 walks through creating and running `wordle.py` inside it.
When an exercise needs a tool or a package, add it
from inside that folder, for example the type checker in the type hinting appendix :

```bash
uv add --dev mypy
```

and the test runner in the libraries appendix (Exercise 13) :

```bash
uv add --dev pytest
```

A starter folder is a complete project of its own : `cd` into it and
`uv run python -m wordle` (or `uv run python wordle.py` before Exercise 6) works
straight away.

The bundle also ships `ruff.toml`, the configuration used to check the course
code. Ruff is optional for the opening exercises; the tooling appendix explains
its editor extension, checks and formatting commands.

## Running a demo

The demos are plain scripts. Run one by giving its path :

```bash
uv run python ../demos/05-functions/10_overwritingreferences.py
```

Running through `uv run` guarantees the command uses your project's Python and
its packages, so you never have to activate an environment by hand.

## Checking your own code

Three commands are worth getting into the habit of. Ruff arrives in Exercise 1,
mypy in the type hinting appendix and pytest in the libraries appendix :

```bash
uv run ruff check .      # style and correctness, without running anything
uv run mypy wordle       # type checking, once you have added annotations
uv run pytest            # run the tests (Exercise 13)
```

Enjoy the course.

## Optional libraries and tools

[libraries/README.md](libraries/README.md) describes the optional topics, their
setup and runnable demos. This is a separate selection for the trainer to choose
with the group: command-line tools, third-party libraries, scraping, SQLAlchemy,
NumPy, pandas, desktop windows and subprocesses. Inheritance is an optional
preview of Advanced Python.

The slides and exercises are separate PDFs in `libraries/`, named
`PRG400-Python-Libraries-and-Tools.pdf` and
`PRG400-Python-Libraries-and-Tools-Exercises.pdf`. The folder has its own
`pyproject.toml` and lockfile; run `uv sync` from inside `libraries/` before using
its examples.
