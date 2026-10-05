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
