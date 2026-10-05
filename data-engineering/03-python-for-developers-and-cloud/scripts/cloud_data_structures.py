#!/usr/bin/env python3
"""
Python Advanced Data Structures & Memory Overhead Benchmark
"""
import sys
from collections import deque

def demonstrate_collections():
    print("=== [1] Memory Footprint: List vs Tuple vs Set ===")
    sample_size = 1000
    sample_list = list(range(sample_size))
    sample_tuple = tuple(range(sample_size))
    sample_set = set(range(sample_size))
    
    print(f"List ({sample_size} ints)  : {sys.getsizeof(sample_list)} bytes")
    print(f"Tuple ({sample_size} ints) : {sys.getsizeof(sample_tuple)} bytes")
    print(f"Set ({sample_size} ints)   : {sys.getsizeof(sample_set)} bytes (Hash table overhead)")
    
    print("\n=== [2] Efficient FIFO with deque ===")
    queue = deque(maxlen=5)
    for i in range(10):
        queue.append(f"event_{i}")
    print(f"Sliding window of last 5 events: {list(queue)}")

if __name__ == "__main__":
    demonstrate_collections()
