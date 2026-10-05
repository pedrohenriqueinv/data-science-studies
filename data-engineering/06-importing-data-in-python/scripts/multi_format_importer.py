#!/usr/bin/env python3
"""
Multi-Format Ingestion Engine
Demonstrates ingestion across CSV, JSON, SQLite, and in-memory streams.
"""
import sqlite3
import pandas as pd
import io

def run_multi_format_demo():
    print("=== [1] Simulating Ingestion from In-Memory CSV Stream ===")
    csv_payload = """id,sensor_name,temperature,status
101,TEMP_A,23.5,OK
102,TEMP_B,48.2,WARNING
103,TEMP_C,21.9,OK
"""
    df_csv = pd.read_csv(io.StringIO(csv_payload))
    print(df_csv)

    print("\n=== [2] Creating SQLite In-Memory Database and Querying ===")
    conn = sqlite3.connect(":memory:")
    df_csv.to_sql("sensors", conn, index=False)
    
    query = "SELECT sensor_name, temperature FROM sensors WHERE temperature > 25.0"
    df_alerts = pd.read_sql(query, conn)
    print(df_alerts)
    conn.close()

if __name__ == "__main__":
    run_multi_format_demo()
