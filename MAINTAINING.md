# Maintaining PRG400

[AGENTS.md](AGENTS.md) contains the course rules and source contracts. The
[course backlog](docs/backlog.md) records trainer-deferred exercise work and
known rendering issues. For shared tools and Slidev behavior, use the
[configured build guide](../Presentation-Template/docs/courseware.md),
[source tools guide](../Presentation-Template/docs/course-tools.md) and
[Slidev guide](../Presentation-Template/docs/slidev.md).

PRG400 declares the fundamentals and libraries decks, their output locations,
bundle allowlist and student repository targets in `courseware.config.ts`.
Build scripts are declared in `build/package.json`; CI calls
`build/ci-build.sh`. The course pins Presentation-Template in
`build/toolchain.json`. Set `PRESENTATION_TEMPLATE_DIR` only for local shared
work; manifests mark those builds so they cannot be released.

The Slidev presentation uses its local launcher. The exercise site opens from
disk and embeds the Marp fallback for portability. The standalone Marp HTML has
an explicit trainer-note waiver; the embedded site copy removes those notes.

## Everyday commands

```bash
bun run --cwd build build                         # fundamentals
bun run --cwd build build -- libraries            # companion deck
bun run --cwd build build -- libraries --serve    # companion authoring
bun run --cwd build build -- --exercises          # exercise PDF
bun run --cwd build site                          # portable exercise site
```

`build/ci-build.sh` runs source checks, the playable Wordle stages, libraries
solutions and each published artifact once. Slidev checks rendered layout and
basic navigation as part of its build. The shared template owns its own tests;
courses do not rerun that toolchain suite on every content edit.

`tests/` contains course-specific checks and fixtures. Optional
`test:animations` runs the exhaustive animation diagnostics against built slides;
`test:examples` runs library demos and checks generated data/native slides. Use
these when changing those examples or animation components. `tools/libraries/`
contains the two authoring generators, not release steps.
