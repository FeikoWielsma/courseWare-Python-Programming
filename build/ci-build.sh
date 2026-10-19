#!/usr/bin/env bash
# The checks and builds of the CI build job (.forgejo/workflows/release.yml), run from the course root
# with TEMPLATE set to the Presentation-Template folder (bun run build/toolchain.ts --path) and both
# uv projects synced. Every command is gating. Independent groups run side by side, each stopping at
# its first failure; the script fails when any group fails, and prints every group's log in full.
#   1. Python gates (fundamentals, libraries) and deck builds (fundamentals, libraries + site) at once
#   2. check:delivery alone: its wheel probe times gestures in tens of milliseconds
#   3. the manifest checks
set -uo pipefail
: "${TEMPLATE:?Set TEMPLATE to the Presentation-Template folder}"
cd "$(dirname "$0")/.."
logs=$(mktemp -d)
trap 'rm -rf "$logs"' EXIT

# Runs one gating command and reports its time. A failure exits the group's subshell: not set -e,
# which bash ignores in functions called from a condition.
step() {
  local start=$SECONDS
  echo "--- $*"
  "$@" || { local status=$?; echo "--- FAILED (exit $status) after $((SECONDS - start)) s: $*"; exit "$status"; }
  echo "--- $((SECONDS - start)) s: $*"
}

gates_fundamentals() {
  step uv run python -m compileall -q demos solutions libraries/demos libraries/solutions
  step uv run python "$TEMPLATE/build/tools/check-fences.py"
  step uv run python "$TEMPLATE/build/tools/check-slide-references.py"
  step uv run python "$TEMPLATE/build/tools/make-starters.py" --check
  step uv run python build/check-solutions.py
  step uv run python build/site/check-quiz.py
  step uv run ruff check .
}

gates_libraries() {
  step uv run --project libraries python libraries/build/make-data.py --check
  step uv run --project libraries python libraries/build/check-demos.py
  step uv run --project libraries python libraries/build/check-solutions.py
  step uv run --project libraries python libraries/build/check-outputs.py
  step uv run --project libraries python libraries/build/native_states.py --check
  cd libraries || exit
  step uv run python "$TEMPLATE/build/tools/check-fences.py"
}

# The fundamentals Marp fallback and exercises share build/dist, so they stay in one group.
deck_fundamentals() {
  cd build || exit
  step bun run check:animations
  step bun run build -- --force
  step bun run build:marp -- --force
  step bun run build -- --exercises --force
}

deck_libraries() {
  cd build || exit
  step bun run libraries -- --skip-lint --force
  step bun run libraries:marp -- --skip-lint --force
  step bun run lint:libraries
  step bun run libraries -- --exercises --force
  step bun run site
}

delivery() {
  cd build || exit
  step bun run check:delivery
}

manifests() {
  cd build || exit
  step bun run verify -- fundamentals
  step bun run verify -- libraries
}

# Runs the named groups at once, then prints each log in order; fails if any group failed.
together() {
  local -A pids
  local name failed=0 start=$SECONDS
  for name in "$@"; do
    ("$name") > "$logs/$name.log" 2>&1 &
    pids[$name]=$!
  done
  for name in "$@"; do
    if wait "${pids[$name]}"; then status=PASS; else status=FAIL; failed=1; fi
    echo "===== $status $name"
    cat "$logs/$name.log"
  done
  echo "===== $(if ((failed)); then echo FAILED; else echo passed; fi): $* ($((SECONDS - start)) s)"
  return "$failed"
}

together gates_fundamentals gates_libraries deck_fundamentals deck_libraries || exit 1
together delivery || exit 1
together manifests || exit 1
