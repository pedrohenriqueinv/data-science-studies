#!/usr/bin/env bash
# ==============================================================================
# Branching, 3-Way Merging & Fast-Forward Demonstration
# ==============================================================================

set -e

DEMO_DIR="/tmp/git_branching_demo"
rm -rf "$DEMO_DIR"
mkdir -p "$DEMO_DIR"
cd "$DEMO_DIR"

git init -b main
git config user.name "Data Engineer"
git config user.email "engineer@datacamp.internal"

echo "print('Base pipeline v1.0')" > pipeline.py
git add pipeline.py
git commit -m "feat: initial pipeline on main"

echo "[1] Creating and switching to feature branch..."
git switch -c feature/parquet-export

echo "print('Exporting records to Apache Parquet format')" >> pipeline.py
git add pipeline.py
git commit -m "feat(storage): implement parquet export"

echo "[2] Switching back to main and creating non-conflicting commit..."
git switch main
echo "# Pipeline documentation" > README.md
git add README.md
git commit -m "docs: add pipeline documentation"

echo "[3] Performing 3-Way Merge..."
git merge feature/parquet-export -m "merge: integrate parquet export feature"

echo "[4] Inspecting visual DAG graph..."
git log --graph --oneline --all --decorate
