# PRG400 remaining work

The course-side courseware integration is implemented. Current build behavior is described in
[MAINTAINING.md](../MAINTAINING.md) and the
[shared configured-course guide](../../Presentation-Template/docs/courseware.md).

The trainer explicitly deferred further pedagogical scaffolding for Exercises 10
to 13 on 2026-10-19. These are outside build migration scope and should remain
separate from migration completion:

- **Exercise 10:** add runnable checkpoints between returning a game result,
  recording it and displaying statistics. Each intermediate result should run;
  the final stage must match the canonical solution and transcript.
- **Exercise 11:** separate the mechanical `play` refactor from the board renderer
  and class methods. Demonstrate state changes on a small object before
  integration; preserve final game behavior and transcript.
- **Exercise 12:** review the cross-module `Mark` alias migration and mypy check
  order alongside neighboring integrations. Steps should identify files and
  checkpoints; all stages must pass mypy and existing tests.
- **Exercise 13:** separate saving, loading and resuming into runnable stages.
  Check persisted settings and interruption behavior at each stage; preserve
  solution, test and transcript behavior.

The [progression audit](notes/progression-audit.md#deferred-exercises-10-to-13)
records the trainer's decision and detailed boundaries. Do not reduce the required
feature set or change the four-day schedule as part of that deferred work.

## Migration validation and rollout

The local migration checks cover source gates, all thirteen Wordle stages,
both slide decks and exercise PDFs, site assembly, browser delivery and artifact
manifests. The shared suites cover routing, packaging, release recovery and
isolated Slidev preparation. Go Programming and GitLab CI/CD retain their page
counts and per-page PDF text. Both authoring commands serve without changing
student manifests.

The course pin includes the shared changes. Publish the shared template commit
before publishing this course branch so clean machines and CI can fetch the pin.
Remote publication and a hosted CI run remain rollout work; local validation
uses the local shared repository as the resolver's fetch transport.
