#!/usr/bin/env python3
"""
Paginated API Collector (Cursor and Offset Patterns)
Demonstrates pulling paginated REST data into a unified batch DataFrame.
"""
import requests
import pandas as pd

def collect_paginated_records(limit_per_page: int = 20, max_pages: int = 3) -> pd.DataFrame:
    base_url = "https://jsonplaceholder.typicode.com/comments"
    all_records = []

    for page in range(1, max_pages + 1):
        params = {"_page": page, "_limit": limit_per_page}
        print(f"Fetching page {page} with limit {limit_per_page}...")
        resp = requests.get(base_url, params=params, timeout=5)
        resp.raise_for_status()
        
        items = resp.json()
        if not items:
            break
        all_records.extend(items)

    df = pd.DataFrame(all_records)
    print(f"Successfully collected {len(df)} total records across {max_pages} pages.")
    return df

if __name__ == "__main__":
    df_comments = collect_paginated_records()
    print(df_comments[["id", "name", "email"]].head())
