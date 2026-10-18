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

- Stricter than before : a stray positional argument (`bun run libraries -- nope`) is now an error;
  previously it was forwarded and ignored.

## Verification (2026-10-18)

`PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/_worktrees/presentation-template-cli`, logs in
`C:/Git/courseWare/_baselines/t3/`, fingerprints in `_baselines/t3/fp/` compared with
`uv run --with pypdf python fingerprint.py compare python/<name>.json t3/fp/<name>.json`.

| Command | Result |
|---|---|
| `build -- --skip-lint` | exit 0; 276 pages, identical text on every page; ZIP 420 entries, same names apart from Vite content hashes |
| `libraries -- --skip-lint --force` | exit 0; 179 pages, identical text; ZIP 302 entries, same names apart from hashes |
| `build:marp -- --force` | exit 0; 243 pages, identical text; `-Marp.html` written |
| `build -- --exercises --force` | exit 0; 135 pages, identical text |
| `libraries:marp -- --skip-lint --force` | exit 0; `-Marp.pdf/.html` and the plain `.html` alias (byte-identical copy) |
| `libraries -- --exercises --force` | exit 0 (no baseline) |
| `lint`, `lint:libraries` | exit 0, "All slides within budget." |
| `slidev -- --with-clicks --range 109` | exit 0, 8 click-state pages, `course-slidev-clicks-109.pdf` |
| `build -- --range 3-4` | exit 0, 2 pages, `course-slidev-3-4.pdf`; root PDF and ZIP untouched |
| `slidev:check` | exit 0, 276 pages, 0 failures |
| `build -- --prepare` without the variable | clear error naming `PRESENTATION_TEMPLATE_DIR` |

Template : `bun run --cwd build typecheck` clean, `bun run --cwd build test` 7 pass,
`bun run --cwd build smoke` SMOKE PASS, `bun test` in `build/slidev` 14 pass.
Not run : `--serve` / `--dev` servers, `check:delivery`, other courses (none call the new entry).

## Left for stage 3

- The entry is the place to write the artifact manifest : it already knows deck, variant
  (normal, Marp, exercises, range, clicks), the PDF target and the archive path.
- Range and click exports still share `build/slidev/dist` with the normal build (they rebuild the
  app there); separate output folders are stage 3.
