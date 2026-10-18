# Courseware toolchain simplification: implementation handoff

Recorded 2026-10-18 after the Python fundamentals and Libraries Slidev work.
This records proposed maintenance work for a future agent. The user requested
this document; implementation of the redesign has not started.

## Objective

Make building, checking, serving, packaging and releasing courses smaller and
easier to maintain. Put shared behavior behind one versioned courseware tool.
Courses supply content, configuration and checks that depend on their subject.

Start by deleting duplicated orchestration. Preserve working renderers and
student behavior while moving their callers to a simpler interface. Avoid a
rewrite of the whole toolchain or a simultaneous migration of every course.

## Start here

Workspace paths on the current machine:

- Course: `C:/Git/courseWare/Python-Programming`.
- Shared toolchain: `C:/Git/courseWare/Presentation-Template`.
- Other courses: sibling repositories under `C:/Git/courseWare/`.

Read both repositories' `AGENTS.md` files and their referenced writing and
technical conventions. Read the shared `docs/build-todo.md`, `docs/slidev.md`,
and this course's `MAINTAINING.md`. Check current branches, changes and remote
state before editing; do not assume this handoff describes future checkout state.

Shared changes must be developed in a Presentation-Template worktree. Its main
checkout serves other courses and must remain on its production branch. Use
`PRESENTATION_TEMPLATE_DIR` explicitly to test a course against that worktree.
Follow the shared repository's regression requirements before merging, including
before/after PDF comparisons for at least two unrelated courses.

Historical Slidev handoffs contain superseded defaults and prerequisites. Use
current code and verification records to establish the baseline. In particular,
the shared Slidev implementation is now present in production; do not resurrect
the old automatic fallback to the foundation worktree.

## Evidence behind the proposal

| Current source | Maintenance problem |
|---|---|
| Course `build/course.ts` and `build/libraries.ts` | Duplicate flag parsing, template discovery, renderer routing, export copying and student packaging |
| Course `build/slidev.ts` and script entry points in configuration files | Additional paths for finding and invoking shared code |
| Course `.forgejo/workflows/release.yml` | Knows build ordering, bundle contents, output filenames, release API details and repository synchronisation |
| Shared `build/slidev/build.ts`, development server and packaged Python launcher | Several serving modes and process lifecycles to understand |
| Shared `build/slidev/delivery.ts` and course workflow | Packaging knowledge is split between presentation delivery and the full student bundle |
| Course browser checks under `build/slidev_checks/` | Repeated Chrome launch, serving, navigation, waiting and cleanup mechanics |
| Course `build/` | Maintained scripts, generated projects, caches, logs and QA evidence coexist; ignore exceptions can accidentally expose scratch scripts |
| Course and shared maintenance notes | Historical handoffs sometimes contradict current defaults and prerequisites |

Release work exposed concrete consequences:

- Windows and Linux produced different XLSX ZIP metadata and PNG compressed
  bytes. The fix normalises workbook metadata and text line endings, while
  comparing decoded PNG pixels exactly.
- A command needed a manually supplied template environment variable even
  though another command could discover the same template.
- A dictionary animation passed general deck validation but failed the more
  specific packaged browser containment check.
- The release workflow used an unsupported tag-deletion route, leaving
  `latest` on an old commit. It now uses the tag endpoint, sets the release
  target explicitly and checks the tag SHA.
- QA scripts placed directly in `libraries/build/` were exposed by the
  intentional ignore exceptions for maintained Python scripts.

Relevant implementation commits: `922ab17`, `b51c313`, `df16703`. These are
context, not a guarantee that a future checkout has no subsequent changes.
Libraries verification is recorded in [the Phase 3 report](libraries-slidev-phase3.md).
Check the remote workflow/release for publication status; this document is not
a release-success record.

## Proposed design

### 1. One CLI, configured per course

Move orchestration into the shared toolchain. The illustrative interface is:

```bash
courseware dev libraries
courseware check libraries
courseware build libraries
courseware release --all
```

These commands are a proposal, not installed commands. Final names can change.
The important contract is that local use and CI invoke the same operations.

A course configuration declares decks, renderer selection, exercise sources,
student-file allowlists and extra subject-specific checks. Python fundamentals
and Libraries should be two configured decks using the same implementation.
Course-specific checks remain in the course; Chrome lifecycle, output handling
and renderer orchestration belong in the shared toolchain.

Keep existing public CLI flags working through temporary compatibility adapters
as required by the shared repository. Do not expose every internal stage or
copy the existing flag combinations into a larger new interface. Add hooks only
for actual differences between existing consumers.

### 2. Pin the toolchain

Each course pins a toolchain release or commit. Its source commit, lockfiles
and toolchain reference must be enough to reconstruct its build inputs.

Keep one explicit local-development override for testing shared changes. Remove
heuristics that silently choose a sibling production checkout or an old worktree.
A Git reference is a sufficient first implementation; publishing to a package
registry is optional and should not block consolidation.

### 3. Separate maintained source from generated work

Proposed course layout:

```text
tools/          maintained course-specific checks
.courseware/    ignored generated projects, caches, logs and QA evidence
dist/           finished deliverables
```

Use separate output locations for student, trainer, final-state PDF and click
exports. A selected-page or click export must not overwrite the normal package
or leave a stale manifest paired with a different app.

Preserve existing downloadable filenames through compatibility copies or a
manifest mapping during migration. Cache inputs must include the toolchain
version, configuration and relevant source/dependency inputs. Avoid introducing
a general-purpose build framework merely to add caching.

### 4. Build once and publish the resulting manifest

The build produces an artifact manifest with:

- Course source commit and toolchain version/reference.
- Deck and export variant, with student/trainer distinction.
- Every deliverable's path, filename, checksum and size.
- Verification results needed to decide whether it can be published.

Packaging, verification and publishing consume this manifest rather than
rediscovering files with globs or repeating filename lists. The same reviewed
artifact is the one uploaded; publishing must not silently rebuild it.

Aim to upload and verify a complete draft release before promotion, leaving the
previous public release available if building or uploading fails. Verify the
actual Forgejo version's draft, tag and publication behavior before implementing
that sequence. Prefer immutable build/release tags, with `latest` as a convenience
pointer rather than the only record of a release. Verify commit provenance and
asset completeness before announcing success.

### 5. Share browser verification and serving mechanics

Provide a shared browser-checking module for Chrome discovery, launch, ports,
timeouts, readiness, reduced-motion emulation, diagnostics and cleanup. Courses
supply expected states and assertions. Existing Python execution/provenance
checks must survive; a generic visual test does not replace them.

Expose two clear serving modes: source development and preview of the packaged
student artifact. Report the actual selected URL/port and guarantee cleanup on
exit and error. Retain the offline Python student launcher and its navigation
behavior; students must not need Bun or Node to view the delivered presentation.

### 6. Make CI a small caller

The workflow should primarily check out inputs, install the pinned toolchain,
check, build and publish. Move bundle assembly and Forgejo publishing details
into maintained, independently runnable code.

Keep student-repository synchronisation and its GitHub mirror as a separate,
retryable stage. A mirror failure must not require rendering every PDF again or
replacing an otherwise valid release. Keep target repositories and credentials
explicit; do not make the shared renderer know Python's repository names.

Use a pinned Linux release-rendering environment, including browser and fonts.
Windows remains supported for authoring. Choose reproducibility assertions at
the appropriate level: exact content/pixels where archive metadata or compression
can legitimately vary. Do not weaken content checks just to make CI green.

A versioned package and a CI image have different roles. Avoid creating several
independently versioned packages or a registry service unless a real need emerges.

### 7. Close migration leftovers and consolidate documentation

Declare renderer selection per deck. Preserve Marp for courses and exercises
that still depend on it. Comparison portals and extra fallback exports should
be explicit capabilities, rather than permanent branches in every normal build.
Do not remove Python's promised fallback artifacts without a deliberate cutover.

Review the visual modules copied between fundamentals and Libraries for shared
ownership now that they have two real consumers. Preserve their demonstrated
state and reduced-motion behavior when consolidating them.

Maintain one current operating guide for commands, configuration, outputs,
development overrides and release recovery. Archive historical handoffs and
link them as history. Avoid parallel documents claiming different active defaults.

## Suggested implementation sequence

1. Inventory current commands, consumers and deliverables. Capture Python and
   unrelated-course baselines before moving code.
2. Add one shared orchestration entry point and course/deck configuration.
   Migrate fundamentals and Libraries; replace their duplicated wrappers with
   compatibility adapters. Keep renderers unchanged.
3. Separate temporary outputs and final artifacts. Introduce the artifact
   manifest; make packaging and preview consume it.
4. Pin toolchain resolution and retain one explicit development override.
5. Extract release publishing and student synchronisation. Make the workflow
   call the same maintained commands used locally.
6. Consolidate browser/server lifecycle code and shared visual modules where
   the existing consumers demonstrate a useful common interface.
7. Update the current operating guide, archive superseded handoffs and remove
   compatibility code only after affected consumers have migrated.

Use small, reviewable commits with preserved behavior. At each stage identify
the old code that can actually be deleted. A new layer that leaves all duplicated
orchestration in place has not met the objective.

## Acceptance checks

- Python fundamentals and Libraries build through one shared orchestration
  implementation; no copied course-specific engine-routing logic remains.
- The normal local and CI operations use the same commands and pinned inputs.
- Existing required CLI flags and student download names remain compatible
  during migration; unrelated courses still work.
- Normal, selected-page, click and trainer outputs cannot overwrite one another.
- A clean checkout can build without an undisclosed local sibling branch or
  worktree. A development override is explicit and reported.
- Packaging and publishing consume a validated artifact manifest. All expected
  PDFs, HTML fallbacks, slides archives and full student bundles are accounted for.
- Public bundles contain no trainer notes, authoring sources, caches or QA logs.
- Preview runs the packaged artifact; ports are reported correctly and processes
  close on success, interruption and failure.
- Existing code, exercise, provenance, animation, reduced-motion, containment,
  offline behavior and physical wheel-navigation checks still pass.
- Publishing can be retried without rebuilding. A simulated upload failure
  preserves the previous public release. Release tags and assets match the
  manifest's source commit.
- Student-repository and mirror synchronisation can be retried independently.
- At least two unrelated courses pass the shared repository's required
  before/after PDF page-count and per-page-text comparisons.
- Documentation has one clear current entry point and labels historical records.

## Decisions to resolve during implementation

Prefer the least elaborate option that satisfies existing consumers:

- Exact config filename/schema and CLI spelling.
- Git-pinned toolchain distribution versus a published package.
- Whether a pinned rendering image is also useful locally or only for releases.
- Forgejo's supported promotion sequence and how existing `latest` links survive.
- Which compatibility adapters can be retired after each course migrates.

These are not reasons to block the initial inventory or wrapper consolidation.
Do not add unrelated course-content changes, redesign Wordle exercises, or
reorganise every repository as part of this maintenance work.

## Suggested subagent brief

> Read `build/notes/courseware-toolchain-simplification.md` in Python-Programming
> and the required instructions in both repositories. Establish the current
> baseline, then implement the first consolidation stage in a shared-template
> worktree and migrate the two Python decks. Preserve existing behavior and
> compatibility. Report deleted duplication, verification evidence and any
> decisions needed before later stages. Do not publish changes to other courses
> or remove their existing renderer support as part of the pilot.
