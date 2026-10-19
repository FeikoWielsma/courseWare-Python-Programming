# PRG400 current design

PRG400 contains eleven fundamentals modules, three appendices and a separate
libraries course. Its thirteen exercises build one Wordle project through
complete solution stages and generated starters.

## Teaching design

- Module 01 introduces Python and its uses, then files, folders, the editor,
  terminal and the edit-save-run cycle. Detailed tooling is in appendix 14.
- Type hints appear in sequence: variables (02), collections (03), signatures
  (05), constructors (11), then recap (12).
- Slides and demos use music and photos, WoW characters for classes, and a film
  watchlist for SQLite. Wordle belongs to exercises.
- Required exercise steps use previously taught features and point to the
  teaching slide or demo. Step support varies without difficulty labels.
- Practice words remain in Python until file loading begins in Exercise 9.
- pytest is taught in Exercise 13. Deep inheritance, generators, decorators,
  dataclasses and collections belong to Advanced Python.

## Exercise contracts

Each `solutions/NN-<exercise stem>/` directory is a complete uv project. Starters
are generated from solutions and handouts. Exercise text, solutions, tests and
starters share names, stage behavior and output expectations. Keep every stage
runnable and check it through the solution suite and scripted transcript.

Further scaffolding for Exercises 10 to 13 is explicitly trainer-deferred and is
outside the courseware migration. Its scope and acceptance criteria remain in the
[live backlog](tasks.md) and [progression audit](notes/progression-audit.md).

## Build design

Both declared decks use Slidev by default and retain Marp fallback output. Deck
configuration, including each deck's Marp output path, lives in
`courseware.config.ts`. Build outputs and manifests live under
`.courseware/<deck>/<variant>/`; Slidev authoring output lives under
`.courseware/<deck>/authoring/`. The shared courseware entry owns build behavior.

The offline site command builds its own fresh fundamentals Marp prerequisite,
then assembles the student site. CI does not build that prerequisite separately.
Current commands and shared toolchain operation are documented in
[MAINTAINING.md](../MAINTAINING.md) and
[the shared configured-course guide](../../Presentation-Template/docs/courseware.md).
