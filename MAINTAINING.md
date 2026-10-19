# Maintaining this course

Build and authoring notes for whoever, human or agent, works on this courseware.
This file is deliberately kept out of the student bundle. Student-facing
documentation goes in `README.md`; do not put behind-the-scenes material there.

See also `AGENTS.md` for the writing and coding conventions, and `build/plan.md`
and `build/tasks.md` for where the conversion stands and what is left.

## Toolchain operating guide

This section is the single current operating guide for courseware commands,
configuration, outputs, development overrides, release recovery, and CI.

### Commands

Courseware commands run through the shared Presentation-Template entry point
`build/courseware.ts`, resolved by `build/toolchain.ts` (pinned in
`build/toolchain.json` or overridden by `PRESENTATION_TEMPLATE_DIR`). Every script
in `build/package.json` maps directly to this orchestration:

| Script | Invocation | Purpose & When to Use |
|---|---|---|
| `build` | `bun run course.ts` | **Canonical fundamentals build**: Renders Slidev presentation, validates slide layout and rendered frames, writes `PRG400-Python-Programming.pdf`, packages student presentation archive `build/dist/Python-Programming-slides.zip`, and records `.courseware/fundamentals/student/artifacts.json`. Use for standard local builds and CI artifact generation. Supported flags: `--exercises` (builds exercises PDF/HTML), `--marp` (builds Marp fallback), `--force` (bypass lint failure), `--skip-lint`, `--no-html`, `--range <pages>`, `--with-clicks`. |
| `serve` | `bun run course.ts --serve` | **Fundamentals dev server**: Starts native Slidev development server with hot module reload on port 3030. Use when authoring or editing canonical slides (`src/slides/`) or native additions (`src/slidev/`). |
| `lint` | `bun run course.ts --lint` | **Fundamentals slide lint**: Validates layout budgets, line heights, and margins for fundamentals slides. Gating in CI. |
| `build:marp` | `bun run course.ts --marp` | **Fundamentals Marp fallback**: Builds static Marp fallback PDF (`PRG400-Python-Programming-Marp.pdf`) and HTML (`PRG400-Python-Programming-Marp.html`), recording `.courseware/fundamentals/marp/artifacts.json`. |
| `serve:marp` | `bun run course.ts --marp --serve` | **Fundamentals Marp dev server**: Launches Marp development server via `marp-cli` with live browser reloading. |
| `slidev` | `bun run slidev.ts` | **Slidev direct passthrough**: Direct pass-through to template `slidev/build.ts` for fundamentals with arbitrary flags (e.g. `--notes` for trainer view, `--range`, `--with-clicks`). |
| `slidev:compare` | `bun run slidev.ts --compare --serve` | **Visual parity portal**: Builds both Slidev and Marp presentations and starts comparison portal server to inspect visual parity. |
| `slidev:pdf` | `bun run slidev.ts --pdf` | **Slidev PDF export**: Renders Slidev presentation directly to PDF. |
| `slidev:check` | `bun run slidev.ts --check-only` | **Slidev frame verification**: Verifies pre-rendered Slidev frames without rebuilding. |
| `slidev:dev` | `bun run slidev.ts --dev` | **Slidev authoring server**: Runs native Slidev development server watching canonical and native sources. |
| `libraries` | `bun run libraries.ts` | **Canonical libraries build**: Builds companion course deck (`libraries/`), canonical PDF (`PRG400-Python-Libraries-and-Tools.pdf`), and student slides archive (`build/dist/PRG400-Python-Libraries-and-Tools-slides.zip`), recording `.courseware/libraries/student/artifacts.json`. |
| `libraries:marp` | `bun run libraries.ts --marp` | **Libraries Marp fallback**: Builds Marp fallback PDF/HTML for libraries and copies the plain `.html` alias (`PRG400-Python-Libraries-and-Tools.html`), recording `.courseware/libraries/marp/artifacts.json`. |
| `libraries:serve` | `bun run libraries.ts --serve` | **Libraries dev server**: Starts Slidev development server for companion course on port 3030. |
| `lint:libraries` | `bun run libraries.ts --lint` | **Libraries slide lint**: Checks slide layout budgets for the libraries deck. Gating in CI. |
| `check:animations` | `uv run python check-slidev-examples.py` | **Static animation checks**: Validates slide example states, core, data structures, and provenance without launching a browser. |
| `check:delivery` | `bun run check-slidev-delivery.ts` | **End-to-end browser delivery check**: Launches headless Chrome via the shared browser module, serves packaged presentation (`.courseware/fundamentals/student/slides`) on an ephemeral port (`port: 0`), and verifies core transitions (136 forward/reverse frames, reduced motion, containment), data structures (33 states), and wheel navigation (8 boundary tests). Gating in CI. |
| `site` | `bun run site.config.ts` | **Offline exercise site build**: Builds self-contained student exercise site into `build/site/dist`. |
| `toolchain` | `bun run toolchain.ts toolchain` | **Inspect toolchain pin**: Validates and prints active template commit against `build/toolchain.json` pin. Fails if uncommitted changes exist or commits diverge without `PRESENTATION_TEMPLATE_DIR`. |
| `pin` | `bun run toolchain.ts pin` | **Re-pin toolchain**: Updates `build/toolchain.json` with a specific template commit SHA (e.g. `bun run pin -- <sha>`). |
| `verify` | `bun run toolchain.ts verify` | **Artifact verification**: Validates `artifacts.json` manifests against content rules. Fails on missing deliverables, checksum/size mismatches, dirty Git source, recorded check failures, or if student deliverables leak caches, QA logs, authoring sources, or un-waived trainer notes. Use `verify -- <deck>` for deck manifests, or `verify -- --bundle` for the student bundle. Gating in CI. |
| `test` | `bun test toolchain.test.ts` | **Toolchain tests**: Runs unit tests for local toolchain resolution and cache verification. |
| `bundle` | `bun run toolchain.ts bundle` | **Student bundle assembly**: Assembles the student distribution tree in `.courseware/bundle/` and packages archive `build/dist/Python-Programming-student.zip` from allowlist in `courseware.config.ts`. |
| `release` | `bun run toolchain.ts release` | **Release orchestration**: Plans and publishes releases. Use `--prepare` to package manifest deliverables into `.courseware/release/upload.zip` for CI, `--dry-run` to inspect planned changes without writing, or `--from <zip>` to publish an uploaded package. Refuses manifests with `toolchain.override: true`. |
| `sync-student` | `bun run toolchain.ts sync-student` | **Student repository sync**: Synchronises `SpiralTrain/Python-Programming-Student` and its GitHub mirror from a published release (`--release [tag]`) or local bundle. Supports `--mirrors-only` to retry mirror synchronization independently. |

Code and test gates:
- `uv sync`: Sync virtual environment for fundamentals.
- `uv sync --project libraries`: Sync virtual environment for libraries companion.
- `uv run ruff check .`: Gating code style and rule checker (zero findings enforced).
- `uv run python "$(bun run --cwd build toolchain.ts --path)/build/tools/check-fences.py"`: Slide code fence validator.
- `uv run python "$(bun run --cwd build toolchain.ts --path)/build/tools/check-slide-references.py"`: Exercise slide reference validator.
- `uv run python "$(bun run --cwd build toolchain.ts --path)/build/tools/make-starters.py" --check`: Starters consistency checker.
- `uv run python build/check-solutions.py`: Solution test runner, mypy validator, and transcript checker.
- `uv run python build/site/check-quiz.py`: Quiz question syntax and answer key validator.
- `uv run python -m compileall -q demos solutions libraries/demos libraries/solutions`: Byte-compilation syntax check.

### Configuration

Toolchain behaviour is governed by three files:

1. **`courseware.config.ts`** (Course root declarative configuration):
   - `decks`: Defines course decks (`fundamentals` and `libraries`).
     - `dir`: Path to deck relative to course root (defaults to `"."`).
     - `renderer`: Default rendering engine (`"slidev"` or `"marp"`). Both decks default to `"slidev"`.
     - `archive`: Target path for packaged student presentation ZIP (`build/dist/*-slides.zip`).
     - `plainMarpHtml`: If true, copies the Marp fallback HTML to `<pdfName>.html` for legacy URLs.
     - *Note*: PDF filenames are not defined in `courseware.config.ts`; each deck declares `pdfName` inside its Markdown preamble header (`src/slides/00-preamble/00-preamble.md`).
   - `bundle`: Allowlist configuration for student distribution package.
     - `archive`: Path to student distribution archive (`build/dist/Python-Programming-student.zip`).
     - `include`: Tracked folders and files shipped to students (`demos/`, `solutions/`, `exercises/`, `appendices/`, `reference/`, `libraries/`, `README.md`, `ruff.toml`, `.devcontainer`).
     - `exclude`: Authoring and build folders stripped from the bundle (`libraries/build`, `libraries/src`).
     - `generated`: Generated artifacts included in bundle (`site: "build/site/dist"`).
     - `waiveMarpHtmlNotes`: Explicit waiver (`true`) for the known issue where the Marp renderer embeds preamble trainer notes into HTML exports.
   - `release`: Configures release pointer (`pointer: "latest"`). Builds receive immutable tags `build-<short-sha>` and advance `latest`.
   - `student`: Git synchronization targets:
     - `repository`: Primary student Git repository (`ssh://git@git.feikowielsma.nl:222/SpiralTrain/Python-Programming-Student.git`).
     - `sshKeyEnv`: Secret env variable name holding deploy key (`STUDENT_REPO_SSH_KEY`).
     - `mirrors`: GitHub mirror configuration (`git@github.com:FeikoWielsma/Python-Programming-Student.git`, key `STUDENT_MIRROR_DEPLOY_KEY`).
     - `author`: Git author identity for sync commits (`Forgejo CI/CD <ci@feikowielsma.nl>`).
     - `gitignore`: Gitignore entries injected into student repository clones.
2. **`build/toolchain.json`** (Pinned toolchain definition):
   - Holds the `repository` URL and exact 40-character git `commit` SHA of `Presentation-Template`.
   - `build/toolchain.ts` reads this file, automatically clones/fetches the commit into `.courseware/toolchain/<commit>`, runs `bun install --frozen-lockfile`, and resolves template paths.
3. **`build/slidev.config.ts`** and **`libraries/build/slidev.config.ts`** (Slidev engine settings):
   - Defines presentation `title` and `accent` color.
   - `compactSlides`: Array of slide identifiers assigned compact layout instead of auto-fitting.
   - `enrichments`: Splicing map injecting native Slidev Vue components and Markdown modules from `src/slidev/` after specific canonical slides.

### Outputs

Every build executes within an isolated variant directory under `.courseware/<deck>/<variant>/`:
- **Variant directories**:
  - `student`: Canonical student Slidev build (`.courseware/<deck>/student/`).
  - `marp`: Static Marp fallback build (`.courseware/<deck>/marp/`).
  - `exercises`: Exercises build (`.courseware/<deck>/exercises/`).
  - `trainer`: Trainer build with speaker notes (`--notes`).
  - `range-<pages>`, `clicks`, `clicks-range-<pages>`: Targeted slide and click export directories.
- **Artifact Manifest (`artifacts.json`)**:
  - Written into each variant directory following schema `courseware-artifacts/1`.
  - Records: `deck`, `variant`, `audience` (`student` or `trainer`), `createdAt`, `source` Git commit and dirty status, `toolchain` commit/pin/override status, check statuses (`slidev`, `lint`), and deliverable metadata (`role`, `path`, `kind`, `size`, `sha256`).
- **Deliverables**:
  - Canonical presentation PDFs: `PRG400-Python-Programming.pdf` (fundamentals) and `PRG400-Python-Libraries-and-Tools.pdf` (libraries) at course root.
  - Exercises deliverables: `exercises/Python-Programming-Exercises.pdf` and `exercises/Python-Programming-Exercises.html`.
  - Fallback outputs: `PRG400-Python-Programming-Marp.pdf`, `PRG400-Python-Programming-Marp.html`, `PRG400-Python-Libraries-and-Tools-Marp.pdf`, `PRG400-Python-Libraries-and-Tools-Marp.html`, and alias `PRG400-Python-Libraries-and-Tools.html`.
  - Presentation ZIP archives: `build/dist/Python-Programming-slides.zip` and `build/dist/PRG400-Python-Libraries-and-Tools-slides.zip`. Packaged folder is `.courseware/<deck>/student/slides/` containing `index.html`, `serve.py`, `slidev/index.html`, and the PDF.
  - Full student distribution bundle: `build/dist/Python-Programming-student.zip` (and unpacked in `SpiralTrain/Python-Programming-Student`).
- **Which file students download**:
  - Students wanting the offline presentation viewer download `Python-Programming-slides.zip`. They extract it and run `python slides/serve.py`, opening `http://127.0.0.1:4188` (requires no Node or internet).
  - Students wanting complete course materials (demos, solutions, exercises, offline site) download `Python-Programming-student.zip` or clone the `SpiralTrain/Python-Programming-Student` repository. Public packages strictly exclude trainer notes, authoring sources, caches, and QA logs.

### Development Override

When developing shared features or fixes across `Presentation-Template` and courses:
- **Environment variable**: `PRESENTATION_TEMPLATE_DIR` points to a local `Presentation-Template` checkout or worktree.
- **Semantics**:
  - Overrides the `build/toolchain.json` pin.
  - Emits loud warnings to stderr and stdout on every run:
    `DEVELOPMENT OVERRIDE: Presentation-Template from PRESENTATION_TEMPLATE_DIR=..., not the pinned commit`
  - Records `toolchain.override: true` in every generated `artifacts.json`.
  - **Publishing safety guard**: `bun run release` strictly refuses to prepare or publish any release from a manifest with `toolchain.override: true`.
- **How to test a template change**:
  1. Check out a template branch or worktree (e.g. `C:/Git/courseWare/_worktrees/presentation-template-cli`).
  2. Set `$env:PRESENTATION_TEMPLATE_DIR="C:/Git/courseWare/_worktrees/presentation-template-cli"` (or bash `export`).
  3. Run course builds, delivery checks (`bun run check:delivery`), and manifest verifications.
- **How to re-pin**:
  1. Push and merge the template branch to `Presentation-Template` remote repository.
  2. Run: `bun run --cwd build pin -- <merged-sha>` (or specify `--repository <url>`).
  3. Unset `PRESENTATION_TEMPLATE_DIR` and run `bun run --cwd build toolchain` to verify clean fetch and status.

### Release Recovery

The release architecture is designed for idempotent execution, draft-first safety, and independent recovery:
- **Draft-first publishing sequence**:
  1. `release.ts` creates or resumes a draft release on Forgejo for immutable tag `build-<short-sha>`.
  2. Uploads only manifest-declared deliverables, validating asset names and byte sizes.
  3. Promotes the draft (`draft: false`).
  4. Stages the `latest` pointer release as a complete draft before archiving the previous `latest` release under `latest-history-<release-id>` and moving `latest`.
  5. If an upload fails midway, the existing public `latest` release and all its assets remain unchanged.
- **Retrying publishing from the same manifest**:
  - The CI `build` job packages all verified deliverables and release metadata into `.courseware/release/upload.zip` and saves it as an Actions artifact.
  - The CI `publish` job restores that exact ZIP and publishes it. If publishing fails (e.g. Forgejo API timeout), the `publish` job can be retried directly from the saved upload ZIP without rebuilding slides or re-running checks.
- **Independent student repository and mirror sync**:
  - The `sync` job runs independently from `build` and `publish`. It downloads release assets via API and pushes to the student Git repository and GitHub mirror.
  - If a network or SSH glitch occurs during sync, trigger sync independently without rebuilding via manual workflow dispatch: provide input `sync_tag: build-<short-sha>`.
  - To retry only the GitHub mirror after the primary student repository is up to date, use `bun run sync-student -- --release <tag> --mirrors-only`.
- **First real run checklist**:
  - Confirm Forgejo API draft creation, promotion (`draft: false`), asset upload/delete, and tag preservation.
  - Confirm runner environment includes Bun 1.4.1, uv, Google Chrome, and Git.
  - Verify repo secrets: `STUDENT_REPO_SSH_KEY` (deploy key on student repo) and `STUDENT_MIRROR_DEPLOY_KEY` (deploy key on GitHub mirror).
  - Perform a manual run with `dry_run: true` input via `workflow_dispatch` and inspect the planned actions report before performing any live release.

### CI Workflow

Continuous integration and automated distribution are defined in `.forgejo/workflows/release.yml`:
- **Triggers**: Push to `master`, or manual `workflow_dispatch` with inputs:
  - `dry_run`: Builds, checks, and verifies, then reports what the release would change without modifying remote state.
  - `sync_tag`: Skips build/publish and only synchronises student repositories from the specified tag.
- **Three independent jobs**:
  1. **`build`**: Runs on Docker image `git.feikowielsma.nl/feiko/courseware-ci-image:latest`.
     - Installs Bun 1.4.1 and uv.
     - Fetches pinned `Presentation-Template` using `bun run build/toolchain.ts --path`.
     - Validates lockfiles (`uv lock --check`) and compiles all Python modules (`python -m compileall`).
     - Gating checks: slide code fences, exercise slide references, starters consistency, solution tests, quiz check, and Ruff.
     - Companion course checks: `libraries` demos, solutions, outputs, data checks, native states, and fences.
     - Slide builds: fundamentals Slidev (`build -- --force`), delivery checks (`check:delivery`), Marp fallback, exercises, offline site, and libraries (Slidev, Marp, exercises).
     - Manifest verification: `verify -- fundamentals` and `verify -- libraries`.
     - Bundle assembly and verification: `bundle` and `verify -- --bundle`.
     - Packages upload archive: `release -- --prepare` creates `.courseware/release/upload.zip`.
     - Uploads `.courseware/release/upload.zip` as Actions artifact `release-${{ github.sha }}`.
  2. **`publish`**: Depends on `build`.
     - Restores artifact `release-${{ github.sha }}` into `.courseware/release`.
     - Fetches pinned template.
     - Runs `release -- --from .courseware/release/upload.zip` (with `--dry-run` if specified).
  3. **`sync`**: Depends on `publish` (or triggers if `sync_tag` is supplied).
     - Fetches pinned template.
     - Synchronises student repository and GitHub mirror via `sync-student -- --release [tag]`.

## Slidev delivery

Slidev is the default for the 13 fundamentals modules. The canonical Markdown
stays in `src/slides/`; native additions and Vue components live in `src/slidev/`
and are inserted by `build/slidev.config.ts`. The course currently has 229 source
topics, 242 Marp pages and 275 Slidev pages, including 33 native additions.
Music and photos recur in the examples, Classes uses game characters and SQLite
uses a film watchlist. The Wordle exercise spine remains separate.

```bash
bun run --cwd build build              # Slidev app, final-state PDF, public ZIP and checks
bun run --cwd build serve              # native Slidev development server on port 3030
bun run --cwd build build:marp          # named static fallback PDF and HTML
bun run --cwd build build -- --exercises
bun run --cwd build site
bun run --cwd build check:animations
bun run --cwd build check:delivery
```

An ordinary build writes `PRG400-Python-Programming.pdf`, packages the public
presentation at `.courseware/fundamentals/student/slides/` and creates
`build/dist/Python-Programming-slides.zip`. The ZIP contains the PDF and `slides/`.
From the extracted folder run `python slides/serve.py`, then open port 4188.
It needs no Node installation or internet connection. The exercise site's module
buttons lead to this presentation; hint previews still work directly from disk.
`build:marp` writes `PRG400-Python-Programming-Marp.pdf` and `.html`. Exercise and
separate `libraries/` builds retain their existing engines.

Builds run the shared `build/courseware.ts` from the Presentation-Template commit
pinned in `build/toolchain.json` (or `PRESENTATION_TEMPLATE_DIR` override),
configured by `courseware.config.ts` in the course root. See [Toolchain operating guide](#toolchain-operating-guide)
above for complete command, configuration, output, and recovery details.

For comparison and trainer exports:

```bash
bun run --cwd build slidev -- --compare --pdf --check
bun run --cwd build slidev -- --with-clicks --range 109
bun run --cwd build slidev:check
bun run --cwd build slidev -- --serve-only
```

Page numbers can change; locate a title in `.courseware/fundamentals/student/manifest.json`
before choosing an export range. Full PDFs show the final state; `--with-clicks`
exports the steps. Ordinary student builds strip speaker notes. Use a separate
`slidev --notes` build for trainers. Native development mode watches canonical
and native sources. Explicit compact layouts are listed in the course config;
there is no automatic pagination or font fitting.

Mermaid fences are rendered at build time by Pele 1.6.0 and embedded as SVG.
Slidev also supports native Mermaid fences, configuration and a custom renderer;
keeping the shared Pele path gives both engines the same diagrams and an offline
student deck. Wheel navigation uses the shared course component, with an 18px
threshold and 120ms quiet period, no fixed cooldown, and immediate reversal.

Historical migration handoffs and verification records are indexed in
[`build/notes/README.md`](build/notes/README.md).
The shared `docs/slidev.md` describes components, exports and remaining limits.

## What this repository is

PRG400 Python Programming, a SpiralTrain classroom course, laid out as
**Presentation as Code** like the sibling Advanced Python, Go, C# and TNO Python
courses. It shares its build with them through `../Presentation-Template`.

Modules 01 to 11 came from a PowerPoint deck, kept for reference as
`PRG400-Python-Programming_og.pdf` and `PRG400-Python-Programming-Exercises_og.pdf`.
The `uv` and `ruff` material inside module 01, and the two appendices,
`12-appendix-type-hinting` and `13-appendix-libraries`, are new.


## Layout

```
src/slides/00-preamble/00-preamble.md      title and logistics, carries pdfName: and language:
src/slides/NN-topic/NN-topic.md            one canonical Markdown file per module
src/slides/12-appendix-type-hinting/       appendix, the type hinting recap
src/slides/13-appendix-libraries/          appendix, datetime, json, re, sys.argv, pytest
src/exercises/NN-topic.md                  one exercise guide per module, ::: markup
demos/<same name as the slide module>/     runnable demo code, files named NN_name.py
solutions/NN-<exercise stem>/              the Wordle game at the end of each exercise
exercises/handouts/NN-<exercise stem>/     what an exercise hands out (data, word lists)
exercises/starters/NN-<exercise stem>/     GENERATED : previous solution + handouts
archive/                                   retired material, not built, linted or shipped
../Presentation-Template/build/tools/make-starters.py regenerates the starters; --check in CI
build/solution-tests/NN-<exercise stem>/   reference tests run by CI against solutions 05 to 12
build/check-solutions.py                   tests (from build/solution-tests/ and stage 13), mypy and a scripted game per stage
build/transcripts/                         the expected output of those scripted games
build/site.config.ts                       the offline exercise site (shared builder)
appendices/                                appendix decks the exercises point at
reference/                                 background reading, shipped to students
build/package.json                         thin wrapper over the shared template build
../Presentation-Template/build/tools/check-fences.py shared fence check, gating in CI
build/plan.md, build/tasks.md              working notes
build/orchestration.md                     the multi-agent rework log, October 2026
```

**The exercises are one continuous project**, a Wordle game, from Exercise 2 to
Exercise 13. `build/plan.md` sections 2 and 4 are the design. Three rules keep it
coherent :

- A solution stage is a complete uv project and is the next exercise's starter.
  Change a solution, then run `uv run python ../Presentation-Template/build/tools/make-starters.py` and commit
  the regenerated starters; never edit a starter by hand.
- Exercise text quotes the solutions verbatim and shows only output produced by
  running them. `WORDLE_SECRET=crane` fixes the secret for a reproducible game.
- Function, module and class names are a contract between the text, the
  solutions, the tests and the starters. Rename across all or not at all.

Exercise guides use the shared markup documented in
`../Presentation-Template/docs/exercise-site.md` : `:::hint`, `:::output`,
`:::solution`, italic slide references. The template's `{\u2605}` step markers are
deliberately not used in this course. The same source
builds the exercises PDF and the offline site (`bun run --cwd build site`).

The toolchain material, `uv` and `ruff` and the editor, sits inside module 01. It
spent a while as a separate `00a-python-tooling` module, which worked but meant two
modules explained how to install Python and disagreed about it. Installing and
running Python is what an introduction is for.

Type hints are introduced as the course goes: variables in module 02, collections
in module 03, signatures in module 05, constructors in module 11. The appendix
`12-appendix-type-hinting` is the recap. It was drafted twice before that, first
inside the chapter 0 toolchain module and then as a standalone module 12 at the
end; both read worse than teaching it in context.


## Building

First time on a machine :

```bash
bun run --cwd build toolchain               # fetches pinned Presentation-Template & installs deps
bunx puppeteer browsers install chrome      # the delivery check and lint height check need it
uv sync                                     # ruff and mypy for the code checks
uv sync --project libraries                 # dependencies for the companion course
```

Then, from this course root :

```bash
bun run --cwd build build                  # animated slides, PDF and student ZIP
bun run --cwd build build -- --exercises   # exercises PDF and HTML
bun run --cwd build serve                  # native Slidev development server
bun run --cwd build lint                   # style and layout linter
```

The ordinary build validates the rendered Slidev frames and runs the canonical
slide linter. `bun run --cwd build lint` also checks the Marp fallback layout.
Diagram checks inspect the rendered Pele SVG rather than placeholders. See the
[Toolchain operating guide](#toolchain-operating-guide) above for all available scripts.

## Checking the code

```bash
TEMPLATE="$(bun run --cwd build toolchain.ts --path)"
uv run python "$TEMPLATE/build/tools/check-fences.py"           # gating in CI
uv run python "$TEMPLATE/build/tools/check-slide-references.py"  # gating in CI
uv run ruff check .                                           # gating in CI, see below
uv run python "$TEMPLATE/build/tools/make-starters.py" --check  # gating in CI
uv run python build/check-solutions.py                        # gating in CI
uv run python -m compileall -q demos solutions libraries/demos libraries/solutions
```

`ruff` is configured in `ruff.toml`, not in `pyproject.toml`, because the student
bundle ships `ruff.toml` and deliberately ships no `pyproject.toml`. Its relative
paths are written to resolve in the bundle as well as here.

`uv run ruff check .` is at **zero findings** and should stay there. Every entry
in `[lint.per-file-ignores]` names the lesson it protects, so before silencing a
new finding, check whether the code is teaching the pattern deliberately. If it
is, add a scoped entry with the reason; if it is not, fix the code.

The scope excludes `archive/` and `reference/`. Retired demo folders live in
`archive/`, not beside the live ones.

## Releasing

`.forgejo/workflows/release.yml` runs on every push to `master`. See the
[Release recovery](#release-recovery) and [CI workflow](#ci-workflow) subsections
in the Toolchain operating guide above.

The student distribution bundle is an **allowlist** configured in `courseware.config.ts`,
not a copy-then-prune: naming what goes in means a folder added later cannot leak into
a student's clone. When you add a module, add its demo folder to `bundle.include` in
`courseware.config.ts`. Python `compileall` in CI recursively covers all code under
`demos/`, `solutions/`, and `libraries/`.

The push to the student repository and GitHub mirror authenticates via secrets
`STUDENT_REPO_SSH_KEY` and `STUDENT_MIRROR_DEPLOY_KEY`. The step skips cleanly if
the secrets are absent.

## House style for the code

All code in the course, on the slides and in the demos, exercises and solutions,
is PEP 8 named and Pythonic. The material inherited camelCase names, trailing
bare `return` statements and CapWords modules from its PowerPoint days; those are
gone and should not come back. Where an unpythonic form is the lesson, keep it and
say so in a comment and in `ruff.toml`.

Type annotations are introduced as the course goes rather than saved for the end,
so demo code reads like real code. A demo and the slide fence that quotes it must
carry the same annotations.


## The reference tree

`reference/` is the background material that ships with the course. It is meant
to feel generous, so keep it that way, but keep it **current**: the point of the
tree is that everything in it is worth a student's time. It replaced a pile that
included the Python 3.5 documentation, a Python 2.7 installer and a copy of
Dive Into Python written against Python 2.3.

`reference/python-docs/` is a curated subset of the official documentation from
`docs.python.org/3/archives/`. When Python moves on, replace it wholesale rather
than adding a second copy :

```bash
curl -LO https://docs.python.org/3/archives/python-3.NN-docs-pdf-a4.tar.bz2
```

Keep the tutorial, library, reference, using, faq and whatsnew PDFs plus the
howtos a fundamentals student might open. Leave out the C API, the extending
and embedding guides and the porting notes.


## Known rough edges

- `demos/*/extra/` folders still ship. They hold older side examples that no
  slide references, kept on purpose as extra practice material (ported to
  Python 3 and held to the ruff rules).


## Optional libraries and tools

`libraries/` imports the teaching sources from Python-Day4-Tour and is maintained
here. The original repository is unchanged. Its own `src/`, `demos/`, `solutions/`
and `data/` preserve the relative paths the examples use. Its dependencies and
lockfile stay separate from the standard-library fundamentals project. Books from
the old repository are not part of this import.

```bash
bun run --cwd build libraries -- --skip-lint
bun run --cwd build libraries:marp -- --skip-lint
bun run --cwd build libraries:serve
# Build both engines and a comparison portal:
bun run --cwd build libraries -- --skip-lint --compare
bun run --cwd build lint:libraries
bun run --cwd build libraries -- --exercises
uv sync --project libraries
uv run ruff check libraries
uv run --project libraries python libraries/build/check-demos.py
uv run --project libraries python libraries/build/check-solutions.py
uv run --project libraries python libraries/build/check-outputs.py
uv run --project libraries python libraries/build/make-data.py --check
uv run --project libraries python libraries/build/native_states.py --check
# Run from libraries/ to audit its slides and handouts with the shared checker:
cd libraries
uv run python "$(bun run --cwd ../build toolchain.ts --path)/build/tools/check-fences.py"
```

`build/libraries.ts` runs the shared `courseware.ts` for the `libraries` deck, which
builds with `libraries/` as its working directory. Slidev is the default, with its configuration in
`libraries/build/slidev.config.ts`; `libraries:serve` starts native authoring on
port 3030. `libraries:marp` retains named `-Marp.pdf` and `-Marp.html` fallbacks
and copies the legacy standalone HTML alias. `--exercises` keeps the existing
exercise builder. Add new optional topics there; they do not enter the
fundamentals PDF, schedule, exercise site or Wordle exercise chain. CI builds and
publishes the Slidev PDF, Marp PDF/HTML, exercises PDF/HTML and
`build/dist/PRG400-Python-Libraries-and-Tools-slides.zip`. It ships the public
presentation as `libraries/slides/` in the student bundle, stripping the optional
`src/` and `build/` directories. The slides ZIP contains the PDF and `slides/`,
with no comparison or trainer sources. Keep optional demo code linted by
`libraries/ruff.toml`. Each course launcher uses port 4188; stop the fundamentals
launcher before starting the libraries launcher, or vice versa.

The example checks use temporary course copies, compile the six interactive
GUI demos, and run the remaining demos and solutions with a Python socket audit
guard and a per-command timeout. Raw stdout, stderr and statuses are written to
the ignored `libraries/build/demo-baseline/`. Quoted stdout is compared as an
ordered excerpt with whitespace ignored; annotated reference fences and recorded
benchmark timings are classified explicitly. Scraping uses the supplied first-page
fixture by default; `--live` opts into the real site and optional second page.
The migration baseline and findings are in `build/notes/libraries-review.md`.

Music metadata and photo attribution are recorded in `libraries/data/SOURCES.md`.
Rebuild the data with `make-data.py` without `--check`; it also regenerates the
report files. Rebuild native slide states with `native_states.py` without
`--check` after changing their demo excerpts. Both checks gate CI. The rewrite
and verification record is `build/notes/libraries-slidev-phase2.md`.
