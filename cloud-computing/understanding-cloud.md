# ☁️ Understanding Cloud Computing — Study Notes

This document contains detailed study notes based on cloud computing fundamentals, service models, providers, and real-world database/infrastructure applications.

---

## 1. Core Services & Concepts

Cloud computing relies on three main types of virtualized services to eliminate the need for physical on-premise hardware:
*   **Compute:** The processing brain of the cloud (e.g., running virtual servers).
*   **Storage:** Where raw files, backups, and data objects reside.
*   **Databases:** Structured frameworks designed for easy data querying, management, and analysis.

### Virtualization & Scalability
*   **Virtualization:** The underlying technology that splits one physical server into multiple independent virtual environments, maximizing hardware efficiency and lowering costs.
*   **Vertical Scalability (Scale Up):** Adding resources (RAM, CPU) to an existing virtual machine.
*   **Horizontal Scalability (Scale Out):** Adding more machines to distribute workload spikes (essential for high-traffic events).

---

## 2. Cloud Service Models

| Model | Full Name | Managed By User | Target Audience | Example |
| :--- | :--- | :--- | :--- | :--- |
| **IaaS** | Infrastructure as a Service | Operating System, Middleware, Apps | SysAdmins | AWS EC2, GCP Compute Engine |
| **PaaS** | Platform as a Service | Application Code Only | Developers | AWS Elastic Beanstalk, Google App Engine |
| **SaaS** | Software as a Service | None (Ready to use) | End Users | Office 365, Google Workspace |

*   **FaaS (Function as a Service / Serverless):** Running specific event-triggered code blocks without managing servers (billing is calculated strictly by code execution milliseconds).

---

## 3. Deployment Models & Strategies
*   **Private Cloud:** Dedicated infrastructure for a single organization. High control but high setup costs.
*   **Public Cloud:** Shared public infrastructure (AWS, GCP, Azure). Highly scalable and pay-as-you-go.
*   **Hybrid Cloud:** Combines Private and Public deployment models.
    *   *Cloud Bursting:* Redirecting overflow traffic from a private cloud to a public cloud during peak demands to prevent system downtime.
*   **Multicloud:** Using different public cloud *providers* (e.g., AWS + Azure) to avoid **vendor lock-in**.

---

## 4. Privacy, Latency, and GDPR
*   **Latency:** The delay in data transmission. Solved by distributing servers globally.
*   **GDPR (General Data Protection Regulation):** EU law protecting personal data (PII).
    *   Requires explicit consent, rapid breach notifications, and data protection (encryption/pseudonymization).
    *   **Geographical Rule:** Personal data cannot leave EU borders unless the destination guarantees equivalent protection.

---

## 5. Major Providers & Service Equivalencies

| Category | AWS (Amazon) | Azure (Microsoft) | GCP (Google) |
| :--- | :--- | :--- | :--- |
| **Object Storage** | Amazon S3 | Azure Blob Storage | Google Cloud Storage |
| **Compute / VMs** | Amazon EC2 | Azure Virtual Machines | Google Compute Engine |
| **Relational DB** | Amazon RDS | Azure SQL Database | Google Cloud SQL |
| **Data Warehouse**| Amazon Redshift | Microsoft Fabric | BigQuery |
| **Streaming** | Amazon Kinesis | Azure Stream Analytics | Google Dataflow |
| **Machine Learning**| Amazon SageMaker | Azure Machine Learning | Google AutoML |

---

## 6. Real-World Case Studies

### 🟢 AWS — NerdWallet
*   **Challenge:** Slow ML deployment pipelines (months) and high on-premise compute costs.
*   **Solution:** Implemented **Amazon SageMaker** for automated lifecycle management and on-demand compute instances.
*   **Results:** Reduced model deployment time to days and cut ML training costs by **75%**.

### 🔵 Azure — The Ottawa Hospital
*   **Challenge:** Needed a cost-effective, secure **Disaster Recovery (DR)** solution for clinical data.
*   **Solution:** Built a hybrid model utilizing Azure Storage and **Azure Site Recovery**.
*   **Results:** Saved **50%** in DR infrastructure costs while synchronizing 700TB of data within 3 months under strict health data privacy compliance.

### 🔴 Google Cloud — Lush Cosmetics
*   **Challenge:** Website crashes during peak holiday shopping (Boxing Day) because legacy systems couldn't handle traffic spikes.
*   **Solution:** Migrated 17 sites to GCP using **Compute Engine** and **Cloud SQL**.
*   **Results:** Survived high-volume peak traffic with **zero outages** and cut hosting costs by **40%**.