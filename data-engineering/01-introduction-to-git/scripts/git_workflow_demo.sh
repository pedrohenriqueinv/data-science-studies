#!/usr/bin/env bash
# ==============================================================================
# Git Fundamentals Automation & Workflow Demonstration
# Simulates full lifecycle: init, staging, commits, log inspection, and revert
# ==============================================================================

set -e

DEMO_DIR="/tmp/git_fundamentals_demo"
rm -rf "$DEMO_DIR"
mkdir -p "$DEMO_DIR"
cd "$DEMO_DIR"

echo "=== [1] Initializing New Git Repository ==="
git init
git config user.name "Data Engineer"
git config user.email "engineer@datacamp.internal"

echo "=== [2] Creating Data Pipeline Files ==="
cat << 'EOF' > pipeline.py
def ingest_data():
    print("Ingesting telemetry records...")

if __name__ == "__main__":
    ingest_data()
EOF

cat << 'EOF' > .gitignore
*.pyc
__pycache__/
*.log
.env
data/raw/*.csv
EOF

echo "=== [3] Staging and Committing Baseline ==="
git add .gitignore pipeline.py
git commit -m "feat: initial commit for data ingestion pipeline"

echo "=== [4] Making Changes & Viewing Diffs ==="
cat << 'EOF' >> pipeline.py

def clean_data():
    print("Cleaning telemetry records...")
EOF

echo "--- Unstaged Diff ---"
git diff

echo "=== [5] Staging Changes and Committing ==="
git add pipeline.py
git commit -m "feat: add clean_data routine"

echo "=== [6] Reverting a Problematic Commit Safely ==="
git revert HEAD --no-edit

echo "=== [7] Final Formatted Commit Graph ==="
git log --oneline --graph --all --decorate

echo "Demo completed successfully in $DEMO_DIR"
