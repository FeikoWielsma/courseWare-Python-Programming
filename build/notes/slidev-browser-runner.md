# Slidev browser delivery gate

`bun run build/check-slidev-delivery.ts` serves the staged public student app
from `build/slidev/dist/student`, finds every `build/slidev_checks/check_*.py`,
and runs each as `uv run python ... --browser <origin>`. The checks run as
asynchronous child processes while Bun's HTTP server remains active. The gate
awaits each check sequentially to keep only one checking browser active. It
also runs `check_delivery.ts` against the same origin for physical wheel,
momentum, editable-control and slide-boundary navigation. It closes the browser
and server in `finally` and exits nonzero when a child check fails.

Set `PRESENTATION_TEMPLATE_DIR` to a Slidev-capable Presentation-Template
worktree. The browser probe accepts `--origin` and `--output`; without those
options it retains its standalone mode and serves the local build itself.

## Pilot package evidence

Run from the course root in PowerShell:

```powershell
$env:PRESENTATION_TEMPLATE_DIR='C:/Git/courseWare/_worktrees/presentation-template-slidev'
bun run build/check-slidev-delivery.ts
```

For this isolated checkout, the ignored `build/slidev/dist/student` folder and
`manifest.json` were copied from the coordinator's staged build. The runner
served that packaged folder on an ephemeral loopback port. Results:

- `check_data_structures.py`: six slides and 33 states matched Python; all 33
  rendered browser states matched Python.
- Physical delivery probe: ordinary forward/reverse, physical wheel
  forward/reverse, momentum grouping, Ctrl-wheel exclusion, scrollable content,
  editable control and source-slide boundary forward/reverse passed.
- The packaged server returned the app from the student output folder; no
  rebuild or write to the coordinator output was performed.

The staged `build/dist/Python-Programming-slides.zip` contains 5,716 entries.
`ZipFile.testzip()` returned no CRC failures. Every `slides/` archive entry
matched the corresponding staged student file by SHA-256. The only entry outside
`slides/` is `default-probe.pdf`, whose SHA-256 matches the staged
`course-slidev.pdf`. No comparison output or manifest is in the archive.

The runner currently discovers the Data Structures pilot as the only
`check_*.py`. It is ready to include later package checks by filename; no
unwritten-module checks were added here.
