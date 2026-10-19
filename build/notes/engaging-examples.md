> Historical record (2026-10-18). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# Engaging examples implementation

The trainer approved this rewrite on 2026-10-18: music and photos recur through
the course, game characters teach Classes, and a film watchlist teaches SQLite.
This supersedes the migration's unchanged-canonical-example requirement within
the assigned modules. The Wordle exercise spine and solutions remain unchanged.

## Example map

- 01: retain the first Hello Python run; use meaningful photo/music names for
  comments, indentation and multiline syntax. Prefer normal four-space blocks.
- 02: track durations, volume and filenames; clean pasted names, format useful
  output and show a short multiline message. Keep reference tables as reference.
- 03: playlists, photo files and festival lineups; lists have a visible order,
  tuples have named roles, dictionaries have meaningful keys, sets answer an
  overlap/missing-items question. Keep the shared-row demonstration explicit.
- 04: photo self-timer, playlist traversal, skipping unavailable tracks, finding
  a suitable track and player commands. Replace statement(s) templates, Gumby,
  letter skipping and the square-root search with concrete executable code.
- 05/06: `format_duration(seconds)` returns a display such as `3:42`; calls and
  returned results precede annotations/docstrings. Playlist mutation versus a
  returned copy, playback settings for scope, track-duration sorting. Reuse
  duration formatting from a module, package and command-line entry point.
- 07: photo filenames, album sizes and track durations. Retain loop equivalents
  for comprehension syntax, filtering and flattening. Recognition-only forms
  remain short and explain a useful transformation.
- 08: parse a track duration, catch specific failures and report the original
  value. Raise ValueError for an invalid duration; an assertion demonstrates an
  internal programmer assumption. Avoid artificial NameError messages and a
  first lesson dominated by bare except or file APIs taught only in module 09.
- 09: small photo/music text files and CSV listening history. Show useful text
  reading with `with` before manual close/internal layers; retain file modes,
  binary IO, encoding, positions and pathlib coverage. No image processing
  package is needed; supplied file names and the existing small image suffice.
- 10: one SQLite film watchlist throughout; add films, mark one watched, rate,
  query and demonstrate commit/rollback. First query is short, not dominated
  by error-handling boilerplate. Keep connections/cursors, parameter binding,
  generated IDs, aggregation, row factory and metadata coverage.
- 11: game characters with independent health/state and meaningful actions.
  Instances and instance methods precede shared class attributes. Plain public
  attributes first, a computed property, then a validating setter that keeps
  calling code unchanged. Inheritance remains introductory only.
- 12: recap the actual music/photo signatures and collections, optional lookup,
  runtime versus checker behaviour and a closed set of playback modes.
- 13: photo dates, playlist JSON, media filenames/logs for regex, a script's
  playlist argument and tests of familiar duration formatting/parsing. A failing
  test should expose a plausible code defect, not claim that 2 + 3 equals 6.

## Ownership and execution

The coordinator owns 01-08 canonical slides/demos and retargeting existing
animations, all existing checks/config, README, release/build/site integration
and this log. The coordinator also refreshes appendix canonical content before
the final appendix animation package. Keep slide titles and demo file stems
where practical so exercise references and routes stay stable; report any
necessary changes and update their consumers.

One Claude Opus 5.5 author owns 09-11 canonical slides/demos plus the existing
partial `src/slidev/stateful/` package and `Stateful*.vue` components. Merge WIP
aa47245b10c73d14c6273ffda7493f76946e4d93 first; its old unchanged-source and Luna
instructions are superseded by this approved scope and the latest shared brief.
Retarget the saved file/record animations, finish useful character animations
and record exact insertion titles and demo provenance in slidev-stateful.md.

Only minimal author output/syntax checks. No new checker infrastructure, full
browser/PDF audits or nested agents. The coordinator uses existing checks and
targeted rendered review. No further Luna rounds. No pushes, publishing or
shared-production merge. The one-use quota timer was deleted at manual resumption
so it cannot launch a duplicate author.

## Implementation log

- Coordinator source/native rewrite saved in `46dfeb5`: modules 01-08 and both
  appendix sources. Ninety-three changed main demos compile; 92 execute with
  their intended success or deliberate exception. The continuous-input demo
  compiles but is not left running. Existing core checks pass 68 states; Data
  Structures passes 33 states, plus five legacy list and three tuple snapshots.
  All six middle programs match their demos and displayed output. Seven pytest
  cases pass; the deliberately broken formatter produces the quoted `1:0`
  versus `1:00` failure. Mypy produces the two intended type errors.
- Opus stateful `9af38f8` integrated: 09-11 canonical examples and seven native
  additions, 52 states. IO now introduces with before manual close; film watchlist
  and game-character examples replace Cars/Friends and Employee/Square.
- An app-owned automatic resumption of the old quota-limited task briefly
  overlapped r2, finished as `e5e6aa3` and was reused by r2. Old resumptions were
  cancelled; no further old run is queued. Only one new author runs at a time.
- Shared `82f5134` fixes UnoCSS treating duration labels such as `[3:42]` as
  invalid arbitrary CSS declarations. A focused regression test and shared
  typecheck pass. Shared production remains unchanged.
- First full build found seven overflow observations on five canonical pages.
  Added explicit compact layouts for four collection slides and shortened the
  formatting slide's duplicated output. Rebuild/render checks follow integration.
- Appendix canonical examples are ready for one final Opus animation package.
  No further Luna review rounds or new exhaustive check infrastructure.
- Completed appendix package `b054bcc`: optional duration lookup and playlist
  JSON round trip, 12 states. Both insertions are integrated. The coordinator
  completed focused browser/export review and the default-delivery cutover;
  [current counts, verification and limits](slidev-rollout.md) supersede the
  intermediate stopping points above.
- 2026-10-18 trainer review: invented track names replaced by well-known songs
  with their real lengths (Imagine 183, Yesterday 125, Respect 149, Toxic 199,
  Thriller 357, Hey Jude, Let It Be, Jolene, Wonderwall, Bohemian Rhapsody).
  Set operations use physics/chemistry again (Curie in both); the else slide
  uses a fixed battery value; the for-loop slide loops over a playlist and a
  string, and the index/enumerate slides use the playlist instead of planets.
- 2026-10-18 trainer review: Classes use World of Warcraft characters (Jaina,
  Thrall, Hogger; `max_level` 60 raised to 70 by an expansion; `Mage` as the
  subclass). A new slide and demo, *A First Attribute and Method*
  (`02_firstmethod.py`), introduce one attribute and one method before health;
  the later class demos moved up one number.
