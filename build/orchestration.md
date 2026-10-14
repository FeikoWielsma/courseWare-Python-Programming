# Orchestration log : the PRG400 rework

Coordinator : the T3 thread that wrote `build/plan.md` (Claude Opus 5.5).
Integration branch : `prg400-wordle`. `master` is untouched until the trainer says so.
Read this first after a context reset or a quota interruption.

## Provider policy (from the trainer)

- Spread evenly, in the order claude >= codex > cursor > antigravity.
- Use the small models (GPT-6-Luna, Claude Haiku 5.5) wherever the work allows.
- Prose (exercise texts, slide wording) : Claude Opus 5.5, also reachable through Cursor.
- Quotas are $20 plans on each provider; 5-hour and weekly limits will be hit.
  Auto-continue is on. Claude runs out first.

## Running

| WP | Where | Model | Branch / id | Started |
|---|---|---|---|---|
| WP0 site port | top-level thread in Presentation-Template | Codex GPT-6.1-Sol, high | thread `mcp:636593ff-b576-4437-b045-639c669484a5`, branch `exercise-site` | 2026-10-14 |
| WP1 solutions chain | delegated, worktree | Codex GPT-6-Luna, high | client id `prg400-wp1-r1` | 2026-10-14 |
| WP3a slides 01-03 | delegated, worktree | Claude Opus 5.5, medium | `prg400-wp3a-r1` | 2026-10-14 |
| WP3b slides 04-06 | delegated, worktree | Cursor Claude Opus 5.5, medium | `prg400-wp3b-r1` | 2026-10-14 |
| WP3c slides 07-09 | delegated, worktree | Codex GPT-6-Astra, medium | `prg400-wp3c-r1` | 2026-10-14 |
| WP3d slides 10-11 | delegated, worktree | Claude Opus 5.5, medium | `prg400-wp3d-r1` | 2026-10-14 |
| WP3e appendices 12-13 | delegated, worktree | Antigravity Gemini 3.8 Flash High | `prg400-wp3e-r1` | 2026-10-14 |

All delegated packages branched from `19409a7`. The shared brief is in each
task prompt : coordinator-only files, gates, notes in `build/notes/<wp>.md`.

## Done by the coordinator

- `19409a7` Round 7 and 8, the prototype, the plan
- `e7d329d` archive of unreferenced demos and stray exercise files; starters check in CI

## Next, in order

1. As each WP3 finishes : review its report, merge its branch into `prg400-wordle`
   (`git merge --no-ff`), apply the coordinator-only changes it asks for
   (`ruff.toml` paths after demo renames, `check-fences.py` ignores), run all gates
   plus build and lint, commit.
   Expected overlaps : WP3a and WP3b both edit `04-control-flow-and-operators.md`
   (WP3a removes the operator slides, WP3b the rest); WP3a removes bytes from 03 and
   WP3c adds it to 09.
2. When WP1 finishes : merge; wire `build/check-solutions.py` into CI; regenerate and
   check starters.
3. When WP0 finishes : review the Presentation-Template branch and the PySpark
   comparison, merge `exercise-site` into Presentation-Template `main` (CI clones
   template `main`), merge the PRG400 site-wiring branch.
4. WP2 exercise texts, after WP1 (and ideally WP0), in `:::` markup, Claude Opus 5.5
   (direct or via Cursor) : WP2a Ex 1-4, WP2b Ex 5 conversion and 6-8, WP2c Ex 9-13.
5. Extras after WP2 : the PRG400 quiz (Q12) and a hidden Wordle Easter egg on the
   site (Q14), small models.
6. WP4 remainder : docs (`AGENTS.md`, `MAINTAINING.md`, `README.md`) on the spine,
   starters and the site; devcontainer check.
7. WP5 student review on a different provider from the authors, then a fix round.
