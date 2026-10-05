#!/usr/bin/env bash
# ==============================================================================
# Automated Merge Conflict Generation & Resolution Simulation
# ==============================================================================

set -e

DEMO_DIR="/tmp/git_conflict_demo"
rm -rf "$DEMO_DIR"
mkdir -p "$DEMO_DIR"
cd "$DEMO_DIR"

git init -b main
git config user.name "Lead Engineer"
git config user.email "lead@datacamp.internal"

cat << 'EOF' > config.py
BATCH_SIZE = 1000
TIMEOUT_SECONDS = 30
EOF
git add config.py
git commit -m "feat: initial configuration"

git switch -c feature/high-throughput
sed -i 's/BATCH_SIZE = 1000/BATCH_SIZE = 50000/' config.py
git add config.py
git commit -m "perf: scale batch size for high throughput"

git switch main
sed -i 's/BATCH_SIZE = 1000/BATCH_SIZE = 5000/' config.py
git add config.py
git commit -m "perf: moderate batch size increase on main"

echo "=== Attempting Merge (Expecting Conflict) ==="
set +e
git merge feature/high-throughput
set -e

echo "=== Conflict Detected! Inspecting Status ==="
git status

echo "=== Resolving Conflict Programmatically ==="
cat << 'EOF' > config.py
# Reconciled setting based on memory benchmarking
BATCH_SIZE = 25000
TIMEOUT_SECONDS = 30
EOF

git add config.py
git commit -m "merge: resolve BATCH_SIZE conflict by setting calibrated value of 25000"

echo "=== Conflict Successfully Resolved ==="
git log --graph --oneline -n 3
