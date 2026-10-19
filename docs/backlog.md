# PRG400 remaining work

## Trainer-deferred exercise scaffolding

The trainer deferred further scaffolding for Exercises 10 to 13 on 2026-10-19.
Keep this work separate from build migration and retain each stage's existing
solution, test, starter and transcript contracts. Do not reduce the required
feature set or change the four-day schedule as part of this follow-up.

- **Exercise 10:** add runnable checkpoints between returning the game result,
  recording it and displaying statistics. Each intermediate result should run.
- **Exercise 11:** separate the mechanical `play` refactor from the board renderer
  and class methods. Demonstrate state changes on a small object before
  integration.
- **Exercise 12:** review the cross-module `Mark` alias migration and mypy check
  order alongside neighboring integrations. This is a review item, not a known
  defect.
- **Exercise 13:** separate saving, loading and resuming into runnable stages.
  Check persisted settings and interruption behavior at each stage.

## Rendering follow-up

Recheck these in a fresh rendered export before changing shared renderer code.
An earlier review found Slidev PDF headers cropped on some pages while the
browser deck remained aligned. The automatic layout check does not inspect PDF
header crops. Current rendered checks find no content overflow or undersized
diagram labels; those older findings are closed. Shared renderer work belongs in
a Presentation-Template worktree and needs its cross-course regression checks.
