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

## Verification

See the report table below (filled in as run).
