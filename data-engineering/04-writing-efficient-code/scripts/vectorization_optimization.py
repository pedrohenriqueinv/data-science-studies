#!/usr/bin/env python3
"""
Pandas Row Iteration Hierarchy Optimization Benchmark
Demonstrates the massive performance difference across DataFrame iteration methods:
1. .iloc / .loc loop
2. .iterrows()
3. .itertuples()
4. .apply()
5. Pure Vectorization (.values / arrays)
"""
import time
import pandas as pd
import numpy as np

def run_pandas_hierarchy():
    N = 100_000
    df = pd.DataFrame({
        "temperature_c": np.random.uniform(-10.0, 45.0, size=N),
        "humidity": np.random.uniform(20.0, 95.0, size=N)
    })

    print(f"Benchmarking Pandas operations over {N:,} rows:")

    # Method A: .iterrows() (Returns pd.Series per row - very slow)
    t0 = time.perf_counter()
    res_iterrows = [row["temperature_c"] * 1.8 + 32 for _, row in df.head(1000).iterrows()]
    t1 = time.perf_counter()
    print(f"1. .iterrows() [extrapolated] : ~{(t1 - t0) * 100:.2f}s")

    # Method B: .itertuples() (Returns namedtuples - fast)
    t0 = time.perf_counter()
    res_itertuples = [row.temperature_c * 1.8 + 32 for row in df.itertuples()]
    t1 = time.perf_counter()
    print(f"2. .itertuples()              : {t1 - t0:.4f}s")

    # Method C: Pure Vectorization (NumPy array C-level execution)
    t0 = time.perf_counter()
    res_vec = df["temperature_c"].values * 1.8 + 32
    t1 = time.perf_counter()
    print(f"3. Vectorized Series / NumPy  : {t1 - t0:.4f}s (Optimal)")

if __name__ == "__main__":
    run_pandas_hierarchy()
