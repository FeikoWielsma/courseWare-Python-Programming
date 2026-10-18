# Stateful animation work in progress

Claude Opus 5.5 hit the five-hour limit on 2026-10-18; the provider reports
reset at 16:40 Europe/Amsterdam. The trainer explicitly chose to wait for Claude
quota, keeping the author model/provider unchanged. This is unverified partial
work and must not be shipped as a completed package.

## Resume

Read `build/slidev-agent-brief.md` in the coordinator checkout, then continue
these existing files instead of recreating them. Parent baseline `2d7cdef`.
Own new `src/slidev/stateful/*.md`, `Stateful*.vue` and this notes file only.
No canonical source, demo, config, shared code, CI or existing component edits.
One Opus author at a time. Keep author checks minimal; Luna verifies in detail.

## Existing partial files

- `components/StatefulFile.vue`: file contents, open/closed handles and positions.
- `stateful/closing-when-with-ends.md`: demo08 usingwith, module 09.
- `stateful/moving-the-file-position.md`: demo09 file_positions, module 09.
- `components/StatefulRecords.vue`: query rows and pending/committed records.
- `stateful/one-row-per-fetch.md`: demo09 fetchone, module 10.
- `stateful/inserts-wait-for-the-commit.md`: demo05 lastinsertedrowid, module 10.

All paths above are relative to `src/slidev/`. No coordinator insertion specs,
build, screenshots or executable verification were completed before the limit.
The record-row fade implementation was being revised; inspect it before use.
Author executed some output probes; do not assume individual states are verified.

## Remaining

Finish the package: inspect/fix these four slides and components, add around two
useful class slides for module 11 using its existing neutral demos (instances,
attribute references or properties already taught). Keep explicit JSON run data,
stationary code with active line, fixed geometry, meaningful reversible motion,
reduced motion and useful final frames. Reuse the established shell/components.
Run displayed Python for output sanity in temporary files/databases where needed.
No full browser/PDF audits or checker authoring; Luna owns them.

Record exact module/source-title/native-file insertion table, click/state counts,
demo provenance, per-state execution meaning, basic checks and remaining issues.
Restore temporary config before the final commit. Do not push, merge to the
coordinator, or spawn further agents.
