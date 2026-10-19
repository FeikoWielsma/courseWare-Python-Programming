# Agent brief : courseware toolchain simplification

Every agent on this job reads this file first, then its package prompt.
The design is `build/notes/courseware-toolchain-simplification.md`; read it too.
Also read `AGENTS.md` here and `../Presentation-Template/AGENTS.md` (in a worktree
checkout, the template's `AGENTS.md` is in your template worktree).

## Where to work

| Repository | Integration worktree | Branch |
|---|---|---|
| Python-Programming | `C:/Git/courseWare/_worktrees/prg-toolchain-int` | `toolchain/integration` |
| Presentation-Template | `C:/Git/courseWare/_worktrees/presentation-template-cli` | `feature/courseware-cli` |

- Work only in the worktree your prompt names, by absolute path. **Never** edit or
  switch branches in `C:/Git/courseWare/Python-Programming` or
  `C:/Git/courseWare/Presentation-Template` (the main checkouts other courses
  build from).
- To build the course against the template worktree, set
  `PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/_worktrees/presentation-template-cli`.
  The worktrees already have `bun install` done for `build/` and `build/slidev/`.
- Never commit to `master` / `main`, push, merge or tag. No network publishing.
- Do not touch other courses, except read-only (baseline builds write outside them).

## Rules

1. **Commit small and often** on your own branch. Quotas can end a session at any
   time; uncommitted work is lost work. Commit after every working step, with a
   message saying what changed.
2. **Keep `build/notes/toolchain-<package>.md` current** (course worktree, or
   `docs/notes/` in the template worktree for template packages): done, left,
   decided, exact commands run. A successor must be able to resume from the branch
   and that file alone.
3. **Verify by running**; quote only real output. Windows: Git Bash, LF line
   endings (`newline="\n"` in Python), use the Edit tool for text with backslashes,
   no `git stash` during renames, stop any server you start.
4. **Coordinator-only files** (report the change you need with exact text, do not
   edit): `build/plan.md`, `build/tasks.md`, `build/orchestration.md`, this brief,
   `AGENTS.md`, `MAINTAINING.md`, `README.md`, `.forgejo/workflows/*`, `ruff.toml`,
   lockfiles. Exception: a package whose prompt says it owns a file.
5. **Preserve behaviour.** Existing CLI flags (`--exercises`, `--marp`, `--serve`,
   `--dev`, `--slides-dir`, `--out`, `--force`, `--skip-lint`, `--no-html`,
   `--pdf`, `--check`, `--range`, `--with-clicks`, `--prepare`, `--check-only`,
   `--serve-only`, `--notes`) and downloadable student filenames must keep working.
   Renderers stay unchanged. Marp stays for what depends on it.
6. **Delete what you replace.** A new layer that leaves the old duplication in place
   does not count. Report lines deleted.
7. Write no Dutch. Code is concise, matches surrounding style, minimal comments.
8. End with a report: branch and commits, what changed, lines deleted, gate results,
   coordinator-only changes needed, open decisions.

## Baselines

Baseline artefacts live **outside** the repositories in
`C:/Git/courseWare/_baselines/` (git-less scratch). Fingerprint format: JSON per
PDF with page count and a sha256 of the whitespace-normalised text of each page.

## Gates (course worktree)

Run what applies to your change; the full set is in `AGENTS.md` under Checks:
`uv run ruff check .`, `bun run --cwd build build -- --skip-lint`,
`bun run --cwd build lint`, `bun run --cwd build libraries`, `bun run --cwd build check:delivery`.
Template worktree: `bun run --cwd build typecheck`, `bun run --cwd build smoke`,
`bun test` in `build/slidev`.
