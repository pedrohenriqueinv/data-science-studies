# 🧠 Data Science & Cloud Engineering Study Repository

Welcome! This repository is dedicated exclusively to storing my academic notes, theoretical summaries, and study guides in **Data Science, Data Engineering, Database Systems, and Cloud Computing**. 

> 📌 **Note:** This is a comprehensive, production-grade study log and reference library. For hands-on deployments and live portfolio codebases, please visit my personal projects portfolio.

---

## 🗺️ Roadmap & Study Topics

Below is the list of topics documented in this repository:

### ⚙️ [Data Engineering in Python (Career Track)](./data-engineering/README.md)
*   **Version Control & Tooling:** [01. Introduction to Git](./data-engineering/01-introduction-to-git/understanding-git-basics.md) and [02. Intermediate Git](./data-engineering/02-intermediate-git/understanding-intermediate-git.md) (Object models, 3-way merges, conflict resolution, audit tracking).
*   **Language Foundations & Cloud:** [03. Python for Developers & Cloud](./data-engineering/03-python-for-developers-and-cloud/understanding-python-cloud.md) (Time complexities, idiomatic patterns, AWS, Azure, GCP service mapping).
*   **Performance & Architecture:** [04. Writing Efficient Code](./data-engineering/04-writing-efficient-code/understanding-writing-efficient-code.md) (CPython bytecode, line/memory profiling, vectorized NumPy/Pandas) and [05. Software Engineering Principles](./data-engineering/05-software-engineering-principles/understanding-software-engineering-principles.md) (Modularity, OOP, packaging, pytest test suites).
*   **Ingestion & Data Quality:** [06. Importing Data](./data-engineering/06-importing-data-in-python/understanding-importing-data.md) (Context managers, HDF5, SAS, Stata, SQLite), [07. Streamlined Ingestion](./data-engineering/07-streamlined-data-ingestion-pandas/understanding-streamlined-ingestion.md) (Out-of-core chunking, strict dtypes, multi-tab Excel), [08. Cleaning Data](./data-engineering/08-cleaning-data-in-python/understanding-cleaning-data.md) (Constraints, regex, record linkage deduplication), and [09. APIs in Python](./data-engineering/09-introduction-to-apis-in-python/understanding-apis-in-python.md) (HTTP protocol, pagination, rate limits, exponential backoff).
*   **Production Pipelines & Orchestration:** [10. ETL & ELT Pipelines](./data-engineering/10-etl-and-elt-pipelines/understanding-etl-elt.md) (Parquet columnar storage, idempotent upserts, transactional safety) and [11. Apache Airflow](./data-engineering/11-apache-airflow/understanding-apache-airflow.md) (Architecture, TaskFlow API `@task`, FileSensors in reschedule mode, DAG scheduling).

### ☁️ [Cloud Computing](./cloud-computing/understanding-cloud.md)
*   **Concepts:** Virtualization, Scalability (Horizontal vs. Vertical), and Billing Models (Pay-as-you-go).
*   **Service & Deployment Models:** IaaS, PaaS, SaaS, FaaS, Hybrid, and Multicloud.
*   **Providers & Equivalencies:** Core services and case studies from AWS, Azure, and Google Cloud.
*   **Data Regulations:** GDPR, PII, and geographical compliance.

### 🗄️ [DBMS & Relational SQL (SGBD & SQL)](./database-management-systems/understanding-sgbd-sql.md)
*   **Fundamentals & Architecture:** Data vs. Information, DBMS core functions, 3-tier client-server model, internal components (Buffer Manager, Query Optimizer, WAL, MVCC).
*   **ACID & Concurrency:** Atomicity, Consistency, Isolation, Durability, ANSI SQL isolation levels, and concurrency anomalies (Dirty, Non-repeatable, and Phantom reads).
*   **SQL Subgroups & Syntax:** DDL, DML, DQL, DCL, and TCL; key operational traps (`DROP` vs. `TRUNCATE` vs. `DELETE`).
*   **Relational Modeling & Case Study:** University Library database (*Biblioteca Universitária*) with Primary Keys, Foreign Keys, referential actions (`RESTRICT`, `CASCADE`, `SET NULL`), and multi-statement ACID transactions (`SAVEPOINT`, `RETURNING`).
*   **Database Landscape:** Architectural comparison between PostgreSQL, MySQL, Oracle Database, Microsoft SQL Server, SQLite, and MariaDB.

### 🐍 [Python for Developers](./Introducion%20To%20Python%20For%20Developers/understanding-python.md)
*   **Basics & Data Types:** Variables, Strings, Integers, Floats, and Booleans (`type()`).
*   **Data Structures:** Lists, Dictionaries (Key-Value), Sets (Unique items), and Tuples (Immutable).
*   **Manipulation & Methods:** Slicing, indexing, string methods, and collection methods.

---

## 🛠️ How to Study with This Repository (70 / 20 / 10 Framework)

1. **70% Hands-On Code Execution:**
   * Explore the `/scripts` and `/dags` folders inside each module.
   * Run the unit test suites with `pytest`.
   * Recreate the Capstone Challenges in blank files before consulting solutions.
2. **20% Active Recall & Spaced Repetition (Anki):**
   * Import the flashcard `.txt` files located inside each module's `anki-flashcards/` folder into [Anki](https://apps.ankiweb.net/).
   * Practice 15 minutes of daily spaced repetition to retain CLI flags, decorators, and internal memory layouts.
3. **10% Architectural Theory:**
   * Read the `understanding-*.md` guides for deep conceptual mental models, comparison tables, and exam/interview prep.

---

## 📄 License
This repository is licensed under the MIT License. Feel free to use the notes and code for your own learning!
