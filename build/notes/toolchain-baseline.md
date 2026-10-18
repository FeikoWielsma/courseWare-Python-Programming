# Toolchain baseline (package T0)

Branch `tc/baseline`, worktree `C:/Git/courseWare/_worktrees/prg-tc-baseline`.
Purpose: "before" fingerprints from unchanged code. Artefacts live outside git in
`C:/Git/courseWare/_baselines/`; see `_baselines/README.md` for commands, versions and
`compare` usage.

## Done

- Python course built against the production template main checkout (`2c1d0f8`,
  read-only, not modified). `PRESENTATION_TEMPLATE_DIR` must be set in this worktree.
- Builds (all exit 0): Slidev deck `--skip-lint` (276 pages), libraries `--skip-lint`,
  `--exercises`, Marp `--marp --skip-lint`.
- `_baselines/fingerprint.py` written; `make` writes per-PDF JSON, `compare` diffs two.
- Fingerprints for the four Python PDFs in `_baselines/python/*.json`.
- Comparison courses: Git-Fundamentals and Bash-Shell-Scripting have no build tooling,
  so they were not built. Go-Programming (PRG350) and PowerShell-Scripting (PRG900) were
  built from throwaway worktrees (since removed); outputs and fingerprints in
  `_baselines/go-programming/` and `_baselines/powershell-scripting/`.

## Environment facts (not code issues)

- Worktree default template path `../Presentation-Template` does not exist; use
  `PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/Presentation-Template`.
- Go and PowerShell `build/package.json` point at `../../Presentation-Template`; run the
  template `build/build.ts` directly from the course `build/` folder instead.
- PowerShell deck refuses to build with 5 lint warnings; baseline used `--force`.

## Commands run

See `_baselines/README.md` (Commands and Timings sections). Logs in `_baselines/logs/`.

## Left

- Nothing for T0. Next package compares candidate builds with
  `fingerprint.py compare python/PRG400-Python-Programming.json <candidate>.json`, etc.
