#!/usr/bin/env python3
"""
End-to-End Data Cleaning & Validation Pipeline
"""
import pandas as pd
import numpy as np

def run_cleaning_pipeline():
    raw_data = {
        "cust_id": [101, 102, 103, 103, 104],  # duplicate 103
        "age": [25, 42, -5, 33, 150],           # invalid -5 and 150
        "join_date": ["2026-01-15", "2025/11/02", "INVALID", "2026-03-01", "2026-02-28"],
        "status": [" active ", "ACTIVE", "InActive", "suspended", "UNKNOWN_VAL"]
    }
    df = pd.DataFrame(raw_data)
    print("=== Raw Corrupted Data ===")
    print(df)

    # 1. Deduplicate by Primary Key
    df_clean = df.drop_duplicates(subset=["cust_id"], keep="first").copy()

    # 2. Enforce Numeric Range Constraint
    df_clean["age"] = np.where((df_clean["age"] >= 18) & (df_clean["age"] <= 100), df_clean["age"], np.nan)

    # 3. Parse Dates Coercing Errors to NaT
    df_clean["join_date"] = pd.to_datetime(df_clean["join_date"], errors="coerce")

    # 4. Standardize Categorical Strings
    allowed_statuses = {"ACTIVE", "INACTIVE", "SUSPENDED"}
    df_clean["status"] = df_clean["status"].str.strip().str.upper()
    df_clean["status"] = df_clean["status"].where(df_clean["status"].isin(allowed_statuses), "OTHER")

    print("\n=== Cleaned & Standardized Data ===")
    print(df_clean)

if __name__ == "__main__":
    run_cleaning_pipeline()
