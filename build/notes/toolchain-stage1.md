# Toolchain stage 1 : shared orchestration entry point (package T3)

Branches : course `tc/stage1` (worktree `_worktrees/prg-tc-stage1`), template
`feature/courseware-cli` (worktree `_worktrees/presentation-template-cli`).
Design : `courseware-toolchain-simplification.md`, sequence steps 1-2.

## Done

- Template `build/courseware.ts` : `bun run <template>/build/courseware.ts [build|lint|slidev] [deck] [flags]`,
  run with the course root (or its `build/`) as working directory. Reads `courseware.config.ts`
  from the course root. Owns flag parsing, renderer routing, PDF/HTML copies, the student ZIP
  (delegates to `slidev/delivery.ts`) and the lint call. Template = its own checkout; prints
  `Template: <dir>` (with `(PRESENTATION_TEMPLATE_DIR)` when the override is set).
- Template `build/courseware.test.ts` (`bun run --cwd build test`) : argument parsing and Slidev flag routing.
- Course `courseware.config.ts` : decks `fundamentals` (root) and `libraries` (`libraries/`).
- Course `build/course.ts`, `build/libraries.ts`, `build/slidev.ts` are adapters calling the entry.
  `lint` script now goes through `course.ts --lint` (was a hard-coded `../../Presentation-Template` path).

## Decided

- Template location from the course : `PRESENTATION_TEMPLATE_DIR`, else `../Presentation-Template`
  (the documented sibling, as `site.config.ts` already does). Removed : the existence probe and the
  silent fallback to `_worktrees/presentation-template-slidev`, and the split where Marp used one
  template and Slidev another. A missing entry is an error naming the variable.
- `pdfName` stays in each deck's preamble (the renderers read it); config holds only what differs
  between decks : `dir`, `renderer`, `archive`, `plainMarpHtml`.
- `renderer: 'marp'` (default) forwards to `build.ts` unchanged, for courses without Slidev.
- No exercise-source field : `build.ts --exercises` already discovers them from the deck folder.

## Left

- Verification builds and baseline comparison (below).
