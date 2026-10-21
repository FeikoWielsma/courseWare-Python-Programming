# PRG400 remaining work

## Trainer-deferred exercise scaffolding

The trainer deferred further scaffolding for Exercises 10 to 13 on 2026-10-19.
Keep this work separate from build migration and retain each stage's existing
solution, test, starter and transcript contracts. Do not reduce the required
feature set or change the four-day schedule as part of this follow-up.

- **Exercise 10:** add runnable checkpoints between returning the game result,
  recording it and displaying statistics. Each intermediate result should run.
- **Exercise 11:** Step 5 now gives `__str__` its own sub-step and `play` a
  skeleton with five gaps. Still open : demonstrate state changes on a small
  object before integration.
- **Exercise 12:** review the cross-module `Mark` alias migration and mypy check
  order alongside neighboring integrations. This is a review item, not a known
  defect.

- **Exercise 5:** the two-pass duplicate-letter scoring in `score_guess` lost
  both students of the October 2026 delivery, as did the move to the interpreter
  that follows it. Supply more of the second pass as a guided fill-in, and check
  each pass on its own before the two are combined. Keep the `score_guess`
  contract and its tests.

## Rendering follow-up

Recheck these in a fresh rendered export before changing shared renderer code.
An earlier review found Slidev PDF headers cropped on some pages while the
browser deck remained aligned. The automatic layout check does not inspect PDF
header crops. Current rendered checks find no content overflow or undersized
diagram labels; those older findings are closed. Shared renderer work belongs in
a Presentation-Template worktree and needs its cross-course regression checks.
