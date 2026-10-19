> Historical record (2026-10-18). Current commands and defaults: MAINTAINING.md; index: ../README.md.

# Toolchain browser and serving survey

Recorded 2026-10-18. Package T2, read-only. No implementation.

Branch `tc/browser-survey` in `C:/Git/courseWare/_worktrees/prg-tc-browser-survey`.
Template reads are from `C:/Git/courseWare/_worktrees/presentation-template-cli`
(`feature/courseware-cli`). Line numbers are from those checkouts.

Done: inventory of Chrome launch, static serving, waits, cleanup, reduced-motion
and diagnostics, plus one proposed module interface. Left: implementing that
module and deleting the duplicates. Decided below; nothing was run except
search. No builds, no servers started.

Design context is sections 5 and 6 of
`build/notes/courseware-toolchain-simplification.md`: one shared browser
checker, courses keep assertions, two serving modes, report the bound URL,
clean up on exit and error, keep the offline Python student launcher.

## Where Chrome actually starts

There is one `puppeteer.launch` in the surveyed tree:
`Presentation-Template/build/lint-slides.ts` `launchBrowser` at lines 634–667.
Every other browser check imports that function. The duplication is the
waiting, port logging, viewport, reduced-motion toggle, diagnostics and
`finally` cleanup around it.

`launchBrowser()` (`lint-slides.ts:634`):

| Piece | Exact behaviour |
|---|---|
| Extra args | `PUPPETEER_EXTRA_ARGS`, else `MERMAID_CHROME_ARGS`, split on whitespace (`636–638`). If neither is set and `process.platform === 'linux'`, args are `--no-sandbox` and `--disable-dev-shm-usage` (`639–640`). Otherwise `args` is `[]`. Windows and macOS get no sandbox flags unless the env var is set. |
| Binary | `CHROME_PATH`, else `PUPPETEER_EXECUTABLE_PATH`, else omitted so Puppeteer picks its own (`642`, `654`). |
| Headless | `true` when an executable path is set; `'shell'` (chrome-headless-shell) otherwise (`653`). Comment at `650–652`: shell mode cannot run on a full Chrome binary. |
| Profile | `fs.mkdtempSync(path.join(os.tmpdir(), 'pt-chrome-profile-'))` (`648`). Passed as `userDataDir` so Puppeteer will not delete it (`655`). Comment at `643–647`: Puppeteer's own temp profile delete hits `EBUSY` on Windows and fails the build. |
| Close | Replaces `browser.close` (`658–666`). Awaits the real close, then `fs.rmSync(userDataDir, { recursive: true, force: true, maxRetries: 5, retryDelay: 200 })`. A remaining lock is swallowed. |
| Not set | No `dumpio`, no `protocolTimeout`, no `timeout`, no `pipe`, no default viewport inside `launch`. Callers set 1280×800 themselves. |

`lintFile` (`686`) launches its own browser only when no `page` was passed
(`724–728`), measures via `setContent` (`756`, default navigation timeout),
and on a Puppeteer error logs one line and continues (`948–949`). Its
`finally` (`950–953`) closes that private browser. A measurement error does
not fail the process by itself.

`lint-slides.ts` `main` (`1028–1057`) launches once, warns and continues with
overflow checks skipped if launch throws (`1034–1036`), reuses that page for
every file, and closes after the loop (`1055–1057`). There is no `finally`:
a throw from `lintFile` skips `browser.close`, so the profile delete in the
wrapped `close` never runs.

`build/build.ts:163–195` does the same one-browser reuse for the Marp build
lint. Launch failure is a warning (`170–172`). Close is after the loop
(`194–196`), again not in `finally`.

`build/site-test.ts:65–118` is outside the requested file list and is the
other `launchBrowser` consumer. It opens `file://` pages, emulates reduced
motion (`72`) without asserting durations, and closes in `finally` (`118`).
The shared module has to keep working for this caller.

## Static server

`serveDirectory(directory, port)` in `build/slidev/build.ts:21–38`:

- Node `http.createServer`. Host is always `127.0.0.1` (`37`).
- Resolves the URL path under `directory`, rejects paths that escape it with
  403 (`28–29`), directories become `index.html`, missing files 404, thrown
  handler errors 400 (`35`).
- MIME map is a fixed object (`22`): html, js, mjs, css, json, svg, png,
  woff2, pdf, md. Anything else is `application/octet-stream`.
- `Cache-Control: no-cache`. `HEAD` ends without a body (`34`).
- The listen callback logs `Presentation comparison: http://localhost:${port}`
  using the **requested** port, not `server.address().port` (`37`).
- No `'error'` listener. `EADDRINUSE` is an unhandled server error.
- Returns the `http.Server` immediately. It does not return a URL, and it
  does not register `SIGINT` / `SIGTERM`.

Callers that pass `0` then read `address().port` and navigate to
`http://127.0.0.1:${port}`. The log line still says `http://localhost:0`.

## Per-file survey

### `build/slidev/check.ts` `checkCourse` (`8–128`)

Serves `output` on port `0` (`19`). Waits with
`if (server.listening) resolve(); else server.once('listening')` (`20`).
Throws if `address()` is missing or a string (`22`). Origin is
`127.0.0.1` plus the bound port (`23`).

`launchBrowser()` then `newPage`, viewport 1280×800 (`24–29`). Launch sits
**outside** `try`. If it throws, the server is never closed.

Diagnostics (`30–47`), the only structured ones in the Slidev checks:

- `setRequestInterception(true)`. Any `http(s)` URL that does not start with
  `origin + '/'` is pushed as `External network dependency` and aborted.
- `response.status() >= 400` becomes `HTTP <status> <url>`.
- `pageerror` is pushed as `String(error)`.
- `console` type `error` is a failure, except text that starts with
  `Failed to patch FloatingVue`, which is a warning (`41–45`).

Waits:

- `goto ${origin}/slidev/#/export`, `waitUntil: 'networkidle0'`, `timeout: 120000` (`48`).
- `waitForFunction` until `.course-frame` count equals `manifest.slidevPages`, `timeout: 120000` (`49`).
- `document.fonts.ready` (`50`).
- Second `goto` of one reveal slide, `networkidle0`, **no timeout** (`101`). Puppeteer default is 30s.
- `waitForSelector('.course-step')`, **no timeout** (`102`).
- Fixed sleeps 400ms, then 300ms after ArrowRight, 300ms after ArrowLeft (`103`, `107`, `110`).
- Optional `goto ${origin}/marp.html#1`, `networkidle0`, **no timeout** (`114`).

`finally` (`124–127`): `browser.close()` then `server.close`, rejecting if
`close` errors. If `browser.close()` throws, the server is left up. Failures
are written to `validation.json` before the throw (`119–122`). No reduced
motion. No screenshots.

### `build/slidev/export-pdf.ts` `exportBrowserPdf` (`10–56`)

Same port-0 serve and the same "already listening" wait (`11–12`). Throws
`Cannot start export server` before launch (`14`), which also leaks the
server. Launch is outside `try` (`15`).

Viewport 1280×800. `goto` the print route
`/slidev/?print=clicks|true#/course-export`, `networkidle0`, `timeout: 120000`
(`20`). `waitForSelector('.print-slide-container')` has **no timeout** (`21`).
`page.pdf` `timeout: 120000` (`45`). `finally` is the same close-browser-then
close-server order (`52–55`). No request interception, no reduced motion.

### `build/slidev/dev.ts` `serveCourseSources` (`10–70`)

Source mode, not a static server. Spawns
`node <slidev.mjs> slides.md --port <port>` with `stdio: 'inherit'` (`19`).
The caller (`build.ts:55`) passes `Number(option('--port') || '3030')`.

Logs the **requested** port before the child is ready (`59`):
`Watching course sources for Slidev on http://localhost:${port}`.

Watch debounce is 180ms (`42`). `close` (`51–56`) sets `stopped`, clears the
timer, closes watchers, and `child.kill()` with no signal (default
`SIGTERM`; no process-group kill, no timeout, no Chrome involved).
`SIGINT` and `SIGTERM` each call `close` once (`57–58`). `finally` calls
`close` again and removes the listeners (`65–68`). A child `error` rejects;
`exit` resolves with the code, or 130 if only a signal (`61–63`).

### `build/slidev/build.ts` flags (`41–110`)

| Flag | What it serves | Port |
|---|---|---|
| `--dev` | `serveCourseSources` (`54–56`), then `return`. Does not build `dist`. | `--port` or **3030** |
| `--serve-only` | `serveDirectory(build/slidev/dist)` and `return` (`48–49`). No build. | `--port` or **4188** |
| `--serve` | After the build (and after `--check` if present), `serveDirectory(output)` (`110`). | `--port` or **4188** |
| checks / PDF | `serveDirectory(output, 0)` inside `check.ts` and `export-pdf.ts`. | ephemeral |

`--serve` and `--serve-only` never read `address().port`, never handle
`SIGINT`, and never call `server.close`. The process stays alive only
because the server holds the event loop. The log still says
`Presentation comparison` and `localhost`.

Generated student launcher (`102`), one line of Python:

```python
ThreadingHTTPServer(("127.0.0.1", 4188), handler).serve_forever()
```

`handler` is `SimpleHTTPRequestHandler` rooted at the script's parent.
It prints `Open http://localhost:4188` **before** `serve_forever`, so a
taken port still prints a URL and then raises. No argument, no
`address()` report, no signal handler beyond the interpreter dying.
`README.txt` (`103`) repeats port 4188.

`run()` (`12–18`) is `spawnSync` with `timeout: 300000` for Slidev and Marp
builds. That timeout is not a browser timeout.

### `build/slidev/delivery.ts` and `package.py`

`packageStudentPresentation` (`8–34`) copies `serve.py` into the student
folder (`18`) and writes `index.html` / `README.txt` that hardcode
`python slides/serve.py` and `http://localhost:4188/slidev/` (`25–29`).
`package.py` only zips the folder plus the PDF (`1–13`). It does not serve.

### `build/src/pdf.ts` `exportPdf` (`53–59`)

Marp path, not Puppeteer. `serve === true` runs marp-cli `--server --watch`
on the combined-markdown directory, with no `--port` and no browser flags
here. `MARP_EXTRA_ARGS` is split on whitespace and appended (`22–25`).
`execFileSync` blocks until that process exits (`50`); this function has
no cleanup of its own. `build/build.ts:39` turns `--serve` or `-s` into
that flag, and skips HTML and bookmarks while serving (`253–267`).

### Course `build/slidev_checks/check_diagrams.ts`

Static SVG audit (`47–104`) does not use a browser. The browser half
(`124–174`) runs only when diagram slides have manifest routes.

Same `serveDirectory(dist, 0)` and the same already-listening wait as
`check.ts` (`126–127`). `launchBrowser` is outside `try` (`130`): a launch
failure leaks the server. Viewport 1280×800. For each case,
`goto http://127.0.0.1:${port}/slidev/#/${id}`, `networkidle0`,
`timeout: 120000`, then `waitForSelector` for `svg.pele`, `timeout: 120000`
(`135–136`). Fonts are awaited inside `page.evaluate` (`138`). No sleeps,
no reduced motion, no console/pageerror hooks. `finally` closes browser
then server (`171–173`). Summary lines go to stdout (`177–178`); failures
are one thrown string (`179`).

### Course `build/slidev_checks/check_delivery.ts`

Optional `--origin`. Without it, imports `serveDirectory` and listens on
port `0` (`19–23`). The listen wait is only `server.once('listening')`
(`44`). It does **not** check `server.listening` first, unlike `check.ts`,
`export-pdf.ts` and `check_diagrams.ts`. If the server is already
listening when the listener is attached, the promise never resolves.
It also has no `'error'` listener on this wait.

Launch is **inside** `try` (`50`), and `finally` uses `browser?.close()`
then closes the server only if this process created it (`147–149`). This
is the only Slidev check that still closes the server when launch throws.

`goto` (`56`) is `networkidle0` with **no timeout**. `waitForSelector`
(`.course-step`) has **no timeout** (`57`). Viewport 1280×800 (`52`).
Sleeps, in order: 500, 250, 250, 60, 120, 60, 60, 120, 60, 180, 900, 900,
20, 20, 950, 350, 900, then up to 16 times 850, then 900, 900 (`58–145`).
Wheel input is a CDP `Input.dispatchMouseEvent` (`36–39`), not
`page.mouse.wheel`, except the scrollable-probe and textarea cases
(`117`, `130`). Diagnostics are `console.log('PASS …')` and thrown
messages that include the probe geometry (`119`). No reduced motion.
No screenshots.

### Course `build/check-slidev-delivery.ts`

Does not launch Chrome itself. Serves the **packaged student** directory
`build/slidev/dist/student` on port `0` (`21–22`). Wait is
`once('listening')` plus `once('error')` (`36–38`), still without an
already-listening check. Logs the bound origin (`43`):
`Serving <dir> at http://127.0.0.1:<port>`. This is the only caller that
prints the port it will actually use.

Runs each `check_*.py` **one at a time** with `uv run python <script> --browser <origin>` (`45–57`), then `check_delivery.ts --origin <origin> --output <dist>` (`59–64`). Comment at `51–52`: sequential so one Chrome exists at a time.

`finally` (`67–72`): `child.kill()` (no signal) for any child whose
`exitCode === null`, waits for `exited`, then `server.close`. Killing the
Bun child does not run that child's `browser.close`, so the
`pt-chrome-profile-*` delete can be skipped. Python `subprocess.run` of
Bun has **no timeout** (see below), so a hung page hangs this orchestrator
until something kills it.

### Course `build/slidev_checks/check_core.py`

Python provenance and traced execution stay in `verify_provenance` /
`verify_static` and do not need a browser. `--browser ORIGIN` (`868`)
calls `browser_plan` (`697`).

If `PRESENTATION_TEMPLATE_DIR` is unset, the template path falls back to
`ROOT.parent / "Presentation-Template"` (`698–699`). The TypeScript checks
throw instead of guessing.

It writes a temporary Bun script (`716–719`) that imports `launchBrowser`
from `lint-slides.ts`. The script (`539–694`):

- Viewport 1280×800 (`547`).
- `goto` `networkidle0`, **no timeout**, cache-bust `?r=<Date.now()>` (`549–551`, `649–651`).
- `waitForSelector` `[data-source-id] .ds-run`, **no timeout** (`553`).
- Forward: ArrowRight, then 300ms plus a mid-transition read, then 350ms
  on the first step; 650ms on later steps (`656–664`). Another 650ms
  before the settled read (`667–668`). Reverse uses the same pair of
  sleeps (`670–685`).
- Reduced motion (`686–688`): `page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }])`, one more `read` of the last state (this `read` navigates), collect every `transitionDuration` and `animationDuration` under `.core-names`, `.core-loop`, `.core-stream`. Then `emulateMediaFeatures([])` clears it.
- `finally { await browser.close(); }` (`691`) **before** `Bun.write` of the JSON (`692`). A close error drops the results.

`subprocess.run` (`720–726`) has no `timeout`. On failure, stderr is the
last 4000 characters (`728`). The assertion (`856–858`) fails the slide
when any duration is not `0s` or `0ms`. That is the only reduced-motion
**assertion** in the requested files. It does not look at Libraries
components.

### Course `build/slidev_checks/check_data_structures.py`

Same fallback template path (`405–406`). `--browser` example in the
docstring is `http://127.0.0.1:4188` (`18–21`). The embedded script
(`324–400`) launches, sets 1280×800, and for every click state `goto`s
`?clicks=<k>` with `networkidle0` and **no timeout** (`335–336`), waits
for `.ds-run` with **no timeout** (`337`), then sleeps **900ms** (`339`).
It does not press keys and does not emulate reduced motion. `finally`
closes the browser (`398`) before `console.log(JSON.stringify(results))`
(`399`). The parent parses the last stdout line (`425`) and on failure
keeps the last 3000 characters of stderr (`424`). `subprocess.run` has
no timeout (`419–421`).

### `libraries/build/` maintained scripts

No Chrome, Puppeteer, static server, or reduced-motion emulation.

| File | What it is |
|---|---|
| `check-demos.py`, `check-outputs.py`, `check-solutions.py` | Python execution checks. They use `check_support.py`. |
| `check_support.py:54–68` | `subprocess.run` default `timeout=45` seconds. On `TimeoutExpired`, status `-1` and `Timeout after <n> seconds`. Not a browser. |
| `make-data.py`, `native_states.py` | Data generation and native-state JSON. |
| `slidev.config.ts` | Deck config only. |

`libraries/build/qa/` is ignored scratch (phase 3 notes mention
`qa_native_browser.mjs`). It is not a maintained script and is not part
of this inventory.

## Near-duplicate differences

| Behaviour | `check.ts` | `export-pdf.ts` | `check_diagrams.ts` | `check_delivery.ts` | `check-slidev-delivery.ts` | core / data-structures scripts |
|---|---|---|---|---|---|---|
| Port | `0` | `0` | `0` | `0`, or `--origin` and no server | `0`, student dir | none; caller passes origin |
| Listen wait | already-listening or `once` | same | same | `once` only | `once` plus `error` | n/a |
| Bound port logged | no (`localhost:0` from `serveDirectory`) | no | no | no | yes, `127.0.0.1` | no |
| Launch vs `try` | outside | outside | outside | inside | no launch | inside the generated `try` |
| Server closed if launch throws | no | no | no | yes | n/a | n/a |
| `browser.close` throws skips `server.close` | yes | yes | yes | yes | n/a | n/a |
| Navigation timeout | 120s, then 30s default | 120s | 120s | 30s default | n/a | 30s default |
| Selector timeout | 30s default | 30s default | 120s | 30s default | n/a | 30s default |
| Viewport | 1280×800 | 1280×800 | 1280×800 | 1280×800 | n/a | 1280×800 |
| Reduced motion | no | no | no | no | no | core only; data-structures no |
| Console / HTTP / pageerror | yes | no | no | no | no | no |
| Chrome args / profile | all via `launchBrowser` | same | same | same | child inherits | same |

`serve.py` versus `serveDirectory`: Python `ThreadingHTTPServer` on a
fixed `4188`, prints before bind, serves the script directory with the
stdlib handler. Node server binds `127.0.0.1` on a caller-chosen port,
prints the requested port (so `0` is wrong), and uses the small MIME map.
Neither reports `server.address()` after a successful bind except the
TypeScript checks that build their own origin and, except
`check-slidev-delivery.ts`, do not print it.

`dev.ts` versus `--serve`: dev is Vite on the authoring project, default
**3030**, kills the child on signals. `--serve` / `--serve-only` are the
static server, default **4188**, no signal handler. Course wrappers
collapse those names. `build/course.ts:26–43` and `build/libraries.ts:27–48`
treat `--serve` and `--dev` as the same branch and invoke
`slidev/build.ts` with `--dev` after stripping both flags. So
`bun run --cwd build serve` is the Vite server on 3030.
`bun run --cwd build slidev -- --serve` (through `build/slidev.ts`, which
forwards argv) is the static server on 4188. Marp `--serve` is a third
process: `build/build.ts` `--server --watch`, and `course.ts:36` rewrites
`--dev` into `--serve` only on that Marp/exercises path.

## Proposed module

One TypeScript module in the template, used by lint, Slidev check, PDF
export, diagram check, delivery check, and the two generated browser
scripts. Courses keep assertions. This is an interface, not code.

```typescript
export interface ChromeDiscovery {
  executablePath?: string;          // unset means Puppeteer's default
  source: 'CHROME_PATH' | 'PUPPETEER_EXECUTABLE_PATH' | 'puppeteer';
  headless: true | 'shell';         // true iff executablePath is set
  args: string[];                   // current env / linux rule
}

export function discoverChrome(): ChromeDiscovery;

export interface LaunchOptions {
  executablePath?: string;
  headless?: true | 'shell';
  args?: string[];                  // default discoverChrome().args
  userDataDir?: string;             // default os.tmpdir()/pt-chrome-profile-*
  viewport?: { width: number; height: number }; // default { width: 1280, height: 800 }
}

export interface LaunchedBrowser {
  browser: import('puppeteer').Browser;
  userDataDir: string;
  close(): Promise<void>;          // real close, then rmSync retries; leftover lock does not throw
}

export function launch(options?: LaunchOptions): Promise<LaunchedBrowser>;

export interface StaticServer {
  url: string;                      // http://127.0.0.1:<bound port>, after listen
  port: number;                     // server.address().port, never the request
  close(): Promise<void>;
}

export interface ServeOptions {
  port?: number;                    // default 0 for checks; 4188 only for packaged preview
  host?: string;                    // default 127.0.0.1
}

export function serve(dir: string, options?: ServeOptions): Promise<StaticServer>;

export function withPage<T>(
  launched: LaunchedBrowser,
  run: (page: import('puppeteer').Page) => Promise<T>,
  viewport?: { width: number; height: number },
): Promise<T>;                     // newPage, viewport, run, page.close() in finally; does not close the browser

export function reducedMotion(page: import('puppeteer').Page, reduce: boolean): Promise<void>;
// reduce true: emulateMediaFeatures [{ name: 'prefers-reduced-motion', value: 'reduce' }]
// reduce false: emulateMediaFeatures []

export interface Diagnostics {
  failures: string[];
  warnings: string[];
  attach(page: import('puppeteer').Page, origin: string): void;
}

export interface DiagnosticsOptions {
  blockExternalHttp: boolean;       // check.ts behaviour
  ignoreConsole: (text: string) => boolean; // default: starts with 'Failed to patch FloatingVue'
}

export function diagnostics(options?: Partial<DiagnosticsOptions>): Diagnostics;

export interface CheckSession {
  browser: LaunchedBrowser;
  server?: StaticServer;            // absent when origin was supplied
  origin: string;
  diagnostics: Diagnostics;
  close(): Promise<void>;          // page-independent; closes browser and server even if one throws
}

export interface CheckSessionOptions extends LaunchOptions {
  dir?: string;                     // served on port 0 when origin is absent
  origin?: string;                  // already served; do not listen
  diagnostics?: Partial<DiagnosticsOptions>;
}

export function openCheck(options: CheckSessionOptions): Promise<CheckSession>;
// listen (if dir), then launch. On launch failure, close the server.
// SIGINT/SIGTERM call close once.
```

`openCheck.close` is the guaranteed cleanup. It always attempts browser
close and server close, and it records the first error instead of
skipping the second `await`. `withPage` is for the lint reuse pattern:
one `launch()`, many pages, one `close()` in a `finally` in `main`.

### What it replaces

| Existing | Replaced by | Stays in the caller |
|---|---|---|
| `lint-slides.ts:634` `launchBrowser` | `launch` / `discoverChrome` | `lintFile` measurement, editorial rules, the shared page loop |
| `build.ts:167` and `lint-slides.ts:1031` open/close | `launch` + `finally` `close` | warning-and-continue if launch fails, so overflow can be skipped |
| `serveDirectory` (`build.ts:21`) | `serve` | MIME and path rules move with it; the "Presentation comparison / localhost:${requested}" log goes away |
| listen/address/`finally` in `check.ts`, `export-pdf.ts`, `check_diagrams.ts`, `check_delivery.ts`, `check-slidev-delivery.ts` | `openCheck` | assertions, PDF capture, wheel probes, script list |
| core and data-structures `BROWSER_SCRIPT` launch, viewport, `goto` timeout gap, `browser.close` | `openCheck` + `withPage` from a small shared runner | the in-page `evaluate` and the Python comparisons |
| `site-test.ts:65` launch and `118` close | `launch` / `close` | `file://` clicks and the reduced-motion call that does not assert durations |

`serveCourseSources` is not replaced by `serve(dir)`. It is mode 1 below.
`serve.py` is not replaced by the TypeScript server. Students do not have
Bun or Node.

### What each course check keeps

- `check_core.py`: demo provenance, traced Python, route plan, name/loop/stream
  assertions, containment (`overflow`), and the rule that reduced-motion
  durations are only `0s` or `0ms`. It stops owning Chrome and the temp
  Bun launcher.
- `check_data_structures.py`: fence execution, object identity, per-kind
  DOM reads (slicing, sequence, references, sets, dict). It does not gain
  a reduced-motion check unless a later Libraries assertion asks for one.
- `check_diagrams.ts`: cache key, Pele SVG structure, and the font-scale /
  viewBox / escaped-text assertions.
- `check_delivery.ts`: keyboard reveal, CDP wheel, momentum, Ctrl+wheel,
  scrollable probe, editable control, slide-boundary crossing, and the
  sleep schedule those gestures need. Timeouts move to the shared `goto`.
- `check-slidev-delivery.ts`: "student directory", sequential children,
  failure collection. The server and the origin line come from `serve`.
- `check.ts`: layout geometry, notes leak, reveal regression, Marp page
  count, `validation.json`. External-HTTP and FloatingVue handling become
  `diagnostics` options so this file stops reimplementing them.
- `export-pdf.ts`: print DOM, link rectangles, `pdf-lib`, click ranges.
- Libraries `check_*.py`: unchanged. A browser helper must not replace
  them.

Default navigation and selector timeout for Slidev checks should be
120000ms, which is what `check.ts` and `check_diagrams.ts` already use
for the long `goto`. The 30s default on the second `check.ts` navigation,
on `check_delivery.ts`, and on both Python scripts is an accident.

## Serving modes, and the two-mode design

What exists today:

| Mode | Entry | Process | Default port | Who prints the URL | Cleanup |
|---|---|---|---|---|---|
| Source dev | `build.ts --dev`; course `--serve` and `--dev` rewrite to this | Vite via `slidev.mjs` | 3030 | `dev.ts:59`, requested port, before ready | `SIGINT`/`SIGTERM`/`finally`, `child.kill()` |
| Packaged static, author | `build.ts --serve` after a build | `serveDirectory(dist)` | 4188 | listen callback, requested port, label "Presentation comparison" | process exit only |
| Packaged static, no rebuild | `--serve-only` | `serveDirectory(existing dist)` | 4188 | same | process exit only |
| Check / PDF | `serveDirectory(dir, 0)` | same Node server | ephemeral | usually not printed; navigation uses `127.0.0.1` | `finally`, with the leaks above |
| Student | generated `serve.py` | Python `ThreadingHTTPServer` | **4188 hardcoded** | printed before bind | interpreter exit |
| Marp preview | `build/build.ts --serve` / `-s` | marp `--server --watch` | marp-cli default | marp-cli | `execFileSync` until exit |

Two modes are enough for Slidev. Marp `--serve` stays on the Marp builder.

1. **Source development.** `serveCourseSources`. Vite, trainer notes,
   watch. Default requested port 3030. This is what `bun run serve` and
   `libraries:serve` already start.
2. **Packaged preview.** Static files of a finished build.
   - Author and CI use `serve(dir)` (the Node server).
   - Students use `python slides/serve.py`, still with no Bun and no Node.
     `delivery.ts` keeps copying that file and the "run this, then open
     the slides" instructions.

`--serve-only` is packaged preview of an existing `dist`, not a third
product. `--serve` on `slidev/build.ts` is packaged preview after a
build. Course-level `--serve` should keep meaning source development for
the current `package.json` scripts; the static preview keeps the
`slidev --serve` / `--serve-only` spelling so those flags do not change
behaviour. Do not make one flag mean both.

Port reporting, both modes:

- Bind first. Read the bound port. Then print one line
  `http://127.0.0.1:<bound>` (source mode can keep `localhost` only if
  Vite is actually on that host; the static server is `127.0.0.1`).
- Never print the requested port. `serveDirectory`'s `localhost:${port}`
  with port `0` is the bug this removes.
- Checks call `serve(dir, { port: 0 })` and pass `server.url` through.
  They do not invent a second origin string.
- Packaged preview requests 4188. If the bind fails, print the error and
  exit nonzero. Do not print `Open http://localhost:4188` first.
  `serve.py` should do the same: bind 4188, then print the URL it bound.
  Student HTML can keep naming 4188 because failure is loud rather than
  a silent move to another port.
- Source dev requests 3030 the same way: log the URL only after the
  child is accepting connections, and include the port Vite actually
  took if it ever differs.
- `--port` still overrides the request for author commands. The printed
  value is still the bound port.

Cleanup, both modes:

- `openCheck` and long-running `serve` handle `SIGINT` and `SIGTERM`.
- `close()` always runs browser close and server close.
- A parent that spawns a check kills the process group so Chrome cannot
  outlive a skipped `browser.close`, and the profile delete still has
  its five retries when the child handles the signal.
- `serve.py` needs no Chrome cleanup. It should stop on `SIGINT`
  without printing a second URL.

## Surprises

- One `puppeteer.launch` already exists. The copies are waits, logs and
  `finally` blocks, and two Python files that paste a Bun script around
  `launchBrowser`.
- `bun run serve` is Vite on 3030. `slidev --serve` is static files on
  4188. The same flag name is rewritten in `course.ts` / `libraries.ts`.
- `serveDirectory` logs `http://localhost:0` for every check and PDF
  export, while the page opens `127.0.0.1` on the real port. Only
  `check-slidev-delivery.ts` prints that real origin.
- `check.ts`, `export-pdf.ts` and `check_diagrams.ts` leak the static
  server if `launchBrowser` throws, and leak it again if `browser.close`
  throws inside `finally`. `check_delivery.ts` does not have the first leak.
- `check_delivery.ts` and `check-slidev-delivery.ts` can wait forever:
  they register `listening` only with `once`, after `listen` may already
  have fired. The other servers check `server.listening` first.
- Reduced motion is asserted in one place (`check_core.py:856`), for
  three component classes, after a media-feature emulation. Libraries
  slides and `check.ts` never emulate it. `site-test.ts` emulates it
  and does not read durations.
- Neither Python browser script sets a subprocess timeout. The delivery
  orchestrator can hang, and `child.kill()` skips the profile delete.
- `serve.py` announces port 4188 before it binds. A busy port still
  shows a URL.
- Lint launch failure is a warning and the build continues.
  `lint-slides.ts` `main` does not close the browser if a later file throws.
