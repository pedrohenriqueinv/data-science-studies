#!/usr/bin/env python3
"""
Multi-Cloud Data Engineering Architecture & Cost Estimator
Calculates monthly operational costs for batch ingestion across AWS, Azure, and GCP.
"""
from dataclasses import dataclass
from typing import Dict

@dataclass
class CloudWorkload:
    monthly_data_gb: float
    compute_hours_per_day: float
    query_scanned_tb: float

def estimate_aws(workload: CloudWorkload) -> Dict[str, float]:
    storage_cost = workload.monthly_data_gb * 0.023  # S3 Standard
    compute_cost = workload.compute_hours_per_day * 30 * 0.096  # m5.large Glue/EC2
    dwh_cost = workload.query_scanned_tb * 5.0  # Athena / Redshift Spectrum ($5/TB)
    return {
        "Storage (S3)": storage_cost,
        "Compute (Glue/EC2)": compute_cost,
        "Querying (Athena)": dwh_cost,
        "Total": storage_cost + compute_cost + dwh_cost
    }

def estimate_gcp(workload: CloudWorkload) -> Dict[str, float]:
    storage_cost = workload.monthly_data_gb * 0.020  # GCS Standard
    compute_cost = workload.compute_hours_per_day * 30 * 0.080  # e2-standard-2
    dwh_cost = workload.query_scanned_tb * 6.25  # BigQuery on-demand ($6.25/TB)
    return {
        "Storage (GCS)": storage_cost,
        "Compute (Dataproc)": compute_cost,
        "Querying (BigQuery)": dwh_cost,
        "Total": storage_cost + compute_cost + dwh_cost
    }

if __name__ == "__main__":
    wl = CloudWorkload(monthly_data_gb=2500.0, compute_hours_per_day=4.0, query_scanned_tb=15.0)
    print("Workload: 2.5 TB storage, 4h daily compute, 15 TB query scans/month")
    print("AWS Estimate:", estimate_aws(wl))
    print("GCP Estimate:", estimate_gcp(wl))
