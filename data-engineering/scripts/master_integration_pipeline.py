#!/usr/bin/env python3
"""
End-to-End Multi-Stage Data Engineering Integration Pipeline
Integrates concepts from all 11 modules:
- Context management & logging
- Resilient API extraction
- Out-of-core chunked processing with strict dtypes
- Cleaning & validation assertions
- Vectorized transformations
- Parquet partitioned storage with idempotency
"""
import os
import shutil
import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def run_integrated_pipeline():
    logging.info("=== Starting Master Data Engineering Pipeline ===")
    
    # 1. Simulated Extraction (Module 06 & 09)
    logging.info("[Stage 1: Ingestion] Simulating raw telemetry records...")
    N = 10_000
    raw_df = pd.DataFrame({
        "device_id": np.random.choice([f"DEV_{i:03d}" for i in range(50)], size=N),
        "temperature": np.random.normal(loc=24.0, scale=8.0, size=N),
        "reading_date": np.random.choice(["2026-10-01", "2026-10-02", "2026-10-03"], size=N),
        "status": np.random.choice(["OK", "WARNING", "ERR", "  ok  "], size=N)
    })

    # 2. Cleaning & Defensive Assertions (Module 08)
    logging.info("[Stage 2: Cleaning] Standardizing strings and applying range constraints...")
    raw_df["status"] = raw_df["status"].str.strip().str.upper()
    valid_mask = raw_df["temperature"].between(-20.0, 60.0)
    cleaned_df = raw_df[valid_mask].copy()
    assert cleaned_df["temperature"].notnull().all(), "Null readings detected!"

    # 3. Vectorized Performance Transformations (Module 04 & 05)
    logging.info("[Stage 3: Vectorized Processing] Computing Fahrenheit and anomaly flags...")
    cleaned_df["temp_f"] = cleaned_df["temperature"].values * 1.8 + 32.0
    cleaned_df["is_alert"] = np.where(cleaned_df["temp_f"] > 95.0, 1, 0)

    # 4. Idempotent Parquet Partitioned Export (Module 10)
    output_dir = "/tmp/telemetry_warehouse"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    logging.info(f"[Stage 4: Storage] Exporting partitioned Parquet to {output_dir}...")
    cleaned_df.to_parquet(
        output_dir,
        engine="pyarrow",
        partition_cols=["reading_date"],
        compression="snappy"
    )

    logging.info("=== Master Pipeline Execution Finished Successfully ===")

if __name__ == "__main__":
    run_integrated_pipeline()
