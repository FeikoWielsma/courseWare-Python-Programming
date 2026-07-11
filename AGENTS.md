# AGENTS.md — Instructions for Claude working on this courseware

Course : *Python Programming* (PRG400) — fundamentals course.
Read this in full before making any changes.

---

## What this is

11 core modules of Marp Markdown slides plus per-module exercise files, converted from the original PDF deck (`PRG400-Python-Programming_og.pdf`, kept for reference).

The build system is shared with sibling courseware repos via `../../Presentation-Template/build/`.
Never modify anything under `Presentation-Template` from here.

## First-time setup

```bash
bun install --cwd ../Presentation-Template/build
bunx puppeteer browsers install chrome      # required by the lint height check
```

## Build commands (from this course root)

```bash
bun run --cwd build build                  # compile slides to PDF
bun run --cwd build build -- --exercises   # compile exercises to PDF
bun run --cwd build serve                  # live Marp server
bun run --cwd build lint                   # style and layout linter
```

Run lint after editing any slide file and fix every warning before stopping.

## File structure

```
src/slides/00-preamble/00-preamble.md      title + logistics (carries pdfName: and language:)
src/slides/01-python-intro/ … 11-python-classes/   one folder per module, one .md per folder
src/exercises/01-…md … 12-…md              exercise guides
demos/01-pythonintro/ … 11-python-classes/ runnable demo files referenced from the slides
solutions/                                  exercise solutions
```

## Conventions

- Slide frontmatter : `footer:` carries the short module name; the build generates the
  course schedule and module overview slides from it. Do not write `# Module N : Title` slides.
- Demo references : a slide that has a matching file in `demos/<module>/` ends with a line
  `` > `demoNN · name` `` where `NN_name.py` (or `demoNN_name.py`) is the demo file.
  Numbers must be gap-free ascending per module file (a drop starts a new group).
- Write in English; businesslike full sentences; no em-dashes on bullet lines; parent bullets
  that introduce sub-bullets end with ` :` (space before colon).
- Every code fence has a language tag and a blank line before it.

## What NOT to do

- Do not edit `*_og.pdf` (original deck) or regenerate it; the build writes `PRG400-Python-Programming.pdf`.
- Do not add dependencies to `build/package.json`.
- Do not write content in Dutch.
