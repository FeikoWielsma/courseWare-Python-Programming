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
- [x] `.gitattributes` added in a commit of its own. The renormalisation itself
      touched almost nothing, because `core.autocrlf` had already been storing LF,
      but it surfaced four binaries under `demos/extrademos` that checkout had
      corrupted **in the working tree** by injecting CR bytes into pickles and a
      `.doc`. The stored copies were clean and were restored from `HEAD`; the
      binary markers stop it recurring. Two demo CSVs had doubled `^M^M` stored
      and are now plain LF.

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

- [x] Clear the ruff findings : `uv run ruff check .` is at zero
      - `demos/`, `appendices/`, `exercises/` and `src/` are genuinely clean
      - the non-bundled demo folders and the two orphan solution folders
        (`solutions/xextra`, `solutions/solutions-generators`, which solve
        exercises this course does not have) are excluded, not fixed
      - every remaining `per-file-ignores` entry names the lesson it protects
- [x] Modernise percent formatting to f-strings, in the demos, the solutions and
      the matching slide fences. Module 02's string-formatting slide and
      Exercise 2 keep `%` because they teach it explicitly.
- [ ] Promote `ruff check .` from informational to gating in CI
- [x] Triage `demos/*/extra/` : all 16 Python 2 files ported to Python 3 rather
      than deleted, and each one run to confirm it still does what it taught.
      `print x` to `print(x)`, `print x,` to `print(x, end=" ")`, `input()` wrapped
      in `int()` where it was compared with a number, `class X(object)` and
      `super(X, self)` modernised in the three MRO demos. The `-x extra` escape
      hatch is gone from the CI gate and the `extra/` prune is gone from the
      bundle, so those directories are now checked and shipped like the rest.
- [x] `demos/09-python-io/createexecutable/build` deleted, 12 MB of committed
      PyInstaller output. The source beside it stays but is still not course
      material, so the bundle continues to skip the folder.
- [ ] Consider deleting `pandas/`, `software/`, `vb/` and `demos/extrademos` from the
      repository, since they belong to other courses


---

## Round 2 : PEP 8 and type hints in context

Asked for after the first pass, and done.

- [x] PEP 8 naming everywhere. 23 identifiers renamed across the slides, demos,
      exercise text and solutions in one pass so they still agree with each other,
      `calcAction` alone appearing 244 times. `Canon.py` and friends became
      `canon.py`, `CanonInfo()` became `canon_info()`, `HelloPython.py` became
      `hello_python.py`.
- [x] Java-isms beyond naming : the trailing bare `return` at the end of a
      function that returns nothing, useless else-after-return, repeated equality
      chains that are really membership tests, `def f( x )` spacing.
- [x] The ruff ignores those names had needed are gone. N802, N803, N806, N815,
      N816 and N999 are enforced again and `ruff check .` is still at zero.
- [x] Type hints introduced as the course goes, so the demos read like real code :
      - module 02, a new `Annotating Variables` slide
      - module 03, a new `Annotating Collections` slide
      - module 05, a new `Annotating a Function` slide, and every signature on the
        slides and in the demos annotated
      - module 11, constructors and methods annotated on the slides and in the demos
- [x] `12-type-hinting` became `12-appendix-type-hinting`, an appendix recap that
      gathers what the course has shown and adds `| None` and `mypy`. Its exercise
      carries `<!-- appendix -->`.
- [x] `AGENTS.md`, `MAINTAINING.md` and `README.md` updated to match

Still open :

- [ ] Promote `ruff check .` from informational to gating in CI. It has been at
      zero across several commits now, so this is safe to do.
- [ ] Annotate the reference solutions. The demos and slides are annotated; the
      solutions under `solutions/` are not, and a student comparing their work
      against them will see the older style.
- [ ] Decide whether `solutions/xextra` and `solutions/solutions-generators`,
      which solve exercises this course does not have, should ship in the bundle.


---

## Round 3 : accuracy, the `with` gap, pathlib, annotated solutions

- [x] `ruff check .` promoted to a **gating** CI step
- [x] Factual errors inherited from the original deck :
      - Python described as GPL "like Perl"; it is the PSF License
      - "No support for `switch` or `case` statements"; Python 3.10 added `match`
      - `raw_input` presented as a current function in the module 09 summary
      - "Both Python 2 and Python 3 are available", years after Python 2 died
      - `set PYTHONPATH=c:\python37\lib`, and an `http://` python.org URL
- [x] Module 01 no longer contradicts the tooling module. It pointed students at
      Anaconda, IDLE and the Jupyter prompt while module 00a teaches uv and VS Code.
- [x] **`with` is taught.** The IO module had eighteen slides and never showed a
      context manager, and Exercise 9 had students call `fw.close()` by hand. There
      is now a `Using with` slide and demo, the exercise wraps its loop in `with`,
      and the reader iterates the file object instead of `readlines()`.
- [x] `match` statement slide and demo added to Control Flow
- [x] The IO module's directory slides rebuilt around `pathlib`, with a new
      `Paths with pathlib` slide; the three demos rewritten and each made
      re-runnable
- [x] The reference solutions are annotated, so a student comparing their work
      against them sees one style
- [x] A block of commented-out Java, a transcription of the Employee class from
      an earlier life of the material, removed from the classes solution

Still open :

- [ ] `solutions/xextra` and `solutions/solutions-generators` still ship in the
      bundle and solve exercises this course does not have. They also still hold
      camelCase names and a Java block, being outside the ruff scope.
- [ ] Git history is still 122 MB, because deleting a file does not shrink it.
      Only a history rewrite would, and that breaks every existing clone.

---

## Round 4 : the reference tree

The extras were kept, but curated. The rule applied throughout was that
everything shipped should be worth a student's time.

- [x] Deleted, 630 MB in total : `pandas/` 467 MB of Python-Data-Analysis
      material, `demos/extrademos` 71 MB of scratch, `documentation/` 62 MB of
      **Python 3.5** docs, `software/` with a Python 2.7 installer, `vb/` with
      Visual Basic and PyInstaller output, `books/diveintopython-5.4` written
      against Python 2.3, and the PyInstaller output under `demos/casestudy`.
- [x] `reference/python-docs/` holds the **Python 3.14** documentation instead:
      tutorial, library, reference, using, faq, whatsnew and ten howtos.
      The C API, extending and porting guides are left out.
- [x] Everything else consolidated under `reference/` : `articles`, `books`,
      `cheatsheets`, `gui` (tkinter, Qt, wxPython survey), `jupyter`,
      `packaging`, `perl-to-python`. `reference/README.md` says what is where.
- [x] Thirteen articles removed: ten Word files that had an identical PDF beside
      them, plus mod_python and the goto joke library.
- [x] `extra/` dissolved into `reference/`, its duplicates dropped
- [x] `conda-virtual-environment.txt` removed
- [x] Both dangling-colon bullets fixed
- [x] `reference/` now ships whole in the student bundle, which grows from
      8.9 MB to 53 MB of material the student can actually use

Found while doing it :

- [x] **`demos/*/extra/` had never been linted.** The bare `"extra"` entry in
      `ruff.toml` matched a directory of that name at any depth, so every
      `demos/NN-topic/extra/` was silently skipped. Removing it exposed 56
      findings, all now fixed: `super(X, self)`, `class X(object)`, percent
      formatting, a function named `filter`, another named `sum`, an exception
      class without an `Error` suffix, and a bare `print`.

Numbers : 5905 tracked files to 1158, 297 MB to 73 MB, 1.1 GB checkout to 492 MB.


---

## Round 5 : the toolchain folds into the introduction

`00a-python-tooling` is gone as a separate module. Installing Python and running
it is what an introduction is for, and having both meant module 01 and the
tooling module gave different answers on how to install Python.

- [x] The seven tooling slides merged into `01-python-intro`, which is now 21
      slides : what Python is, the toolchain, installing it, running it, and the
      syntax basics.
- [x] `Installing uv` absorbed into `Getting Started`, so there is one slide
      about getting an interpreter rather than two that disagreed.
- [x] `Setting up PATH` reframed as the manual-install route, since `uv` needs
      none of it.
- [x] The two summaries merged into one.
- [x] `demos/00a-python-tooling/` folded into `demos/01-pythonintro/` and the six
      demos renumbered so the pills stay in slide order.
- [x] Exercise 1 retitled `Python Intro`, matching the module name as every other
      exercise does.
- [x] `ruff.toml`, the workflow's two lists, `AGENTS.md`, `MAINTAINING.md` and
      `README.md` all follow.

Stale text found and fixed while doing it : `AGENTS.md` still said ruff was
informational with 944 findings, and still showed the `-x extra` flag that went
two rounds ago.


---

## Round 6 : Pythonic idioms, missing solutions, dead weight

- [x] **`enumerate` is taught.** `Iterating by Sequence Index` kept
      `for index in range(len(planets))` as the form to recognise, and now says
      plainly why Python avoids it. A new `Iterating with enumerate` slide follows,
      and the demo shows all three ways side by side.
- [x] `sorted(key=)`, `min`/`max(key=)`, `any` and `all` on a new
      `Built-ins that Take a Function` slide in the Comprehensions module, beside
      `map`, `filter` and `reduce` where they belong, rather than early in Control
      Flow where they would have been a distraction. Ten demos renumbered so the
      pills stay in slide order.
- [x] Solutions written for exercises 12 and 13, so all thirteen have one. The
      type hinting solution passes `mypy`; the libraries solution runs and its
      five unit tests pass.
- [x] Two demos that could not run are gone: `12_readsqlpanda.py` imported pandas,
      deleted from the repo last round, and `using-mysql.py` imported a MySQL
      connector that is not a dependency. Both shipped to students and failed.
- [x] `solutions/xextra` and `solutions/solutions-generators` deleted. They solved
      exercises this course does not have, and being outside the ruff scope they
      were the last place camelCase names and a commented-out Java block survived.
      Their ruff exclusions are gone with them.

Deliberately not done :

- Git history stays at 122 MB. Only a rewrite would shrink it, and that breaks
  every existing clone for a repository cloned a handful of times. The student
  repository is rebuilt from the bundle and is unaffected either way.
- `@dataclass` gets no mention. PRG404 owns it, and a fundamentals course that
  has just taught `__init__` by hand does not need the shortcut in the same hour.


---

## Round 7 : the slide code catches up with the demos

The PEP 8 pass of Round 2 reached the demos but not most slide fences, which
still carried `print (x)`, single quotes, five-space indents and unaligned
comments. Comparing every fence against its demo also turned up real errors.

- [x] Every parseable python fence on the slides and in the exercises run through
      `ruff format`, keeping each fence's own blank lines so no slide grew, and
      keeping column-aligned comments aligned. Left alone, because the layout is
      the lesson : the quotes slide, the line-continuation slide, and the
      single-statement-suite one-liners.
- [x] `print("Label: ", value)` printed a double space that no output fence
      showed. The trailing space is gone across slides, demos and solutions.
- [x] Code that did not run, or did something other than the slide said :
      - `10 · Fetching Rows` imported `sqlite3` and called `lite.connect`
      - `demo09 · bytesandbytesarrays` passed the builtin `str` to `bytearray`
      - two `09` fences had a literal line break inside `"...\n"`
      - `03` used the builtin `dict` where it meant `dict1`, and `tuple[2] = 1000`
        assigned into the builtin type
      - `06 · globals and locals` printed `locals()` outside the function
      - `11 · Example Data Hiding` never created `s`
      - `08 · Example User Defined Exceptions` set `self.args` to a string, so
        `e.args` was a tuple of characters. Now `NetworkError`, via `super().__init__`
      - `08 · except Clause Multiple Exceptions` kept the Python 2 trailing comma
        that once meant "no newline"; now `end=" "`
      - `demo08 · destructordemo` ended in `eval(input())`
      - `demo10 · testharness`'s companion `importtestharness.py` never imported
        anything. `testharnass` is spelled `testharness` throughout.
- [x] Python 2 claims removed from module 08 : the `raise [Exception [, args [,
      traceback]]]` grammar, string exceptions, and "`else` cannot be combined
      with `finally`" (the slide's own diagram combines them)
- [x] Output that Python no longer prints : dict and set orders in module 07,
      `dir(math)` in module 06, the unhashable-key message, slice results shown
      as lists for tuples, `reload` without `importlib`
- [x] Module 10 used `test.db`, `cars.db` and `Cars.db` for the same table. The
      last is a different file on Linux. All `cars.db` now.
- [x] `UP030` added to the fence checker's ignores, for the format-numbering slide

Still open :

- [ ] About 50 demo-backed slides still differ from their demo beyond being an
      excerpt. Most are deliberate : the slide shows an expression where the demo
      prints it, a grammar skeleton, or the error the demo comments out. A gating
      fence-to-demo check is not practical for that reason.


---

## Round 8 : towards the Wordle spine

The plan for this round onwards is `build/plan.md`.

- [x] Cheap coherency fixes on the slides : three cross-language comparisons
      removed, `Python Features` rewritten (COM, ActiveX, CORBA gone), the lambda
      slide's false claim about enclosing scopes, the raw-string example that
      demonstrated nothing, "32-bit code points", the dated f-string and
      `reduce` wording, "Toilettes"
- [x] Calculator exercises and solutions 2 to 11 archived in `archive/calculator/`,
      excluded from ruff and from the bundle
- [x] Prototype : Exercise 5 rewritten on the Wordle spine, with ★ tiers and
      reference-solution blocks; solutions for Exercises 4 and 5; the first
      handout (`test_wordle.py`, 9 tests); `build/make-starters.py` with a
      `--check` mode for CI
- [ ] Everything else : see `build/plan.md` section 9


---

## Round 9 : the Wordle spine, built by agents (2026-10-14 to 2026-10-18)

The plan was `build/plan.md`; the run is logged in `build/orchestration.md`, the
agents' own notes in `build/notes/`.

- [x] The shared exercise site, ported from PySpark into Presentation-Template, with
      `:::` markup, ★ tiers, a quiz engine and plug-ins; PRG400 wired to it
- [x] Wordle solutions for all 13 exercises, starters generated from them,
      `build/check-solutions.py` (tests, mypy, scripted games) in CI
- [x] All 13 exercise texts rewritten for the spine, every output produced by running
- [x] Slides 01 to 13 reworked (plan section 5), properties re-taught (section 6)
- [x] A 39-question quiz checked by `build/site/check-quiz.py`, and a hidden Wordle
- [x] A student review (no blockers, 26 findings), and a fix round for all of them
      except F13's last continuation paragraph and the timing decision below
- [x] Template fixes : Chrome EBUSY, PDF pagination

Still open, for the trainer :

- [ ] **Day 4 timing.** After the fixes the reviewer and the fixer estimate Exercise 9
      at about 65 minutes (45 stated), 10 at about 80 (60), 11 at about 110 (90).
      None of their steps can become optional without breaking the solution chain.
      Options : give Exercises 9 and 10 more time and treat 12 and 13 as take-home,
      or start module 09 on day 3.
- [ ] Push Presentation-Template `main` (CI clones it), review PySpark's
      `shared-exercise-site` branch, merge `prg400-wordle` into `master`.


## Trainer feedback : diagrams, examples and optional topics (2026-10-17)

- [x] Give the `if` diagram room and separate the `for` diagram from its example.
- [x] Teach `match` with string literals and a final wildcard; remove sequence
      patterns, captures, guards and shape matching from the beginner demo.
- [x] Rework Modules around one delivery-cost function, then reuse it from a
      report, a package and its entry point. Keep every slide fence in its demo.
- [x] Replace abstract comprehension examples with filenames, order totals,
      stock and readings. Separate nested rows from flattening and show the
      equivalent loops for flattening.
- [x] Import Python-Day4-Tour teaching material into `libraries/`, with separate
      slides and exercises PDFs and a separate uv project. Preserve its runnable
      paths; omit books, generated databases and old build tooling.
- [x] Add a local build wrapper, CI builds, release assets and bundle inclusion.
      Shared Presentation-Template sources and the original tour repo are unchanged.
- [x] Keep the fundamentals schedule, Wordle chain and exercise site separate.
- [x] Verify fences, slide references, Ruff, starters, all 13 solution stages,
      quiz, both slide decks, both exercises PDFs and the offline site.

Verification details : 25 fundamentals demos ran; 113 non-GUI optional demo smoke
checks passed, with command-line entry points checked via `--help`. Six tkinter
window demos were compiled but not launched. Import fixes include an offline HTTP
client, an offline robots.txt parser in place of an unrelated live API call, and
a CSV reader that no longer skips its header. Rendered PDF pages were inspected.

## Parallel Slidev foundation (2026-10-18)

- [x] Add an isolated shared Slidev toolchain, theme, converter and export path in
      a Presentation-Template worktree; keep Marp as the default build.
- [x] Convert all 13 fundamentals modules alongside Marp from the same source.
- [x] Preserve the original 239 page boundaries, with two additional Magic Move
      examples; retain the 299 original code/output fences.
- [x] Match the requested header/footer positions and linked module overviews.
- [x] Check all 241 browser frames, progressive reveals, diagrams and local assets.
- [x] Export and render-review both course PDFs; verify all five code click states.
- [x] Verify the included Python launcher and document commands and limitations.

Details and executed evidence: `build/notes/slidev-foundation.md`. This opt-in
comparison does not change the existing exercise site or release allowlists.
