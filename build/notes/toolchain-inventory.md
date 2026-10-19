# Courseware Toolchain Inventory

Comprehensive inventory of commands, CI workflows, deliverables, shared template
consumers, duplicated orchestration logic, and build directory contents for the
Python courseware toolchain.

---

## 1. Commands & Procedures

### 1.1 Package.json Scripts (`build/package.json`)

All commands run from `build/` (or from course root via `bun run --cwd build <script>`).

|| Script Name | Command Executed | Handling Script & Lines | Accepted & Handled Flags | Purpose |
|---|---|---|---|---|
| `build` | `bun run course.ts` | `build/course.ts:44-63` | `--force`, `--skip-lint`, `--no-html`, `--out <file>`, `--slides-dir <dir>`, `--range <p>`, `--with-clicks`, `--prepare`, `--check-only`, `--serve-only` | Primary Slidev deck build: exports PDF, checks delivery, runs linter, and packages student presentation zip. |
| `serve` | `bun run course.ts --serve` | `build/course.ts:42-43` -> `slidev/build.ts:47-50` | `--slides-dir <dir>`, `--port <port>` | Launches native Slidev live development server on port 3030 (or `--port`). |
| `build:marp` | `bun run course.ts --marp` | `build/course.ts:33-41` -> `build.ts:35-50` | `--force`, `--skip-lint`, `--no-html`, `--slides-dir <dir>`, `--out <file>` | Builds fallback Marp PDF (`PYG400-Python-Programming-Marp.pdf`) and copies `build/dist/combined.html` to Marp HTML. |
| `serve:marp` | `bun run course.ts --marp --serve` | `build/course.ts:33-41` -> `build.ts:35` | `--slides-dir <dir>` | Runs Marp presentation live development server. |
| `slidev` | `bun run slidev.ts` | `build/slidev.ts:10-11` -> `slidev/build.ts:35-101` | Passthrough: all flags accepted by `slidev/build.ts` | Direct low-level entry point to Slidev build engine. |
| `slidev:dev` | `bun run slidev.ts --dev` | `build/slidev.ts:10` -> `slidev/build.ts:47` | `--slides-dir <dir>`, `--port <port>` | Runs Slidev development server directly. |
| `slidev:pdf` | `bun run slidev.ts --pdf` | `build/slidev.ts:10` -> `slidev/build.ts:77` | `--range <p>`, `--with-clicks`, `--slides-dir <dir>` | Exports Slidev PDF without full course wrapper packaging. |
| `slidev:check` | `bun run slidev.ts --check-only` | `build/slidev.ts:10` -> `slidev/build.ts:41` | None | Verifies existing Slidev build output in `build/slidev/dist`. |
| `slidev:compare` | `bun run slidev.ts --compare --serve` | `build/slidev.ts:10` -> `slidev/build.ts:61,100` | `--port <port>` | Builds both Slidev and Marp versions, builds side-by-side portal, and serves on port 4188. |
| `check:animations` | `uv run python check-slidev-examples.py` | `build/check-slidev-examples.py` | None | Validates animated slide snippets, data structures, and state transitions. |
| `check:delivery` | `bun run check-slidev-delivery.ts` | `build/check-slidev-delivery.ts` | None | Checks student presentation bundle structure, serve.py launcher, offline navigation, and license texts. |
| `lint` | `bun run ../../Presentation-Template/build/lint-slides.ts` | `Presentation-Template/build/lint-slides.ts:453-485` | `--verbose` zp/ `-v`, `--fix`, `--slides-dir <dir>`, positional `.md` paths | Runs Puppeteer dynamic overflow linter, title length check, and house-style rules on slide markdown. |
| `site` | `bun run site.config.ts` | `build/site.config.ts:40-41` -> `build-site.ts:60-63` | `--file <path>`, `--out <dir>` | Builds static offline exercise site with quiz, hints, revealable solutions, and Wordle game. |
| `libraries` | `bun run libraries.ts` | `build/libraries.ts:50-73` | Same as `course.ts`: `--force`, `--skip-lint`, `--no-html`, `--out <file>`, `--slides-dir <dir>`, etc. | Builds optional Libraries Slidev deck, checks delivery, exports PDF, and packages libraries slides zip. |
| `libraries:marp` | `bun run libraries.ts --marp` | `build/libraries.ts:36-47` -> `build.ts:35-50` | `--force`, `--skip-lint`, `--no-html`, `--slides-dir <dir>`, `--out <file>` | Builds Libraries Marp fallback PDF and HTML (including standalone HTML alias). |
| `libraries:serve` | `bun run libraries.ts --serve` | `build/libraries.ts:48-49` -> ``slidev/build.ts:47-50` | `--slides-dir <dir>`, `--port <port>` | Serves Libraries Slidev deck on port 3030. |
| `lint:libraries` | `bun run libraries.ts --lint` | `build/libraries.ts:34-35` -> `lint-slides.ts:453` | Any `lint-slides.ts` flags (`--verbose`, `--fix`, etc.) | Runs slide linter on `libraries/src/slides`. |

### 1.2 Forgejo CI Workflow Steps (`.forgejo/workflows/release.yml`)

The workflow triggers on `push` to `master` and `workflow_dispatch` (lines 3-8). It runs in container `git.feikowielsma.nl/feiko/courseware-ci-image:latest` on runner `docker-build` (lines 21-24).

Global Environment Variables (lines 12-18):
- `SLIDES_PDF: PRG400-Python-Programming.pdf`
- `MARP_PDF: PRG400-Python-Programming-Marp.pdf`
- `MARP_HTML: PRG400-Python-Programming-Marp.html`
- `EXERCISES_PDF: PRG400-Python-Programming-Exercises.pdf`
- `EXERCISES_HTML: PRG400-Python-Programming-Exercises.html`

| Step Name | Lines | Inputs / Trigger | Action Performed | Outputs / Artifacts | Env Vars & Secrets Referenced |
|---|---|---|---|---|---|
| Checkout | 26-27 | Repository commit | Clones native course repository via `actions/checkout@4` | Workspace checkout | None |
| Install uv | 33-37 | Shell script | Downloads and installs `uv` binary via `astral.sh/uv/install.sh`, adds `$home/.local/bin` to `GITHUB_PATH` | `uv` in `PATHp | `GITHUB_PATH` |
| Check the lockfile is current | 41-44 | `pyproject.toml`, `uv.lock`, libraries counterparts | Runs `uv lock --check` and `uv lock --check --project libraries` | Verified lockfiles | None |
| Install the project | 46-48 | `uv.lock` | Runs `uv sync --frozen` | Course virtualenv | None |
| Check the Python compiles | 52-73 | Demo and solution source trees | Runs `uv run python -m compileall -q` across 13 demo dirs, `solutions/`, `libraries/demos/`, and `libraries/solutions/` | Compilation verification | None |
| Checkout Presentation Template | 75-78 | `GITHUB_SERVER_URL` | Shallow-clones `SpiralTrain/Presentation-Template.git` into sibling directory `../Presentation-Template` | Sibling template repo | `GITHUB_SERVER_URL` |
| Check the slide code fences | 85-86 | Slides and handouts | Runs `uv run python ../Presentation-Template/build/tools/check-fences.py` | Verified slide fences | None |
| Check exercise slide references | 88-89 | Slides and exercises | Runs `uv run python ../Presentation-Template/build/tools/check-slide-references.py` | Verified slide references | None |
| Check the exercise starters are current | 95-96 | Exercise starters and solutions | Runs `uv run python ../Presentation-Template/build/tools/make-starters.py --check` | Verified starter sync | None |
| Check the exercise solutions | 101-102 | Solutions & test suite | Runs `uv run python build/check-solutions.py` (runs pytest on Wordle stages and transcript checks) | Verified solution code | None |
| Check the quiz | 107-108 | `build/site/quiz.jsonx | Runs `uv run python build/site/check-quiz.py` | Verified quiz answers | None |
| Check the style | 114-115 | Course Python code | Runs `uv run ruff check .` scoped by `ruff.toml` | Verified style | None |
| Check optional libraries examples | 117-129 | `libraries/` sources | Runs `uv sync --project libraries --frozen`, checks data via `make-data.py --check`, demos, solutions, outputs, native states (`native_states.py --check`), and fences | Verified libraries suite | None |
| Install Bun 1.4 for Slidev | 133-138 | `bun.sh` installer | Installs Bun v1.4.1 needed for v2 lockfile format | Bun 1.4 binary | None |
| Install template dependencies | 140-149 | `Presentation-Template` | Verifies `delivery.ts` exists; runs `bun install --frozen-lockfile` in template `build/` and `build/slidev/` | Installed node_modules in template | None |
| Build slides and exercises | 151-167 | Course sources, template | Executes sequential builds: animations check, slidev build (`build -- --force`), delivery check, Marp build (`build:marp -- --force`), exercises (`build -- --exercises --force`), site (`bun run site`), libraries build (`libraries -- --skip-lint --force`), libraries Marp, lint libraries, and libraries exercises | All PDFs, HTMLs, site, and slide zips | `PRESENTATION_TEMPLATE_DIR`, `CHROME_PATH`, `MARP_EXTRA_ARGS` |
| Assemble student bundle | 169-236 | Generated PDFs, HTMLs, site, slidev student outputs, demo dirs, solutions | Populates `/tmp/student-bundle` using allowlist: slides app, 5 root documents, site dist, solutions, exercises, appendices, reference, libraries (with `build/` and `src/` stripped), `README.md`, `ruff.toml`, `.devcontainer`. Prunes OS/tool caches | `/tmp/student-bundle` | `SLIDES_PDF , `MARP_PDF , `MARP_HTML`, `EXERCISES_PDF , `EXERCISES_HTML` |
| Package student zip | 238-245 | `/tmp/student-bundle` | Zips `/tmp/student-bundle` into `build/dist/Python-Programming-student.zip` | `build/dist/Python-Programming-student.zip` | None |
| Publish latest release | 247-295 | Built assets, git SHA | Deletes previous `latest` release & tag in Forgejo API, creates fresh `latest` release pointing at `GITHUB_SHA`, uploads 5 root PDFs/HTMLs, libraries PDFs/HTMLs, and all `*.zip` in `build/dist` | Published Forgejo release `latest` | `GITHUB_TOKEF` (secret), `GITHUB_SERVER_URL`, `GITHUB_REPOSITORY`, `GITHUB_SHA` |
| Push to student repository | 297-353 | `/tmp/student-bundle` | Clones `SpiralTrain/Python-Programming-Student.git` via SSH, replaces contents, generates student `.gitignore`, commits and pushes to `main` | Updated student repository | `STUDENT_REPO_SSH_KEY` (secret) |
| Mirror student repository to GitHub | 355-373 | Student repository clone | Pushes `/tmp/Python-Programming-Student` via SSH deploy key to `git@github.com:FeikoWielsma/Python-Programming-Student.git` | Synced GitHub mirror | `STUDENT_MIRROR_DEPLOY_KEY` (secret) |

### 1.3 Maintaining.md Procedures

Procedures documented in `MAINTAINING.md` for human operators:

| Procedure / Task | Lines | Exact Commands Run | Notes & Preconditions |
|---|---|---|---|
| Initial environment setup | 40-44 | `bun install --cwd ../Presentation-Template/build`<br>`bunx puppeteer browsers install chrome`<br>`uv sync` | Installs template node dependencies, Puppeteer Chrome browser for overflow checking, and Python virtualenv. |
| Normal course build | 48 | `bun run --cwd build build` | Builds animated slides, Slidev PDF, checks delivery, and generates student slides zip. |
| Exercises build | 49 | `bun run --cwd build build -- --exercises` | Assembles exercise guides, solutions, and generates exercises PDE and HTML. |
| Slidev dev server | 50 | `bun run --cwd build serve` | Native Slidev authoring server on port 3030. |
| Slide linter | 51 | `bun run --cwd build lint` | Checks slide layout, heights, title lengths, and Marp fallback layout. |
| Code quality checks | 59-65 | `uv run python ../Presentation-Template/build/tools/check-fences.py`<br>`uv run python ../Presentation-Template/build/tools/check-slide-references.py`<br>`uv run ruff check .`<br>`uv run python ../Presentation-Template/build/tools/make-starters.py --check`<br>`uv run python build/check-solutions.py`<br>`uv run python -m compileall -q demos/01-pythonintro ... solutions` | Pre-commit gating checks matching CI. Zero findings required for ruff. |
| Reference tree maintenance | 114 | `curl -LO https://docs.python.org/3/archives/python-3.NN-docs-pdf-a4.tar.bz2` | Downloads official Python documentation archives to curate `reference/python-docs/`. |
| Libraries Slidev build | 137 | `bun run --cwd build libraries -- --skip-lint` | Builds optional libraries Slidev deck and packages slides zip. |
| Libraries Marp fallback | 138 | `bun run --cwd build libraries:marp -- --skip-lint` | Generates `-Marp.pdf`, `-Marp.html`, and legacy `.html` alias. |
| Libraries dev server | 139 | `bun run --cwd build libraries:serve` | Starts libraries authoring server on port 3030. |
| Libraries comparison portal | 141 | `bun run --cwd build libraries -- --skip-lint --compare` | Builds both engines and comparison portal. |
| Libraries linter | 142 | `bun run --cwd build lint:libraries` | Runs linter against `libraries/src/slides`. |
| Libraries exercises build | 143 | `bun run --cwd build libraries -- --exercises` | Builds libraries exercises PDF and HTML. |
| Libraries Python checks | 144-152 | `uv sync --project libraries`<br>`uv run ruff check libraries`<br>`uv run --project libraries python libraries/build/check-demos.py`<br>`uv run --project libraries python libraries/build/check-solutions.py`<br>`uv run --project libraries python libraries/build/check-outputs.py`<br>`uv run --project libraries python libraries/build/make-data.py --check@<br>`uv run --project libraries python libraries/build/native_states.py --check`<br>`cd libraries && uv run python ../../Presentation-Template/build/tools/check-fences.py` | Full validation suite for optional topics. |

---

## 2. Deliverables Inventory

Every deliverable produced by the toolchain, its creation origin, consumption path, staging location, and user-facing filenames:

| Deliverable Name | File / Directory Produced | Creating Script / Step | Consuming Script / Step | Download Filename (Student / Trainer) |
|---|---|---|---|---|
| Main Slidev Presentation PDF | `PRG400-Python-Programming.pdf` (copied from `build/slidev/dist/course-slidev.pdf`) | `build/course.ts:58-60` (`bun run build -- --force`) | `delivery.ts:packageStudentPresentation` (line 21); `.forgejo/workflows/release.yml:184` (copied to student bundle); line 277 (uploaded to release) | `PRG400-Python-Programming.pdf` |
| Main Slidev Presentation App | `build/slidev/dist/student/` (`slidev/`, `licenses/`, `serve.py`, `index.html`, `README.txt`) | `Presentation-Template/build/slidev/delivery.ts:6-27` | `.forgejo/workflows/release.yml:182` (copied to student bundle as `${BUNDLE}/slides`); zipped by `package.py` | Bundled in zips and student git repo |
| Main Slidev Slides Archive | `build/dist/Python-Programming-slides.zip` | `Presentation-Template/build/slidev/delivery.ts:25` (`package.py`) | `.forgejo/workflows/release.yml:287` (uploaded to release assets) | `Python-Programming-slides.zip` |
| Main Marp Fallback PDF | `PRG400-Python-Programming-Marp.pdf` | `build/course.ts:33-41` -> `build.ts` (`bun run build:marp -- --force`) | `.forgejo/workflows/release.yml:184` (copied to bundle); line 277 (uploaded to release) | `PYG400-Python-Programming-Marp.pdf` |
| Main Marp Fallback HTML | `PRG400-Python-Programming-Marp.html` | `build/course.ts:38-40` (copied from `build/dist/combined.html`) | `.forgejo/workflows/release.yml:184` (copied to bundle); line 277 (uploaded to release) | `PRG400-Python-Programming-Marp.html` |
| Main Exercises PDF | `PRG400-Python-Programming-Exercises.pdf` | `build/course.ts:33-37` -> `build.ts --exercises` -> `src/exercises.ts:89` | `.forgejo/workflows/release.yml:184` (copied to bundle); line 277 (uploaded to release) | `PYG400-Python-Programming-Exercises.pdf` |
| Main Exercises HTML | `PYG400-Python-Programming-Exercises.html` | `Presentation-Template/build/src/exercises.ts:98` | `.forgejo/workflows/release.yml:184` (copied to bundle); line 277 (uploaded to release) | `PRG400-Python-Programming-Exercises.html` |
| Exercise Site | `build/site/dist/` (`index.html`, exercise pages, quiz, assets, presentation dialog) | `build/site.config.ts` -> `build-site.ts` (`bun run site`) | `.forgejo/workflows/release.yml:213` (copied to `${BUNDLE}/site`) | Distributed in student bundle / zip (`site/index.html`) |
| Libraries Slidev Presentation PDF | `libraries/PRG400-Python-Libraries-and-Tools.pdf` (from `libraries/build/slidev/dist/course-slidev.pdf`) | `build/libraries.ts:68-70` (`bun run libraries -- --skip-lint --force`) | `delivery.ts:packageStudentPresentation`; `.forgejo/workflows/release.yml:277Z (uploaded to release) | `PRG400-Python-Libraries-and-Tools.pdf` |
| Libraries Slidev Presentation App | `libraries/build/slidev/dist/student/` | `Presentation-Template/build/slidev/delivery.ts:6-27` | `.forgejo/workflows/release.yml:223` (copied to `${BUNDLE}/libraries/slides`); zipped by `package.py` | Bundled in student repo as `libraries/slides/` |
| Libraries Slidev Slides Archive | `build/dist/PYG400-Python-Libraries-and-Tools-slides.zip` | `Presentation-Template/build/slidev/delivery.ts:25` (`package.py`) | `.forgejo/workflows/release.yml:287Z (uploaded to release assets) | `PYG400-Python-Libraries-and-Tools-slides.zip` |
| Libraries Marp Fallback PDF | libraries/PRG400-Python-Libraries-and-Tools-Marp.pdf` | `build/libraries.ts:36-47` -> `build.ts` | `.forgejo/workflows/release.yml:277Z (uploaded to release) | `PRG400-Python-Libraries-and-Tools-Marp.pdf` |
| Libraries Marp Fallback HTML | `libraries/PYG400-Python-Libraries-and-Tools-Marp.html` & `libraries/PRG400-Python-Libraries-and-Tools.html` | `build/libraries.ts:42-45` (copied from `libraries/build/dist/combined.html`) | `.forgejo/workflows/release.yml:277Z (uploaded to release) | `PRG400-Python-Libraries-and-Tools-Marp.html` & `PRG400-Python-Libraries-and-Tools.html` |
| Libraries Exercises PDF | `libraries/PYG400-Python-Libraries-and-Tools-Exercises.pdf` | `build/libraries.ts:36-40` -> `build.ts --exercises` | `.forgejo/workflows/release.yml:277` (uploaded to release) | `PYG400-Python-Libraries-and-Tools-Exercises.pdf` |
| Libraries Exercises HTML | libraries/PRG400-Python-Libraries-and-Tools-Exercises.html` | `Presentation-Template/build/src/exercises.ts:98` | `.forgejo/workflows/release.yml:277Z (uploaded to release) | `PRG400-Python-Libraries-and-Tools-Exercises.html` |
| Full Student Bundle Archive | `build/dist/Python-Programming-student.zip` | `.forgejo/workflows/release.yml:238-245` (`zip -rq`) | `.forgejo/workflows/release.yml:287` (uploaded to release assets) | `Python-Programming-student.zip` |
| Full Student Git Repository | Forgejo `SpiralTrain/Python-Programming-Student` (`main`) | `.forgejo/workflows/release.yml:297-353` | Direct student / trainer clone | Git clone (`main` branch) |
| GitHub Student Mirror | GitHub `FeikoWielsma/Python-Programming-Student` (`main`) | `.forgejo/workflows/release.yml:355-373` | GitHub Codespaces / online students | GitHub clone / Codespace |

---

## 3. Consumers of the Shared Template Across CourseWare

Perspective on the whole courseware suite: 48 course repositories were surveyed under `C:/Git/courseWare`. Exactly 22 contain `build/package.jsong` scripts interfacing with Presentation-Template.

### 3.1 Template Invocations & CLI Flags Per Course

| Course Repository | Template Invocations (from `build/package.jsong`, scripts, workflows) | CLI Flags Actually Used | Uses Slidev? |
|---|---|---|---|
| **Python-Programming** | `build/course.ts`, `build/libraries.ts`, `build/slidev.ts`, `build/site.config.ts`, `lint-slides.ts`, `tools/check-fences.py`, `tools/check-slide-references.py`, `tools/make-starters.py` | `--marp`, `--serve`, `--dev`, `--compare`, `--pdf`, `--check-only`, `--check`, `--force`, `--skip-lint`, `--no-html`, `--exercises`, `--lint`, `--range`, `--with-clicks`, `--slides-dir`, `--out`, `--notes` | **YES** (Only consumer of Slidev) |
| **Advanced-Python** | `build.ts`, `lint-slides.ts` | `--serve`, `--force`, `--exercises` | No (Marp only) |
| **Agentic-AI-LangChain** | `build.ts`, `lint-slides.ts` | `--serve`, `--force`, `--exercises` | No (Marp only) |
| **App-Development-with-Cursor** | `build.ts`, `lint-slides.ts` | `--serve` | No (Marp only) |
| **App-Development-with-Cursor-diagrams** | `build.ts`, `lint-slides.ts` | `--serve` | No (Marp only) |
| **courseBuildingAIAgents** | `build.ts`, `lint-slides.ts` | `--serve` | No (Marp only) |
| **Csharp-Programming** | `build.ts`, `lint-slides.ts` | `--serve`, `--force`, `--exercises` | No (Marp only) |
| **GitLab-CI-CD** | `build.ts`, `lint-slides.ts`, `build/build-supplementary.ts` | `--serve`, `--force`, `--exercises` | No (Marp only) |
| **Go-Programming** | `build.ts`, `lint-slides.ts` | `--serve`, `--force`, `--exercises` | No (Marp only) |
| **Multi-Agents-LangGraph** | `build.ts`, `lint-slides.ts` | `--serve`, `--force`, `--exercises` | No (Marp only) |
| **Open Source AI** | `build.ts`, `lint-slides.ts` | `--serve`, `--force`, `--exercises` | No (Marp only) |
| **PowerBI** | `build.ts`, `lint-slides.ts` | `--serve` | No (Marp only) |
| **PowerShell-Scripting** | `build.ts`, `lint-slides.ts` | `--serve`, `--force`, `--exercises` | No (Marp only) |
| **PySpark** | `build/build-achmea.ts` -> `build.ts`, `lint-slides.ts`, `site/build-site.ts` | `--part <1>2`, `--lint`, `--serve`, `--no-exercises`, `--exercises`, `--force`, `--slides-dir` | No (Marp only) |
| **Python-Data-Analysis** | `build.ts`, `lint-slides.ts` | `--serve`, `--force`, `--exercises` | No (Marp only) |
| **Python-Day4-Tour** | `build.ts`, `lint-slides.ts` | `--serve`, `--force`, `--exercises` | No (Marp only) |
| **Python-Forensics** | `build.ts`, `lint-slides.ts` | `--serve`, `--force`, `--exercises` | No (Marp only) |
| **Python-Machine-Learning** | `build.ts`, `lint-slides.ts` | `--serve`, `--exercises`, `--force` | No (Marp only) |
| **TNO-Python** | `build/build-tno.ts` -> `build.ts`, `lint-slides.ts` | `--part <1>2|3`, `--lint`, `--serve`, `--no-exercises`, `--exercises`, `--force` | No (Marp only) |
| **Using-AI-Agents** | `build.ts`, `lint-slides.ts` | `--serve` | No (Marp only) |
| **Advanced-Csharp-Programming** | `courseWare-Presentation-Template/build/build.ts`, `lint-slides.ts` | `--serve` | No (Marp only) |
| **Java-Programming** | `courseWare-Presentation-Template/build/build.ts`, `lint-slides.ts` | `--serve` | No (Marp only) |

### 3.2 Slidev Adoption Status

- **Only 1 course uses Slidev**: `Python-Programming` (for both `Python-Programming` fundamentals and `libraries/` optional topics).
- **All other 47 courses** use Marp (`build.ts`) or custom wrapper scripts that invoke Marp `build.ts`. No other course contains a `slidev.config.ts`, invokes `slidev/build.ts`, or imports `delivery.ts`.

### 3.3 Compatibility Flags Required by Consumers

To ensure backward compatibility across all courses during simplification, the shared toolchain must preserve:
- `--serve` / `-s` (interactive preview/dev)
- `--force` (ignore lint warnings in CI builds)
- `--exercises` (build exercises PDF/HTML instead of slide deck)
- `--slides-dir <dir>` (specify non-standard slide source directories)
- `--out <path>` (custom output file location)
- `--skip-lint` (bypass Puppeteer lint pass)
- `--no-html`, (skip HTML generation)
- `--lint`, (run linter mode)

---

## 4. Duplicated Logic & Cross-File Repetition

Significant duplication exists between course wrappers, the shared template, and the release workflow:

| Duplicated Area | Files & Line References | Specific Duplication Details |
|---|---|---|
| **Template Discovery & Fallback Resolution** | `build/course.ts:6-10`<br>`build/libraries.ts:8-11`<br>`build/slidev.ts:4-9` <br>`build/site.config.ts:39`<br>`PySpark/build/course-layout.ts:14-22` | Identical resolution logic checking `process.env.PRESENTATION_TEMPLATE_DIR`, checking if `build/slidev/build.ts` exists in production sibling, and falling back to `../_worktrees/presentation-template-slidev` or `../../Presentation-Template`. Repeated in 5 separate files. |
| **CLI Option Parsing (`value()`)j* | `build/course.ts:12-17@<br>`build/libraries.ts:13-18a<br>`Presentation-Template/build/slidev/build.ts:36-37`<br>`Presentation-Template/build/site/build-site.ts:60-63` | Hand-rolled CLI argument extractors scanning `process.argv` for `--flag` and returning the next index value. |
| **Child Process Spawner (`run()`)j* | `build/course.ts:18-22@<br>`build/libraries.ts:19-23H<br>`build/slidev.ts:10-11`<br>`build/site.config.ts:40-41` <br>`Presentation-Template/build/slidev/build.ts:12-20` | Repetitive wrappers around `spawnSync(process.execPath, ['run', ...])` with error throwing and status forwarding. |
| **Preamble Frontmatter & Target PDF Resolution** | `build/course.ts:27-31` <br>`build/libraries.ts:28-32@<br>`Presentation-Template/build/src/helpers.ts:10-15@<br>`Presentation-Template/build/src/exercises.ts:85-87` | Regex `pdfName:\s*["']?([^\r\n"']+)` used to extract default PDF filename from `00-preamble/00-preamble.md`, appending `-Marp.pdf` for fallbacks or `-Exercises.pdf` for exercise guides. |
| **Marp Fallback Routing & HTML Copyingj* | `build/course.ts:33-41`<br>`build/libraries.ts:36-47@<br>`Presentation-Template/build/slidev/build.ts:61-76` | Forwarding `--marp` to `build.ts`, waiting for `build/dist/combined.html`, and copying it to `<target>.html` (plus legacy alias in libraries). |
| **Slidev Build & Gating Flags Assembly** | `build/course.ts:44-57` <br>`build/libraries.ts:50-67` | Exact duplicate logic: checking for `--notes`, stripping `--force`, `--skip-lint`, `--no-html`, checking `selected` (`--range`, `--with-clicks`), checking `prepareOnly`, and conditionally pushing `--pdf` and `--check`. |
| **Slidev Post-Build PDF & Delivery Packaging** | `build/course.ts:58-63` <br>`build/libraries.ts:68-73` | Copying `build/slidev/dist/course-slidev.pdf` to target PDF, importing `delivery.ts:packageStudentPresentation`, and building the slides zip archive. |
| **Student Delivery Assembly & Allowlist** | `Presentation-Template/build/slidev/delivery.ts:6-27@<br>`.forgejo/workflows/release.yml:169-236` | `delivery.ts` builds `output/student/` (slidev app, serve.py, licenses, index.html, README). `release.yml` duplicates knowledge of bundle structure: copying `student/` to `${BUNDLE}/slides`, copying demo allowlist `01` to `13`, copying `site/dist` to `${BUNDLE}/site`, stripping `libraries/build` and `libraries/src`, and running shell `find` commands to prune `__pycache__` and cache directories. |
| **Slidev Configuration Structure** | `build/slidev.config.ts:1-65`<br>`libraries/build/slidev.config.ts:1-20` | Both declare `{ title, accent, compactSlides, enrichments }`. Course-specific config duplicated across multiple config files. |

---

## 5. Build Directory File Categorization & Gitignore Analysis

### 5.1 Maintained Files (Version-Controlled Source Code)

#### In `build/` (Course Root):
- **Orchestration & CLI Wrappers**:
  - `build/course.ts` [course.ts](file:///C:/Git/courseware/Python-Programming/build/course.ts) - Main course orchestrator
  - `build/libraries.ts` [libraries.ts](file:///C:/Git/courseWare/Python-Programming/build/libraries.ts) - Libraries deck orchestrator
  - `build/slidev.ts` [slidev.ts](file:///C:/Git/courseWare/Python-Programming/build/slidev.ts) - Direct Slidev CLI wrapper
  - `build/package.json` [package.json](file:///C:/Git/courseWare/Python-Programming/build/package.json) - Script declarations
  - `build/course-tools.toml` - Course tools configuration
  - `build/slidev.config.ts` - Slidev layout & enrichment config
  - `build/site.config.ts` - Exercise site builder config & wrapper
- **Validation & Test Scripts**:
  - `build/check-slidev-delivery.ts` - Student delivery bundle structure & offline check
  - `build/check-slidev-examples.py` - Animation & slide code execution check
  - `build/check-solutions.py` - Wordle solution test runner & transcript check
  - `build/site/check-quiz.py` - Quiz code execution validator
  - `build/slidev_checks/check_core.py`, `check_data_structures.py`, `check_delivery.ts`, `check_diagrams.ts` - Granular Slidev checks
- **Exercise Site Components**:
  - `build/site/plugin.ts`, `build/site/presentation.ts`, `build/site/quiz.jsonx
  - `build/site/assets/wordle.css`, `build/site/assets/wordle.js`
- **Solution Verification Suites**:
  - `build/solution-tests/05-functions/test_wordle.py`
  - `build/solution-tests/06-modules/` (`test_display.py`, `test_scoring.py`)
  - `build/solution-tests/07-comprehensions/` (`test_display.py`, `test_scoring.py`, `test_solver.py`)
  - `build/solution-tests/08-exception-handling/` (`test_display.py`, `test_exceptions.py`, `test_scoring.py`, `test_solver.py`)
  - `build/solution-tests/09-python-io/` (`test_display.py`, `test_exceptions.py`, `test_scoring.py`, `test_solver.py`, `test_words.py`)
  - `build/solution-tests/10-database-access/` (`test_display.py`, `test_exceptions.py`, `test_scoring.py`, `test_solver.py`, `test_stats.py`, `test_words.py`)
  - `build/solution-tests/11-python-classes/` (`test_display.py`, `test_exceptions.py`, `test_game.py`, `test_scoring.py`, `test_solver.py`, `test_stats.py`, `test_words.py`)
  - `build/solution-tests/12-type-hinting/` (`test_display.py`, `test_exceptions.py`, `test_game.py`, `test_scoring.py`, `test_solver.py`, `test_stats.py`, `test_words.py`)
  - `build/transcripts/01-environment-configuration.txt` through `13-python-libraries.txt`
- **Documentation & Plan Records**:
  - `build/orchestration.md`, `build/plan.md`, `build/plan-2026-08-conversion.md`, `build/tasks.md`, `build/slidev-agent-brief.md`
  - `build/notes/*.md` (all historical design and review notes)

#### In `libraries/build/`:
- `libraries/build/slidev.config.ts` - Slidev layout and enrichments config
- `libraries/build/check-demos.py` - Demo execution verifier
- `libraries/build/check-solutions.py` - Solution code verifier
- `libraries/build/check-outputs.py` - Output reference verifier
- `libraries/build/check_support.py` - Shared test support library
- `libraries/build/make-data.py` - Fixture generation and reports script
- `libraries/build/native_states.py` - Native slide state excerpt rebuilder

---

### 5.2 Generated Files & Build Artifacts (Ignored by Git)

- `build/dist/` - Built distribution deliverables:
  - `combined.md`, `combined.html` (Marp staging)
  - `Python-Programming-slides.zip`, `PYG400-Python-Libraries-and-Tools-slides.zip`, `Python-Programming-student.zip`
- `build/slidev/` - Slidev staging directory:
  - `.courseware/` staging workspace (`slides.md`, `package.json`, fonts, components)
  - `dist/` (`slidev/` compiled app, `course-slidev.pdf`, `student/` public bundle, `manifest.jsonx, `build.log`)
- `build/site/dist/` - Generated static exercise website (`index.html`, exercise html pages, quiz, assets)
- `build/.mermaid-cache/` & `libraries/build/.mermaid-cache/` - Rendered SVG cache for diagrams, marked for simplification
- `build/spiraltrain-logo.png` & `libraries/build/spiraltrain-logo.png` - Copied logos for CSS relative resolution
- Root and libraries release deliverables (ignored by pattern):
  - `/PRG400-Python-Programming*.pdf`, `/PRG400-Python-Programming*.html`
  - `libraries/PRG400-Python-Libraries-and-Tools*.pdf`, `libraries/PYG400-Python-Libraries-and-Tools*.html`
- `libraries/build/slidev/` - Libraries Slidev compiled static output and PDF

---

### 5.3 QA Scratch Directories & Diagnostic Logs

Located primarily in `libraries/build/` from past migration phases:
- `libraries/build/qa/` - QA sandbox containing `linux-venv/` (full Linux virtualenv) and `slidev-pages/` (179 page JPEG visual verification snapshots)
- `libraries/build/authoring/` - Scratch authoring tests
- `libraries/build/delivery-check/` - Packaging verification scratch
- `libraries/build/demo-baseline/` - Output capture baseline logs from demo runs
- `libraries/build/initial-baseline/` & `libraries/build/marp-baseline/` - Pre-migration baseline PDFs and exports
- `libraries/build/phase2-*.log` - 10 diagnostic log files (`phase2-build.log`, `phase2-demos.log`, `phase2-exercises.log`, `phase2-final-build.log`, `phase2-lint.log`, `phase2-marp.log`, `phase2-native.log`, `phase2-outputs.log`, `phase2-solutions.log`)
- `build/prototypes/presentation-framework/` - Scratch prototype implementation

---

### 5.4 `.gitignore` Rules Analysis & Exposure Flaw

#### Current `.gitignore` Rules for Build Outputs (lines 56-80):
```gitignore
# Presentation-as-Code build outputs
build/dist/
build/.mermaid-cache/
build/spiraltrain-logo.png
node_modules/
__pycache__/
**/.mypy_cache/
**/.ruff_cache/
**/.pytest_cache/

# Built course decks
/PRG400-Python-Programming.pdf
/PYG400-Python-Programming.html
/PYG400-Python-Programming-Marp.pdf
/PRG400-Python-Programming-Marp.html
/PYG400-Python-Programming-Exercises.pdf
/PYG400-Python-Programming-Exercises.html
demos/10-python-database-access/*.db
build/site/dist/
exercises/starters/*/uv.lock

# Optional libraries deck build outputs
libraries/build/*
!libraries/build/*.py
!libraries/build/*.toml
!libraries/build/*.ts
libraries/PRG400-Python-Libraries-and-Tools*.pdf
libraries/PYG400-Python-Libraries-and-Tools*.html
libraries/data/*.db
build/slidev/
build/prototypes/presentation-framework/
```

#### Identified `.gitignore` Weakness:
In lines 74-77:
```gitignore
libraries/build/*
!libraries/build/*.py
!libraries/build/*.toml
!libraries/build/*.ts
```
The negative ignore `!libraries/build/*.py` was intended to keep maintained checker scripts (`check-demos.py`, `check-solutions.py`, `make-data.py`, etc.) tracked while ignoring build outputs.
However, because it uses an unrestricted glob `*.py`:
1. Any temporary, diagnostic, or QA scratch Python script placed directly in `libraries/build/` is automatically **un-ignored** and appears as untracked in `git status`.
2. This previously caused accidental exposure of scratch scripts during phase work.
3. Solution: Maintained scripts should either be explicitly named in `.gitignore` allowlist or isolated from transient build outputs by moving scratch/generated files into `.courseware/` or `dist/`.
