#!/usr/bin/env python3
"""
Modular Production ETL Pipeline with Logging and Validation
"""
import logging
import sqlite3
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class ProductionETL:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path)
        self._setup_schema()

    def _setup_schema(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS dw_daily_sales (
                    date_key TEXT PRIMARY KEY,
                    total_transactions INTEGER,
                    gross_revenue REAL,
                    net_revenue REAL
                )
            """)

    def extract(self) -> pd.DataFrame:
        logging.info("Extracting transactional records from upstream sources...")
        raw_events = [
            {"tx_id": 1, "timestamp": "2026-10-01 10:15:00", "amount": 150.0, "tax": 15.0},
            {"tx_id": 2, "timestamp": "2026-10-01 12:30:00", "amount": 200.0, "tax": 20.0},
            {"tx_id": 3, "timestamp": "2026-10-01 18:45:00", "amount": 350.0, "tax": 35.0},
        ]
        return pd.DataFrame(raw_events)

    def transform(self, df_raw: pd.DataFrame) -> pd.DataFrame:
        logging.info("Transforming: calculating net revenue and daily aggregates...")
        df_raw["date_key"] = pd.to_datetime(df_raw["timestamp"]).dt.strftime("%Y-%m-%d")
        df_raw["net_amount"] = df_raw["amount"] - df_raw["tax"]
        
        aggregated = df_raw.groupby("date_key").agg(
            total_transactions=("tx_id", "count"),
            gross_revenue=("amount", "sum"),
            net_revenue=("net_amount", "sum")
        ).reset_index()
        return aggregated

    def load(self, df_transformed: pd.DataFrame):
        logging.info("Loading: idempotent upsert into data warehouse table...")
        with self.conn:
            for row in df_transformed.itertuples(index=False):
                self.conn.execute("""
                    INSERT INTO dw_daily_sales (date_key, total_transactions, gross_revenue, net_revenue)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT(date_key) DO UPDATE SET
                        total_transactions=excluded.total_transactions,
                        gross_revenue=excluded.gross_revenue,
                        net_revenue=excluded.net_revenue
                """, (row.date_key, row.total_transactions, row.gross_revenue, row.net_revenue))
        logging.info("Load stage completed successfully.")

    def run(self):
        raw = self.extract()
        transformed = self.transform(raw)
        self.load(transformed)

if __name__ == "__main__":
    pipeline = ProductionETL()
    pipeline.run()
