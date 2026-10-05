# 🌪️ Introduction to Apache Airflow: Orchestration, DAGs & TaskFlow API

> **Track:** Data Engineering in Python  
> **Module:** 11 - Introduction to Apache Airflow in Python  
> **Focus:** Airflow 5 Core Components, TaskFlow API (`@task`), XComs, Sensors, SLAs & Branching

---

## 1. The 5 Core Architectural Components

Apache Airflow is a platform to programmatically author, schedule, and monitor workflows as Directed Acyclic Graphs (DAGs):

```
                   ┌──────────────────────────────────────┐
                   │         Webserver (UI Portal)        │
                   └──────────────────┬───────────────────┘
                                      │
                   ┌──────────────────▼───────────────────┐
                   │               Scheduler              │
                   │    (Monitors DAGs & Triggers Tasks)  │
                   └──────┬────────────────────────┬──────┘
                          │                        │
        ┌─────────────────▼────────┐     ┌─────────▼────────────────┐
        │   Metadata Database      │     │         Executor         │
        │ (PostgreSQL/MySQL state) │     │ (Sequential/Celery/K8s)  │
        └──────────────────────────┘     └─────────┬────────────────┘
                                                   │
                                         ┌─────────▼────────┐
                                         │  Worker Nodes    │
                                         │ (Execute Tasks)  │
                                         └──────────────────┘
```

1. **Webserver:** Renders the web interface for monitoring and DAG inspection.
2. **Scheduler:** Orchestrates execution, checks schedules, and delegates tasks to executor.
3. **Metadata Database:** Stores task states, variables, connections, and execution history.
4. **Executor:** Mechanism determining *how* tasks run (Local, Celery, Kubernetes).
5. **Workers:** Processes/containers that physically execute task code.

---

## 2. Modern TaskFlow API (`@task`) vs Classical Operators

Modern Airflow replaces verbose `PythonOperator` declarations with the clean `@task` decorator:

```python
from airflow.decorators import dag, task
from datetime import datetime, timedelta

@dag(
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    default_args={"retries": 2, "retry_delay": timedelta(minutes=5)}
)
def telemetry_orchestrator():
    
    @task
    def extract_metrics() -> list:
        return [120, 240, 310]

    @task
    def aggregate_metrics(metrics: list) -> float:
        return sum(metrics) / len(metrics)

    @task
    def publish_report(avg_val: float):
        print(f"Published average: {avg_val:.2f}")

    # Implicit XCom passing and dependency definition:
    raw_data = extract_metrics()
    avg = aggregate_metrics(raw_data)
    publish_report(avg)

pipeline = telemetry_orchestrator()
```

## 3. Sensors: Poke vs Reschedule Modes

Sensors wait asynchronously for external events (e.g. file arrival in S3 or database record creation):

* **`mode='poke'` (Default):** Worker slot remains locked and blocked throughout the wait cycle. **Wastes worker slots!**
* **`mode='reschedule'`:** Releases worker back to pool between check intervals, re-enqueueing only when interval expires. **Mandatory for production!**

```python
from airflow.sensors.filesystem import FileSensor

wait_for_raw_file = FileSensor(
    task_id="wait_for_file",
    filepath="/landing_zone/daily_feed.csv",
    poke_interval=60,       # Check every 60 seconds
    timeout=3600,           # Fail if file does not arrive within 1 hour
    mode="reschedule"       # Free worker slot between checks
)
```

## 4. Scheduling & Cron Mechanics

Airflow execution operates on **Data Intervals**:
* A DAG scheduled for `@daily` with `start_date=2026-10-01` runs at the **end** of the interval (`2026-10-02 00:00:00`), after all data for that day has been collected.
* **`catchup=False`:** Crucial setting preventing Airflow from executing hundreds of historical backfill runs upon activation.

## 5. Practical Exercises & Capstone Solutions

### Exercise 1: Diagnosing 'DAG Import Error'
* **Problem:** A red banner in the Airflow UI displays "DAG Import Error".
* **Solution:** Run `airflow dags list-import-errors` in CLI, or run `python dag_file.py` to identify missing package dependencies or global syntax errors.

### Exercise 2: XCom Size Limits
* **Problem:** Passing a 500MB Pandas DataFrame directly between `@task` functions crashes Airflow.
* **Solution:** XComs store data in the Airflow metadata database (PostgreSQL bytea/text), which is limited and not designed for Big Data. Pass **file paths or S3 URIs** via XCom instead, keeping data in object storage.
