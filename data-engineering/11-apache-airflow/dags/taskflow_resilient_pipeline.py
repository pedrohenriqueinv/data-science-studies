#!/usr/bin/env python3
"""
Sensor-Driven Resilient File Ingestion Pipeline
Demonstrates FileSensor in reschedule mode triggering downstream processing.
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator

def transform_file():
    print("Processing discovered landing file into Parquet warehouse...")

with DAG(
    dag_id="sensor_landing_ingestion",
    schedule_interval="@hourly",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    default_args={"retries": 1, "retry_delay": timedelta(minutes=2)}
) as dag:

    sensor_task = FileSensor(
        task_id="wait_for_partner_feed",
        filepath="/opt/airflow/data/inbox/partner_feed.csv",
        poke_interval=120,
        timeout=1800,
        mode="reschedule"
    )

    process_task = PythonOperator(
        task_id="process_partner_data",
        python_callable=transform_file
    )

    sensor_task >> process_task
