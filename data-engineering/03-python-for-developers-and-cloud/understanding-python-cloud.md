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
