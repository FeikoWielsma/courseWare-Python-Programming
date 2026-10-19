# Toolchain stage 6b : course browser checks on the shared module (package T7)

Branch `tc/browser6` in `C:/Git/courseWare/_worktrees/prg-tc-browser6`.
Template (read-only) `C:/Git/courseWare/_worktrees/presentation-template-cli`,
`build/browser.ts`. Every command below sets
`PRESENTATION_TEMPLATE_DIR` to that worktree.

Commits on top of `e3ce3b7`:

- `10405ea` Run course browser checks through the shared browser module.
- `3796044` Keep the generated selector waits inside the ruff line limit.

`git diff --shortstat e3ce3b7..HEAD` for those two: 5 files, 59 insertions, 78 deletions.

## Done

- `build/check-slidev-delivery.ts` serves the packaged presentation named by the
  artifact manifest (`presentation` role, `.courseware/fundamentals/student/slides`)
  with `serve(dir, { port: 0 })`. The origin is `server.url`. `finally` still
  kills a child that has not exited, then `server.close()`.
- `build/slidev_checks/check_diagrams.ts` and `check_delivery.ts` use
  `withBrowser`. Diagram checks serve that same presentation deliverable.
  `check_delivery.ts` uses `--origin` when the delivery runner is already
  serving, and otherwise serves the presentation. Viewport, the 120s navigation
  and selector limit, and page close come from `withBrowser` / `browserTimeoutMs`.
- Generated launchers in `check_core.py` and `check_data_structures.py` import
  `withBrowser`, `browserTimeoutMs` and (core only) `reducedMotion` from
  `build/browser.ts`. They no longer import `launchBrowser`.
- Assertions kept: reduced-motion durations only `0s` or `0ms`; containment;
  traced Python and provenance; wheel, momentum, Ctrl+wheel, scrollable probe,
  editable control and slide-boundary checks, including the sleep schedule;
  diagram font floor (10px), viewBox and escaped text.
- `libraries/build/` maintained scripts do not launch Chrome or serve. None
  were edited, so the libraries `check-*.py` commands were not run.

## Decided

- Course checks import `build/browser.ts` by absolute path under
  `PRESENTATION_TEMPLATE_DIR`. Python still falls back to
  `../Presentation-Template` when that variable is unset. The TypeScript checks
  still throw.
- No new console or external-HTTP diagnostics. These checks did not have them.
- The diagram check and a standalone delivery probe open the `presentation`
  deliverable (`.courseware/<deck>/student/slides`), not the variant folder and
  not `build/slidev/dist`. The page map stays `manifest.json` in the variant folder.

## Shared module lacked

`deleteProfile` in template `build/browser.ts` gives up too soon on Windows.
After `check:delivery` (three Chrome sessions: core, data structures, wheel),
the headless processes were gone and these directories were still in `%TEMP%`,
each with a `chrome_debug.log` for `127.0.0.1:53900`:

- `pt-chrome-profile-75ocRr` (00:03:23, core)
- `pt-chrome-profile-2YFfSa` (00:05:15, 103 files)
- `pt-chrome-profile-WAVdgg` (00:06:16)

`Remove-Item -Recurse` succeeded a minute later, so the lock does not last.
`slidev:check` and both `check_diagrams.ts` runs left no new profile. The
retry (`maxRetries: 5`, `retryDelay: 200`, linear backoff, error swallowed)
is the gap. Suggested replacement:

```typescript
function deleteProfile(userDataDir: string) {
  const deadline = Date.now() + 10_000;
  while (true) {
    try {
      fs.rmSync(userDataDir, { recursive: true, force: true });
      return;
    } catch {
      if (Date.now() >= deadline) return;
      Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 200);
    }
  }
}
```

Those three directories were removed by hand after that check so this package
does not leave them. Other `pt-chrome-profile-*` directories were already in
`%TEMP%` and were left alone. No `node` / `bun` / headless Chrome process
whose command line contained `prg-tc-browser6` was still running afterwards.

## Verification (2026-10-18)

| Command | Result |
|---|---|
| `bun run --cwd build build -- --skip-lint` | exit 0. 276 pages, 230 topics, 0 failures, 1 upstream warning. Bound URLs `127.0.0.1:64106` and `:55187`. |
| `bun run --cwd build libraries -- --skip-lint` | exit 0. 179 pages, 160 topics, 0 failures, 1 upstream warning. |
| `bun run --cwd build check:delivery` | exit 0 in 192s. Served `.../student/slides` at `http://127.0.0.1:53900`. Core: 136 forward/reverse frames, reduced motion and containment pass. Data structures: 33 rendered states. Wheel probe: eight PASS lines, boundary `#/03-data-structures-3?clicks=7 -> #/03-data-structures-3-enhancement`. |
| `bun run --cwd build check:animations` | exit 0. Static core (10 slides, 68 states), data structures (33 states), 5 list states and 3 tuple states. No browser. |
| `bun run --cwd build slidev:check` | exit 0. `http://127.0.0.1:63432`. 276 pages, 230 topics, 0 failures, 1 upstream warning. Profile directory removed. |
| `bun run build/slidev_checks/check_diagrams.ts` | exit 0. Nine fences, browser text 11.5px–25.6px, all at least 10px. `http://127.0.0.1:56288`. Profile directory removed. |
| `uv run ruff check .` | All checks passed. |

Intentional failure: the diagram font comparison was temporarily `< 10000` (message text left as the real 10px floor). `check_diagrams.ts` threw and the shell reported exit 126:

```text
01-python-intro-1: diagram text renders at 11.5px; minimum is 10px.
...
11-python-classes-14: diagram text renders at 25.6px; minimum is 10px.
```

The comparison was restored. `git status` after that is only this notes file.
