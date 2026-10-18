# Slidev animation package contract

Read this before implementing an assigned package. The coordinator's checkout
is `C:/Git/courseWare/Python-Programming`; this file there remains available even
when a delegated worktree starts from an earlier commit.

## Start

1. Read `AGENTS.md`, `build/notes/slidev-handoff.md` and the accepted plan at
   `C:/Git/courseWare/Python-Programming/build/notes/slidev-migration-plan.md`.
2. Read shared writing/conventions from `C:/Git/courseWare/Presentation-Template`.
   The shared Slidev implementation is
   `C:/Git/courseWare/_worktrees/presentation-template-slidev`; read its
   `AGENTS.md` and `docs/slidev.md` before using its tooling.
3. Inspect your branch/status and assigned demos. Set
   `PRESENTATION_TEMPLATE_DIR` to that absolute shared feature worktree when
   building from a delegated checkout. Install dependencies only in the shared
   toolchain when needed; course `build/package.json` stays a thin wrapper.

## Implement within the assigned file boundary

- Keep canonical course slides, demos, exercises and solutions intact. Quote
  their code verbatim, including annotations. Additional labels follow house
  style and explain only already-taught concepts.
- Put native slides under your assigned `src/slidev/<package>/` folder, one
  Slidev page with frontmatter per file. Use unique Vue component names under
  `src/slidev/components/`; keep styling scoped. Existing examples are references,
  not an instruction to repeat one pattern everywhere.
- Use Slidev click state and reversible, meaningful transitions. Highlight an
  active element, move values or references, or morph code only when it explains
  a change. Honour reduced motion. Final states must print intelligibly.
- Use stable keys for moving objects; repeated values must remain separate
  objects. Account for the shared 1280 by 800 frame and its header/footer.
- Canonical Mermaid syntax is rendered by Pele during preparation. Native
  additions go through the same preprocessing. Report renderer issues rather
  than replacing shared rendering from your package.
- Add a package-local executable check under
  `build/slidev_checks/check_<package>.py`. Execute the Python actually displayed
  by the slide, compare state/output against the data actually passed to its
  component, and verify provenance against the cited demo. Report any example
  that needs a different verification method. Existing global checker integration
  belongs to the coordinator.

## Verify and hand back

1. Render the package using a temporary config or an ignored scratch checkout;
   restore coordinator-owned files before committing. Inspect initial,
   intermediate, final and reverse states, and final/click PDF output. Record
   exact commands and any missing checks honestly.
2. Keep `build/notes/slidev-<package>.md` current. Include an insertion list with
   exact module slug, existing title and native file, click counts, demo paths,
   state-check command, design rationale and remaining findings.
3. Commit only assigned source/check/notes files on your branch. Report branch,
   commit hashes, changed files and evidence. Do not push or merge.

Coordinator-owned files: existing check scripts, `build/slidev.config.ts`, other
project configuration and lockfiles, CI, README, maintenance/agent docs, shared
template files, the plan/tasks and orchestration log. Report precise changes
needed there. Each package owns only the files named in its delegated brief.
