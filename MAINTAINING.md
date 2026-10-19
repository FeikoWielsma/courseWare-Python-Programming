# Maintaining PRG400

Use [AGENTS.md](AGENTS.md) for course rules and
[build/notes](build/notes/README.md) for historical evidence and content reviews.
The [shared configured-course guide](../Presentation-Template/docs/courseware.md)
covers pinned toolchains, shared commands, manifests, overrides, bundling and
release. This file records the PRG400-specific command and configuration details.

## Course commands

First use: install Bun and uv, run `bun run --cwd build toolchain`, then sync
both uv projects using the checks below. Rendering needs Chrome; use the
machine's `CHROME_PATH` or install Puppeteer's browser with
`bunx puppeteer browsers install chrome`.

The authoritative scripts are in `build/package.json`. Run them from the course
root with `--cwd build`:

```powershell
bun run --cwd build build
bun run --cwd build lint
bun run --cwd build build -- --exercises
bun run --cwd build libraries
bun run --cwd build site
bun run --cwd build verify -- fundamentals
bun run --cwd build verify -- libraries
```

`build` renders the fundamentals Slidev deck; `libraries` renders the companion
deck. `site` builds a fresh fundamentals Marp fallback, then assembles the
portable exercise site and embeds the Marp HTML. The site build owns this
prerequisite, so CI does not schedule another fundamentals Marp build. Run
`bun run --cwd build` to inspect all current scripts and flags.

## Checks

```powershell
uv sync
uv sync --project libraries
uv run ruff check .
uv run python build/check-solutions.py
uv run python build/site/check-quiz.py
$template = bun run build/toolchain.ts --path
uv run python "$template/build/tools/check-fences.py"
uv run python "$template/build/tools/check-slide-references.py"
uv run python "$template/build/tools/make-starters.py" --check
```

`build/ci-build.sh` runs the full CI groups, including demo and library checks,
Slidev delivery, site assembly and artifact verification.

## Course configuration

`courseware.config.ts` declares the `fundamentals` and `libraries` decks, their
renderer, slide archive and `marpOutput` path. It also owns the student bundle
allowlist, generated site files, release pointer and student repository targets.
Add a new demo directory to `bundle.include` when needed. The student bundle is
an allowlist and includes Marp outputs through their artifact manifests.

Both Slidev development servers use `.courseware/<deck>/authoring/`. Build
variants and their `artifacts.json` manifests live in
`.courseware/<deck>/<variant>/`. Marp fallback PDFs and HTML use the paths set by
each deck's `marpOutput` configuration. Keep these locations in course config;
shared renderer behavior belongs in Presentation-Template.

## Release

`.forgejo/workflows/release.yml` defines push and manual release jobs. Inspect it
when changing triggers or required secret names. Use its dry-run input to inspect
a release plan. `build/toolchain.json` pins Presentation-Template; use
`PRESENTATION_TEMPLATE_DIR` only for local cross-repository development. Builds
using that override are marked in their manifests and cannot be released. After a
shared change is merged, update the pin with `bun run build/toolchain.ts pin -- <commit>`.

## Delivery limits

The Slidev presentation needs its local launcher; the exercise site opens from
disk. Its embedded deck uses Marp for that portability. Some Slidev PDF headers
remain cropped; the existing evidence and scope are in the
[introduction review](build/notes/gentler-introduction.md). Keep this limitation
visible until a rendered export demonstrates the fix.

The bundle currently waives trainer-note findings in the standalone Marp HTML;
the embedded site copy removes those notes. The waiver is explicit in
`courseware.config.ts` and remains separate from this toolchain migration.
