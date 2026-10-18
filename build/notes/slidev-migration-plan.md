# Slidev adoption and animation plan

Recorded 2026-10-18. Entry context: [handoff](slidev-handoff.md).

## Accepted scope

- Cover all 13 fundamentals modules, beginning with a Data Structures pilot.
- Keep `src/slides/` as the canonical course source. Add native Slidev slides
  and Vue components where motion explains the subject.
- Make Slidev the default build, release and student presentation delivery after
  verification. Retain explicit Marp build and delivery commands as a fallback.
- The separate `libraries/` companion course remains outside this conversion.
- Example selection should favour engaging, realistic tasks involving music,
  photos, films or small games. Avoid defaulting to stock items and order status.
  Keep examples small and introduce one language mechanism at a time. The
  trainer approved the broader rewrite: music/photos recur, Classes uses game
  characters and SQLite uses a film watchlist. Assigned authors may update their
  canonical slides/demos and matching animations together. See
  [the example map](engaging-examples.md) for current ownership.
- Claude Opus 5.5 authors animations. Luna completed the initial audits; the
  trainer has stopped further Luna rounds. The coordinator owns focused
  verification, integration and the cutover.

## Sequence and completion criteria

1. **Establish the baseline.** Run the existing converter, Python snapshots,
   shared typecheck and course browser checks. Record page/topic/fence counts,
   renderer versions and outstanding parity gaps. Luna traces every existing
   Mermaid fence through Pele, the generated deck and PDF output. Completion:
   an evidence-based parity matrix and a diagram inventory, including cold and
   warm cache behaviour, placeholders and unsupported syntax.
2. **Render a Data Structures pilot.** Opus extends the existing mutation and
   unpacking examples with useful indexing/slicing, nested reference, set and
   dictionary demonstrations. Components use stable identities, restrained
   transitions and reversible click state. Show the actual browser frames and
   exported states before spreading the visual convention. Completion: a
   teachable module, verified Python states, readable final/click PDFs and a
   concrete visual review.
3. **Enrich the remaining modules.** Use isolated worktrees and bounded batches:
   values/control flow/functions/comprehensions, then modules/exceptions/IO/
   database/classes/appendices. Inspect every module for useful motion; a static
   fact or overview can stay static. Candidate explanations include name/object
   references, loop execution, calls and return values, scope, imports,
   comprehensions, exception paths, resource lifetimes, transactions and
   properties. Completion: an animation inventory covering every module, each
   addition tied to an existing topic/demo, with executed state/output checks.
4. **Integrate and close migration blockers.** The coordinator applies insertion
   config, promotes substantive regressions into checks, and resolves navigation,
   presenter/notes, authoring, PDF links and delivery findings. Diagram checks
   cover appearance, labels, fonts, sizing and export, rather than only valid SVG.
   Completion: every parity feature is verified or has an explicit, concrete
   delivery limitation and working classroom path.
5. **Prepare the default cutover.** Preserve exercise build flags and the offline
   exercise site while routing ordinary slide builds, release assets and student
   slide links to Slidev. Keep named Marp fallback commands and artefacts. Verify
   the student launcher and CI packaging locally. Shared template changes stay
   in its feature worktree; integration into production requires PDF page-count
   and per-page-text comparisons for two unrelated courses. Completion: a
   reviewable, locally verified release configuration and working fallback.
6. **Acceptance.** The coordinator checks integrated output and unresolved prior
   findings using existing checks and targeted visual review, without new Luna
   rounds. Inspect browser motion and rendered PDF pages, run course gates,
   update the handoff and record remaining limits.
   Completion: full and click PDFs, offline presentation folder, source coverage,
   animation/diagram checks and a reproducible verification report.

## Rendering decision

Slidev 53 supports native `mermaid` fences, per-fence rendering options,
`setup/mermaid.ts` configuration and a custom renderer through
`setup/mermaid-renderer.ts`. The course currently calls shared
`processDiagrams()` before Slidev compilation, rendering Mermaid syntax with
Pele 1.6.0 and embedding themeable inline SVG. Preserve that consistent rendering
path unless evidence warrants a reviewed change. Motion within a diagram needs
explicit choreography; accepting Mermaid syntax does not establish that motion.

Upstream route checked against GitHub and installed Slidev 53 on 2026-10-18:
[PR #2465](https://github.com/slidevjs/slidev/pull/2465) merged the supported
custom-renderer hook on 2026-03-03. The installed client invokes custom renderers
before its Mermaid renderer. A Pele adapter can return `render(code, options).svg`
after mapping the supported options. No Slidev fork or upgrade is necessary.
Current GitHub issue/PR searches for Pele in `slidevjs/slidev` and Slidev in
`obsidianmd/pele` returned no entries. The general hook already provides the seam.
For the accepted canonical-source workflow, keep existing cached build-time Pele
rendering: it is implemented and adds no browser diagram-rendering step. Use the
client hook if native, live Mermaid authoring becomes a requirement; that route
still needs explicit font, theme, sizing and export checks. This is an engineering
effort recommendation, not a measured performance comparison between renderers.

Primary references: [Mermaid fences](https://sli.dev/features/mermaid),
[configuration](https://sli.dev/custom/config-mermaid),
[custom renderer](https://sli.dev/custom/config-mermaid-renderer),
[animation](https://sli.dev/guide/animations).

## Ownership and orchestration

- Initial work: one Opus pilot author and one Luna research/verification agent.
- Remaining work: one Opus author at a time, with focused coordinator checks and
  no further Luna agents, following the trainer's quota-saving decisions.
- Each author has an isolated worktree, a module/file boundary, a notes file and
  a commit. The coordinator reads each diff and integrates it.
- Coordinator-only: config, shared tooling, existing check scripts, CI,
  `AGENTS.md`, README, maintenance docs, task list, orchestration log and cutover.
- Existing course prose, demo fences, original slide boundaries, neutral
  examples, type hints and the Wordle exercise contracts remain authoritative.
- Every animation has finite, reversible steps, a useful static final state and
  reduced-motion behaviour. No automatic resizing or pagination.
- Show the rendered pilot before rollout, following the shared
  [orchestration guide](../../../Presentation-Template/docs/agents/orchestration.md).
- No push, deployment or shared-production merge is included in this local
  implementation run.

## Run log

- Planning: both repositories clean; course branch `feature/slidev-course` at
  `77a1478`, shared feature worktree at `fb036ff`.
- Live model catalogue confirms `claudeAgent / claude-opus-5-5` and
  `codex / gpt-6-luna`.
- User scope and source/default decisions recorded above. No delegated work had
  begun when those decisions were requested.
- Baseline rerun: shared TypeScript check and all five converter tests pass;
  existing Python animations match five list and three tuple states; 556 Python
  fences and all exercise slide references pass; Ruff passes.
- Existing built-course validation rerun: 241 pages, 226 topics, zero failures.
  The known FloatingVue private-patch warning is still recorded.
- Started isolated Opus Data Structures pilot and Luna parity/diagram audit.
  The remaining module packages wait for the rendered pilot review.
- Trainer approved the rendered pilot style for the remaining modules. Rollout
  uses stationary code with an active line, moving values/references and
  reversible steps. Opus authors focus on animation implementation and basic
  sanity checks; Luna and the coordinator own detailed verification, per the
  trainer's explicit request to reduce Opus verification tokens.
- Bounded rollout packages: core (01, 02, 04, 05), middle (06, 07, 08),
  stateful (09, 10, 11), appendices (12, 13). Each module is inspected; additions
  are chosen where motion explains a mechanism. No quota/usage tool is exposed
  by the live provider catalogue.
- Started core and middle author tasks plus Luna's student/browser gate task.
  The trainer cancelled the middle author during source inspection to conserve
  quota. Core continues; middle, stateful and appendices remain queued, with
  only one Opus task to run at a time.
- Integrated core author `f2a0eba`: ten native additions across 01, 02, 04 and 05,
  65 states / 55 clicks, reusing the pilot shell. The combined course now has
  257 pages, with its 226 original topics and 299 fences unchanged. Detailed
  verification follows in a fresh Luna round. The core notes record grouped
  loop/call line execution; these states need tracing rather than prefix runs.
- Integrated middle author `986c3db`: six additions across 06/07/08, 34 states
  and 28 clicks. Full-course verification follows; the stateful author package
  (09/10/11) is next, still one Opus task at a time.
- Stateful author hit Claude's five-hour limit. User explicitly chose to wait,
  keeping Claude Opus 5.5. Four partial 09/10 slides and two components are saved
  as WIP `aa47245b10c73d14c6273ffda7493f76946e4d93` on
  `t3/slidev-native-animations`, checkout
  `C:/Users/feiko/.t3/worktrees/Python-Programming/t3-54be0d52`.
  They are not integrated or verified; module 11 remains to be authored.
- Provider reports reset 16:40 Europe/Amsterdam on 2026-10-18. A 16:45 daily
  wake-up is configured to delete itself on its first trigger, then launch one
  new stateful author round from the WIP commit. Timer ID:
  `scheduled-task:command:mcp:65d72ca9-7c48-4607-8a2d-6e8cc26ddf97:schedule-task:slidev-20261018-claude-reset-resume`.
  Do not substitute providers/models or duplicate a manually resumed author.
- Integrated Luna core verification `6f4bd4a`: all 65 states match traced Python,
  130 settled forward/reverse browser frames pass, reduced motion and motion
  containment pass, and the 10 final / 65 click PDF pages were reviewed. The
  coordinator clarified the final return caption to account for the function
  binding remaining in global scope; no animation state changed.
- Trainer stopped further Luna verification rounds to conserve tokens. Middle
  round r5 was interrupted during mapping, before a checker or report was
  completed. No further Luna agents are to be launched automatically. Existing
  checks remain available; the coordinator runs focused checks where edits need
  them rather than commissioning exhaustive per-state checking infrastructure.
- Trainer explicitly authorizes a module 05 content rework: replace abstract
  syntax, show_message, change_me and summation with useful concrete examples;
  introduce annotations after calls/results are understood. Keep the accepted
  animations and retarget their data/code. Use delivery pricing for function
  fundamentals and CSV export columns for mutation versus rebinding. Update
  slides, demos, native additions, existing checks and exercise references as
  needed; preserve the Wordle solution contracts. This is an explicit exception
  to the migration's earlier unchanged-source baseline, which must be recounted.
