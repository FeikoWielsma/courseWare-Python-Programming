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
`00a-python-tooling` and the two appendices, `12-appendix-type-hinting` and
`13-appendix-libraries`, are new material.

## Layout

```
src/slides/00-preamble/00-preamble.md      title and logistics, carries pdfName: and language:
src/slides/00a-python-tooling/             uv, ruff and the editor
src/slides/NN-topic/NN-topic.md            one Marp Markdown file per module
src/slides/12-appendix-type-hinting/       appendix, the type hinting recap
src/slides/13-appendix-libraries/          appendix, datetime, json, re, unittest
src/exercises/NN-topic.md                  one exercise guide per module
demos/<same name as the slide module>/     runnable demo code, files named NN_name.py
solutions/                                 reference solutions
build/package.json                         thin wrapper over the shared template build
build/check-fences.py                      the python fences on the slides, gating in CI
build/plan.md, build/tasks.md              working notes
```

**The `00a-` prefix is load bearing.** The build discovers modules with
`readdirSync(slidesDir).sort()` and skips only `00-preamble`, so `00a-python-tooling`
sorts between the preamble and `01-python-intro`. That is what let the toolchain
module be added without renumbering eleven slide directories, eleven demo
directories, eleven exercise files and every pill. Do not "tidy" it into `01-`.

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
uv run python build/check-fences.py    # gating in CI
uv run ruff check .                    # informational in CI, see below
uv run python -m compileall -q demos/01-pythonintro ... solutions
```

`ruff` is configured in `ruff.toml`, not in `pyproject.toml`, because the student
bundle ships `ruff.toml` and deliberately ships no `pyproject.toml`. Its relative
paths are written to resolve in the bundle as well as here.

`uv run ruff check .` is at **zero findings** and should stay there. Every entry
in `[lint.per-file-ignores]` names the lesson it protects, so before silencing a
new finding, check whether the code is teaching the pattern deliberately. If it
is, add a scoped entry with the reason; if it is not, fix the code.

The scope deliberately excludes the demo folders no slide references and the two
orphan solution folders. `ruff.toml` and the bundle allowlist in the workflow
should name the same set; keep them in step.

## Releasing

`.forgejo/workflows/release.yml` runs on every push to `master`. It checks the
Python, builds both decks, publishes a `latest` release with the four documents
plus a zip, and pushes a student bundle to
`SpiralTrain/Python-Programming-Student`.

The bundle is an **allowlist**, not a copy-then-prune. This repository is around
800 MB and most of it belongs to other courses; `pandas/` alone is 397 MB. Naming
what goes in means a folder added later cannot leak into a student's clone. When
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

## Known rough edges

- `pandas/`, `software/`, `vb/`, `demos/extrademos` and the other unreferenced
  demo folders belong to earlier versions of the course or to sibling courses.
  They are excluded from ruff and from the student bundle, but still in the repo.
- `solutions/xextra` and `solutions/solutions-generators` solve exercises this
  course does not have, and still ship in the bundle. Worth deciding on.
- The `demos/12-pythonlibraries-*` folders are superseded by
  `demos/13-appendix-libraries` and no longer ship.
