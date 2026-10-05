#!/usr/bin/env python3
"""
Resilient REST API Client with Retry & Exponential Backoff
"""
import time
import requests
from typing import Dict, Any, Optional

class ResilientAPIClient:
    def __init__(self, base_url: str, max_retries: int = 3, backoff_factor: float = 1.5):
        self.base_url = base_url
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.session = requests.Session()

    def get_with_retry(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        for attempt in range(1, self.max_retries + 1):
            try:
                print(f"[Attempt {attempt}] GET {url}")
                # Using a dummy public testing endpoint
                response = self.session.get(url, params=params, timeout=5.0)
                
                if response.status_code == 429:
                    retry_after = float(response.headers.get("Retry-After", self.backoff_factor ** attempt))
                    print(f"Rate limited (429)! Backing off for {retry_after}s...")
                    time.sleep(retry_after)
                    continue

                response.raise_for_status()
                return response.json()

            except (requests.ConnectionError, requests.Timeout) as err:
                if attempt == self.max_retries:
                    print(f"Max retries exhausted for {url}: {err}")
                    raise
                wait_time = self.backoff_factor ** attempt
                print(f"Network error: {err}. Retrying in {wait_time:.1f}s...")
                time.sleep(wait_time)

if __name__ == "__main__":
    client = ResilientAPIClient("https://jsonplaceholder.typicode.com")
    data = client.get_with_retry("posts/1")
    print("Received Payload:", data)
