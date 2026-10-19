# Toolchain stage 5: release assembly and publishing (T9)

Branch `tc/release`, worktree `prg-tc-release`; workflow owner for
`.forgejo/workflows/release.yml`. Shared release implementation is in the
`feature/courseware-release` Presentation-Template worktree. Design:
`courseware-toolchain-simplification.md`, sections 4 and 6, acceptance checks.

## Done

- `courseware.config.ts` declares the student bundle allowlist, archive, release pointer,
  student repository, GitHub mirror and credential environment-variable names. It keeps
  the named Marp HTML trainer-note waiver explicit; strict verification is the default.
- `release.yml` now checks, builds, verifies and prepares a manifest-backed upload ZIP in
  `build`; uploads that ZIP as an Actions artifact; restores it in a fresh `publish` job;
  and runs student/mirror sync in a separate `sync` job. All toolchain-dependent jobs
  fetch the pinned template independently. No job depends on another job's filesystem.
- Student sync can be retried with `workflow_dispatch.sync_tag` without rebuilding.
  Dry-run builds/checks/verifies and asks the publisher for a read-only report; it skips
  sync and performs no release writes.
- The shared implementation and its offline Forgejo failure/retry behavior are
  documented in the template worktree's `docs/notes/toolchain-release.md`.

## Workflow review

Compared with `git show master:.forgejo/workflows/release.yml`, every prior gating
operation remains: lockfile checks, frozen installs, Python compileall, code-fence and
slide-reference checks, starter check, solution tests, quiz check, Ruff, libraries
checks, animation checks, delivery checks, both decks and their Marp/exercises outputs,
site build, libraries lint, per-manifest verification, and bundle verification. The
compileall paths are now the course's `demos`, `solutions`, and libraries paths.

The cross-job data is explicit: the build job uploads only
`.courseware/release/upload.zip` as artifact `release-${{ github.sha }}`; publish restores
that named artifact into `.courseware/release`; sync downloads the configured published
release through the API. Each job separately checks out the same event commit and
resolves the same pinned template. The workflow parses with Python `yaml.safe_load`.

The workflow shrank from 381 lines on `master` to 211 lines: **170 lines removed**.

## Verification (2026-10-19)

Template gates: `bun run --cwd build typecheck` passed; `bun run --cwd build test` had 53
passes and 0 failures; `bun run --cwd build smoke` reported `SMOKE PASS`; `bun test` in
`build/slidev` had 14 passes and 0 failures.

Course checks and builds, using the exact pinned template commit fetched from the local
template worktree:

- `bun run --cwd build toolchain` validated the pin at
  `98d878cb707636b24a78e616110b52f5ce82a947`.
- `bun run --cwd build check:animations` passed static animation and provenance checks.
- `bun run --cwd build build -- --force`: fundamentals Slidev, 276 pages, 0 validation
  failures. `check:delivery` passed core and data-structure browser checks and the
  physical wheel probe.
- `bun run --cwd build build:marp -- --force`: 243-slide PDF and HTML.
- `bun run --cwd build build -- --exercises --force`: exercises PDF and HTML.
- `bun run --cwd build site`: 13 exercise pages and offline site.
- `bun run --cwd build libraries -- --skip-lint --force`: 179-page Slidev deck, 0
  validation failures. `libraries:marp --skip-lint --force`, `lint:libraries`, and
  `libraries -- --exercises --force` all passed.
- `verify -- fundamentals` and `verify -- libraries`: student, Marp and exercises
  manifests passed for both decks.
- `bundle` and `verify -- --bundle`: 1,840 files / 77.2 MB; passed with only the two
  configured Marp HTML trainer-note paths reported as waived.
- Fake Forgejo: an injected partial upload failed while the previous `latest` release,
  tag and asset remained unchanged. Retrying the prepared upload published
  `build-9fe8eff` and `latest` and retained the former pointer under its history tag.
- Local bare Git repositories: student repository and mirror `main` refs matched;
  mirrors-only retry passed.
- Fingerprint comparisons against `C:/Git/courseWare/_baselines/python/`: fundamentals
  Slidev (276 pages), Marp (243), exercises (135), and libraries Slidev (179) each had
  identical text on every page.
- Python `yaml.safe_load` reported `YAML PASS`.

The build used the pinned resolver with
`PRESENTATION_TEMPLATE_REPOSITORY=file:///C:/Git/courseWare/_worktrees/presentation-template-release`,
not `PRESENTATION_TEMPLATE_DIR`. The latter marks manifests as development overrides,
which the publisher correctly refuses. No real Forgejo or GitHub endpoint was contacted.

## Decisions and remaining coordination

- Keep `build-<short-sha>` as the immutable build-release tag and `latest` as the moving
  pointer. Preserve the previous public pointer release under
  `latest-history-<release-id>` before changing `latest`.
- Use the reviewed prepared ZIP between build and publish jobs so publish retries reuse
  exact bytes and do not render again.
- Keep student repository and GitHub mirror sync separate from rendering and release
  publishing. The release note in the template worktree lists the retry behavior.
- **Do not enable real publishing until the target Forgejo version and API behaviors are
  confirmed.** Confirm draft creation/tag behavior, tag create/read/delete, promotion via
  `draft:false`, published-release retagging and asset retention, upload/list/download
  behavior, pagination and size limits. Also confirm the installed Forgejo Actions
  runner supports the artifact upload/download actions and paths used here.
- Before first CI, push/merge the template and repin to its merged fetchable commit. The
  current course pin matches the local template feature commit and is not yet evidence
  that the server can fetch it. Confirm Forgejo context variables and artifact transport;
  secret names/scopes for release API, student SSH push and GitHub mirror; then perform a
  `dry_run=true` workflow run and inspect the report. The template note gives the full
  first-run checklist.

## Commits

- `5c93185` Add manifest-driven release, independent publish and student-sync jobs.
- `9fe8eff` Pin the reviewed release toolchain for local and CI callers.

No course workflow edits remain uncommitted. This note records T9 evidence; real server
facts and publishing remain open for the integration coordinator.
