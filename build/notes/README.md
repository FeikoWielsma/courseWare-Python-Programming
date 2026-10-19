# Build Notes Index

Index of the toolchain design record and the live behaviour notes in this folder.
Historical handoffs, work-package reports and the old conversion plan are in [`history/`](history/).

Current commands and operating procedures are in [`MAINTAINING.md`](../../MAINTAINING.md).

Current course content revision: [a gentler introduction](gentler-introduction.md).

Teaching-order review and remaining scaffolding decisions:
[progression audit](progression-audit.md).

## Summary by Classification

| Classification | Count | Description |
|---|---|---|
| **DESIGN** | 1 | Implemented toolchain design (`courseware-toolchain-simplification.md`) |
| **CURRENT** | 6 | Live toolchain behaviour notes (`toolchain-stage1.md`, `toolchain-stage3.md`, `toolchain-pin.md`, `toolchain-release.md`, `toolchain-browser6.md`, `toolchain-perf.md`) |
| **HISTORY** | 43 | Superseded handoffs, baselines and the old conversion plan, in `history/` |

---

## Orchestration Logs

- [`build/orchestration.md`](../orchestration.md): Multi-agent rework and execution log across rounds and packages (October 2026).

---

## Index of Notes

| File | Date | Status | Description | Superseded By |
|---|---|---|---|---|
| [courseware-toolchain-simplification.md](courseware-toolchain-simplification.md) | 2026-10-18 | DESIGN | Design record for the shared courseware toolchain. The redesign is in place. | [MAINTAINING.md](../../MAINTAINING.md) |
| [engaging-examples.md](history/engaging-examples.md) | 2026-10-18 | HISTORICAL | Implementation record and example map for music, photo, and character examples | [slidev-rollout.md](history/slidev-rollout.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [functions-examples.md](history/functions-examples.md) | 2026-10-18 | HISTORICAL | Early draft of functions examples rework before playlist/duration theme approval | [engaging-examples.md](history/engaging-examples.md) and [slidev-rollout.md](history/slidev-rollout.md) |
| [hints-pass.md](history/hints-pass.md) | 2026-10-17 | HISTORICAL | Exercise hints audit and revision notes for Exercises 2 to 13 | [slide-gaps.md](history/slide-gaps.md) and current exercise texts |
| [libraries-review.md](history/libraries-review.md) | 2026-10-18 | HISTORICAL | Pre-migration safety net and test baseline review for the libraries/ course | [libraries-slidev-phase1.md](history/libraries-slidev-phase1.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [libraries-slidev-phase1.md](history/libraries-slidev-phase1.md) | 2026-10-18 | HISTORICAL | Phase 1 migration record for libraries/ Slidev adoption with Marp fallback | [libraries-slidev-phase2.md](history/libraries-slidev-phase2.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [libraries-slidev-phase2.md](history/libraries-slidev-phase2.md) | 2026-10-18 | HISTORICAL | Phase 2 migration record replacing library examples with music, photos, and WoW characters | [libraries-slidev-phase3.md](history/libraries-slidev-phase3.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [libraries-slidev-phase3.md](history/libraries-slidev-phase3.md) | 2026-10-18 | HISTORICAL | Phase 3 delivery review, visual QA, and verification record for libraries/ delivery | [MAINTAINING.md](../../MAINTAINING.md) and [toolchain-stage1.md](toolchain-stage1.md) |
| [libraries-slidev-plan.md](history/libraries-slidev-plan.md) | 2026-10-18 | HISTORICAL | Multi-phase plan for converting libraries/ companion course to Slidev | [libraries-slidev-phase3.md](history/libraries-slidev-phase3.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [slide-gaps.md](history/slide-gaps.md) | 2026-10-17 | HISTORICAL | Gap audit of slide coverage for concepts required in Exercises 7 to 10 and 13 | [wp7.md](history/wp7.md), [wp8a.md](history/wp8a.md), and current slide decks |
| [slidev-appendices.md](history/slidev-appendices.md) | 2026-10-18 | HISTORICAL | Package completion report for native Slidev animations in Appendices 12 and 13 | [slidev-rollout.md](history/slidev-rollout.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [slidev-browser-runner.md](history/slidev-browser-runner.md) | 2026-10-18 | HISTORICAL | Pilot package evidence and specification for browser delivery gate (check-slidev-delivery.ts) | [slidev-delivery-verification.md](history/slidev-delivery-verification.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [slidev-core-verification.md](history/slidev-core-verification.md) | 2026-10-18 | HISTORICAL | Independent verification report for core Slidev animations (modules 01, 02, 04, 05) | [slidev-rollout.md](history/slidev-rollout.md) |
| [slidev-core.md](history/slidev-core.md) | 2026-10-18 | HISTORICAL | Package completion report for native Slidev animations in core modules | [slidev-rollout.md](history/slidev-rollout.md) |
| [slidev-data-structures.md](history/slidev-data-structures.md) | 2026-10-18 | HISTORICAL | Stage 2 pilot package report for native Slidev Data Structures animations (module 03) | [slidev-rollout.md](history/slidev-rollout.md) |
| [slidev-delivery-verification.md](history/slidev-delivery-verification.md) | 2026-10-18 | HISTORICAL | Delivery verification report for baseline Slidev delivery before release wiring | [slidev-rollout.md](history/slidev-rollout.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [slidev-foundation.md](history/slidev-foundation.md) | 2026-10-18 | HISTORICAL | Implementation record of parallel Slidev foundation and tooling in template branch | [slidev-handoff.md](history/slidev-handoff.md), [slidev-rollout.md](history/slidev-rollout.md), and [toolchain-stage1.md](toolchain-stage1.md) |
| [slidev-handoff.md](history/slidev-handoff.md) | 2026-10-18 | HISTORICAL | Migration handoff document defining Slidev parity objectives and initial stopping points | [slidev-rollout.md](history/slidev-rollout.md) and [toolchain-stage1.md](toolchain-stage1.md) |
| [slidev-integration.md](history/slidev-integration.md) | 2026-10-18 | HISTORICAL | Integration evidence and decision log for Slidev adoption plan continuation | [slidev-rollout.md](history/slidev-rollout.md) |
| [slidev-middle.md](history/slidev-middle.md) | 2026-10-18 | HISTORICAL | Package completion report for native Slidev animations in middle modules (06, 07, 08) | [slidev-rollout.md](history/slidev-rollout.md) |
| [slidev-migration-plan.md](history/slidev-migration-plan.md) | 2026-10-18 | HISTORICAL | Multi-stage adoption and animation plan for migrating PRG400 to Slidev | [slidev-rollout.md](history/slidev-rollout.md) |
| [slidev-parity-diagrams.md](history/slidev-parity-diagrams.md) | 2026-10-18 | HISTORICAL | Feature parity audit between Marp and Slidev, including Mermaid diagram rendering | [slidev-rollout.md](history/slidev-rollout.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [slidev-rollout.md](history/slidev-rollout.md) | 2026-10-18 | HISTORICAL | Integration record of completed Slidev rollout across all 13 modules | [toolchain-stage1.md](toolchain-stage1.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [slidev-stateful.md](history/slidev-stateful.md) | 2026-10-18 | HISTORICAL | Package completion report for native Slidev animations in stateful modules (09, 10, 11) | [slidev-rollout.md](history/slidev-rollout.md) |
| [toolchain-baseline.md](history/toolchain-baseline.md) | 2026-10-18 | HISTORICAL-EVIDENCE | Package T0 baseline builds, output hashes, and cross-course fingerprints | [toolchain-stage1.md](toolchain-stage1.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [toolchain-browser-survey.md](history/toolchain-browser-survey.md) | 2026-10-18 | HISTORICAL-EVIDENCE | Package T2 survey of browser lifecycle and dev-server duplication across courses | [toolchain-browser6.md](toolchain-browser6.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [toolchain-browser6.md](toolchain-browser6.md) | 2026-10-18 | CURRENT | Package T7 course browser checks migrated onto shared browser module (`build/browser.ts`) | None (Live behaviour) |
| [toolchain-docs.md](history/toolchain-docs.md) | 2026-10-18 | HISTORICAL-EVIDENCE | Package T6 documentation consolidation, contradiction audit, and Stage 7 preparation | [MAINTAINING.md](../../MAINTAINING.md) |
| [toolchain-inventory.md](history/toolchain-inventory.md) | 2026-10-18 | HISTORICAL-EVIDENCE | Package T1 comprehensive inventory of all toolchain commands, deliverables, and CI | [MAINTAINING.md](../../MAINTAINING.md) |
| [toolchain-pin.md](toolchain-pin.md) | 2026-10-19 | CURRENT | Package T8 pinned toolchain resolution (`build/toolchain.json`), cache (now per machine, see toolchain-perf.md), and override guard | None (Live behaviour) |
| [toolchain-perf.md](toolchain-perf.md) | 2026-10-19 | CURRENT | Package PERF: build time (settled delivery check, concurrent CI groups) and the per-machine toolchain cache, with measurements | None (Live behaviour) |
| [toolchain-release.md](toolchain-release.md) | 2026-10-19 | CURRENT | Package T9 manifest-driven release assembly, independent publish and student-sync jobs | None (Live behaviour) |
| [toolchain-stage1.md](toolchain-stage1.md) | 2026-10-18 | CURRENT | Package T3 shared orchestration entry point (`courseware.ts`) and deck configuration | None (Live behaviour) |
| [toolchain-stage3.md](toolchain-stage3.md) | 2026-10-18 | CURRENT | Package T4 separate variant outputs (`.courseware/<deck>/<variant>/`) and artifact manifest schema | None (Live behaviour) |
| [wp1.md](history/wp1.md) | 2026-10-14 | HISTORICAL | Work package 1 progress report for Wordle reference solutions and starter generation | [`build/tasks.md`](../tasks.md) and current solution files |
| [wp2a.md](history/wp2a.md) | 2026-10-17 | HISTORICAL | Work package 2a progress report for exercise texts 1 to 4 (Wordle spine) | [wp2b.md](history/wp2b.md) and current exercise texts |
| [wp2b.md](history/wp2b.md) | 2026-10-17 | HISTORICAL | Work package 2b progress report for exercise texts 5 to 8 (containers, tier badges) | [wp2c.md](history/wp2c.md) and current exercise texts |
| [wp2c.md](history/wp2c.md) | 2026-10-17 | HISTORICAL | Work package 2c progress report for exercise texts 9 to 13 | [wp7.md](history/wp7.md) and current exercise texts |
| [wp3a.md](history/wp3a.md) | 2026-10-15 | HISTORICAL | Work package 3a progress report for slides and demos 01 to 03 | [slidev-core.md](history/slidev-core.md) and current slide files |
| [wp3b.md](history/wp3b.md) | 2026-10-17 | HISTORICAL | Work package 3b progress report for slides and demos 04 to 06 | [slidev-middle.md](history/slidev-middle.md) and current slide files |
| [wp3c.md](history/wp3c.md) | 2026-10-14 | HISTORICAL | Work package 3c implementation report for module 09 (binary IO, bytes, CSV) | [slidev-stateful.md](history/slidev-stateful.md) and current slide files |
| [wp3d.md](history/wp3d.md) | 2026-10-15 | HISTORICAL | Work package 3d progress report for modules 10 (SQLite) and 11 (Classes) | [slidev-stateful.md](history/slidev-stateful.md) and current slide files |
| [wp3e.md](history/wp3e.md) | 2026-10-14 | HISTORICAL | Work package 3e progress report for Appendix slides and demos 12 & 13 | [slidev-appendices.md](history/slidev-appendices.md) and current slide files |
| [wp5.md](history/wp5.md) | 2026-10-17 | HISTORICAL | Work package 5 independent student review findings of PRG400 course | [wp8a.md](history/wp8a.md), [wp8b.md](history/wp8b.md), and [wp8c.md](history/wp8c.md) |
| [wp6.md](history/wp6.md) | 2026-10-17 | HISTORICAL | Work package 6 implementation notes for exercise-site quiz and Wordle Easter egg | [wp8c.md](history/wp8c.md) and [release.yml](../../.forgejo/workflows/release.yml) |
| [wp7.md](history/wp7.md) | 2026-10-17 | HISTORICAL | Work package 7 resolution report aligning solutions and exercise texts 9 to 13 | [wp8a.md](history/wp8a.md) and current exercise texts / solutions |
| [wp8a.md](history/wp8a.md) | 2026-10-17 | HISTORICAL | Work package 8a resolution report fixing student review findings in solutions and exercises | Current exercise solutions and tests |
| [wp8b.md](history/wp8b.md) | 2026-10-17 | HISTORICAL | Work package 8b factual slide corrections report | [slidev-rollout.md](history/slidev-rollout.md) and current slide decks |
| [wp8c.md](history/wp8c.md) | 2026-10-17 | HISTORICAL | Work package 8c exercise site and PDF pagination fixes report | Current exercise site build and [MAINTAINING.md](../../MAINTAINING.md) |

---

## Historical Top-Level Documents

| File | Date | Status | Description | Superseded By |
|---|---|---|---|---|
| [history/plan-2026-08-conversion.md](history/plan-2026-08-conversion.md) | 2026-08-15 | HISTORICAL | Initial conversion plan from original PRG400 PowerPoint/PDF to presentation-as-code | [`build/plan.md`](../plan.md) and [MAINTAINING.md](../../MAINTAINING.md) |
