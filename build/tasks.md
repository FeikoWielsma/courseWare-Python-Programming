# PRG400 tasks

Checklist for the work described in `build/plan.md`. Tick as you go.

---

## Phase 1 : Content repairs

- [ ] `02 · Format Method` : rebuild the format-field diagram as inline SVG
- [ ] `09 · Result of Calling open` : restore the transcript and the wrapper-stack SVG
- [ ] `02-variables-and-data-types.md:13` : restore `- Variables represent memory locations to store values :`
- [ ] `05-functions.md:13` : restore `- Blocks of reusable code performing some action :`
- [ ] `06-modules.md:13` : restore `- Used to organize number of Python definitions in single file :`
- [ ] Remove the four Perl-comparison NOTES blocks (modules 01, 02, 05, 06)
- [ ] `01 · Python in Interactive Mode` : add the transcript as a text fence
- [ ] `06 · Virtual Environments` : add the `.venv` directory tree as HTML
- [ ] `10 · Retrieving Data` : add the result set as a text fence
- [ ] `10 · Metadata` : add the `PRAGMA table_info` output as a text fence
- [ ] Add `> \`exercise02 · Variables and Data Types\`` to the module 02 summary
- [ ] Add `> \`exercise05 · Functions\`` to the module 05 summary
- [ ] Add `> \`exercise06 · Modules\`` to the module 06 summary

## Phase 2 : Fence hygiene

- [ ] Retag output and traceback fences as ```` ```text ```` (~30 sites, modules 01, 04, 05, 06, 09)
- [ ] Retag grammar skeletons as ```` ```text ```` (module 08 try/except forms, module 05 lambda form)
- [ ] Retag shell fences as ```` ```bash ```` where any remain tagged `python`
- [ ] Port `build/check-fences.py` from Advanced-Python and retarget its paths
- [ ] `uv run python build/check-fences.py` passes clean

## Phase 3 : Diagrams

Repairs are tracked in Phase 1. New diagrams :

- [ ] 01 `Running Python` : source to bytecode to interpreter loop
- [ ] 02 `Everything is an Object` : two names, one object, `id()`
- [ ] 02 `Strong Typing` : why `"1" + 1` raises
- [ ] 03 `Accessing Lists` : positive and negative index rulers
- [ ] 03 `Accessing Lists` : slice boundaries
- [ ] 03 `Sets` : union, intersection, difference
- [ ] 03 `Dictionaries` : key to hash to bucket to value
- [ ] 04 `if Statement` : if / elif / else flow
- [ ] 04 `while Loop` : condition, body, `else` on normal exit
- [ ] 04 `for Loop` : iterable, iterator, item, `break`
- [ ] 05 `Pass by Value` : mutating through a shared reference
- [ ] 05 `Overwriting References` : rebinding leaves the original untouched
- [ ] 05 `Scope of Variables` : LEGB lookup order
- [ ] 06 `Locating Modules` : `sys.path` search order
- [ ] 06 `Packages in Python` : package tree with `__init__.py`
- [ ] 07 `Syntax List Comprehensions` : anatomy against the equivalent loop
- [ ] 07 `Zip Function` : two sequences into pairs
- [ ] 08 `Exception Handling` : try / except / else / finally
- [ ] 08 `Python Standard Exceptions` : exception hierarchy
- [ ] 09 `File Positions` : `tell()` and `seek()` on a byte ruler
- [ ] 10 `DB API Concepts` : connect to cursor to execute to fetch to commit
- [ ] 11 `Accessing Attributes` : instance dict, class dict, bases
- [ ] 11 `Override Base Methods` : base and derived class diagram
- [ ] 11 `Example Class and Objects` : rebuild the table with `rowspan` / `colspan`
- [ ] `ls build/.mermaid-cache/ | grep placeholder` returns nothing
- [ ] `grep -o 'viewBox="[^"]*"' build/.mermaid-cache/*.svg` shows no cropped diagrams

## Phase 4 : Module 00a, Modern Python

- [ ] Create `src/slides/00a-modern-python/00a-modern-python.md`, footer `Modern Python`
- [ ] Toolchain slides : tooling overview, installing uv, projects with uv, virtual environments, ruff, editor setup
- [ ] Type hinting slides : why, basic syntax, collections, optional, not enforced, mypy, summary
- [ ] Create `demos/00a-modern-python/` with pills numbered from `demo01`
- [ ] Rewrite `src/exercises/01-environment-configuration.md` for uv, ruff and VS Code
- [ ] Add `> \`exercise01 · Modern Python\`` to the module 00a summary
- [ ] Annotate the signatures in `05-functions` syntax and default-argument slides
- [ ] Annotate the `__init__` attributes in `11-python-classes`
- [ ] Confirm the schedule slide picks the module up in the right position

## Phase 5 : Appendix, Python Libraries

- [ ] Create `src/slides/12-appendix-libraries/` with `appendix: true`, footer `Python Libraries`
- [ ] Slides : overview, datetime (3), json (3), re (4), unittest (3), summary
- [ ] Point the pills at the existing `demos/12-pythonlibraries-*` folders
- [ ] Give `src/exercises/12-python-libraries.md` an `<!-- appendix -->` first line and real content
- [ ] Record the demo-folder-naming exception in `AGENTS.md`
- [ ] Confirm the appendix divider appears on the schedule slide

## Phase 6 : Repository furniture

- [x] `ruff.toml` with the vendored and other-course exclusions
- [x] `README.md`, student-facing
- [ ] `pyproject.toml`
- [ ] `.python-version` : `3.14`
- [ ] `.gitattributes` — **deferred deliberately.** `* text=auto eol=lf` would
      renormalise line endings across 5000+ tracked files in one commit. Do it on
      its own, not mixed into content work.
- [ ] `MAINTAINING.md`, maintainer-facing, excluded from the bundle
- [ ] Expand `AGENTS.md` : diagram conventions, mermaid pitfalls, fence rules, title register, pill rules, appendix mechanism
- [ ] `uv sync` produces a `uv.lock` and CI can run `--frozen`

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

- [ ] Clear the ~950 ruff findings inside the `ruff.toml` scope
- [ ] Promote `ruff check .` from informational to gating in CI
- [ ] Triage `demos/*/extra/` : 16 files are Python 2 and do not compile, so the
      whole `extra/` tree is excluded from the student bundle and from the
      `compileall` gate. Port them or delete them, then drop the exclusion.
- [ ] `demos/09-python-io/createexecutable/build` is 12 MB of committed
      PyInstaller output. Excluded from the bundle; delete it from the repository.
- [ ] Consider deleting `pandas/`, `software/`, `vb/` and `demos/extrademos` from the
      repository, since they belong to other courses
