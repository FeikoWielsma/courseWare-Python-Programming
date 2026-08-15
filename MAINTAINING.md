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
`00a-python-tooling`, `12-type-hinting` and the `13-appendix-libraries` appendix
are new material.

## Layout

```
src/slides/00-preamble/00-preamble.md      title and logistics, carries pdfName: and language:
src/slides/00a-python-tooling/             uv, ruff and the editor
src/slides/NN-topic/NN-topic.md            one Marp Markdown file per module
src/slides/13-appendix-libraries/          appendix, carries appendix: true
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

Type hinting is module 12, deliberately at the end. It was drafted as part of the
chapter 0 toolchain module and moved, because annotating a signature before `def`
has been taught in module 05 is backwards for a first course.

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
uv run python -m compileall -q -x extra demos/01-pythonintro ... solutions
```

`ruff` is configured in `ruff.toml`, not in `pyproject.toml`, because the student
bundle ships `ruff.toml` and deliberately ships no `pyproject.toml`. Its relative
paths are written to resolve in the bundle as well as here.

The repository is **not** at zero ruff findings. There are around 944 inside the
configured scope, nearly all of them dated style in demo code that came from the
original deck. CI runs ruff with `continue-on-error` until they are cleared; the
plan for that is in `build/tasks.md`.

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

## Known rough edges

- `.gitattributes` has not been added. `* text=auto eol=lf` would renormalise
  line endings across 5000+ tracked files in one commit, so it wants doing on its
  own rather than mixed into content work.
- `demos/*/extra/` holds sixteen Python 2 files that do not compile. The whole
  `extra/` tree is excluded from the bundle and from the `compileall` gate.
- `demos/09-python-io/createexecutable/build` is 12 MB of committed PyInstaller
  output, excluded from the bundle and worth deleting from the repository.
- `pandas/`, `software/`, `vb/` and `demos/extrademos` belong to other courses.
