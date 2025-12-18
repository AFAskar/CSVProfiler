#!/usr/bin/env bash
set -euo pipefail
test -f .venv/bin/activate && source .venv/bin/activate
rm -rf output/demo
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
  - dnf:   sudo dnf install vhs

After installing, ensure `vhs` is on your PATH.
EOF
  exit 1
fi

if ! command -v glow >/dev/null 2>&1; then
  cat >&2 <<'EOF'
Missing dependency: glow

The demo tape renders Markdown using `glow`.

Install options (pick one):
  - Snap:  sudo snap install glow
  - Brew:  brew install glow
  - Go:    go install github.com/charmbracelet/glow@latest
  - dnf:   sudo dnf install glow

After installing, ensure `glow` is on your PATH.
EOF
  exit 1
fi

cd "$repo_root"

# Generate docs/cli-demo.gif
vhs "$tape_file"

echo "Removing Demo Generated Files"
rm -rf output/demo
echo "Generated: $repo_root/docs/cli-demo.gif"
