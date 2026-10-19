# Python Libraries and Tools

Optional material for the Python Programming course (PRG400). Choose topics with
the trainer to suit the group. The modules are a selection, not an additional
required day or a continuation of the Wordle exercises.

Start with command-line programs for scripting, web scraping and SQLAlchemy for
working with databases, NumPy and pandas for data work, or GUI toolkits for desktop
programs. The inheritance module previews Advanced Python and can be skipped.
The web-scraping and SQLAlchemy modules share the book dataset; SQLAlchemy can
rebuild the database from the supplied seed without running the scraper first.
The data modules share a music listening history; NumPy also uses a photo and a
generated audio tone. Play counts are fictional. Song editions and the photo
source are recorded in [data/SOURCES.md](data/SOURCES.md).

This folder has its own Python project. Run the commands below from `libraries/`.

Extra material for the Python Programming course (PRG400). The fundamentals
course covers the language itself. This material covers the libraries and tools
built around it : class design and inheritance, command-line programs,
third-party libraries worth knowing, web scraping into a database, SQLAlchemy,
NumPy, pandas, GUI toolkits, and an appendix on running other programs.

It is self-contained. Nothing here depends on the fundamentals bundle, and every
demo runs offline.

## What is in this bundle

- **`PRG400-Python-Libraries-and-Tools.pdf`** : the Slidev slides, with every
  reveal visible for reading and printing.
- **`slides/`** : the animated presentation. From this folder, run
  `python slides/serve.py`, then open `http://localhost:4188/slidev/`.
  Arrow keys and the mouse wheel advance or reverse reveals.
- **`PRG400-Python-Libraries-and-Tools-slides.zip`** : a separate release download
  containing the presentation, Python launcher and PDF. Extract it before use.
- **`../archive/PRG400-Python-Libraries-and-Tools-Marp.pdf`** and **`.html`** : the
  optional static fallback, kept in the course archive. The HTML opens from disk.
- **`PRG400-Python-Libraries-and-Tools-Exercises.pdf`** : the exercises, one per module.
- **`demos/`** : the runnable example programs shown on the slides, one folder
  per module. A slide that shows a demo names it at the bottom, for example
  `demo09 · views_and_copies`, which is the file
  `demos/06-numpy/09_views_and_copies.py`.
- **`solutions/`** : reference solutions for the exercises.
- **`exercises/starters/`** : starting files to copy into your own work folder.
- **`data/`** : the CSV, HTML, spreadsheet and database files the demos read.
- **`reference/`** : background reading and bonus examples, none of it required.

The modules :

| Folder | Module |
|---|---|
| `demos/01-inheritance/` | Classes that build on each other |
| `demos/02-command-line-programs/` | Scripts that behave like proper command-line tools |
| `demos/03-modern-toolbelt/` | Progress bars, colour, tables, and judging a library |
| `demos/04-web-scraping/` | Reading a web page into a database |
| `demos/05-sqlalchemy/` | Databases without writing every query by hand |
| `demos/06-numpy/` | Arrays of numbers |
| `demos/07-pandas/` | Tables of anything |
| `demos/08-gui/` | Desktop windows with tkinter; interactive demos, no exercise handout or solution |
| `demos/09-appendix-subprocess/` | Running other programs |

## Setting up

The material needs Python 3.14 and [**uv**](https://docs.astral.sh/uv/), the
Python project manager. If uv is not installed :

- Windows (PowerShell) :

  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

- macOS or Linux :

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

From the folder you unzipped this into, install the dependencies :

```bash
uv sync
```

That reads `pyproject.toml`, installs NumPy, pandas, SQLAlchemy, requests,
BeautifulSoup, rich, tqdm and the rest into a local `.venv/`, and pins the
interpreter. There is no environment to activate afterwards.

Unlike the fundamentals bundle, this one ships a `pyproject.toml` and a
`uv.lock`, because the material is about third-party libraries rather than the
standard library.

### tkinter on Linux

Module 08 uses `tkinter`, which is part of the standard library but is packaged
separately by most Linux distributions. On Debian and Ubuntu :

```bash
sudo apt install python3-tk
```

Check it with :

```bash
python -c "import tkinter; print(tkinter.TkVersion)"
```

## Running a demo

The web-scraping demos and solutions use `data/books-fixture.html` by default.
Pass `--live` to fetch the real site instead. The scraping solution's offline
run covers the first page; `--live` also includes the optional second page.

Every demo is a plain script that runs on its own and prints its results. Run
one by giving its path :

```bash
uv run demos/06-numpy/09_views_and_copies.py
```

Running through `uv run` guarantees the command uses this project's Python and
its packages.

The demos in `demos/04-web-scraping/` read a saved copy of a web page from
`data/`, so they work without a network connection and do not depend on a site
still being there. The three that can also fetch the live page take an explicit
`--live` flag :

```bash
uv run demos/04-web-scraping/01_fetching_pages.py --live
```

The demos in `demos/08-gui/` open a window and block until it is closed. Run
those from a desktop session rather than over a plain SSH connection. Each one
says so in a comment at the top of the file.

## The exercises

Each module except the interactive GUI module has an exercise in the exercises
PDF, starting files under `exercises/starters/`, and a solution under
`solutions/`. Copy the starter into a folder of your own, for example
`work/01-inheritance/`, so your code stays separate from the material. Run it
from `libraries/` so the supplied `data/` paths resolve.

The solutions are complete programs rather than fragments, so they can be run
and read alongside the exercise text.

## Where to go next

Modules 01 and 05 are previews of the Advanced Python course (PRG404), which
covers multiple inheritance and the method resolution order, protocols and
structural typing, dataclasses, decorators, generators, context managers,
logging and concurrency.

Worth reading before then :

- **`logging`** : the standard library's answer to structured application logs,
  with levels, handlers and rotation. It is a module of the Advanced course.
- **SQLAlchemy**, further than module 05 goes : eager loading with
  `selectinload`, and Alembic for schema migrations.
- **pandas** : the official *10 minutes to pandas* guide, then the *Essential
  basic functionality* page of the user guide.
- **`typer`**, once the `argparse` patterns in module 02 are familiar.

`reference/` carries background reading and the GUI examples the course does not
cover : the same inventory table written with PySide6 and with Streamlit, each
with notes on what it does differently from the tkinter version.
