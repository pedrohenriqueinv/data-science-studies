# 🌿 Intermediate Git: Branching, Merging & Remote Synchronization

> **Track:** Data Engineering in Python  
> **Module:** 02 - Intermediate Git  
> **Focus:** Branching Strategies, 3-Way Merges, Conflict Resolution, Remote Tracking

---

## 1. Branching Mechanics & HEAD Pointers

In Git, a branch is not a copy of files; it is an **extremely lightweight 41-byte movable pointer** to a commit hash.

* **`HEAD`:** A reference pointing to the currently checked-out branch or commit.
* **`git switch <branch>` / `git checkout <branch>`:** Moves `HEAD` to point to a different branch reference.
* **Detached HEAD State:** Occurs when `HEAD` points directly to a commit hash rather than a named branch reference. Any commits made here will be orphaned unless a new branch is created.

```
Commit C1 ───► Commit C2 ───► Commit C3 (main)
                              ▲
                             HEAD
```

---

## 2. Fast-Forward vs 3-Way Merge

When integrating changes from a feature branch into `main`:

### A. Fast-Forward Merge
Occurs when no new commits were made on `main` since the feature branch diverged. Git simply advances the `main` pointer forward to the tip of the feature branch. No merge commit is created.

### B. 3-Way Merge (`git merge --no-ff`)
Occurs when `main` and the feature branch have diverged (both have new commits). Git computes a 3-way merge using:
1. **Common Ancestor Commit (Base)**
2. **Current Branch Commit (`HEAD` / Ours)**
3. **Incoming Branch Commit (Theirs)**

Git creates a new **Merge Commit** with two parent hashes.

```
       C3 ───► C4 (feature/etl-parquet)
      ▲         │
     /          ▼
C1 ───► C2 ───────► C5 [Merge Commit] (main)
```

## 3. Merge Conflict Resolution Mechanics

A merge conflict occurs when two branches modify the **exact same line** of code in different ways, or one branch deletes a file that another modified.

### Conflict Markers Anatomy

When Git halts execution due to a conflict, it decorates the file with markers:

```python
<<<<<<< HEAD (Ours - current branch)
DATABASE_URI = "postgresql://prod_user:secret@prod-db.internal:5432/analytics"
=======
DATABASE_URI = "postgresql://etl_user:strong_password@analytics-db.cloud:5432/dw"
>>>>>>> feature/cloud-db (Theirs - incoming branch)
```

### Resolution Protocol:
1. Identify conflicting files via `git status`.
2. Open files and manually edit to reconcile logic.
3. Remove all marker lines (`<<<<<<<`, `=======`, `>>>>>>>`).
4. Stage resolved files: `git add <file>`.
5. Finalize merge: `git commit -m "merge: resolve database URI configuration conflict"`.

---

## 4. Remote Operations: Fetch vs Pull vs Push

| Command | Action | Impact on Working Directory |
| :--- | :--- | :--- |
| `git fetch <remote>` | Downloads commits, tags, and refs from remote to `origin/<branch>` | **Zero impact** on local files. Safe inspection. |
| `git pull <remote> <branch>` | Performs `git fetch` followed immediately by `git merge` | Updates working directory; may trigger conflicts. |
| `git push -u <remote> <branch>` | Uploads local commits and binds upstream tracking branch | Updates remote repository refs. |
