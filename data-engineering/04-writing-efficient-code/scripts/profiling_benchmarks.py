#!/usr/bin/env python3
"""
CPU and Memory Profiling Demonstration for Data Pipelines
Compares naive Python iteration vs built-in comprehensions vs NumPy vectorization.
"""
import time
import sys
import numpy as np

def benchmark_execution():
    N = 2_000_000
    print(f"Generating benchmark dataset with {N:,} elements...")
    data_list = list(range(N))
    data_arr = np.arange(N, dtype=np.int64)

    # 1. Naive Loop
    t0 = time.perf_counter()
    res_loop = []
    for x in data_list:
        res_loop.append(x * 2)
    t1 = time.perf_counter()
    loop_time = t1 - t0
    print(f"[1] Naive For-Loop         : {loop_time:.4f}s (Baseline)")

    # 2. List Comprehension
    t0 = time.perf_counter()
    res_comp = [x * 2 for x in data_list]
    t1 = time.perf_counter()
    comp_time = t1 - t0
    print(f"[2] List Comprehension     : {comp_time:.4f}s ({loop_time/comp_time:.2f}x faster)")

    # 3. NumPy SIMD Vectorization
    t0 = time.perf_counter()
    res_np = data_arr * 2
    t1 = time.perf_counter()
    np_time = t1 - t0
    print(f"[3] NumPy Vectorization    : {np_time:.4f}s ({loop_time/np_time:.2f}x faster!)")

if __name__ == "__main__":
    benchmark_execution()
