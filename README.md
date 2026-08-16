# Python Programming (PRG400)

Welcome. This bundle contains everything you need for the course : the slides,
the lab exercises, runnable example code, reference solutions and some
background reading. This page explains what is here and how to run it.

This repository is refreshed automatically after every change to the course
material, so a `git pull` always gives you the latest version.

## What is in this bundle

- **`PRG400-Python-Programming.pdf`** : the course slides. The same deck is also
  available as `.html` if you prefer reading in a browser.
- **`PRG400-Python-Programming-Exercises.pdf`** : the lab guide, one exercise per
  module.
- **`demos/`** : the runnable example programs shown on the slides, one folder
  per module (for example `demos/05-functions/`). A slide that shows a demo names
  it at the bottom, for example `demo03 · overwritingreferences`, which is the
  file `demos/05-functions/03_overwritingreferences.py`.
- Type annotations appear from module 2 onwards, and
  **`demos/12-appendix-type-hinting/`** gathers them up in the appendix.
- **`solutions/`** : reference solutions for the exercises, in case you get stuck
  or want to compare. Try the exercise first.
- **`exercises/`** : supporting files for a few of the exercises.
- **`appendices/`** : the appendix decks and their exercises.
- **`reference/`** : background reading, none of it required. The official
  Python 3.14 documentation as PDFs, articles on single topics, books,
  cheatsheets, and material on GUI work, notebooks and packaging. It has its
  own `README.md` describing what is where.

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

3. Install an editor. The course demonstrates
   [**VS Code**](https://code.visualstudio.com) with the Microsoft **Python**
   extension and the Astral [**Ruff**](https://docs.astral.sh/ruff/) extension.
   Any editor works, but the slides assume VS Code.

## Creating your own project

You build your own project for the code you write this week, the same way you
would at work. The bundle deliberately ships no `pyproject.toml`, you create one :

```bash
uv init course-work
cd course-work
```

`uv init` writes a `pyproject.toml` and pins the project to a Python version.
When an exercise needs a package, add it from inside that folder :

```bash
uv add requests
```

The last module uses a type checker, which you add the same way :

```bash
uv add --dev mypy
```

The bundle does ship a `ruff.toml`. That is the linter configuration the course
material is written against, so the Ruff extension will not flag the demo files
over style choices the course makes on purpose, and it holds the code you write
to the same rules.

## Running a demo

The demos are plain scripts. Run one by giving its path :

```bash
uv run python ../demos/05-functions/03_overwritingreferences.py
```

Running through `uv run` guarantees the command uses your project's Python and
its packages, so you never have to activate an environment by hand.

## Checking your own code

Two commands are worth getting into the habit of. The course sets both up in
module 1 and uses them throughout :

```bash
uv run ruff check .      # style and correctness, without running anything
uv run mypy .            # type checking, once you have added annotations
```

Enjoy the course.
