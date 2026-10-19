# Slidev animation package contract

Read this before implementing an assigned package. The coordinator's checkout
is `C:/Git/courseWare/Python-Programming`; this file there remains available even
when a delegated worktree starts from an earlier commit.

## Start

1. Read `AGENTS.md`, `build/notes/history/slidev-handoff.md` and the accepted plan at
   `C:/Git/courseWare/Python-Programming/build/notes/history/slidev-migration-plan.md`.
2. Read shared writing/conventions from `C:/Git/courseWare/Presentation-Template`
   `main`. Read its `AGENTS.md` and `docs/slidev.md` before using its tooling.
3. Inspect your branch/status and assigned demos. Set
   `PRESENTATION_TEMPLATE_DIR` to that absolute shared feature worktree when
   building from a delegated checkout. Install dependencies only in the shared
   toolchain when needed; course `build/package.json` stays a thin wrapper.

## Implement within the assigned file boundary

- The trainer now authorizes canonical example replacements within explicitly
  assigned modules. Read `build/notes/history/engaging-examples.md` for the accepted map
  and ownership. Keep the subject coverage, useful teaching order and exercise
  contracts; quote the updated demos verbatim in slides and native additions.
  Preserve annotations after their introduction. The first Functions examples
  remain unannotated by explicit trainer direction. Additional labels follow
  house style and explain only already-taught concepts.
- Music and photos are recurring themes, game characters teach Classes and a
  film watchlist teaches SQLite. Use small realistic tasks, one new mechanism at
  a time and supplied offline data. No external services or setup are needed.
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
- The trainer approved the Data Structures pilot on 2026-10-18. Follow its
  stationary code, active line, moving values/references and reversible steps.
  Reuse `DataStructuresRun` where it helps; do not redesign the shared shell.
- Author verification is deliberately small, per the trainer's request: execute
  displayed Python to establish its output and perform basic syntax/build sanity.
  Focus Opus time on implementing the animations. Do not write exhaustive check
  scripts, run full-course browser audits or export/review PDFs in author tasks.
- Keep state data readily inspectable and record its demo provenance and expected
  states. The trainer has stopped further token-heavy Luna verification rounds.
  The coordinator owns focused existing checks and necessary visual review.
  Do not create exhaustive new checker scripts or launch additional reviewers.

## Verify and hand back

1. Perform the small author checks above. A temporary config may be used for
   syntax/build sanity; restore coordinator-owned files before committing.
   Record exact commands and leave integration checks to the coordinator.
2. Keep `build/notes/slidev-<package>.md` current. Include an insertion list with
   exact module slug, existing title and native file, click counts, demo paths,
   state-check command, design rationale and remaining findings.
3. Commit only assigned source/check/notes files on your branch. Report branch,
   commit hashes, changed files and evidence. Do not push or merge.

Coordinator-owned files: existing check scripts, `build/slidev.config.ts`, other
project configuration and lockfiles, CI, README, maintenance/agent docs, shared
template files, the plan/tasks and orchestration log. Report precise changes
needed there. Each package owns only the files named in its delegated brief.
