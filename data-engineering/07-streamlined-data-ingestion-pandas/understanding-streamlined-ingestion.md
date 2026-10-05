# 🐼 Streamlined Data Ingestion with pandas: Out-of-Core Processing & Strict Typing

> **Track:** Data Engineering in Python  
> **Module:** 07 - Streamlined Data Ingestion with pandas  
> **Focus:** Chunking Patterns, Strict `dtype` Allocation, Excel Multi-Sheet Ingestion, Database Streaming

---

## 1. Out-of-Core Ingestion & The Chunking Pattern

When incoming datasets exceed physical RAM (e.g., 20GB CSV on an 8GB laptop), attempting `pd.read_csv()` causes kernel termination via Out-Of-Memory (OOM).

The **Chunking Pattern** streams the file in bounded batches:

```python
import pandas as pd

# Generator yielding bounded DataFrames
chunk_iterator = pd.read_csv("massive_transactions.csv", chunksize=50_000)

total_revenue = 0.0
for chunk in chunk_iterator:
    # Filter and aggregate in-flight; discard chunk to free RAM
    valid_tx = chunk[chunk["status"] == "SETTLED"]
    total_revenue += valid_tx["amount"].sum()

print(f"Total Aggregated Revenue: ${total_revenue:,.2f}")
```

---

## 2. Memory Reduction via Strict `dtype` Specification

By default, Pandas infers data types as 64-bit (`int64`, `float64`, or `object` strings), wasting up to 80% of RAM. Specifying explicit types drastically reduces memory footprint:

| Default Inferred Type | Optimized Type | RAM Savings | Safe Value Range |
| :--- | :--- | :--- | :--- |
| `int64` (8 bytes) | `int8` (1 byte) | **87.5%** | $-128$ to $127$ |
| `int64` (8 bytes) | `uint16` (2 bytes) | **75.0%** | $0$ to $65,535$ |
| `float64` (8 bytes) | `float32` (4 bytes) | **50.0%** | Standard 7-digit decimal precision |
| `object` (pointer array) | `category` | **Up to 90%** | Columns with low cardinality (< 5% unique values) |
| `object` (string) | `string[pyarrow]` | **60-80%** | Zero-copy Arrow memory buffers |

## 3. Streaming Relational Databases with SQLAlchemy Engines

Querying millions of rows without loading all rows into RAM:

```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql+psycopg2://user:pass@host:5432/db")

# Stream query in batches of 10,000 rows
with engine.connect().execution_options(stream_results=True) as conn:
    for chunk_df in pd.read_sql("SELECT * FROM fact_orders", con=conn, chunksize=10000):
        process_batch(chunk_df)
```
