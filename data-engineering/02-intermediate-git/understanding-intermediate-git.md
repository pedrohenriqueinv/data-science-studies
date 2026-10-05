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
