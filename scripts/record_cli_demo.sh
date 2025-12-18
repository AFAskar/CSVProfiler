#!/usr/bin/env bash
set -euo pipefail
test -f .venv/bin/activate && source .venv/bin/activate
rm -rf outputs/demo
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tape_file="$repo_root/demos/cli-demo.tape"

if [[ ! -f "$tape_file" ]]; then
  echo "Tape not found: $tape_file" >&2
  exit 1
fi

if ! command -v vhs >/dev/null 2>&1; then
  cat >&2 <<'EOF'
Missing dependency: vhs

Install options (pick one):
  - Snap:  sudo snap install vhs
  - Go:    go install github.com/charmbracelet/vhs@latest

After installing, ensure `vhs` is on your PATH.
EOF
  exit 1
fi

cd "$repo_root"

# Generate docs/cli-demo.gif
vhs "$tape_file"

rm -rf outputs/demo
echo "Generated: $repo_root/docs/cli-demo.gif"
