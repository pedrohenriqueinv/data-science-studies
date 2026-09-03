# 🧠 Data Science & Cloud Engineering Study Repository

Welcome! This repository is dedicated exclusively to storing my academic notes, theoretical summaries, and study guides in Data Science, Data Engineering, Database Systems, and Cloud Computing. 

> 📌 **Note:** This is a theoretical and conceptual study log. For hands-on projects, deployments, and code portfolios, please visit my personal portfolio repository.

---

## 🗺️ Roadmap & Study Topics

Below is the list of topics documented in this repository:

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
*   **Review & Exam Prep:** Pocket cheat sheets, top 6 exam pitfalls, and a 15-question commented assessment test.

### 🐍 [Python for Developers](./Introducion%20To%20Python%20For%20Developers/understanding-python.md)
*   **Basics & Data Types:** Variables, Strings, Integers, Floats, and Booleans (`type()`).
*   **Data Structures:** Lists, Dictionaries (Key-Value), Sets (Unique items), and Tuples (Immutable).
*   **Manipulation & Methods:** Slicing, indexing (positive/negative), string methods (`.lower()`, `.upper()`, `.replace()`), and collection methods (`.keys()`, `.values()`, `.items()`, `.append()`).

---

## 🛠️ How to Use This Repository

If you want to use my notes to study:
1. Navigate to the specific directory of interest (e.g., `/cloud-computing`, `/database-management-systems`, or `/Introducion To Python For Developers`).
2. Read the `.md` (Markdown) files containing organized summaries.
3. (Optional) Run the practical SQL scripts under `/scripts` (such as `biblioteca_universitaria.sql` in PostgreSQL / pgAdmin).
4. (Optional) Import any `.txt` or `.apkg` files inside the `anki-flashcards` directory into your **Anki** to practice active recall.

## 📄 License
This repository is licensed under the MIT License. Feel free to use the notes for your own learning!
