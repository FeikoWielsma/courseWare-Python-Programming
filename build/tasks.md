# PRG400 tasks

Checklist for the work described in `build/plan.md`. Tick as you go.

---

## Phase 1 : Content repairs

- [x] `02 · Format Method` : rebuild the format-field diagram as inline SVG
- [x] `09 · Result of Calling open` : restore the transcript and the wrapper-stack SVG
- [x] `02-variables-and-data-types.md` : restore `- Variables represent memory locations to store values :`
- [x] `05-functions.md` : restore `- Blocks of reusable code performing some action :`
- [x] `06-modules.md` : restore `- Used to organize number of Python definitions in single file :`
- [x] Remove the four Perl-comparison NOTES blocks (modules 01, 02, 05, 06)
- [x] `01 · Python in Interactive Mode` : add the transcript as a text fence
- [x] `06 · Virtual Environments` : add the `.venv` directory tree (text fence, not
      HTML : a fence carries the same information and stays theme-safe)
- [x] `10 · Retrieving Data` : add the result set as a text fence
- [x] `10 · Metadata` : add the `PRAGMA table_info` output as a text fence
- [x] Exercise pills on every module summary

Found while doing the above, not in the original inventory :

- [x] Seven exercise pills sat **mid-list** on the summary slides of modules 03, 04,
      07, 08, 09, 10 and 11, orphaning the trailing bullets. Moved to the end.
- [x] Three summary slides had the exercise cloud text glued onto a bullet :
      `...converted valueExercise 2`, `- Global variables :Exercise 5`,
      `...its own Python binaryExercise 6`, plus `...string literals :Exercise 1`
- [x] 19 code fences were a single block split in two by the conversion, separated
      by four blank lines. Merged.
- [x] 31 stray blank lines inside bullet lists, which broke one list into several
- [x] `04 · else Statement` and `10 · Committing Data` : the merge exposed bodies
      that had lost their indentation, so the code did not parse
- [x] `04 · Loop with else Combination` : `print("..." % (n)))`, unbalanced parenthesis
- [x] `05 · Variable Length Arguments` : `testArgLists(44)08_variable_argumentlist`,
      a demo filename glued onto the call
- [x] `03 · Lists` : a `th` from `4th` stranded on its own line inside a fence
- [x] `03`, `06` : smart quotes and an ellipsis inside code
- [x] `03 · Delete Tuple Elements` : Python 2 `print tup;` in the traceback
- [x] `08 · Exception Handling` : a stray leading space made the second `try` invalid
- [x] `09 · Writing Text Files` : the Polish sample was double-encoded mojibake, on
      the slide and in `demos/09-python-io/textfilepolish.txt`
- [x] `class X(object)` dropped in module 11 slides, exercise and demos, and in
      `solutions/` (Python 2 residue on the slides that teach how to write a class)

## Phase 2 : Fence hygiene

- [x] Retag output, transcript and traceback fences as ```` ```text ````
- [x] Retag grammar skeletons as ```` ```text ```` (module 08 try/except forms,
      module 05 lambda form, module 06 import forms, the `=>` pseudo-notation)
- [x] Retag shell fences as ```` ```bash ````, and lift the prose that had been
      glued inside them (`export PATH=... and press Enter`)
- [x] 47 fences retagged in total
- [x] Port `build/check-fences.py` from Advanced-Python
      - it now reconfigures stdout to UTF-8, because the findings quote characters
        a Windows console cannot encode and the script died on the first one.
        Worth pushing back to Advanced-Python, which has the same latent bug.
- [x] `uv run python build/check-fences.py` passes clean
- [x] Wire it into CI as a gating step

## Phase 3 : Diagrams

Repairs are tracked in Phase 1. New diagrams :

- [x] 01 `What is Python?` : source to bytecode to virtual machine.
      Moved here from `Running Python`, which is about launch modes, not
      about what interpretation means.
- [x] 02 `Everything is an Object` : two names, one object, `id()`
- [x] 02 `Strong Typing` : a three-line comparison fence rather than a diagram.
      `1 + 1`, `"1" + "1"`, `"1" + 1`. A diagram here would have been decoration.
- [x] 03 `Accessing Lists` : one ruler carrying positive indexes, negative
      indexes and the extent of `li[1:3]`
- [x] 04 `if Statement` : if / else flow
- [x] 04 `while Loop` : condition, body, exit
- [x] 04 `for Loop` : items left, assign, body, exit
- [x] 05 `Mutating Versus Rebinding` : **a new slide.** `Pass by Value` and
      `Overwriting References` are both three fences deep with no room, and the
      contrast between them is the point, so it earns a slide of its own.
- [x] 05 `Scope of Variables` : LEGB lookup order
- [x] 06 `Locating Modules` : search order, first hit wins
- [x] 06 `Packages in Python` : package tree with `__init__.py`
- [x] 07 `Syntax List Comprehensions` : anatomy of the three parts
- [x] 08 `Unexpected Errors` : exception hierarchy. Placed on the module opener
      rather than beside the standard-exceptions tables, which are already tall.
- [x] 08 `try-finally Clause` : try / except / else / finally flow
- [x] 09 `File Positions` : `tell()` and `seek()` on a byte ruler
- [x] 10 `DB API Concepts` : connect, cursor, execute, fetch, commit, close
- [x] 11 `Example Class and Objects` : rebuilt with `rowspan` and `colspan`, so
      the instance methods span the object columns as they do in the original
- [x] **11 `Encapsulation` : the deck's one pre-existing diagram was broken.**
      Its `D((internal data))` circle was cropped away by `trimSvgViewBox`,
      leaving four `method` boxes with arrows pointing at nothing. Rebuilt with
      rectangles as a client / accessors / hidden attribute chain.
- [x] `ls build/.mermaid-cache/ | grep placeholder` returns nothing
- [x] No diagram is cropped; every viewBox starts at `3 3`

Considered and deliberately not done :

- 03 `Sets` : a Venn of union, intersection and difference. The slide already
  carries three fences whose output shows exactly that, so it would not fit and
  would not add.
- 03 `Dictionaries` : key to hash to bucket. Implementation detail beyond what a
  fundamentals course needs.
- 07 `Zip Function` : the fence already prints the pairs.
- 11 `Accessing Attributes` and `Override Base Methods` : both slides are wall to
  wall code fences with no room, and neither concept was struggling.

## Phase 4 : Module 00a, Python Tooling, and module 12, Type Hinting

- [x] Create `src/slides/00a-modern-python/00a-modern-python.md`, footer `Modern Python`,
      13 slides
- [x] Toolchain slides : tooling overview, installing uv, creating a project, adding
      dependencies, ruff, editor setup
- [x] Type hinting slides : why, basic syntax, collections, optional, not enforced,
      mypy, summary
- [x] Create `demos/00a-modern-python/`, seven demos numbered `01_` to `07_`
      - every demo was run, and the output on the slides is the output it actually gives
      - `02_ruff_findings.py` is written badly on purpose and is excluded in `ruff.toml`
      - `07_mypy_error.py` really does fail `mypy`, with the message the slide quotes
- [x] Rewrite `src/exercises/01-environment-configuration.md` for uv, ruff and VS Code
- [x] Move `exercise01` from the module 01 summary to the module 00a summary
- [x] Annotate the signatures in `05-functions`, and the matching demo files
      - the slides said `showmessage` and `printinfo` where the demos said
        `show_message` and `print_info`; aligned on the demo names
      - the `Calling Functions` traceback quoted the Python 2 wording
        `takes exactly 1 argument (0 given)`; now the 3.x wording
- [x] Annotate `__init__` in `11-python-classes` and in `03_classwithinit.py`
- [x] Confirm the schedule slide lists Modern Python first, with no renumbering
- [x] Add the new demo folder to the CI compileall gate and the bundle allowlist
- [x] Record the `00a-` naming rationale and the diagram rules in `AGENTS.md`

**Resolved : the type hinting half was moved to the end.** The chapter 0 module is
now `00a-python-tooling` (uv, ruff, editor, 7 slides) and type hinting is
`12-type-hinting` (7 slides), after Python Classes. Consequences, all done :

- [x] `demos/00a-modern-python/` split into `demos/00a-python-tooling/` (2 demos) and
      `demos/12-type-hinting/` (5 demos, renumbered from `01_`)
- [x] The annotations added to the Functions and Classes slides were **reverted**.
      Modules 01 to 11 now carry no annotations at all, so nothing in the deck uses
      a notation the course has not taught yet. The naming fixes made in the same
      pass were kept (`show_message`, `print_info`, the modern traceback wording).
- [x] Exercise 1 is `Exercise 1 : Python Tooling` and its type checker step moved to
      the new `src/exercises/12-type-hinting.md`
- [x] `ruff.toml`, the CI compileall list and the bundle allowlist repointed

## Phase 5 : Appendix, Python Libraries

- [x] Create `src/slides/13-appendix-libraries/` with `appendix: true`, footer
      `Python Libraries`, 16 slides. Numbered 13, not 12, because type hinting took 12.
- [x] Slides : overview, datetime (3), json (3), re (4), unittest (3), summary
- [x] **Own demo folder rather than the planned exception.** The plan was to point the
      pills at the existing `demos/12-pythonlibraries-*` folders and record a
      naming exception in `AGENTS.md`. Those folders turned out to be a mix of
      `demo01_*.py`, bare names and scratch subfolders, so instead
      `demos/13-appendix-libraries/` holds ten fresh numbered demos that the slides
      reference. The one-demo-folder-per-module rule is intact and no exception was
      needed. The old folders stay in the repository as extra material and are no
      longer in the student bundle.
- [x] Every demo was run; the output quoted on the slides is what it prints
- [x] `src/exercises/12-python-libraries.md` renamed to `13-python-libraries.md`,
      given `<!-- appendix -->` as its first line and real content
- [x] Confirmed the appendix divider appears on the schedule slide, and that the
      exercise is separated under its own APPENDIX heading in the exercises TOC

## Phase 6 : Repository furniture

- [x] `ruff.toml` with the vendored and other-course exclusions
- [x] `README.md`, student-facing
- [x] `pyproject.toml` — no runtime dependencies, because every bundled demo imports
      only the standard library. `mypy` and `ruff` are dev dependencies.
- [x] `.python-version` : `3.14`
- [x] `MAINTAINING.md`, maintainer-facing, excluded from the bundle
- [x] Expand `AGENTS.md` : the `00a-` prefix rationale, why type hinting is last,
      the appendix mechanism, fence-language rules, the mermaid cropping trap, the
      inline-SVG whitespace trap, and the two workflow edits a new module needs
- [x] `uv lock` produces `uv.lock`; CI now runs `uv lock --check` then
      `uv sync --frozen`, and every check runs through `uv run`
- [x] Removed a stale `.venv` that pointed at a Python removed in the Windows
      reinstall, which made `uv lock` fail outright
- [ ] `.gitattributes` — **still deferred deliberately.** `* text=auto eol=lf` would
      renormalise line endings across 5000+ tracked files in one commit. Do it on
      its own, not mixed into content work.

## Phase 7 : CI and student repository

- [x] Create `SpiralTrain/Python-Programming-Student` — public, default branch
      `main`, matching `Advanced-Python-Student`
- [x] Generate a fresh ed25519 keypair
- [x] Register the public key as a **write** deploy key on the student repo
      (`prg400-ci-push`, key id 3)
- [x] Store the private half as `STUDENT_REPO_SSH_KEY` on `SpiralTrain/Python-Programming`
- [x] Delete the local private key copy
- [x] Write `.forgejo/workflows/release.yml`
- [x] Bundle step uses an allowlist, not copy-then-prune
- [x] Untrack the built PDFs and ignore the built HTML, matching Advanced-Python
- [x] Push to `master` and confirm the release assets appear
- [x] Confirm the student repository receives the bundle on `main`
- [x] Check the zip size : 9.5 MB, anonymous clone is 22 MB

## Follow-up, not this round

- [ ] Clear the ~944 ruff findings inside the `ruff.toml` scope
- [ ] Promote `ruff check .` from informational to gating in CI
- [ ] Modernise percent formatting to f-strings in modules 04, 10 and 11 and in
      `src/exercises/02`, together with their demo files. `UP031` is ignored in
      `build/check-fences.py` for now because the string-formatting slide in
      module 02 teaches percent formatting on purpose; once the incidental uses
      are gone that ignore can be narrowed.
- [ ] Triage `demos/*/extra/` : 16 files are Python 2 and do not compile, so the
      whole `extra/` tree is excluded from the student bundle and from the
      `compileall` gate. Port them or delete them, then drop the exclusion.
- [ ] `demos/09-python-io/createexecutable/build` is 12 MB of committed
      PyInstaller output. Excluded from the bundle; delete it from the repository.
- [ ] Consider deleting `pandas/`, `software/`, `vb/` and `demos/extrademos` from the
      repository, since they belong to other courses
