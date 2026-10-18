# Build Notes Index

Index of all documentation, handoff notes, work-package reports, and toolchain design records in uild/notes/ (and historical top-level conversion records).

Current canonical commands and operating procedures are maintained in [MAINTAINING.md](../../MAINTAINING.md).

## Summary by Classification

| Classification | Count | Description |
|---|---|---|
| **ACTIVE-WORK** | 6 | Active toolchain simplification design, surveys, baselines, and implementation records (	oolchain-*.md, courseware-toolchain-simplification.md) |
| **HISTORICAL** | 39 | Superseded handoff notes, phase completion reports, review evidence, and legacy conversion plans (38 notes in this directory, plus top-level uild/plan-2026-08-conversion.md) |
| **CURRENT** | 0 | Standalone notes describing live behaviour without being superseded (0 files; live commands and defaults are consolidated in [MAINTAINING.md](../../MAINTAINING.md)) |

---

## Index of Notes

| File | Date | Status | Description | Superseded By |
|---|---|---|---|---|
| [courseware-toolchain-simplification.md](courseware-toolchain-simplification.md) | 2026-10-18 | ACTIVE-WORK | Architectural proposal and 7-stage simplification plan for courseware toolchain | None (Active design) |
| [ngaging-examples.md](engaging-examples.md) | 2026-10-18 | HISTORICAL | Implementation record and example map for music, photo, and character examples | [slidev-rollout.md](slidev-rollout.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [unctions-examples.md](functions-examples.md) | 2026-10-18 | HISTORICAL | Early draft of functions examples rework before playlist/duration theme approval | [ngaging-examples.md](engaging-examples.md) and [slidev-rollout.md](slidev-rollout.md) |
| [hints-pass.md](hints-pass.md) | 2026-10-17 | HISTORICAL | Exercise hints audit and revision notes for Exercises 2 to 13 | [slide-gaps.md](slide-gaps.md) and current exercise texts |
| [libraries-review.md](libraries-review.md) | 2026-10-18 | HISTORICAL | Pre-migration safety net and test baseline review for the libraries/ course | [libraries-slidev-phase1.md](libraries-slidev-phase1.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [libraries-slidev-phase1.md](libraries-slidev-phase1.md) | 2026-10-18 | HISTORICAL | Phase 1 migration record for libraries/ Slidev adoption with Marp fallback | [libraries-slidev-phase2.md](libraries-slidev-phase2.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [libraries-slidev-phase2.md](libraries-slidev-phase2.md) | 2026-10-18 | HISTORICAL | Phase 2 migration record replacing library examples with music, photos, and WoW characters | [libraries-slidev-phase3.md](libraries-slidev-phase3.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [libraries-slidev-phase3.md](libraries-slidev-phase3.md) | 2026-10-18 | HISTORICAL | Phase 3 delivery review, visual QA, and verification record for libraries/ delivery | [MAINTAINING.md](../../MAINTAINING.md) and [	oolchain-stage1.md](toolchain-stage1.md) |
| [libraries-slidev-plan.md](libraries-slidev-plan.md) | 2026-10-18 | HISTORICAL | Multi-phase plan for converting libraries/ companion course to Slidev | [libraries-slidev-phase3.md](libraries-slidev-phase3.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [slide-gaps.md](slide-gaps.md) | 2026-10-17 | HISTORICAL | Gap audit of slide coverage for concepts required in Exercises 7 to 10 and 13 | [wp7.md](wp7.md), [wp8a.md](wp8a.md), and current slide decks |
| [slidev-appendices.md](slidev-appendices.md) | 2026-10-18 | HISTORICAL | Package completion report for native Slidev animations in Appendices 12 and 13 | [slidev-rollout.md](slidev-rollout.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [slidev-browser-runner.md](slidev-browser-runner.md) | 2026-10-18 | HISTORICAL | Pilot package evidence and specification for browser delivery gate (check-slidev-delivery.ts) | [slidev-delivery-verification.md](slidev-delivery-verification.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [slidev-core-verification.md](slidev-core-verification.md) | 2026-10-18 | HISTORICAL | Independent verification report for core Slidev animations (modules 01, 02, 04, 05) | [slidev-rollout.md](slidev-rollout.md) |
| [slidev-core.md](slidev-core.md) | 2026-10-18 | HISTORICAL | Package completion report for native Slidev animations in core modules | [slidev-rollout.md](slidev-rollout.md) |
| [slidev-data-structures.md](slidev-data-structures.md) | 2026-10-18 | HISTORICAL | Stage 2 pilot package report for native Slidev Data Structures animations (module 03) | [slidev-rollout.md](slidev-rollout.md) |
| [slidev-delivery-verification.md](slidev-delivery-verification.md) | 2026-10-18 | HISTORICAL | Delivery verification report for baseline Slidev delivery before release wiring | [slidev-rollout.md](slidev-rollout.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [slidev-foundation.md](slidev-foundation.md) | 2026-10-18 | HISTORICAL | Implementation record of parallel Slidev foundation and tooling in template branch | [slidev-handoff.md](slidev-handoff.md), [slidev-rollout.md](slidev-rollout.md), and [	oolchain-stage1.md](toolchain-stage1.md) |
| [slidev-handoff.md](slidev-handoff.md) | 2026-10-18 | HISTORICAL | Migration handoff document defining Slidev parity objectives and initial stopping points | [slidev-rollout.md](slidev-rollout.md) and [	oolchain-stage1.md](toolchain-stage1.md) |
| [slidev-integration.md](slidev-integration.md) | 2026-10-18 | HISTORICAL | Integration evidence and decision log for Slidev adoption plan continuation | [slidev-rollout.md](slidev-rollout.md) |
| [slidev-middle.md](slidev-middle.md) | 2026-10-18 | HISTORICAL | Package completion report for native Slidev animations in middle modules (06, 07, 08) | [slidev-rollout.md](slidev-rollout.md) |
| [slidev-migration-plan.md](slidev-migration-plan.md) | 2026-10-18 | HISTORICAL | Multi-stage adoption and animation plan for migrating PRG400 to Slidev | [slidev-rollout.md](slidev-rollout.md) |
| [slidev-parity-diagrams.md](slidev-parity-diagrams.md) | 2026-10-18 | HISTORICAL | Feature parity audit between Marp and Slidev, including Mermaid diagram rendering | [slidev-rollout.md](slidev-rollout.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [slidev-rollout.md](slidev-rollout.md) | 2026-10-18 | HISTORICAL | Integration record of completed Slidev rollout across all 13 modules | [	oolchain-stage1.md](toolchain-stage1.md) and [MAINTAINING.md](../../MAINTAINING.md) |
| [slidev-stateful.md](slidev-stateful.md) | 2026-10-18 | HISTORICAL | Package completion report for native Slidev animations in stateful modules (09, 10, 11) | [slidev-rollout.md](slidev-rollout.md) |
| [	oolchain-baseline.md](toolchain-baseline.md) | 2026-10-18 | ACTIVE-WORK | Package T0 baseline builds, output hashes, and cross-course fingerprints | None (Active reference baseline) |
| [	oolchain-browser-survey.md](toolchain-browser-survey.md) | 2026-10-18 | ACTIVE-WORK | Package T2 survey of browser lifecycle and dev-server duplication across courses | None (Active architectural input for stage 6) |
| [	oolchain-docs.md](toolchain-docs.md) | 2026-10-18 | ACTIVE-WORK | Package T6 documentation consolidation, contradiction quotes, and MAINTAINING.md outline | None (Active stage 7 design) |
| [	oolchain-inventory.md](toolchain-inventory.md) | 2026-10-18 | ACTIVE-WORK | Package T1 comprehensive inventory of all toolchain commands, deliverables, and CI | None (Active reference inventory) |
| [	oolchain-stage1.md](toolchain-stage1.md) | 2026-10-18 | ACTIVE-WORK | Package T3 verification of shared orchestration entry (courseware.ts) | None (Active implementation record) |
| [wp1.md](wp1.md) | 2026-10-14 | HISTORICAL | Work package 1 progress report for Wordle reference solutions and starter generation | [uild/tasks.md](../tasks.md) and current solution files |
| [wp2a.md](wp2a.md) | 2026-10-17 | HISTORICAL | Work package 2a progress report for exercise texts 1 to 4 (Wordle spine) | [wp2b.md](wp2b.md) and current exercise texts |
| [wp2b.md](wp2b.md) | 2026-10-17 | HISTORICAL | Work package 2b progress report for exercise texts 5 to 8 (containers, tier badges) | [wp2c.md](wp2c.md) and current exercise texts |
| [wp2c.md](wp2c.md) | 2026-10-17 | HISTORICAL | Work package 2c progress report for exercise texts 9 to 13 | [wp7.md](wp7.md) and current exercise texts |
| [wp3a.md](wp3a.md) | 2026-10-15 | HISTORICAL | Work package 3a progress report for slides and demos 01 to 03 | [slidev-core.md](slidev-core.md) and current slide files |
| [wp3b.md](wp3b.md) | 2026-10-17 | HISTORICAL | Work package 3b progress report for slides and demos 04 to 06 | [slidev-middle.md](slidev-middle.md) and current slide files |
| [wp3c.md](wp3c.md) | 2026-10-14 | HISTORICAL | Work package 3c implementation report for module 09 (binary IO, bytes, CSV) | [slidev-stateful.md](slidev-stateful.md) and current slide files |
| [wp3d.md](wp3d.md) | 2026-10-15 | HISTORICAL | Work package 3d progress report for modules 10 (SQLite) and 11 (Classes) | [slidev-stateful.md](slidev-stateful.md) and current slide files |
| [wp3e.md](wp3e.md) | 2026-10-14 | HISTORICAL | Work package 3e progress report for Appendix slides and demos 12 & 13 | [slidev-appendices.md](slidev-appendices.md) and current slide files |
| [wp5.md](wp5.md) | 2026-10-17 | HISTORICAL | Work package 5 independent student review findings of PRG400 course | [wp8a.md](wp8a.md), [wp8b.md](wp8b.md), and [wp8c.md](wp8c.md) |
| [wp6.md](wp6.md) | 2026-10-17 | HISTORICAL | Work package 6 implementation notes for exercise-site quiz and Wordle Easter egg | [wp8c.md](wp8c.md) and [.forgejo/workflows/release.yml](../../.forgejo/workflows/release.yml) |
| [wp7.md](wp7.md) | 2026-10-17 | HISTORICAL | Work package 7 resolution report aligning solutions and exercise texts 9 to 13 | [wp8a.md](wp8a.md) and current exercise texts / solutions |
| [wp8a.md](wp8a.md) | 2026-10-17 | HISTORICAL | Work package 8a resolution report fixing student review findings in solutions and exercises | Current exercise solutions and tests |
| [wp8b.md](wp8b.md) | 2026-10-17 | HISTORICAL | Work package 8b factual slide corrections report | [slidev-rollout.md](slidev-rollout.md) and current slide decks |
| [wp8c.md](wp8c.md) | 2026-10-17 | HISTORICAL | Work package 8c exercise site and PDF pagination fixes report | Current exercise site build and [MAINTAINING.md](../../MAINTAINING.md) |

---

## Historical Top-Level Documents

| File | Date | Status | Description | Superseded By |
|---|---|---|---|---|
| [../plan-2026-08-conversion.md](../plan-2026-08-conversion.md) | 2026-08-15 | HISTORICAL | Initial conversion plan from original PRG400 PowerPoint/PDF to presentation-as-code | [uild/plan.md](../plan.md) and [MAINTAINING.md](../../MAINTAINING.md) |
