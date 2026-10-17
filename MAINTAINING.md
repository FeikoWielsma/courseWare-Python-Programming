# Maintaining this course

Build and authoring notes for whoever, human or agent, works on this courseware.
This file is deliberately kept out of the student bundle. Student-facing
documentation goes in `README.md`; do not put behind-the-scenes material there.

See also `AGENTS.md` for the writing and coding conventions, and `build/plan.md`
and `build/tasks.md` for where the conversion stands and what is left.

## What this repository is

PRG400 Python Programming, a SpiralTrain classroom course, laid out as
**Presentation as Code** like the sibling Advanced Python, Go, C# and TNO Python
courses. It shares its build with them through `../Presentation-Template`.

Modules 01 to 11 came from a PowerPoint deck, kept for reference as
`PRG400-Python-Programming_og.pdf` and `PRG400-Python-Programming-Exercises_og.pdf`.
The `uv` and `ruff` material inside module 01, and the two appendices,
`12-appendix-type-hinting` and `13-appendix-libraries`, are new.

## Layout

```
src/slides/00-preamble/00-preamble.md      title and logistics, carries pdfName: and language:
src/slides/NN-topic/NN-topic.md            one Marp Markdown file per module
src/slides/12-appendix-type-hinting/       appendix, the type hinting recap
src/slides/13-appendix-libraries/          appendix, datetime, json, re, sys.argv, pytest
src/exercises/NN-topic.md                  one exercise guide per module, ::: markup
demos/<same name as the slide module>/     runnable demo code, files named NN_name.py
solutions/NN-<exercise stem>/              the Wordle game at the end of each exercise
exercises/handouts/NN-<exercise stem>/     what an exercise hands out (data, word lists)
exercises/starters/NN-<exercise stem>/     GENERATED : previous solution + handouts
archive/                                   retired material, not built, linted or shipped
../Presentation-Template/build/tools/make-starters.py regenerates the starters; --check in CI
build/solution-tests/NN-<exercise stem>/   reference tests run by CI against solutions 05 to 12
build/check-solutions.py                   tests (from build/solution-tests/ and stage 13), mypy and a scripted game per stage
build/transcripts/                         the expected output of those scripted games
build/site.config.ts                       the offline exercise site (shared builder)
appendices/                                appendix decks the exercises point at
reference/                                 background reading, shipped to students
build/package.json                         thin wrapper over the shared template build
../Presentation-Template/build/tools/check-fences.py shared fence check, gating in CI
build/plan.md, build/tasks.md              working notes
build/orchestration.md                     the multi-agent rework log, October 2026
```

**The exercises are one continuous project**, a Wordle game, from Exercise 2 to
Exercise 13. `build/plan.md` sections 2 and 4 are the design. Three rules keep it
coherent :

- A solution stage is a complete uv project and is the next exercise's starter.
  Change a solution, then run `uv run python ../Presentation-Template/build/tools/make-starters.py` and commit
  the regenerated starters; never edit a starter by hand.
- Exercise text quotes the solutions verbatim and shows only output produced by
  running them. `WORDLE_SECRET=crane` fixes the secret for a reproducible game.
- Function, module and class names are a contract between the text, the
  solutions, the tests and the starters. Rename across all or not at all.

Exercise guides use the shared markup documented in
`../Presentation-Template/docs/exercise-site.md` : `:::hint`, `:::output`,
`:::solution`, italic slide references. The template's `{\u2605}` step markers are
deliberately not used in this course. The same source
builds the exercises PDF and the offline site (`bun run --cwd build site`).

The toolchain material, `uv` and `ruff` and the editor, sits inside module 01. It
spent a while as a separate `00a-python-tooling` module, which worked but meant two
modules explained how to install Python and disagreed about it. Installing and
running Python is what an introduction is for.

Type hints are introduced as the course goes: variables in module 02, collections
in module 03, signatures in module 05, constructors in module 11. The appendix
`12-appendix-type-hinting` is the recap. It was drafted twice before that, first
inside the chapter 0 toolchain module and then as a standalone module 12 at the
end; both read worse than teaching it in context.

## Building

First time on a machine :

```bash
bun install --cwd ../Presentation-Template/build
bunx puppeteer browsers install chrome      # the lint height check needs it
uv sync                                     # ruff and mypy for the code checks
```

Then, from this course root :

```bash
bun run --cwd build build                  # slides PDF and HTML
bun run --cwd build build -- --exercises   # exercises PDF and HTML
bun run --cwd build serve                  # live presenter mode
bun run --cwd build lint                   # style and layout linter
```

**Order matters when a slide has a diagram.** The lint pass inside `build` runs
before mermaid is rendered, so it measures a placeholder and will report a diagram
slide as fitting when it does not. Run `build` first to populate
`build/.mermaid-cache/`, then run `lint` separately.

## Checking the code

```bash
uv run python ../Presentation-Template/build/tools/check-fences.py    # gating in CI
uv run python ../Presentation-Template/build/tools/check-slide-references.py # gating in CI
uv run ruff check .                    # gating in CI, see below
uv run python ../Presentation-Template/build/tools/make-starters.py --check   # gating in CI
uv run python build/check-solutions.py         # gating in CI
uv run python -m compileall -q demos/01-pythonintro ... solutions
```

`ruff` is configured in `ruff.toml`, not in `pyproject.toml`, because the student
bundle ships `ruff.toml` and deliberately ships no `pyproject.toml`. Its relative
paths are written to resolve in the bundle as well as here.

`uv run ruff check .` is at **zero findings** and should stay there. Every entry
in `[lint.per-file-ignores]` names the lesson it protects, so before silencing a
new finding, check whether the code is teaching the pattern deliberately. If it
is, add a scoped entry with the reason; if it is not, fix the code.

The scope excludes `archive/` and `reference/`. Retired demo folders live in
`archive/`, not beside the live ones.

## Releasing

`.forgejo/workflows/release.yml` runs on every push to `master`. It checks the
Python, builds both decks, publishes a `latest` release with the four documents
plus a zip, and pushes a student bundle to
`SpiralTrain/Python-Programming-Student`.

The bundle is an **allowlist**, not a copy-then-prune: naming what goes in means a
folder added later cannot leak into a student's clone. When
you add a module, add its demo folder to two places in the workflow: the
`compileall` list and the bundle `for item in` list.

The push to the student repository authenticates with a repo-level
`STUDENT_REPO_SSH_KEY` secret, whose public half is registered as a write deploy
key named `prg400-ci-push` on the student repository. The step skips cleanly if
the secret is absent.

## House style for the code

All code in the course, on the slides and in the demos, exercises and solutions,
is PEP 8 named and Pythonic. The material inherited camelCase names, trailing
bare `return` statements and CapWords modules from its PowerPoint days; those are
gone and should not come back. Where an unpythonic form is the lesson, keep it and
say so in a comment and in `ruff.toml`.

Type annotations are introduced as the course goes rather than saved for the end,
so demo code reads like real code. A demo and the slide fence that quotes it must
carry the same annotations.

## The reference tree

`reference/` is the background material that ships with the course. It is meant
to feel generous, so keep it that way, but keep it **current**: the point of the
tree is that everything in it is worth a student's time. It replaced a pile that
included the Python 3.5 documentation, a Python 2.7 installer and a copy of
Dive Into Python written against Python 2.3.

`reference/python-docs/` is a curated subset of the official documentation from
`docs.python.org/3/archives/`. When Python moves on, replace it wholesale rather
than adding a second copy :

```bash
curl -LO https://docs.python.org/3/archives/python-3.NN-docs-pdf-a4.tar.bz2
```

Keep the tutorial, library, reference, using, faq and whatsnew PDFs plus the
howtos a fundamentals student might open. Leave out the C API, the extending
and embedding guides and the porting notes.

## Known rough edges

- `demos/*/extra/` folders still ship. They hold older side examples that no
  slide references, kept on purpose as extra practice material (ported to
  Python 3 and held to the ruff rules).

## Optional libraries and tools

`libraries/` imports the teaching sources from Python-Day4-Tour and is maintained
here. The original repository is unchanged. Its own `src/`, `demos/`, `solutions/`
and `data/` preserve the relative paths the examples use. Its dependencies and
lockfile stay separate from the standard-library fundamentals project. Books from
the old repository are not part of this import.

```bash
bun run --cwd build libraries -- --skip-lint
bun run --cwd build lint:libraries
bun run --cwd build libraries -- --exercises
uv sync --project libraries
uv run ruff check libraries
```

The course-local `build/libraries.ts` runs the shared template with `libraries/`
as its working directory. Add new optional topics there; they do not enter the
fundamentals PDF, schedule, exercise site or Wordle exercise chain. CI builds and
publishes both optional PDFs and HTML files and ships `libraries/` in the student
bundle. Keep optional demo code linted by `libraries/ruff.toml`.
