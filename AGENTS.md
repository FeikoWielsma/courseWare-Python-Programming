# AGENTS.md — Instructions for Claude working on this courseware

Course : *Python Programming* (PRG400) — fundamentals course.
Read this in full before making any changes.

---

## What this is

14 modules of Marp Markdown slides plus per-module exercise files. Modules 01 to 11 are
converted from the original PDF deck (`PRG400-Python-Programming_og.pdf`, kept for
reference). `00a-python-tooling` and the two appendices, `12-appendix-type-hinting`
and `13-appendix-libraries`, are new material.

Working notes live in `build/plan.md` (where the conversion stands, what is left) and
`build/tasks.md` (the checklist). Read those before picking up work.

The build system is shared with sibling courseware repos via `../../Presentation-Template/build/`.
Never modify anything under `Presentation-Template` from here.

**The `00a-` prefix is deliberate.** The build discovers modules with
`readdirSync(slidesDir).sort()` and skips only `00-preamble`, so `00a-python-tooling`
sorts after the preamble and before `01-python-intro` without renumbering anything
else. The schedule slide lists modules by footer name and carries no numbers, so it
picks the module up on its own. Do not renumber `01` to `11` to make room.

**Type hints are taught as the course goes.** Variables are annotated in module 02,
collections in module 03, signatures in module 05 and constructors in module 11, so
the demo code looks like real code rather than a stripped-down teaching dialect.
`12-appendix-type-hinting` is the recap: it gathers what has been shown and adds
`| None` and a checker. When you touch a demo, keep its annotations, and keep the
matching slide fence identical to it.

**Both appendices carry `appendix: true`** in their frontmatter, which puts them under
their own Appendix divider on the schedule slide. Their exercise files start with
`<!-- appendix -->` as the very first line, which separates them in the exercises
table of contents.

**All code in the course is PEP 8 named and Pythonic.** The material inherited a set
of Java-isms, camelCase names and trailing bare `return` statements, and they were
removed across the slides, demos, exercise text and solutions together. Do not
reintroduce them. Where an unpythonic form is the lesson, such as the Java-style
accessors that the property slide improves on, keep it and say so in a comment.

## First-time setup

```bash
bun install --cwd ../Presentation-Template/build
bunx puppeteer browsers install chrome      # required by the lint height check
uv sync                                     # ruff and mypy for the code checks
```

## Build commands (from this course root)

```bash
bun run --cwd build build                  # compile slides to PDF
bun run --cwd build build -- --exercises   # compile exercises to PDF
bun run --cwd build serve                  # live Marp server
bun run --cwd build lint                   # style and layout linter
```

Run lint after editing any slide file and fix every warning before stopping.

## Python code

```bash
uv run python build/check-fences.py     # gating in CI, must be clean
uv run ruff check .                     # informational in CI, ~944 findings today
uv run python -m compileall -q -x extra demos/01-pythonintro solutions
```

`ruff` is configured in `ruff.toml`, not in `pyproject.toml`, because the student
bundle ships `ruff.toml` and deliberately ships no `pyproject.toml`.

The repository is **not** at zero ruff findings, unlike the sibling Advanced Python
course. Clearing them is tracked in `build/tasks.md`. Do not "fix" a finding in a
demo where the anti-pattern is the lesson; add a scoped entry to
`[lint.per-file-ignores]` with a comment saying why.

## File structure

```
src/slides/00-preamble/00-preamble.md      title + logistics (carries pdfName: and language:)
src/slides/00a-python-tooling/             uv, ruff and the editor
src/slides/01-python-intro/ … 11-python-classes/   one folder per module, one .md per folder
src/slides/12-appendix-type-hinting/       appendix, the type hinting recap
src/slides/13-appendix-libraries/          appendix, carries appendix: true
src/exercises/01-…md … 13-…md              exercise guides
demos/00a-python-tooling/                  demos for the tooling module
demos/01-pythonintro/ … 13-appendix-libraries/  runnable demo files referenced from the slides
solutions/                                  exercise solutions
appendices/                                 appendix decks the exercises point at
reference/                                  background reading, shipped to students
build/check-fences.py                       the python fences on the slides, gating in CI
build/plan.md, build/tasks.md               working notes
```

Demo files are named `NN_name.py` here, matching the `> \`demoNN · name\`` pill, rather
than the `demoNN_name.py` form the sibling Advanced Python course uses.

`src/exercises/01-environment-configuration.md` is Exercise 1 and belongs to
`00a-python-tooling`, not to `01-python-intro`. Module 01 has no exercise, which
matches the original course flow where the first coding exercise follows Variables
and Data Types.

**A new module means two edits to `.forgejo/workflows/release.yml`** : its demo folder
joins the `compileall` list and the bundle `for item in` list. The bundle is an
allowlist, so a folder that is not named there does not reach the student.

## Conventions

- Slide frontmatter : `footer:` carries the short module name; the build generates the
  course schedule and module overview slides from it. Do not write `# Module N : Title` slides.
- Demo references : a slide that has a matching file in `demos/<module>/` ends with a line
  `` > `demoNN · name` `` where `NN_name.py` (or `demoNN_name.py`) is the demo file.
  Numbers must be gap-free ascending per module file (a drop starts a new group).
- Write in English; businesslike full sentences; no em-dashes on bullet lines; parent bullets
  that introduce sub-bullets end with ` :` (space before colon).
- **The deck is background-agnostic.** Do not add comparisons to the student's other
  languages, and do not add speaker NOTES blocks; only the preamble carries those.
  Cross-language framing belongs in the room, not in the material.
- Every code fence has a language tag and a blank line before it.
  - ```` ```python ```` is for Python. Program output, transcripts, tracebacks, file
    content and grammar skeletons that are not valid Python take ```` ```text ````;
    shell commands take ```` ```bash ````.
  - `build/check-fences.py` extracts every python fence and checks it. Run
    `uv run python build/check-fences.py` before stopping; CI gates on it.
- Diagrams are ` ```mermaid ` fences, or inline SVG where mermaid cannot express the
  shape. The build renders mermaid to SVG and caches it in `build/.mermaid-cache/`.
  - **Run `build` first, then `lint` separately.** The lint pass inside `build` runs
    before mermaid is rendered, so it measures a placeholder and will call a diagram
    slide fitting when it does not.
  - Use plain `graph LR`, `flowchart LR`, `classDiagram` or `sequenceDiagram` with no
    theme directives and no hardcoded colours. Prefer wide over tall.
  - **Keep the outer edges of a diagram made of rectangles.** `trimSvgViewBox` in the
    shared build crops to a bounding box computed from `<rect>` elements only, so a
    circle `((…))` or a `[*]` marker at an extreme is silently cut off. The
    Encapsulation slide shipped broken for exactly this reason. Check with
    `grep -o 'viewBox="[^"]*"' build/.mermaid-cache/*.svg`; a healthy diagram starts at
    `viewBox="3 3 …"`.
  - Inline SVG takes a `viewBox` and `width="100%"`, uses `currentColor` and no
    background fill, so it follows the theme in both light and dark.
    - **Do not rely on leading or trailing spaces inside `<text>`.** Chrome collapses
      them and `xml:space` on the parent `<g>` is not inherited. Position each run
      explicitly, and right-align with `text-anchor="end"` where padding matters.

## What NOT to do

- Do not edit `*_og.pdf` (original deck) or regenerate it; the build writes `PRG400-Python-Programming.pdf`.
- Do not add dependencies to `build/package.json`.
- Do not write content in Dutch.
