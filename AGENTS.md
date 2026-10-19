# AGENTS.md : instructions for agents working on this course

Course : *Python Programming* (PRG400), the four-day Python fundamentals course.

Read first, in this order :

1. `../Presentation-Template/WRITING-STYLE.md` : shared course writing rules.
2. `../Presentation-Template/docs/course-conventions.md` : frontmatter, demo pills,
   code fences, diagrams and appendices.
3. This file : PRG400-specific decisions and contracts.
4. `build/plan.md` (current design) and `build/tasks.md` (remaining backlog).

For configured builds, toolchain resolution and shared commands, read
[`../Presentation-Template/docs/courseware.md`](../Presentation-Template/docs/courseware.md)
and [MAINTAINING.md](MAINTAINING.md). Shared build changes belong in a
Presentation-Template worktree and must keep other courses building.

Historical migration records and content reviews are indexed in
[`build/notes/README.md`](build/notes/README.md).

## Course identity

Eleven modules and three appendices (`12-appendix-type-hinting`,
`13-appendix-libraries`, `14-appendix-python-tooling`) use Markdown slides with
native Slidev additions and runnable demos. Thirteen exercises build one Wordle
game. Modules 01 to 11 came from `archive/PRG400-Python-Programming_og.pdf`,
which is retained as reference and never edited.

## Course-specific rules

- **Module 01 opens with Python context** : What is Python, Background, Features
  and Applications, followed by files, folders, the editor, terminal and the
  edit-save-run cycle. Keep only uv setup needed to run a file. Detailed tooling,
  Ruff and syntax reference belong in appendix 14.
- **Exercise 1 practises running code** : plain `print()` statements, comments
  and repairing a syntax error. No imports, functions, annotations or file
  reading. Exercise 3 supplies practice words written directly in Python.
- **Type hints are taught as the course goes** : variables in 02, collections in
  03, signatures in 05, constructors in 11; appendix 12 is the recap. Preserve
  annotations in touched demos and identical slide fences. Functions examples
  teach calls and results before signatures introduce annotations.
- **Teaching examples** use music and photos, WoW characters for classes, and a
  film watchlist for SQLite. The libraries course uses music and photos for data,
  WoW for inheritance, and books.toscrape.com for scraping and SQLAlchemy. See
  `build/notes/history/engaging-examples.md` before rewriting examples. Wordle
  contracts remain separate.
- **Pythonic code** applies to slides, demos, exercises and solutions. Keep an
  unpythonic form only when it is the lesson, and identify that lesson in a
  comment or scoped `ruff.toml` ignore.
- **f-strings everywhere**; `%` and `str.format` appear once for recognition.
- **Properties** : plain attributes first, `@property` for computed values or
  rules. Do not use `get_x`, `set_x` or `property(get, set)`.
- **pytest, not unittest**. Deep inheritance, generators, decorators,
  dataclasses and collections belong to Advanced Python.
- Demo files use `NN_name.py` (`demoNN_name.py` in module 07). Student-facing
  content is in English.

## Exercises : the Wordle spine

The shared pattern is [`exercise-spine.md`](../Presentation-Template/docs/agents/exercise-spine.md).
Here, `solutions/NN-<exercise stem>/` is a complete uv project and
`exercises/starters/` is generated from solutions and handouts. Never edit a
starter by hand. `build/check-solutions.py` runs each stage's tests (from
`build/solution-tests/` for 05 to 12, from its solution folder for 13), mypy from
Exercise 12, and scripted games against `build/transcripts/`.

Names (`score_guess`, `play`, `Game`, module names) are contracts between text,
solutions, tests and starters. Exercise text quotes solution code verbatim and
shows output produced by running it. Use `secret = "crane"` for repeatable checks.

Vary support without star or difficulty labels: short code, a hinted skeleton, or
only a signature and expected output. Word lists stay in Python until Exercise 9.
Every required step uses concepts already taught, and each code-writing step has
a first hint naming its teaching slide or demo. Keep timings out. Slides and demos
stay separate from Wordle. `archive/` contains retired material, not source
content.

## Checks

```powershell
uv sync
uv sync --project libraries
$template = bun run build/toolchain.ts --path
uv run python "$template/build/tools/check-fences.py"
uv run python "$template/build/tools/check-slide-references.py"
uv run python "$template/build/tools/make-starters.py" --check
uv run ruff check .
uv run python build/check-solutions.py
uv run python build/site/check-quiz.py
bun run --cwd build build -- --skip-lint
bun run --cwd build build -- --exercises
bun run --cwd build site
bun run --cwd build verify -- fundamentals
bun run --cwd build verify -- libraries
```

`build/ci-build.sh` runs CI gates, including delivery and libraries checks. The
site command builds a fresh fundamentals Marp prerequisite itself. `ruff` lives in
`ruff.toml` because the student bundle ships that file and no `pyproject.toml`.
When a lesson intentionally violates a Ruff rule, scope its ignore and name the
lesson in a comment.

## Releasing

`.forgejo/workflows/release.yml` runs on pushes to `master`. Add new demo folders
to `bundle.include` in `courseware.config.ts`. The bundle is an allowlist;
MAINTAINING.md and the shared courseware guide describe operations.
