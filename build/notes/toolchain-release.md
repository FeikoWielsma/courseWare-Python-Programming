# Toolchain stage 5 : release assembly and publishing (T9)

Branch `tc/release`, worktree `prg-tc-release`.
Resumed after the rate limit; `git merge toolchain/integration` committed as `6009c66`.

## Done

- Course configuration declares the bundle allowlist, named Marp HTML notes waiver,
  moving release pointer, student repository and mirror; credentials are env names.
- Workflow uses the pin resolver after installing Bun, preserving all prior gates.
- Build prepares the manifest upload ZIP; a separate publish job restores those bytes.
  Student sync is separate and supports a tag-only dispatch with no build.
- Added `bundle`, `release` and `sync-student` package scripts.

## Left

- YAML and shell validation, template gates, real builds, fake publishing failure/retry,
  local bare-repository sync and PDF comparisons.
- Pin the completed release toolchain and record evidence before completion.

## Decided

- Only the explicit `waiveMarpHtmlNotes` config accepts the existing Marp presenter
  notes; default shared behavior stays strict.
- Workflow concurrency queues releases instead of cancelling an in-flight promotion.
- CI upload/download-artifact v3 stores the prepared ZIP for independent publishing
  retries. Confirm support on the actual Forgejo Actions runner before first release.
- No real Forgejo/GitHub contact and no push. The final merged template must be pushed
  and the course re-pinned by the coordinator before CI can fetch it.
