#!/usr/bin/env python3
"""
High-Performance SQLAlchemy to Pandas Streamer
"""
import sqlite3
import pandas as pd

def demonstrate_db_streaming():
    conn = sqlite3.connect(":memory:")
    
    # Populate test table with 5,000 logs
    conn.execute("CREATE TABLE access_logs (id INTEGER, endpoint TEXT, latency_ms REAL)")
    rows = [(i, "/api/v1/data" if i % 3 == 0 else "/api/v1/auth", (i % 100) * 2.5) for i in range(5000)]
    conn.executemany("INSERT INTO access_logs VALUES (?, ?, ?)", rows)
    conn.commit()

    print("Streaming database query in chunks of 1,000 rows:")
    query = "SELECT endpoint, latency_ms FROM access_logs WHERE latency_ms > 50.0"
    
    total_slow_requests = 0
    for chunk in pd.read_sql(query, conn, chunksize=1000):
        total_slow_requests += len(chunk)
        print(f"  -> Received chunk with {len(chunk)} slow requests")

    print(f"Total slow requests detected: {total_slow_requests}")
    conn.close()

if __name__ == "__main__":
    demonstrate_db_streaming()
