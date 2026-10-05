#!/usr/bin/env python3
"""
Chunked CSV Streaming Processor with Accumulator
Demonstrates streaming a high-volume simulated transaction file with fixed memory footprint.
"""
import io
import pandas as pd
import numpy as np

def simulate_chunked_streaming():
    # Generate in-memory CSV with 10,000 records
    print("Generating simulated transaction stream...")
    rows = []
    for i in range(10_000):
        rows.append(f"{i},{'EUR' if i % 2 == 0 else 'USD'},{np.random.uniform(10, 500):.2f}")
    csv_raw = "tx_id,currency,amount\n" + "\n".join(rows)

    # Process stream in bounded chunks of 2,500 rows with strict dtypes
    dtypes = {
        "tx_id": "uint32",
        "currency": "category",
        "amount": "float32"
    }
    
    stream = io.StringIO(csv_raw)
    reader = pd.read_csv(stream, chunksize=2500, dtype=dtypes)
    
    currency_totals = {}
    for batch_idx, chunk in enumerate(reader):
        print(f"Processing chunk {batch_idx + 1} | RAM: {chunk.memory_usage(deep=True).sum() / 1024:.2f} KB")
        grouped = chunk.groupby("currency", observed=True)["amount"].sum()
        for curr, val in grouped.items():
            currency_totals[curr] = currency_totals.get(curr, 0.0) + val

    print("\nFinal Stream Aggregation Results:")
    for curr, total in currency_totals.items():
        print(f"  - {curr}: ${total:,.2f}")

if __name__ == "__main__":
    simulate_chunked_streaming()
