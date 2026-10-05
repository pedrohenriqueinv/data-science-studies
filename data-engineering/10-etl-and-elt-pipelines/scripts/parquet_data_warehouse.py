#!/usr/bin/env python3
"""
Parquet Columnar Data Warehouse Partitioning & Ingestion
"""
import os
import shutil
import pandas as pd
import numpy as np

def demonstrate_parquet_partitioning():
    output_dir = "/tmp/warehouse_partitioned"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    print("Generating multi-region transaction logs...")
    df = pd.DataFrame({
        "event_id": np.arange(10_000),
        "region": np.random.choice(["US-EAST", "EU-WEST", "AP-SOUTH"], size=10_000),
        "year": 2026,
        "amount": np.random.exponential(scale=50.0, size=10_000)
    })

    print(f"Writing partitioned Parquet dataset to {output_dir}...")
    df.to_parquet(
        output_dir,
        engine="pyarrow",
        partition_cols=["region", "year"],
        compression="snappy"
    )

    print("Reading single partition EU-WEST with zero disk scan of other regions:")
    df_eu = pd.read_parquet(
        output_dir,
        filters=[("region", "==", "EU-WEST")]
    )
    print(f"Loaded {len(df_eu)} rows from EU-WEST partition.")

if __name__ == "__main__":
    demonstrate_parquet_partitioning()
