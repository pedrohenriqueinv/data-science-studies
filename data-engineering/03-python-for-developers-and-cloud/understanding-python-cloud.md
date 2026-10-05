# 🐍 Python for Developers & Cloud Infrastructure Foundations

> **Track:** Data Engineering in Python  
> **Module:** 03 - Python for Developers & Cloud  
> **Focus:** Advanced Data Structures, Idiomatic Python, Cloud Providers (AWS/GCP/Azure)

---

## 1. Advanced Python Internals for Data Engineers

### Built-in Collections & Time Complexities

| Data Structure | Implementation | Lookup Complexity | Insertion Complexity | Best Use Case in Pipelines |
| :--- | :--- | :--- | :--- | :--- |
| **`list`** | Dynamic array of C pointers | $O(1)$ by index / $O(n)$ by value | $O(1)$ amortized append | Ordered sequential records |
| **`dict`** | Hash table with open addressing | $O(1)$ average / $O(n)$ worst | $O(1)$ amortized | Key-value lookups, dimension mapping |
| **`set`** | Hash table (keys only) | $O(1)$ average | $O(1)$ average | Deduplication, membership testing |
| **`tuple`** | Fixed-size immutable array | $O(1)$ by index | Immutable ($N/A$) | Database rows, dictionary compound keys |
| **`collections.deque`** | Doubly-linked list of blocks | $O(n)$ random access | $O(1)$ append / popleft | Streaming sliding windows, FIFO queues |

---

## 2. Idiomatic Python & Defensive Programming

```python
from typing import List, Dict, Optional
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def process_batch(records: List[Dict[str, any]], threshold: float = 100.0) -> List[Dict[str, any]]:
    """Filters and transforms a batch of raw telemetry events.
    
    Args:
        records: List of raw dictionaries extracted from message broker.
        threshold: Minimum metric value required to retain record.
        
    Returns:
        List of enriched records with formatted timestamp and normalized metric.
        
    Raises:
        KeyError: If mandatory keys 'device_id' or 'val' are missing.
    """
    cleaned = []
    for item in records:
        try:
            val = float(item["val"])
            if val >= threshold:
                cleaned.append({
                    "device_id": str(item["device_id"]).strip().upper(),
                    "metric_val": val,
                    "status": "VALIDATED"
                })
        except (ValueError, KeyError) as err:
            logging.warning(f"Dropping corrupted record {item}: {err}")
            continue
    return cleaned
```

## 3. Cloud Provider Architecture (AWS vs Azure vs GCP)

In enterprise data engineering, Python code runs on cloud infrastructure. Below is the multi-cloud service equivalence matrix:

```
                    ┌──────────────────────────────────────────────┐
                    │       Enterprise Cloud Data Platform         │
                    └──────────────────────┬───────────────────────┘
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         ▼                                 ▼                                 ▼
   [ Amazon AWS ]                   [ Microsoft Azure ]               [ Google Cloud ]
   • S3 (Object Store)              • ADLS Gen2 (Blob Store)          • Cloud Storage (GCS)
   • EMR / Glue (Spark/ETL)         • Synapse / Databricks            • Dataproc / Dataflow
   • Redshift (Cloud DWH)           • Synapse SQL Dedicated           • BigQuery (Serverless DWH)
   • Lambda (Serverless Python)     • Azure Functions                 • Cloud Functions
```

### Cloud Cost Models:
* **IaaS (Infrastructure as a Service):** Pay for EC2 / Compute Engine VM uptime by the second.
* **PaaS (Platform as a Service):** Pay for managed database engines (AWS RDS, Cloud SQL).
* **Serverless / FaaS:** Pay strictly per execution millisecond and allocated RAM (AWS Lambda, BigQuery query scan volume).

## 4. Practical Exercises & Capstone Solutions

### Exercise 1: Dictionary Lookup vs Linear Search
* **Problem:** You have a 1,000,000-row customer list and need to look up country codes. Why should you avoid `[row['country'] for row in customers if row['id'] == target_id]`?
* **Solution:** Linear scan across a list is $O(n)$. Converting the list once into a lookup dictionary `{row['id']: row['country'] for row in customers}` reduces subsequent lookups to $O(1)$ constant time.

### Exercise 2: Handling Cloud API Timeouts
* **Problem:** When sending payloads to a cloud API (e.g. AWS Lambda or GCP Cloud Function), what Python pattern prevents infinite hanging?
* **Solution:** Explicit socket timeout parameters: `requests.post(url, json=data, timeout=(3.05, 27))` where the tuple defines `(connect_timeout, read_timeout)`.
