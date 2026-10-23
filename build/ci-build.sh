#!/usr/bin/env bash
# Release gates: source contracts, playable exercises, then the actual deliverables.
# Deep animation/demo diagnostics are optional package scripts, not release gates.
set -euo pipefail
cd "$(dirname "$0")/.."
TEMPLATE="${TEMPLATE:-$(bun run build/toolchain.ts --path)}"

echo 'Checking course sources and exercises'
bun run --cwd build test
uv run ruff check .
uv run python "$TEMPLATE/build/tools/check-fences.py"
uv run python "$TEMPLATE/build/tools/check-slide-references.py"
uv run python "$TEMPLATE/build/tools/make-starters.py" --check
uv run python tests/wordle/check.py
uv run python tests/site/check-quiz.py
uv run --project libraries python tests/libraries/check-solutions.py
uv run --project libraries python tests/libraries/check-web.py
uv run --project libraries python tests/libraries/check-dashboards.py
(cd libraries && uv run python "$TEMPLATE/build/tools/check-fences.py")

echo 'Building published artifacts'
bun run --cwd build build
bun run --cwd build build -- --exercises
bun run --cwd build build -- libraries
bun run --cwd build build -- libraries --marp --skip-lint
bun run --cwd build build -- libraries --exercises
# Site assembly builds and embeds the fundamentals Marp fallback.
bun run --cwd build site

echo 'Verifying deliverables'
bun run --cwd build verify -- fundamentals
bun run --cwd build verify -- libraries
