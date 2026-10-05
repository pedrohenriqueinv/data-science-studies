# 📦 Introduction to Git: Architecture, Auditing & Core Commands

> **Track:** Data Engineering in Python  
> **Module:** 01 - Introduction to Git  
> **Focus:** Object Database, SHA-1 Hashing, Staging Lifecycle, Commit Graphs

---

## 1. The Git Internal Object Model

Git is not a delta-based version control system; it is a **content-addressable filesystem** built on four core object types stored in `.git/objects`:

1. **Blob (Binary Large Object):** Compressed binary data of a file. Filenames and permissions are NOT stored in blobs.
2. **Tree:** Represents a directory. Maps filenames and file modes to SHA-1 hashes of Blobs or child Trees.
3. **Commit:** A pointer to a root Tree, containing author/committer metadata, timestamp, commit message, and parent commit hashes.
4. **Annotated Tag:** A permanent reference pointing to a specific commit object with a cryptographic signature or message.

```
       [Commit Object]
              │
              ▼
         [Tree Object] (root directory)
         ┌────┴─────────────────┐
         ▼                      ▼
  [Blob: script.py]       [Tree: pipeline/]
                                │
                                ▼
                         [Blob: config.yaml]
```

---

## 2. Core Workflow & Staging Area

The Git lifecycle operates across three primary local areas:

* **Working Directory:** The actual sandbox where files are edited on disk.
* **Staging Area (Index):** The preparation buffer that determines what will be included in the next commit snapshot.
* **Repository (.git):** The permanent object database holding the history of commits.

### Essential Commands Matrix

| Operation | Command | Technical Behavior |
| :--- | :--- | :--- |
| **Initialize** | `git init` | Creates `.git` database and default branch (`main`) |
| **Status Check** | `git status` | Compares Working Tree vs Index vs HEAD |
| **Stage File** | `git add <file>` | Creates Blob in `.git/objects` and updates Index |
| **Commit Snapshot** | `git commit -m "<msg>"` | Generates Tree and Commit objects, advances HEAD |
| **Inspect History** | `git log --oneline --graph` | Renders DAG of commits with truncated 7-char hashes |
| **Unstage** | `git restore --staged <file>` | Removes changes from Index, preserving Working Tree |
| **Discard Changes** | `git restore <file>` | Replaces Working Tree file with version from Index |

---

## 3. Pitfalls & Anti-Patterns

* **Nested Repositories:** Running `git init` inside a subdirectory of an existing repository creates an untracked git boundary that prevents parent tracking.
* **Committing Large Binary Datasets:** Committing raw CSVs/Parquet (>100MB) inflates the `.git` packfile permanently. Use `.gitignore` and remote cloud storage (S3/GCS) instead.

## 4. Advanced Inspection: Git Diff & Log Formats

Understanding precisely what changed before staging or committing is critical in production pipelines:

```bash
# Compare Working Tree changes against Staging Area (unstaged changes)
git diff

# Compare Staging Area changes against the last commit (staged changes)
git diff --staged

# Compare two distinct commits across history
git diff <commit_hash_1> <commit_hash_2>

# Display commit history showing files modified and change statistics
git log --stat -n 5

# Format log with custom date and author information
git log --pretty=format:"%h - %an, %ar : %s"
```

### Git Revert vs Git Reset

* **`git revert <commit>`:** Creates a brand-new commit that applies the exact inverse patch of the target commit. **Safe for public/shared branches.**
* **`git reset --soft <commit>`:** Moves HEAD to target commit; keeps changes staged.
* **`git reset --hard <commit>`:** Moves HEAD and destroys all uncommitted changes in both Index and Working Directory. **Destructive!**

## 5. Step-by-Step Practical Exercises & Solutions

### Exercise 1: Checking Staged vs Unstaged Differences
* **Problem:** You modified `extract.py` and staged it with `git add`. Then you added another print statement to `extract.py`. How do you inspect ONLY the unstaged print statement?
* **Solution:** Run `git diff`. To view the staged portion, run `git diff --staged`.

### Exercise 2: Unstaging Without Data Loss
* **Problem:** You accidentally ran `git add .` which included a sensitive `.env` file. You need to remove `.env` from staging without deleting the physical file.
* **Solution:** `git restore --staged .env` (or in legacy Git: `git reset HEAD .env`).

### Exercise 3: Inspecting Single-File History
* **Problem:** A data validation function inside `transforms.py` stopped working. How do you inspect all past commits that specifically touched this file?
* **Solution:** `git log -p -- transforms.py`
