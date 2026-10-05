# 🔄 ETL and ELT in Python: Pipeline Architecture & Production Storage

> **Track:** Data Engineering in Python  
> **Module:** 10 - ETL and ELT in Python  
> **Focus:** ETL vs ELT Paradigms, Columnar Storage (Parquet), Transactional Safety, Idempotency

---

## 1. Architectural Paradigms: ETL vs ELT

```
ETL (Extract - Transform - Load):
[ Sources ] ──► [ Extraction Engine ] ──► [ Transform Server (Python/RAM) ] ──► [ Clean DW/BI ]
* Ideal for: Strict privacy (stripping PII before storage), legacy relational data warehouses.

ELT (Extract - Load - Transform):
[ Sources ] ──► [ Extraction Engine ] ──► [ Raw Storage / Data Lake ] ──► [ In-Warehouse SQL Transform ]
* Ideal for: Modern Cloud Data Warehouses (BigQuery, Snowflake, Databricks), massive scale.
```

### Architectural Comparison Matrix

| Dimension | ETL (Extract-Transform-Load) | ELT (Extract-Load-Transform) |
| :--- | :--- | :--- |
| **Compute Placement** | Dedicated worker/pipeline server | Distributed Cloud Data Warehouse |
| **Raw Data Retention** | Often discarded or lost | Preserved 100% in raw staging layers |
| **Transform Tooling** | Python, Spark, Pandas | dbt, SQL, BigQuery, Snowflake |
| **Flexibility** | Rigid; changes require re-ingesting | Highly agile; recalculate transforms retroactively |
| **Data Privacy (PII)** | Anonymized *before* reaching storage | Anonymized *inside* warehouse via views |

---

## 2. Modern Storage: Parquet vs CSV

In production data lakes, CSV is an anti-pattern. **Apache Parquet** provides:
* **Columnar Layout:** Scans only queried columns, slashing I/O by up to 95%.
* **Compression:** Snappy/GZIP compression reduces storage costs by 80%.
* **Embedded Schema:** Stores data types, nullability, and min/max statistics per chunk.

## 3. Idempotency & Transactional Safety

An **Idempotent Pipeline** can be executed multiple times with identical parameters without altering the final state of the database or duplicating records.

### Idempotency Strategies:
1. **Partition Overwriting:** Overwrite the target partition (`YEAR=2026/MONTH=10`) rather than appending.
2. **Upsert (MERGE INTO):** Match on primary key; update existing records, insert new ones.
3. **Staging Table Swap:** Load data into a temporary table, validate integrity, and perform an atomic transaction swap.

## 4. Practical Exercises & Capstone Solutions

### Exercise 1: Pipeline Idempotency Guarantee
* **Problem:** An hourly ingestion job failed at 14:45. Re-running it resulted in duplicated revenue metrics for hour 14. How do you prevent this?
* **Solution:** Replace blind `INSERT` with an idempotent upsert (`ON CONFLICT ... DO UPDATE`) or clear the specific execution partition before writing (`DELETE FROM table WHERE batch_hour = '14'`).

### Exercise 2: Column Pruning with Parquet
* **Problem:** A dataset has 400 columns, but your reporting query only uses 3.
* **Solution:** Use `pd.read_parquet('dataset.parquet', columns=['user_id', 'country', 'revenue'])`. Parquet reads only the byte offsets for those 3 columns directly from disk.
