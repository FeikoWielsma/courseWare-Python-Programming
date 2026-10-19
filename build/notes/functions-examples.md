> Historical record (2026-10-18). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# Functions examples rework

Historical first rewrite. The trainer subsequently approved music and photos;
the implemented Functions examples now use `format_duration` and playlists.
See [the current example map](engaging-examples.md).

Trainer feedback on 2026-10-18 authorized replacing the old abstract examples
while retaining the native animation design. This supersedes the earlier
migration requirement to leave all canonical Functions content unchanged.

- Start with unannotated `delivery_cost`, then calls and a usable returned value.
- Show a receipt function before introducing `-> None`.
- Introduce annotations and docstrings after those concrete examples.
- Reuse delivery charges for positional, keyword and default arguments.
- Use CSV export columns for mutation and returning a new list; use delivery
  settings for scope, dispatch details for variable arguments and order totals
  for lambda sorting. Remove the abstract skeleton and retired toy demos.
- Renumber the 15 main demos in teaching order and update demo pills, README,
  exercise hint wording, native additions, route IDs and existing state checks.
- The early unannotated examples are intentional trainer direction; annotations
  remain on the examples after the annotation lesson. Wordle solutions and
  exercise contracts were not changed.

The module now has 19 source slides (previously 17) plus four native additions.
The whole course baseline is now 228 source topics, 241 Marp pages, 265 Slidev
pages and 297 canonical code/output fences. Source changes explain these new
counts; other modules retain their content.

Checks: all 15 main demos run; all 16 Functions Python fences match verbatim,
in-order demo excerpts; the existing core trace checker passes 67 states;
Ruff, fence/reference checks and the module's Marp layout lint pass. The new
rebinding example uses explicit list concatenation before star unpacking, with
a scoped, documented RUF005 exception. Detailed Luna rounds are stopped at the
trainer's request; only focused existing checks and visual review are used.

The first browser pass caught a caption below the frame during the longer
rebinding animation. An explicit 16px code layout reserves room for its call
frame. The list examples also use wider name boxes so function names are legible.
Final export/browser results are recorded in `slidev-integration.md`.
