# 📥 Importing Data in Python: Flat Files, Binaries & Database Connections

> **Track:** Data Engineering in Python  
> **Module:** 06 - Importing Data in Python  
> **Focus:** Context Managers, NumPy I/O, Heterogeneous Binaries (HDF5, SAS, Stata, Pickle), SQLite & SQLAlchemy

---

## 1. File I/O & Context Managers

The bedrock of data ingestion is safe file handling using context managers (`with open`), ensuring file descriptors are closed even when exceptions occur:

```python
# Streaming line-by-line without loading entire file into memory:
with open("telemetry_huge.log", mode="r", encoding="utf-8") as file:
    for line in file:
        if "ERROR" in line:
            process_alert(line)
```

---

## 2. Ingesting Scientific & Heterogeneous Binary Formats

| Format | Extension | Python Library | Primary Industry Use Case |
| :--- | :--- | :--- | :--- |
| **NumPy Array** | `.npy` / `.npz` | `np.load()` / `np.save()` | Machine learning weights, tensor matrices |
| **Pickle** | `.pkl` | `pickle.load()` | Internal Python object serialization (Warning: Insecure!) |
| **Excel** | `.xlsx` / `.xls` | `pd.read_excel()` | Business sheets, multi-tab reporting |
| **SAS** | `.sas7bdat` | `pd.read_sas()` | Pharmaceutical trials, clinical research, banking |
| **Stata** | `.dta` | `pd.read_stata()` | Econometrics, academic statistical studies |
| **HDF5** | `.h5` / `.hdf5` | `h5py.File()` | High-volume IoT sensor streams, genomics (>100GB) |
| **MATLAB** | `.mat` | `scipy.io.loadmat()` | Engineering simulations, signal processing |

## 3. Relational Database Ingestion via SQLAlchemy

Direct DB ingestion bypasses intermediate flat files. Using SQLAlchemy engines establishes robust database connectivity:

```python
from sqlalchemy import create_engine
import pandas as pd

# Creating connection engine
engine = create_engine("sqlite:///enterprise_dw.db")

# Executing parameterized SQL queries into DataFrame
query = """
    SELECT customer_id, SUM(order_total) AS total_revenue
    FROM orders
    WHERE order_date >= :start_date
    GROUP BY customer_id
    HAVING SUM(order_total) > 1000
"""

df_vip = pd.read_sql(query, con=engine, params={"start_date": "2026-01-01"})
```
