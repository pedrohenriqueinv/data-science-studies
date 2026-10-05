#!/usr/bin/env python3
"""
Automated SQLite Schema Introspection & Metadata Extraction
"""
import sqlite3

def inspect_database_schema():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # Create sample normalized tables
    cursor.execute("""
        CREATE TABLE dim_customer (
            customer_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            tier TEXT DEFAULT 'STANDARD'
        )
    """)
    cursor.execute("""
        CREATE TABLE fact_transaction (
            tx_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            amount REAL,
            FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id)
        )
    """)
    conn.commit()

    # Query sqlite_master to introspect tables
    cursor.execute("SELECT type, name, sql FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print(f"Discovered {len(tables)} tables in schema:")
    for t_type, name, ddl in tables:
        print(f"\n--- Table: {name} ---")
        print(ddl)

    conn.close()

if __name__ == "__main__":
    inspect_database_schema()
