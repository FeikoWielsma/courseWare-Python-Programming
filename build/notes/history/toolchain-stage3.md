# Toolchain stage 3 : separate outputs and the artifact manifest (package T4)

Branches : course `tc/stage3` (worktree `_worktrees/prg-tc-stage3`), template
`feature/courseware-cli` (worktree `_worktrees/presentation-template-cli`).
Design : `courseware-toolchain-simplification.md`, sections 3 and 4, sequence step 3.

## Done

- Every Slidev variant builds in its own folder : `<course>/.courseware/<deck>/<variant>/`,
  variant `student`, `trainer` (`--notes`), `range-<pages>`, `clicks`, `clicks-range-<pages>`
  (`slidevVariant` in template `build/artifacts.ts`). `courseware.ts` passes `--output`; a direct
  `slidev/build.ts` run defaults to `<root>/.courseware/<variant>/`. A build clears its folder first
  (refuses a folder that holds the course or is not a Slidev output). `build.log` and `converted.md`
  moved into the variant folder. `build/slidev/dist` is no longer written.
- Marp fallback and exercises builds record manifests too (`marp`, `exercises` folders hold only
  `artifacts.json`; the Marp renderer still works in `build/dist`, unchanged).
- `courseware.ts` writes `artifacts.json` per deck and variant, deleting the old one before a build.
- Packaging (`slidev/delivery.ts`) takes the app and PDF from the manifest and returns the
  `presentation` and `archive` deliverables. The packaged folder is now `<variant>/slides/`
  (was `build/slidev/dist/student/`).
- `--serve-only` serves the `presentation` (or trainer `app`) named in the manifest, not the
  comparison folder. `--check-only` checks the folder the same flags select.
- `courseware.ts verify [deck] [--variant v] [--bundle <zip|folder>]` validates (template
  `build/artifacts.ts`, ZIP reader `build/zip.ts`, content rules in `slidev/delivery.ts`).
  Tests : `build/artifacts.test.ts` (in `bun run --cwd build test`).
- Deliverables keep their paths and names : root PDFs/HTML, `build/dist/*-slides.zip`.
  The manifest maps them; no `dist/` folder and no compatibility copies were needed.
- Course : `.gitignore` ignores `.courseware/`; `check-slidev-delivery.ts` finds the packaged
  presentation through `artifacts.json`; `slidev_checks/*` read the page map from
  `.courseware/fundamentals/student/manifest.json`.

## Manifest schema (`courseware-artifacts/1`)

```json
{
  "schema": "courseware-artifacts/1",
  "deck": "fundamentals", "variant": "student", "audience": "student",
  "createdAt": "2026-10-18T21:31:20.676Z",
  "source": { "commit": "<course HEAD or null>", "dirty": false },
  "toolchain": { "commit": "<template HEAD>", "ref": "feature/courseware-cli", "dirty": false,
                 "dir": "C:/Git/courseWare/_worktrees/presentation-template-cli", "override": true },
  "deliverables": [
    { "role": "pdf", "path": "PRG400-Python-Programming.pdf", "name": "PRG400-Python-Programming.pdf",
      "kind": "file", "size": 2456101, "sha256": "..." },
    { "role": "app", "path": ".courseware/fundamentals/student/slidev", "kind": "directory", "files": 412, "...": "" },
    { "role": "presentation", "path": ".courseware/fundamentals/student/slides", "kind": "directory", "files": 419, "...": "" },
    { "role": "archive", "path": "build/dist/Python-Programming-slides.zip", "kind": "file", "...": "" }
  ],
  "checks": { "slidev": "pass", "lint": "skipped" }
}
```

Paths are relative to the course root. A directory's `sha256` covers every relative path and
file checksum; `size` is the byte total. Roles : `pdf`, `html`, `html-alias`, `app`,
`presentation`, `archive`. Checks : `pass`, `fail`, `skipped`, `forced` (`--force` lint).

Expected roles (verify fails when one is missing) : slidev `student` pdf+presentation+archive;
Marp-renderer `student` pdf; `marp` pdf+html (+html-alias with `plainMarpHtml`); `exercises`
pdf+html; `trainer` app; range/clicks pdf. A `--no-html` student build is therefore not publishable.

Verify checks : schema; expected roles; recorded checks not `fail`; each deliverable exists with
the recorded kind, size and sha256; for student audience, the presentation folder and the ZIP
contain no caches/workspaces (`.courseware`, `.work`, `node_modules`, `__pycache__`, ...), QA
records (`build.log`, `validation.json`, `*-export.json`, `artifacts.json`), authoring sources
(`manifest.json`, `slides.md`, `converted.md`, `marp.md`, `src/slides`, `src/slidev`) or trainer
note phrases (same heuristic as `check.ts`, now shared); the ZIP holds `slides/index.html`,
`slides/serve.py`, `slides/slidev/index.html` and the PDF. `--bundle` applies the content rules
to an assembled student bundle against every deck's notes.

## Decided

- Least elaborate layout : `.courseware/<deck>/<variant>/` at the course root (also for
  libraries, so nothing new appears inside `libraries/`, which release.yml copies whole).
  No `dist/`; deliverable paths unchanged, so the release keeps working with two `cp` edits.
- The manifest sits in the folder of the app it describes, and a build clears that folder, so a
  manifest cannot outlive or be paired with another variant's app.
- Verify is a pure check (exit code); it does not write results into the manifest. Publishing
  must run it immediately before upload.
- `prepare.ts` (not in the package's file list) changed : `converted.md` goes to the output
  folder and the unused default output argument is gone. `check.ts` takes the deck root instead
  of deriving it from `../../..` and uses the shared `notePhrases`.

## Found

- The Marp HTML (`PRG400-Python-Programming-Marp.html`, also the baseline from production) embeds
  the preamble's trainer notes (Marp presenter view). It is a release asset and in the student
  bundle. `verify --bundle` reports it. Renderer change, not made here : open decision.

## Verification (2026-10-18)

`PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/_worktrees/presentation-template-cli`; logs and
fingerprints in `C:/Git/courseWare/_baselines/t4/`.

| Command | Result |
|---|---|
| `build -- --skip-lint` | exit 0; 276 pages, identical text on every page; ZIP 420 entries, same names (Vite hashes normalised, `t4/zipnames.py`) |
| `libraries -- --skip-lint --force` | exit 0; 179 pages identical; ZIP 302 entries, same names |
| `build:marp -- --force`, `build -- --exercises --force` | exit 0; 243 and 135 pages identical |
| `libraries:marp`, `libraries -- --exercises` | exit 0; manifests with alias / exercises |
| `build -- --range 3-4`, `slidev -- --with-clicks --range 109`, `slidev -- --notes` | exit 0; 2 pages, 8 click pages, trainer app, each in its own folder |
| `courseware.ts verify` (after the three above) | PASS student, trainer, range-3-4, clicks-range-109, marp, exercises; libraries PASS ×3 |
| Tamper (`t4/tamper.sh`, log `t4/tamper.log`) | appended PDF byte, trainer app packaged, build.log+page map in slides, ZIP deleted : each FAIL with the cause; restored : PASS |
| `slidev -- --serve-only --port 4291` | serves `.courseware/fundamentals/student/slides`; `/slidev/` 200, `/manifest.json` 404; stopped |
| `check:delivery` | exit 0; check_core, check_data_structures, wheel probe PASS |
| `slidev:check`, `lint`, `uv run ruff check .` | exit 0, 0 failures; within budget; all passed |
| `verify --bundle` on a release-style bundle (`t4/bundle.sh`, 1840 files) | only the Marp HTML notes above |
| Go PRG350, PowerShell PRG900 deck + exercises with the template worktree | identical text on every page |

Template : `typecheck` clean, `bun run --cwd build test` 17 pass, `smoke` SMOKE PASS,
`bun test` in `build/slidev` 14 pass.

## Left for stage 5

- Publish from the manifests : assets = `pdf`, `html`, `html-alias`, `archive` deliverables of
  each deck's `student`, `marp`, `exercises` manifests. Run `verify` first; refuse when
  `source.dirty` or `source.commit` differs from the release commit.
- The full student bundle and `build/site/dist` have no manifest yet; bundle assembly should move
  into code and record a `bundle` deliverable, then `verify --bundle` it.
- `package.py` ZIPs carry build timestamps, so archive checksums differ per build (retries reuse
  the same files, so this does not block retrying without rebuilding).
- `dev.ts` still writes authoring output to `build/slidev/authoring/` (not in this package).
