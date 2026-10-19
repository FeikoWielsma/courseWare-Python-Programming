> Historical record (2026-08-15). Current commands and defaults: MAINTAINING.md; index: ../README.md.

# PRG400 conversion plan

Where the Presentation-as-Code conversion of *Python Programming* (PRG400) stands,
and what is left. Companion checklist : `build/tasks.md`. Conventions : `AGENTS.md`.

Written 2026-08-15.

---

## Where it stands

The conversion from `PRG400-Python-Programming_og.pdf` (197 pages) is complete in
text terms and sound in structure :

- Every original slide title is present, in the original order, across 11 module files.
- All 12 exercises are converted from `PRG400-Python-Programming-Exercises_og.pdf`.
- All 118 demo pills resolve to real files under `demos/`.
- `bun run --cwd build lint` reports no overflow.
- Per-slide character volume against the original shows one slide meaningfully
  shortened (`File Open Modes`, an acceptable table trim). Nothing else lost text.

What is missing is everything the original expressed as a picture, the tooling and
repository furniture the sibling courses carry, and two chapters of new material.

## Audience note

The next delivery is to a student with a Perl and Linux systems administration
background. **The material itself stays background-agnostic.** Commit `ed5b907`
added Perl-comparison speaker notes to modules 01, 02, 05 and 06; these come out.
Cross-language framing belongs in the room, not in the deck. Neither
Advanced-Python nor TNO-Python carries speaker notes outside the preamble.

---

## Phase 1 : Content repairs

These are defects, not improvements. Do them first.

### 1.1 Two gutted slides

Both were image-only in the original and the conversion dropped the image without
leaving anything behind.

| Slide | Original | Current state |
|---|---|---|
| `02 · Format Method` (og p35) | Annotated diagram of `"Art: {0:5d}, Price per Unit: {1:8.2f}".format(453, 59.058)` with arrows from each field into the rendered result string, then the same for named fields | Title plus a demo pill. No body at all. |
| `09 · Result of Calling open` (og p149) | Interactive transcript showing `TextIOWrapper` / `BufferedReader` / `FileIO` for three modes, then a stacked box diagram of the wrapper chain | Three parent bullets ending in ` :` with nothing underneath |

Rebuild both as inline SVG in the house style : `viewBox`, `width="100%"`,
`fill="currentColor"`, `stroke="currentColor"`, no background fill, no hardcoded
colours. See `../Advanced-Python/src/slides/11-concurrency/11-concurrency.md:222`
for the reference pattern.

### 1.2 Three truncated opening bullets

Commit `ed5b907` replaced each module's first bullet with a Perl NOTES block and
left a fragment behind. Restore the original wording :

| File | Now | Restore to |
|---|---|---|
| `02-variables-and-data-types.md:13` | `- Variables are` | `- Variables represent memory locations to store values :` |
| `05-functions.md:13` | `- A function` | `- Blocks of reusable code performing some action :` |
| `06-modules.md:13` | `- A module` | `- Used to organize number of Python definitions in single file :` |

That is the complete extent of the bullet loss from that commit; the rest of its
diff is the deliberate pip-to-uv rewrite, which stays.

### 1.3 Perl notes out

Remove the four `<!-- NOTES: Perl comparison … -->` blocks in modules 01, 02, 05
and 06. Leave the incidental in-content mentions that the original deck itself
carries (`Processed at runtime by the interpreter like Perl and PHP code`,
`Like associative arrays in Perl and PHP`, `Influenced by ODBC, JDBC and Perl's DBI`) —
those are the original author's words and are not audience-specific framing.

### 1.4 Four dropped screenshots

Originals that became nothing. None of these needs to be a screenshot; a fenced
transcript or a small HTML block carries the same information and stays legible
in both light and dark.

| Slide | Original | Replacement |
|---|---|---|
| `01 · Python in Interactive Mode` (og p10) | Windows command prompt screenshot | ```` ```text ```` transcript |
| `06 · Virtual Environments` (og p110) | Explorer window showing `Include/ Lib/ Scripts/ pyvenv.cfg` | small HTML directory tree, retargeted at what `uv init` produces |
| `10 · Retrieving Data` (og p170) | `fetchall()` result set beside the code | ```` ```text ```` output fence |
| `10 · Metadata` (og p174) | `PRAGMA table_info(Cars)` output | ```` ```text ```` output fence |

### 1.5 Missing exercise pills

Modules 01, 02, 05 and 06 have no `> \`exerciseNN · Name\`` line on their summary
slide; modules 03, 04, 07 to 11 do. Add pills for 02, 05 and 06. Exercise 1
(Environment Configuration) moves to the new module 00a instead, and module 01
ends without an exercise, matching the original course flow where the first
coding exercise follows Variables and Data Types.

---

## Phase 2 : Fence hygiene

Roughly 37 fences are tagged ```` ```python ```` but hold console output,
tracebacks, or pseudo-syntax. Examples : the `try: / Do you operations here /
except:` skeletons throughout module 08, `lambda [arg1 [,arg2,.....argn]]:expression`
in module 05, `raise [Exception [, args [, traceback]]]` in module 08, and every
program-output block in modules 01, 04, 05, 06 and 09.

- Output, transcripts and tracebacks take ```` ```text ````.
- Shell commands take ```` ```bash ```` (module 01 has three already).
- Grammar skeletons that are not valid Python take ```` ```text ````.

Then port `build/check-fences.py` from Advanced-Python. It extracts every
```` ```python ```` fence and `ast.parse`s it, which catches the classic
conversion defect of a PDF footer glued onto a line of code. This becomes a
gating CI step.

---

## Phase 3 : Diagrams

Target roughly 25 in total, mermaid where the shape is a graph and inline SVG
where it is a layout. The rule from `AGENTS.md` applies : a diagram that merely
restates a bullet list is not worth the space.

Read the mermaid constraints in `../Advanced-Python/AGENTS.md` before starting,
particularly the `trimSvgViewBox` cropping bug (keep the outer edges of a diagram
made of rectangles) and the ordering rule (run `build` first to populate
`build/.mermaid-cache/`, then run `lint` separately, because the lint pass inside
`build` measures a placeholder).

### Repairs, from Phase 1

1. `02 · Format Method` — SVG, format-field to output mapping
2. `09 · Result of Calling open` — SVG, `TextIOWrapper → BufferedReader → FileIO` stack
3. `01 · Python in Interactive Mode` — text fence
4. `06 · Virtual Environments` — HTML tree
5. `10 · Retrieving Data` — text fence
6. `10 · Metadata` — text fence

### New

| # | Module | Slide | Form | What it shows |
|---|---|---|---|---|
| 7 | 01 | Running Python | mermaid `graph LR` | source to bytecode to interpreter loop |
| 8 | 02 | Everything is an Object | SVG | two names bound to one object, `id()` identity |
| 9 | 02 | Strong Typing | mermaid | why `"1" + 1` raises where a weakly typed language coerces |
| 10 | 03 | Accessing Lists | SVG | positive and negative index rulers over one list |
| 11 | 03 | Accessing Lists | SVG | slice boundaries, why `a[1:3]` has two elements |
| 12 | 03 | Sets | SVG | union, intersection and difference as three small Venn pairs |
| 13 | 03 | Dictionaries | mermaid | key to hash to bucket to value |
| 14 | 04 | if Statement | mermaid `flowchart TD` | if / elif / else decision flow |
| 15 | 04 | while Loop | mermaid | condition, body, and the `else` branch on normal exit |
| 16 | 04 | for Loop | mermaid | iterable to iterator to item, and where `break` leaves |
| 17 | 05 | Pass by Value | SVG | mutating through a shared reference |
| 18 | 05 | Overwriting References | SVG | rebinding the parameter name, the original untouched |
| 19 | 05 | Scope of Variables | mermaid | LEGB lookup order |
| 20 | 06 | Locating Modules | mermaid `flowchart LR` | `sys.path` search order, first hit wins |
| 21 | 06 | Packages in Python | HTML tree | package directory with `__init__.py` |
| 22 | 07 | Syntax List Comprehensions | SVG | anatomy of `[expr for x in it if cond]` labelled against the equivalent loop |
| 23 | 07 | Zip Function | SVG | two sequences interleaving into pairs |
| 24 | 08 | Exception Handling | mermaid `flowchart TD` | try / except / else / finally, including the raise path |
| 25 | 08 | Python Standard Exceptions | mermaid `graph LR` | `BaseException` to `Exception` to the common concrete classes |
| 26 | 09 | File Positions | SVG | `tell()` and `seek()` against a byte ruler |
| 27 | 10 | DB API Concepts | mermaid `sequenceDiagram` | connect, cursor, execute, fetch, commit, close |
| 28 | 11 | Accessing Attributes | mermaid | instance dict, then class dict, then base classes |
| 29 | 11 | Override Base Methods | mermaid `classDiagram` | base and derived with the overridden method |

`11 · Example Class and Objects` already renders the original table, but flattened :
the original spans the three instance methods across all object columns. Rebuild
as an HTML table with `rowspan` and `colspan` so it reads as it did.

---

## Phase 4 : New module 00a, Modern Python

A single chapter covering the toolchain and a type-hinting primer, placed between
the preamble and Python Intro. Directory `src/slides/00a-modern-python/`, which
sorts after `00-preamble` and before `01-python-intro` under the build's
`readdirSync().sort()`, so **nothing existing renumbers** : no demo folders move,
no exercise files rename, no pills change. The schedule slide lists modules by
footer name with no numbers, so it picks the new module up automatically.

Footer : `Modern Python`.

Slides, roughly 15 :

**Toolchain**

1. `Modern Python Tooling` — what uv and ruff replace and why
2. `Installing uv` — the one thing installed by hand; `uv python install`
3. `Projects with uv` — `uv init`, `uv add`, `uv run`, `pyproject.toml`, `uv.lock`
4. `Virtual Environments` — what `.venv` is, why `uv run` means never activating
5. `Linting with ruff` — `ruff check`, `ruff format`, `ruff.toml`
6. `Editor Setup` — VS Code with the Python and Ruff extensions

**Type hinting primer, 6 to 8 slides as agreed**

7. `Why Type Hints` — documentation that cannot drift, tooling that reads it
8. `Basic Type Syntax` — `age: int = 25`, `def f(a: float) -> float`
9. `Typing Collections` — `list[int]`, `dict[str, int]`, `tuple[int, ...]`
10. `Optional Values` — `str | None`, why a default of `None` needs it
11. `Hints Are Not Enforced` — the interpreter ignores them at runtime
12. `Checking with mypy` — one run, one error, one fix
13. `Summary : Modern Python`

Deliberately out of scope, because PRG404 module 01 owns them : `Protocol`,
`TypeVar`, generics, `Callable`, overloads, `dataclass` interaction.

Then weave hints through the existing deck, lightly :

- `05-functions` — annotate the signatures in the syntax and default-argument slides
- `11-python-classes` — annotate attributes in the `__init__` examples
- Leave modules 01 to 04 unannotated, so the basics stay uncluttered

New demo folder `demos/00a-modern-python/`, numbered pills from `demo01`.

**Exercise 1** (`src/exercises/01-environment-configuration.md`) is rewritten as
the setup exercise for this module, modelled on
`../Advanced-Python/src/exercises/00-setup.md` : install uv, install Python, install
VS Code plus the Python and Ruff extensions, create a check project, run a first
annotated function through mypy. The current text (PyCharm, Spyder, Eclipse,
`C:\Python310`, manual PATH editing) is replaced. It keeps the number 1 and
becomes the summary pill of module 00a.

---

## Phase 5 : Appendix module, Python Libraries

The original deck stops at module 11, but `demos/12-*` holds runnable material for
nine libraries with no slides at all, and `src/exercises/12-python-libraries.md` is
a three-line pointer.

Add `src/slides/12-appendix-libraries/` with `appendix: true` in the frontmatter,
which puts it under its own Appendix divider on the schedule slide. Footer :
`Python Libraries` with no prefix.

Roughly 18 slides across the four libraries the demos best support :

- `Standard Library Overview` — batteries included, how to find things
- `datetime` — `date`, `datetime`, `timedelta`, formatting, parsing (3 slides)
- `json` — `dumps`, `loads`, `dump`, `load`, custom encoding (3 slides)
- `Regular Expressions with re` — `match`, `search`, `findall`, `sub`, groups (4 slides)
- `unittest` — `TestCase`, assertions, fixtures, running (3 slides)
- `Summary : Python Libraries`

Skipped, because they are other courses' material or too large for an appendix :
numpy (Python-Numpy), selenium, tkinter and Qt (the GUI decks), xml and threads
(PRG404 appendices 17 to 19).

`src/exercises/12-python-libraries.md` gets `<!-- appendix -->` as its first line
and real content drawn from the existing `exercises/*.doc` files.

The reused demos stay where they are; the slide pills point at the existing
`demos/12-pythonlibraries-*` folders. Note that this breaks the
one-demo-folder-per-module rule from `AGENTS.md`; record the exception there.

---

## Phase 6 : Repository furniture

PRG400 has none of the tooling files its siblings carry.

| File | Source | Notes |
|---|---|---|
| `pyproject.toml` | adapt from Advanced-Python | project metadata only; PRG400 needs no third-party runtime dependencies beyond the odd demo |
| `ruff.toml` | copy from Advanced-Python | separate file, not in `pyproject.toml`, so the student bundle can ship it without shipping a `pyproject.toml` |
| `.python-version` | new | `3.14`, matching the siblings |
| `.gitattributes` | copy from Advanced-Python | `eol=lf` normalisation, binary markers |
| `build/check-fences.py` | copy from Advanced-Python | retarget at PRG400's slide paths |
| `README.md` | adapt from Advanced-Python | student-facing; ships in the bundle |
| `MAINTAINING.md` | adapt from Advanced-Python | maintainer-facing; deliberately **not** in the bundle |

`ruff.toml` excludes the vendored and other-course directories :
`demos/Qt-Python-Binding-Examples-master`, `demos/extrademos`, `demos/feiko`,
`demos/casestudy`, `pandas`, `vb`, `gui`, `tkinter`, `jupyter`, `software`.

Inside that scope ruff currently reports about 700 findings in `demos/01-*` to
`demos/11-*` and 116 in `solutions/`. **As agreed, these are not fixed in this
round.** Ruff runs in CI as an informational step; `check-fences.py` is the gating
one. Clearing the 800 and promoting ruff to gating is tracked as follow-up work in
`build/tasks.md`.

Also expand `AGENTS.md` from its current 59 lines toward the Advanced-Python
version : the diagram conventions and mermaid pitfalls, the fence-language rule,
the slide-title register, the demo and exercise pill rules, and the appendix
mechanism.

---

## Phase 7 : CI and the student repository

Model : `../Advanced-Python/.forgejo/workflows/release.yml`.

### 7.1 The student repository

`SpiralTrain/Python-Programming-Student` does not exist. Create it, then wire a
dedicated write key so no existing key material is copied around :

1. `fj repo create` under the `SpiralTrain` org, private.
2. Generate a fresh `ed25519` keypair locally.
3. Register the public half as a **write** deploy key on the student repo through
   the Forgejo API, using the application token `fj` already holds.
4. Store the private half as the `STUDENT_REPO_SSH_KEY` secret on
   `SpiralTrain/Python-Programming`, via `fj actions secrets create`.
5. Delete the local copy of the private key.

If the token turns out to lack the scope for deploy keys, fall back to asking for
the key to be added through the web UI; the workflow itself is unaffected.

### 7.2 The workflow

`.forgejo/workflows/release.yml`, on push to `master` and `workflow_dispatch`:

```
env:
  SLIDES_PDF:      PRG400-Python-Programming.pdf
  SLIDES_HTML:     PRG400-Python-Programming.html
  EXERCISES_PDF:   PRG400-Python-Programming-Exercises.pdf
  EXERCISES_HTML:  PRG400-Python-Programming-Exercises.html
```

Steps, following the sibling exactly except where noted :

1. Checkout.
2. Install `uv`.
3. Check the Python : `uv sync --frozen`, `uv run python build/check-fences.py`
   (gating), `uv run ruff check .` with `continue-on-error: true` (informational
   for now), `compileall` over `demos/01-*` to `demos/12-*` and `solutions`.
4. Clone `SpiralTrain/Presentation-Template`, `bun install --frozen-lockfile`.
5. Build slides and exercises with `--force`, Chrome flags as in the sibling.
6. Name the slides HTML.
7. Assemble the student bundle.
8. Package `Python-Programming-student.zip`.
9. Publish the `latest` release with the four documents plus the zip.
10. Push to the student repository, with the same "skip if the secret is absent"
    guard, the same clear-then-copy so removals propagate, and the same generated
    student `.gitignore`.

### 7.3 Bundle contents

**Allowlist, not copy-then-prune.** The repository is roughly 800 MB and most of
it belongs to other courses (`pandas/` alone is 397 MB), so a list of what goes in
is safer than a list of what comes out : a stray folder added later cannot leak
into a student's clone.

Included :

```
PRG400-Python-Programming.pdf / .html
PRG400-Python-Programming-Exercises.pdf / .html
demos/00a-modern-python/
demos/01-pythonintro/ … demos/11-python-classes/
demos/12-pythonlibraries-datetime/  -json/  -regexp/  -unittesting/
solutions/
appendices/
cheatsheets/
README.md
ruff.toml
```

Excluded by omission, and worth naming so the reasoning survives : `pandas/`
(Python-Data-Analysis material, 397 MB), `demos/extrademos` (46 MB),
`demos/12-pythonlibraries-xml` (32 MB), `demos/casestudy` (13 MB),
`demos/Qt-Python-Binding-Examples-master`, `demos/feiko`, `software/`
(includes `python-2.7.1.msi`), `vb/`, `gui/`, `tkinter/`, `jupyter/`,
`documentation/` (62 MB), `books/`, `articles/`, `extra/`, and the loose
`*.doc` and `*.pdf` files at the repository root.

Target zip : well under 100 MB, against the roughly 800 MB the repository holds.

The same `find`-based sweep as the sibling strips `__pycache__`, `.venv`,
`.idea`, `*.pyc` and the Windows droppings from whatever is copied.

---

## Order of work

Phase 1 and 2 first : they are defects, and Phase 3 builds on the same slides.
Phase 6 and 7 can proceed in parallel with Phase 3 since they touch different
files. Phase 4 and 5 are new content and come last, so the deck is correct before
it grows.

After every slide edit : `bun run --cwd build build` to populate the mermaid
cache, then `bun run --cwd build lint` separately for a true height measurement.
