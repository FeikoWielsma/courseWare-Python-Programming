# Libraries Slidev Phase 3: delivery review

Completed 2026-10-18. This closes the verification and delivery work in
[`libraries-slidev-plan.md`](libraries-slidev-plan.md). The reviewed build has
179 Slidev pages, 169 Marp pages and ten native additions with 55 authored
states. The normal build retains one known upstream FloatingVue console warning;
there were no Slidev layout failures and lint remained within budget.

## Browser and GUI behavior

Chromium was run with Puppeteer Core and its native
`page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }])`
API, which emulates the browser media feature used by CSS. The browser check
visited all ten native additions, advanced and reversed every authored state,
compared the displayed captions and outputs with the executed Python state data,
confirmed computed transitions are `0s` in reduced-motion mode, and compared
the restored DOM and visual state after reversing. All 55 states passed. The
reproducible QA runner is ignored at `libraries/build/qa/qa_native_browser.mjs`;
the executed state manifest is generated at `libraries/build/slidev/dist/native-qa.json`.

The six interactive Tk demos were also exercised as visible Linux GUI windows
under WSLg by a scripted UI driver. Checks covered window close, entry/combobox
and Add callbacks, weighted grid and Save, left/right click bindings, 40-row
Treeview sorting and selection, and SQLite filtering including SQL-like input
treated as data. All six passed. Tk, fonts, Poppler, and small X11 input/screenshot utilities were
installed in the disposable Arch WSL QA environment because those system
packages were absent; this did not change project dependencies. The demo-created
database was removed after the check.

## Export review

The final Slidev and Marp PDFs were rendered page by page. Nine Slidev module
sheets plus the preamble sheet were visually inspected, along with a nine-module
Marp spot-check sheet and the 32-page exercise PDF sheet. The separate native click
export contains 55 pages for the ten additions; its full contact sheet was also
visually inspected. No clipping, overlap, cut-off code, or other rendering
defect was found. The exercise PDF built successfully. The handout source does
not quote command output blocks, so there were no per-handout quoted outputs to
match; the 37 solution commands passed the solution/output checkers.

The clicked export can be reproduced with:

```bash
bun run --cwd build libraries -- --with-clicks --range 11,13,68,91,109,114,117,134,141,146 --force
```

## Delivery and checks

The student ZIP was checked as a 302-entry archive: no `src/`, `build/` or
`notes/` paths, no Markdown, Vue or TypeScript authoring files, and no unsafe
paths. Its PDF is byte-identical to the canonical Slidev PDF. A fresh extraction
was served locally; the Slidev app and PDF both returned HTTP 200.

The implementation checks passed:

- `make-data.py --check`: 12 generated data artifacts reproduce.
- `native_states.py --check`: ten additions and 55 states match.
- `check-demos.py`: 119 compiled, 113 non-GUI executed, zero failures.
- `check-solutions.py`: 37 commands, zero failures.
- `check-outputs.py`: zero mismatches; no quoted output blocks in exercise
  handouts.
- `ruff check .`, `uv lock --check --project libraries`, and
  `bun run --cwd build lint:libraries` passed.
- Shared fence checking found 144 Python fences, 139 complete fences and five
  snippets, with no problems; all slide references resolved.
- The Slidev/Marp comparison build and the exercise PDF build completed without
  layout failures.

Temporary page renders, contact sheets, extracted delivery files, logs, and QA
scripts are under ignored `libraries/build/`. No release, commit, or push was
performed.

## Release portability correction

The first remote release check exposed XLSX ZIP platform flags that differed
between Windows and Linux. Workbook archives now use fixed platform metadata
and stored entries; generated text uses LF line endings. PNG checks compare
exact decoded pixels because zlib builds can encode identical pixels differently.
The complete data check passes on both Windows and Linux.
