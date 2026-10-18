# Toolchain documentation consolidation and Stage 7 preparation (Package T6)

This document records the findings for Package T6: an audit of historical documentation,
exact contradiction quotes against current code/behaviour, and the proposed replacement
outline for a single consolidated operating guide section in `MAINTAINING.md`.

## 1. Documentation Taxonomy & Status Summary

All documentation files across `build/notes/` (and top-level conversion documents) have been
indexed in [`build/notes/README.md`](README.md) and classified according to their current relevance:

| Classification | Count | Description |
|---|---|---|
| **ACTIVE-WORK** | 6 | Active simplification design, surveys, inventory, and stage records (`courseware-toolchain-simplification.md`, `toolchain-baseline.md`, `toolchain-browser-survey.md`, `toolchain-inventory.md`, `toolchain-stage1.md`, and this file `toolchain-docs.md`) |
| **HISTORICAL** | 39 | Superseded handoff notes, phase reports, review evidence, and legacy conversion plans (38 files in `build/notes/` + `build/plan-2026-08-conversion.md`) |
| **CURRENT** | 0 | Standalone notes describing live behaviour without being superseded (0 files; live commands and defaults are consolidated in [`MAINTAINING.md`](../../MAINTAINING.md)) |

All 39 **HISTORICAL** files have been prepended with the standard historical banner:
`> Historical record (<date>). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.`

---

## 2. Contradictions Between Historical Notes and Live Behaviour

Comparing historical notes against current code (specifically following the Stage 1 shared orchestration entry point implementation in `toolchain-stage1.md` and `courseware.config.ts`) revealed the following concrete contradictions:

### 2.1 Worktree Fallback and Template Discovery (`presentation-template-slidev`)

Historical notes repeatedly refer to a dedicated, ephemeral sibling worktree (`_worktrees/presentation-template-slidev`) and rely on existence probes or hardcoded paths that fall back to it:

- **`slidev-rollout.md`**:
  > "Shared changes are on `feature/slidev-foundation` in `../_worktrees/presentation-template-slidev`; Presentation-Template main is untouched. That shared feature must reach main before the course release, because CI clones main and checks for the delivery toolchain."
- **`slidev-browser-runner.md`**:
  > "`$env:PRESENTATION_TEMPLATE_DIR='C:/Git/courseWare/_worktrees/presentation-template-slidev'`"
- **`slidev-handoff.md`**:
  > "Shared changes are on `feature/slidev-foundation` in `../_worktrees/presentation-template-slidev`; Presentation-Template main is untouched."
- **`slidev-foundation.md`**:
  > "Branch `feature/slidev-foundation` in worktree `C:/Git/courseWare/_worktrees/presentation-template-slidev`"
- **`slidev-core.md`**:
  > "`PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/_worktrees/presentation-template-slidev`"
- **`slidev-data-structures.md`**:
  > "shared toolchain `C:/Git/courseWare/_worktrees/presentation-template-slidev`"
- **`slidev-appendices.md`**:
  > "`C:/Git/courseWare/_worktrees/presentation-template-slidev` at `82f5134`."

**Current Live Behaviour:**
Stage 1 (`toolchain-stage1.md`) completely removed the silent probe and fallback to `_worktrees/presentation-template-slidev`. The template location is resolved strictly via `PRESENTATION_TEMPLATE_DIR` (explicit environment override) or defaults to `../Presentation-Template` (the standard sibling directory). A missing template is now an explicit, fatal error naming the variable.

---

### 2.2 Default Build Renderer and Release Wiring (Marp vs Slidev)

Earlier audit and verification notes were written while Marp was still the default engine:

- **`slidev-parity-diagrams.md`**:
  > "2. The course's ordinary build, release workflow and student bundle still use Marp. `build/package.json` exposes Slidev only through opt-in scripts; `.forgejo/workflows/release.yml` does not build or package the Slidev delivery folder. The selected 'Slidev default after verification, Marp fallback' cutover is not implemented."
- **`slidev-delivery-verification.md`**:
  > "The ordinary `build` script still points to Marp, and `.forgejo/workflows/release.yml` builds only Marp and its exercises... Keep Marp the default until the coordinator updates and locally verifies the release workflow, packages the student delivery zip and checks the release artifact."

**Current Live Behaviour:**
Slidev is the canonical default build renderer for both `fundamentals` (`bun run --cwd build build`) and `libraries` (`bun run --cwd build libraries`). Marp is an explicit opt-in fallback via `build:marp` and `libraries:marp`. `.forgejo/workflows/release.yml` actively builds and packages Slidev deliverables for student distribution.

---

### 2.3 Orchestration and Entry Point Routing

Notes written during the Slidev migration describe `build/course.ts` as the primary routing script containing courseware business logic:

- **`slidev-rollout.md`**:
  > "`build` now routes to `build/course.ts`: public Slidev app, canonical final-state PDF and `build/dist/Python-Programming-slides.zip`."
- **`slidev-handoff.md`**:
  > "`build` routes to `build/course.ts`"

**Current Live Behaviour:**
As implemented in Stage 1, all orchestration, flag parsing, renderer routing, and deliverable bundling logic now lives in the shared template entry point `courseware.ts` (`bun run <template>/build/courseware.ts [build|lint|slidev] [deck] [flags]`). Course-side scripts (`build/course.ts`, `build/libraries.ts`, `build/slidev.ts`) are thin adapter shims forwarding directly to the shared template entry, reading declarative configuration from `courseware.config.ts`.

---

### 2.4 Template Split and Lint Command Resolution

Earlier notes describe a split where Marp and Slidev resolved template files through different paths, including hardcoded relative paths for linting:

- **`slidev-foundation.md`**:
  > "Marp commands continue to use `../Presentation-Template`... Slidev commands use `PRESENTATION_TEMPLATE_DIR` pointing to the Slidev worktree."
- **`toolchain-stage1.md` (recording the previous state)**:
  > "`lint` script now goes through `course.ts --lint` (was a hard-coded `../../Presentation-Template` path)."

**Current Live Behaviour:**
There is no longer any engine-specific template split. All commands (build, lint, serve) resolve template assets through the unified `PRESENTATION_TEMPLATE_DIR` or `../Presentation-Template` hierarchy.

---

### 2.5 Companion Course (`libraries/`) Slidev Scope

Early migration notes stated that `libraries/` was out of scope for Slidev:

- **`slidev-migration-plan.md`**:
  > "The separate `libraries/` companion remains outside this migration."
- **`slidev-parity-diagrams.md`**:
  > "The separate `libraries/` course remains outside scope."
- **`slidev-rollout.md` (earlier section)**:
  > "The separate `libraries/` companion remains outside this migration."

**Current Live Behaviour:**
The companion course `libraries/` has undergone full 3-phase migration (`libraries-slidev-phase1.md` through `phase3.md`). It defaults to Slidev (`bun run --cwd build libraries`), retains explicit Marp fallbacks (`libraries:marp`), and builds through the shared `courseware.ts` entry.

---

### 2.6 Browser Delivery Gate Discovery

Notes from the delivery gate implementation describe single-pilot discovery:

- **`slidev-browser-runner.md`**:
  > "The runner currently discovers the Data Structures pilot as the only `check_*.py`. It is ready to include later package checks by filename; no unwritten-module checks were added here."

**Current Live Behaviour:**
The browser runner sequentially executes all test checks present in `build/slidev_checks/check_*.py` across all completed modules.

---

### 2.7 CI Test Suite Status

Work package notes contain pending follow-up items for the coordinator:

- **`wp6.md`**:
  > "Coordinator follow-up needed: run `uv run python build/site/check-quiz.py` in CI beside the existing fence and Ruff checks."

**Current Live Behaviour:**
`check-quiz.py` is actively integrated into `.forgejo/workflows/release.yml` and is a gating CI check.

---

### 2.8 CLI Positional Parameter Strictness

- **Historical behaviour**:
  Stray positional arguments were silently forwarded or ignored by underlying scripts.
- **Current Live Behaviour (`toolchain-stage1.md`)**:
  > "Stricter than before : a stray positional argument (`bun run libraries -- nope`) is now an error; previously it was forwarded and ignored."

---

### 2.9 Slide and Page Counts Drift

Historical reports document snapshot page counts from specific dates that have drifted as slides were refined:
- **`slidev-parity-diagrams.md`**: Slidev 241 pages, Marp 239 pages.
- **`slidev-rollout.md`**: Fundamentals 275 Slidev pages (33 native additions), 242 Marp pages.
- **`libraries-review.md`**: Libraries Marp 168 pages.
- **Current Verified Counts (`toolchain-stage1.md`)**:
  - Fundamentals Slidev: 276 pages
  - Fundamentals Marp: 243 pages
  - Fundamentals Exercises: 135 pages
  - Libraries Slidev: 179 pages
  - Libraries Marp: 169 pages

---

## 3. Replacement Structure for Single Operating Guide in `MAINTAINING.md`

Per Section 7 of `courseware-toolchain-simplification.md`, the repository must maintain **one current operating guide** covering commands, configuration, outputs, development overrides, and release recovery.

Below is the drafted replacement outline for the coordinator to integrate into `MAINTAINING.md`:

### Outline: Consolidated Toolchain Operating Guide

#### 1. Commands
- **First-Time Setup**:
  - Node/Bun prerequisites (`bun install --cwd ../Presentation-Template/build`).
  - Browser binaries for layout & height checks (`bunx puppeteer browsers install chrome`).
  - Python toolchain sync (`uv sync` for fundamentals, `uv sync --project libraries` for companion).
- **Canonical Build Commands**:
  - Fundamentals: `bun run --cwd build build` (Slidev presentation app, canonical PDF, student ZIP).
  - Exercises: `bun run --cwd build build -- --exercises` (exercises PDF and HTML).
  - Fallbacks: `bun run --cwd build build:marp` (named Marp fallback PDF and HTML).
  - Development Server: `bun run --cwd build serve` (native Slidev dev server on port 3030).
  - Linting: `bun run --cwd build lint` (slide layout, height budget, and fence checks).
- **Libraries Companion Commands**:
  - Build: `bun run --cwd build libraries` (Slidev PDF and student slides ZIP).
  - Fallbacks: `bun run --cwd build libraries:marp` (Marp fallback PDF and HTML).
  - Development Server: `bun run --cwd build libraries:serve` (dev server on port 3030).
  - Linting: `bun run --cwd build lint:libraries` (layout budget lint).
- **Code & Test Gates**:
  - Python linting: `uv run ruff check .` (enforcing zero findings across live lessons).
  - Code reference & fence validation: `uv run python ../Presentation-Template/build/tools/check-fences.py`.
  - Solutions & starters: `uv run python build/check-solutions.py` and `make-starters.py --check`.
  - Quiz validation: `uv run python build/site/check-quiz.py`.
  - Delivery verification: `bun run --cwd build check:delivery`.

#### 2. Configuration
- **Courseware Configuration (`courseware.config.ts`)**:
  - Root declarative config defining decks (`fundamentals` and `libraries`).
  - Deck settings schema: directory (`dir`), default renderer (`renderer: 'slidev' | 'marp'`), archive generation (`archive: boolean`), and plain HTML aliasing (`plainMarpHtml: boolean`).
  - Preamble metadata: role of `pdfName` inside presentation source headers.
- **Engine Configuration**:
  - Slidev configuration in `build/slidev.config.ts` and `libraries/build/slidev.config.ts`.
  - Layout budgets, UnoCSS styling rules, and Pele diagram configuration.

#### 3. Outputs
- **Artifact Manifest & Locations**:
  - Canonical presentation PDFs: `Python-Programming.pdf`, `PRG400-Python-Libraries-and-Tools.pdf`.
  - Named fallbacks: `Python-Programming-Marp.pdf`, `Python-Programming-Marp.html`.
  - Student packages: `build/dist/Python-Programming-slides.zip`, `build/dist/PRG400-Python-Libraries-and-Tools-slides.zip`.
  - Exercises deliverables: `exercises/Python-Programming-Exercises.pdf`.
- **Packaging Integrity & Content Boundaries**:
  - Strict allowlist structure for student repository bundle (`SpiralTrain/Python-Programming-Student`).
  - Clean separation: exclusion of trainer notes, intermediate build caches, source markdown, and authoring QA logs from public packages.

#### 4. Development Override
- **Template Location Resolution**:
  - Default resolution: sibling directory `../Presentation-Template`.
  - Explicit override: `PRESENTATION_TEMPLATE_DIR=/path/to/template-worktree`.
  - Error diagnostics: fatal failure mode when template is absent, clearly identifying missing variable or path.
- **Multi-Course Testing**:
  - Testing against alternative course checkouts without dirtying main working copies.

#### 5. Release Recovery
- **CI / CD Workflow**:
  - Automated workflow execution in `.forgejo/workflows/release.yml` on push to `master`.
  - Step sequences: Python verification -> build both decks -> publish `latest` release -> push to student repo.
- **Authentication & Secrets**:
  - Repo-level deploy key `STUDENT_REPO_SSH_KEY` (`prg400-ci-push`).
  - Handling absent or revoked secrets (clean skip semantics).
- **Incident Recovery Procedures**:
  - Handling partial workflow failures or broken releases.
  - Re-triggering release builds and re-generating student distribution archives.
  - Restoring release tags and rolling back corrupted artifacts.
