# Toolchain performance (package PERF, 2026-10-19)

Course branch `perf/build-time` (from master c3da932), template branch `perf/build-time` (from
main a22a746, notes only: `docs/notes/toolchain-perf.md`), CI image branch `perf/build-time`
in `C:/Git/courseWare/_worktrees/ci-image-perf` (not built, not pushed).
Measured on the 16-thread Windows 11 development machine, development override unless noted.

## A. Build time

### Where the time went (before, serial, as release.yml ran it)

| Step | s (run 1) | s (run 2, warm caches) |
|---|---:|---:|
| uv lock --check, uv sync, compileall, fences, references, starters, quiz, ruff | 6 | 6 |
| check-solutions (fundamentals) | 13 | 6 |
| libraries make-data, outputs, native states, fences | 7 | 5 |
| **libraries check-demos** (113 demos, one at a time) | **44** | **52** |
| libraries check-solutions | 17 | 17 |
| check:animations | 1 | 1 |
| build (Slidev app, PDF, lint, check, ZIP) | 26 | 106 (outlier) |
| **check:delivery** | **192** | **195** |
| build:marp | 17 | 11 |
| build --exercises | 12 | 8 |
| site | 16 | 4 |
| libraries Slidev, Marp, lint, exercises | 35 | 33 |
| verify x2, bundle, verify --bundle, release --prepare | 7 | 8 |
| **Total** | **393** | **451** |

CI adds about 110 s of setup: Bun download, the template fetch and `bun install` (about 85 s,
of which Puppeteer downloads 683 MB of Chrome that CI never uses), uv and its Python and wheels.
That matches the ~7 min the build job took.

Inside `check:delivery` (192 s): `check_core` 112 s (136 click states, each a fixed 650 ms
sleep, plus 300 + 350 ms around one mid-transition frame per direction), `check_data_structures`
62 s (33 fresh page loads with `networkidle0`, each followed by a fixed 900 ms sleep), the wheel
probe 17 s; all three one after another. Not duplicated anywhere: the Slidev deck is built once,
Marp once per deck, each lint once. The Slidev PDF is one `page.pdf` call, already optimal.

### What changed

1. **Delivery check** (`build/slidev_checks/browser_support.ts`, `check_core.py`,
   `check_data_structures.py`, `check-slidev-delivery.ts`):
   - a click is read once it renders the expected `data-ds-step` and no finite animation is
     running (`document.getAnimations()`, polled per frame), instead of after a fixed sleep;
   - the page's animations run 10x faster through the CDP Animation domain (DevTools' animation
     speed): same frames, same end state, less time;
   - the mid-transition frame is still sampled 300 ms into the transition at normal speed;
   - new explicit failures: a click not rendered and settled within 2 s, and any transition
     longer than 650 ms (the old reading time, so a slower transition no longer passes by luck);
   - routes are read on up to 4 pages of one browser (`COURSE_CHECK_PAGES`); the two animation
     checks run side by side; the wheel probe (60 ms gesture windows) still runs alone, unchanged.
2. **Libraries demo check**: each module folder runs in order in its own copy of the course,
   folders in a process pool, reports printed in file order. Same PASS lines. The only output
   difference: `09/10_when_not_to_shell_out` no longer lists `player.log`, which a demo in folder
   03 wrote into the shared copy. Isolation is stricter, not weaker.
3. **`build/ci-build.sh`** runs every gate of the old steps (all 24 commands) in groups: Python
   gates of both projects and both deck builds (plus site) side by side; then `check:delivery`
   alone; then verify. A failed step stops its group; every log is printed; the step fails.
4. **release.yml**: Bun and uv downloaded only when missing; `PUPPETEER_SKIP_DOWNLOAD=true` on
   the template fetch (all three jobs); both uv projects synced in one step; the fetch step now
   fails when `toolchain.ts --path` fails (it used to write an empty `TEMPLATE` and pass).
5. **CI image** (branch only): Bun 1.4.1, `PUPPETEER_SKIP_DOWNLOAD=true`, and Bun's package cache
   prewarmed from the template's two lockfiles, so the CI template install links instead of
   downloading.

### After

| | s |
|---|---:|
| check_core | 112 -> 11 |
| check_data_structures | 62 -> 12 |
| check:delivery | 192 -> 29 to 30 (6+ passing runs) |
| libraries check-demos | 44 -> 16.5 alone, 24 inside the concurrent phase |
| phase 1 (gates + decks + site at once) | 49 to 53 |
| **build/ci-build.sh total** | **81, 84, 82** (override); **78** through the pinned path |
| + bundle, verify --bundle, release --prepare | 7 |

Local build-job steps: **393 s -> about 88 s** (4.5x).

### Proof the checks still fail

Each mutation rebuilt the deck and ran `check:delivery` (all restored afterwards):

| Mutation (DataStructuresRun.vue) | Result |
|---|---|
| `--ds-time: 1500ms` | check_core fails: `click 1 runs a 1500 ms transition, longer than 650 ms` ... |
| caption of the previous click shown | both checks fail on the caption |
| `data-ds-step` updated 3 s late | both fail: mid-transition `wrong state`, `click 1 not rendered and settled 2000 ms after the key press` |
| a demo exiting 3, a demo opening a socket | check-demos `2 failed`, exit 1 |
| `TEMPLATE` pointing nowhere | both gate groups FAIL at their first step, script exits 1 before check:delivery |

The last one found a real bug in the first version of `ci-build.sh`: bash ignores `set -e`
inside functions called from `cmd || exit`, so a failed gate let its group continue and pass.
`step` now exits its group explicitly.

### Output identical

All four PDFs from the pinned-path run match `_baselines/python/*.json` page for page
(`fingerprint.py compare`: 276, 243, 135, 179 pages, identical text). Both slide ZIPs have the
same entry names as `_baselines/python/zip-listings` modulo hashes (420 and 302 entries).
`release --prepare` succeeds from the pinned path.

### Projected for CI (not measured)

- Setup: the template install loses the 683 MB browser download now; with the rebuilt image it
  only links from the prewarmed cache (expected a few seconds on Linux instead of ~85 s).
- Steps: ~85 s here with 16 threads. The runner's core count is unknown; with 4 cores phase 1
  should stay near the longest group (~55 s); with 2 cores expect closer to the sum of the
  CPU-bound parts, still well under the old serial time because check:delivery (the biggest
  part) is mostly waiting, not computing.
- Expected build job: about 3 min with the current image, about 2 to 2.5 min with the new one,
  from ~7 min. Forgejo runner concurrency (`capacity`) is not visible from here, so the work
  stays in one job instead of parallel jobs that would each repeat the setup.

### First real CI run: check

- The "Check and build" step log shows four `===== PASS` groups, then delivery, then manifests,
  and each group's per-command timings (`--- N s: ...`).
- `check:delivery` passes on the runner's CPU (the 2 s settle limit and the wheel probe's timing
  windows). If it is flaky, set `COURSE_CHECK_PAGES=1` on the step first.
- The template fetch log shows no Chrome download; renders still use `/usr/bin/google-chrome-stable`.
- `TEMPLATE` resolves to `~/.cache/courseware/toolchain/a22a7469cebb` (or the new pin).
- After rebuilding the image: the Bun step prints `1.4.1` without downloading; the template
  install reports `311 packages installed` in seconds.

## B. Toolchain cache

### Why 830 MB

`build/node_modules` 318 MB and `build/slidev/node_modules` 511 MB (50,160 files) for 1.7 MB of
template source; the biggest packages and what they are for are in the template's
`docs/notes/toolchain-perf.md`. mermaid (122 MB) and monaco-editor (98 MB) come with
`@slidev/cli` but are not in the built 4.6 MB app. Two workspaces each hold typescript, pdf-lib,
shiki, katex and zod.

But Bun hard-links every file from its global cache: only 170 of the 50,160 files (0.7 MB) have
a single link. A toolchain shows 830 MB and adds about 3 MB of disk. The real per-checkout cost
was time (75 to 90 s per checkout to fetch and link 50,000 files on Windows) and path length.

### What changed

- `build/toolchain.ts`: the pinned template goes to one per-machine cache,
  `<cache>/toolchain/<12-char commit>`: `COURSEWARE_CACHE_DIR`, else `%LOCALAPPDATA%\courseware`,
  `~/Library/Caches/courseware`, `$XDG_CACHE_HOME/courseware` (`~/.cache/courseware`; CI).
  Every checkout and worktree shares it; a lock serialises a first fetch and install (a lock of a
  process that has gone is taken over). The short folder name keeps paths under 260 characters.
- `bun run --cwd build toolchain` reports each cached toolchain: size, the part not hard-linked,
  last use. `toolchain -- --prune [--keep N]` removes all but the pin and the N (default 2) most
  recently used, stale partial fetches, and the old per-checkout `.courseware/toolchain`.
- Tests: 10 in `build/toolchain.test.ts` (shared cache across checkouts, lock takeover and
  waiting, prune order, platform defaults).

| | Before | After |
|---|---|---|
| Toolchains for N checkouts of one pin | N x 830 MB shown (N x ~3 MB real), N installs | 1 x 792 MB shown, 3 MB real, 1 install |
| Fetch + install per new worktree (Windows) | 90 s | 0 s once the machine has the pin |

Not trimmed: `--production` would remove only typescript and @types (no real disk), and it
breaks diagrams because `pele` is a devDependency used at runtime. mermaid and monaco are
dependencies of `@slidev/cli`. Nothing safe was left to remove.

## Open decisions

- Rebuild and push the CI image (steps in its README); then the Bun and template steps are
  near-instant. Requires anonymous HTTPS read access to Presentation-Template, which the
  workflow's fetch already relies on.
- Move `pele` to `dependencies` in the template (correctness; lockfile change).
- The Marp and exercises builds of the fundamentals deck stay in one group because both write
  `build/dist` and `build/.mermaid-cache`; separating them would save ~5 s at some risk.
- Existing `.courseware/toolchain` folders in the main checkouts are no longer used; run
  `bun run --cwd build toolchain -- --prune` once after merging.
