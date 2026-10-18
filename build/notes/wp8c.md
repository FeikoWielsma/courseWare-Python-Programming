> Historical record (2026-10-17). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# WP8c : exercise site and PDF pagination fixes

Date: 2026-10-17. Package: `wp8c`.

## Course site findings

- **F01:** submitted Wordle rows now render `guesses[r].word`; each tile still uses `guesses[r].states` for its colour and accessible state label.
- **F21:** Enter is left to the browser when a button is focused, preserving button activation. Enter elsewhere in the dialog still submits the typed guess.
- **F20:** the test row says it is available from Step 4, where Exercise 5 adds the handout and pytest dependency. The type-check row says it follows Step 1, where Exercise 12 installs mypy.

## Shared PDF pagination finding

On branch `exercise-pdf-pagination`, the exercises stylesheet avoids breaks inside hint blocks, before hints and expected-output labels, after a paragraph that introduces code or a table, and before that following code or table. The solution cue now has explicit avoid-break rules so it stays with the step content before the solution page. The output label has a visually empty marker added by the preprocessor so the print stylesheet can identify and keep it with its output.

## Verification

The site was built from this worktree's `build/` directory with `PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/Presentation-Template bun run site.config.ts`. A headless Puppeteer run loaded the generated site over `file://`, typed `wordle` outside a field, froze the date-derived answer to `crane`, and checked `error` and the winning `crane` row. The first row displayed `error` with labels `e present`, `r correct`, `r absent`, `o absent`, `r absent`; the winning row displayed `crane` with five `correct` labels. Enter on the focused Close button closed the dialog. Exercise 5 and 12 pages showed the qualified starter rows.

The PRG400 exercises PDF changed from **117 to 118 pages**. All pages were rendered with `uv run --with pymupdf`; the two pages containing only “Solution on next page” (before: pages 67 and 80) are gone. The four orphaned hint/output blocks are now with their step content, and the Exercise 6 Step 2 prompt and table are together. The Exercise 5 Step 5 closing paragraph remains a page continuation, but it is with its solution cue and is not a detached hint/output block. Near-empty pages (text length at most 45 characters) went from **2 to 0**; orphaned hint/output blocks went from **4 to 0**, and the separated prompt/table pair went from **1 to 0**. The extra page comes from keeping introducing text and its table/output blocks together; it is a pagination change, with no course text changes apart from updated TOC page numbers.

Comparison PDFs were built before and after using the same shared template:

| Course PDF | Before | After | Page text comparison |
|---|---:|---:|---|
| Advanced C# exercises | 86 | 86 | All 86 page texts are identical. |
| PySpark Block 1 exercises | 96 | 97 | Content reflows across pages; the only text-token change is the TOC page number 69 to 70. |
| PySpark Block 2 exercises | 64 | 65 | Content reflows across pages; the only text-token change is the TOC page number 46 to 47. |

The PySpark page increases come from the improved generic grouping rules. The exercise wording is unchanged. The PySpark checkout's source files were not edited.

Gates passed:

- `uv run ruff check .`
- `uv run python build/site/check-quiz.py` (39 questions and 25 executable examples)
- `bun run --cwd build typecheck`
- `bun run --cwd build test:site`

The generated site/PDF artifacts were not staged.
