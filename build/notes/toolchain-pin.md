# Toolchain stage 4 : pin the toolchain (package T8)

Branches : course `tc/pin` (worktree `_worktrees/prg-tc-pin`), template `feature/courseware-pin`
(worktree `_worktrees/presentation-template-pin`, from `feature/courseware-cli` with stages 1, 3
and the browser module). Design : `courseware-toolchain-simplification.md` section 2.

## Done

- Course `build/toolchain.json` records the pin : `{ "repository": <URL>, "commit": <40-hex SHA> }`.
- Course `build/toolchain.ts` resolves the template, in this order :
  1. `PRESENTATION_TEMPLATE_DIR` : used as is; prints `DEVELOPMENT OVERRIDE: ...` on stderr.
  2. `.courseware/toolchain/<commit>` (already ignored) : fetched on demand into
     `<commit>.partial-<pid>` (`git init`, `fetch --depth=1 origin <sha>`, falling back to a full
     fetch, `checkout <sha>`), renamed when complete. Then verified on every run : `HEAD` equals the
     pin and `git status --porcelain` is empty, else an error saying which and to delete the folder.
     The first run installs `build/` and `build/slidev/` with `bun install --frozen-lockfile` and
     marks it in `.git/courseware-installed` (inside `.git`, so the checkout stays clean); a failed
     install is an error and is retried next run.
  3. Otherwise an error : the commit cannot be fetched; pin a pushed commit or use the override.
  `PRESENTATION_TEMPLATE_REPOSITORY` replaces the recorded URL for the fetch only (CI's HTTPS
  URL, or a local test remote); the commit is still verified.
- `build/toolchain.ts --path` prints the folder (Python checks and CI use it);
  `build/toolchain.ts <args>` runs the template's `courseware.ts` with them.
- The sibling default `../Presentation-Template` is gone from every course script :
  `course.ts` (now 3 lines, the resolver moved to `toolchain.ts`), `site.config.ts`,
  `check-slidev-delivery.ts`, `slidev_checks/check_delivery.ts`, `check_diagrams.ts` (these three
  required the variable) and `check_core.py`, `check_data_structures.py` (sibling fallback).
- Scripts : `bun run toolchain` (report and validate), `bun run pin -- [ref] [--repository url]`,
  `bun run verify -- <deck>`, `bun run test` (resolver tests).
- Template `courseware.ts` :
  - prints `Template: <dir> at <sha> (pinned)`, or `DEVELOPMENT OVERRIDE: template <dir> at <sha>
    ... from PRESENTATION_TEMPLATE_DIR, not the pinned <pin>`, or `(no build/toolchain.json)` for a
    course without a pin (other courses keep working);
  - refuses to run (exit 1) without the override when its HEAD is not the pin or it is dirty;
  - `toolchain` prints the line and the pin, exit 1 on a mismatch or a malformed pin;
  - `pin [ref] [--repository url]` writes the commit of `ref` (default `HEAD`) in the template
    checkout running it, keeps the recorded repository (else `origin`'s URL), and warns when no
    remote-tracking branch contains the commit.
- Manifest (`courseware-artifacts/1`) : `toolchain` keeps `commit, ref, dirty, dir, override` and
  gains `pin` (the course's pinned SHA, or null). `verify` fails a non-override manifest whose
  toolchain commit is not the pin or was dirty, and prints a `NOTE ... DEVELOPMENT OVERRIDE` line
  for an override build (still PASS, so local gates run with the override).
- Tests : course `build/toolchain.test.ts` (override, fetch then cache hit with the remote gone,
  repository override, missing SHA leaves no cache, dirty / untracked / other commit / broken cache,
  malformed pin); template `build/toolchain.test.ts` (pin format, status, pin helper) and an
  `artifacts.test.ts` case for the pin check.

## Decided

- JSON file, not a field in `courseware.config.ts` : `pin` rewrites it mechanically, Python and
  shell can read it without executing course code, and the diff of a re-pin is one line.
  `build/` because the bootstrap reading it is there.
- Fetch per course checkout, not a machine-wide cache : the cache sits in the already-ignored
  `.courseware/`, needs no new location or variable, and is removed with the checkout.
  Cost : about 90 s and ~1 GB of `node_modules` per checkout and pin on first use.
- Verification fails rather than repairs : a dirty or moved cache is reported, not reset, so local
  edits are never discarded silently.
- `pin` resolves refs in the checkout that runs it (normally the override checkout you tested
  with), so it needs no network.

## Pinning to a local test remote

A commit that is only on a local branch cannot be fetched from the server. Point the fetch at a
local repository instead, by either :

```bash
PRESENTATION_TEMPLATE_REPOSITORY=file:///C:/Git/courseWare/_worktrees/presentation-template-pin bun run --cwd build toolchain
# or record it (not for committing): bun run --cwd build pin -- <sha> --repository file:///C:/...
```

A worktree path works : `git` resolves its shared repository.

## Final pin value

`build/toolchain.json` pins the tip of `feature/courseware-pin` at this package's last template
commit, with the server URL. That commit is not on the remote yet. **The coordinator must push
and merge the template, then re-pin to the merged SHA** :
`PRESENTATION_TEMPLATE_DIR=<checkout at the merged commit> bun run --cwd build pin -- <merged sha>`,
then `bun run --cwd build toolchain` without the variable.

## Verification (2026-10-19)

Clean checkout : `git worktree add --detach C:/Users/feiko/AppData/Local/Temp/prg-pin-clean/Python-Programming tc/pin`
(no `Presentation-Template` beside it), no `PRESENTATION_*` variables, `build/toolchain.json`
repository set to `file:///C:/Git/courseWare/_worktrees/presentation-template-pin` in a local-only
test commit (`812d914`, not on `tc/pin`). The temp worktree and its logs were removed afterwards; fingerprint in `_baselines/t8/`.

| Command | Result |
|---|---|
| `bun run toolchain` (first run) | fetched 3627a35, `bun install --frozen-lockfile` in `build/` (311 packages) and `build/slidev/` (655), `Template: ...\.courseware\toolchain\3627a35... (pinned)`; 1 m 29 s |
| `bun run build -- --skip-lint` | exit 0; `(pinned)`; 276 pages, 0 failures; ZIP written; identical text on every page against `_baselines/python/PRG400-Python-Programming.json` |
| `bun run verify -- fundamentals` | `PASS fundamentals student`; manifest `toolchain` : commit = pin = 3627a35, `override: false`, `dirty: false` |
| `bun run check:delivery` | exit 0; check_core, check_data_structures, wheel probe PASS (Python checks resolved the template through `toolchain.ts --path`) |
| `git status --porcelain` in the cache after build and delivery | empty |
| final pin adef04a on `tc/pin`, fetched with `PRESENTATION_TEMPLATE_REPOSITORY=file:///...` | `(pinned)`; `verify` PASS |
| same pin from the real ssh remote (`GIT_SSH_COMMAND="ssh -o BatchMode=yes"`) | `ERROR Cannot fetch ... (fatal: unable to read tree (adef04a...))`, no cache left : the commit is not pushed |
| template tip run directly against `tc/pin` without the override | `ERROR template is adef04a..., build/toolchain.json pins 3627a35...`, nonzero exit |
| `PRESENTATION_TEMPLATE_DIR=<template worktree> bun run toolchain` | two `DEVELOPMENT OVERRIDE` lines (bootstrap, template), exit 0 |
| `bun run --cwd build test` (course) | 6 pass |
| `uv run ruff check .` | All checks passed |

Template : `typecheck` clean, `bun run --cwd build test` 27 pass, `smoke` SMOKE PASS,
`bun test` in `build/slidev` 14 pass. Not run : `libraries`, Marp, exercises and site builds
through the pin (same resolver path), other courses (no pin, so `courseware.ts` behaves as before;
none of them calls it yet).

## Coordinator : release.yml (T9 owns it)

Replace the `Checkout Presentation Template` step, the `test -f` guard and both `bun install`
lines in `Install template dependencies`, and the `PRESENTATION_TEMPLATE_DIR` env of
`Build slides and exercises`, with :

```yaml
      - name: Fetch the pinned Presentation-Template
        shell: bash
        env:
          PRESENTATION_TEMPLATE_REPOSITORY: ${{ github.server_url }}/SpiralTrain/Presentation-Template.git
        run: |
          echo "TEMPLATE=$(bun run build/toolchain.ts --path)" >> "$GITHUB_ENV"
```

placed after `Install Bun 1.4 for Slidev` (the fetch runs `bun install --frozen-lockfile`).
Then `../Presentation-Template/build/tools/...` becomes `"$TEMPLATE/build/tools/..."` in the
fences, slide-references and starters steps, and in the libraries step
`uv run python "$TEMPLATE/build/tools/check-fences.py"` (it is absolute, so `cd libraries` is
fine). The two verify lines become `bun run verify -- fundamentals` and `bun run verify -- libraries`.
The build steps need no template variable at all. Optional : cache `.courseware/toolchain/` keyed
on `hashFiles('build/toolchain.json')`. Publishing should refuse a manifest with
`toolchain.override: true`.

## Coordinator : documentation

- Course `AGENTS.md` Checks and `MAINTAINING.md` : `../Presentation-Template/build/tools/X.py` →
  `"$(bun run build/toolchain.ts --path)/build/tools/X.py"`; MAINTAINING line 38 becomes :
  "Builds run the shared `build/courseware.ts` from the Presentation-Template commit pinned in
  `build/toolchain.json`; `build/toolchain.ts` fetches it into `.courseware/toolchain/<commit>`
  and installs its dependencies on first use. `PRESENTATION_TEMPLATE_DIR` is the development
  override and is reported as `DEVELOPMENT OVERRIDE` by the build and in every artifact manifest.
  `bun run --cwd build toolchain` shows the pin; after a template merge, re-pin with
  `PRESENTATION_TEMPLATE_DIR=<checkout> bun run --cwd build pin -- <sha>`." The line saying the
  Slidev toolchain must be merged into template main before a release becomes "the pin must be a
  pushed commit".
- AGENTS.md "Read first" links to `../Presentation-Template/...` docs stay (reading, not building).
- Template `AGENTS.md` (after the `courseware.ts` paragraph) : "A course with
  `build/toolchain.json` pins this repository; `courseware.ts` refuses to run from any other commit
  unless `PRESENTATION_TEMPLATE_DIR` is set. Changes reach such a course only when it re-pins."
  `docs/course-tools.md` keeps its sibling default for courses without a pin.

## Open decisions

- Per-checkout cache (~1 GB, ~90 s per checkout and pin) versus a shared machine cache.
- Two override lines (bootstrap on stderr, template on stdout) : keep both, or drop the bootstrap's
  when it forwards to `courseware.ts`.
- Whether `verify` should also fail a manifest whose pin differs from the course's current pin
  (today the `source.commit` check at publish time covers that).
- Other courses : adopt `build/toolchain.ts` (copied, about 75 lines) when they move to
  `courseware.config.ts`.
