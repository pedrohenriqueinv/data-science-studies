#!/usr/bin/env bash
# ==============================================================================
# Capstone 3 Solution: Repairing Nested Git Repositories in Enterprise Projects
# ==============================================================================

set -e

TARGET_DIR="/tmp/enterprise_telemetry_project"
rm -rf "$TARGET_DIR"
mkdir -p "$TARGET_DIR/telemetry/ingestion"
cd "$TARGET_DIR"

echo "[1] Setting up root enterprise repository..."
git init
git config user.name "Lead Engineer"
git config user.email "lead@enterprise.com"

echo "print('Root pipeline')" > telemetry/main.py
echo "print('Ingestion worker')" > telemetry/ingestion/worker.py

echo "[2] Simulating accidental nested git init..."
cd telemetry/ingestion
git init
cd "$TARGET_DIR"

echo "[3] Auditing: Locating accidental nested .git directories..."
find . -mindepth 2 -name ".git" -type d

echo "[4] Fixing: Removing nested .git directory safely..."
rm -rf telemetry/ingestion/.git

echo "[5] Staging and committing clean unified repository..."
git add telemetry/
git commit -m "feat(telemetry): unify telemetry module and remove nested git boundary"

echo "[6] Verifying repository integrity..."
git status
git log --oneline
