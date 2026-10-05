# 🌐 Introduction to APIs in Python: REST Architecture, Pagination & Network Resilience

> **Track:** Data Engineering in Python  
> **Module:** 09 - Introduction to APIs in Python  
> **Focus:** HTTP Verbs, Status Codes, Custom Headers, Rate Limits, Retry Logic & Exponential Backoff

---

## 1. HTTP Protocol Foundations & REST Conventions

In modern cloud data architectures, APIs serve as the primary gateway to SaaS applications, message brokers, and third-party feeds:

### HTTP Status Code Architecture

| Range | Classification | Engineering Action Required |
| :--- | :--- | :--- |
| **`2xx`** | Success (`200 OK`, `201 Created`) | Parse payload and load into pipeline buffer |
| **`3xx`** | Redirection (`301 Moved`, `304 Not Modified`) | Follow redirect or skip re-ingestion if cached |
| **`4xx`** | Client Error (`400 Bad Request`, `401 Unauthorized`, `429 Too Many Requests`) | Do NOT blindly retry! Check tokens, headers, or back off for `429` |
| **`5xx`** | Server Error (`500 Internal`, `502 Bad Gateway`, `503 Unavailable`) | Transient failure: retry with exponential backoff |

---

## 2. Request Headers & Authentication Mechanisms

```python
import requests

headers = {
    "Authorization": "Bearer eyJhbGciOi...",
    "Accept": "application/json",
    "User-Agent": "EnterpriseDataIngestionPipeline/2.1"
}

response = requests.get("https://api.enterprise.com/v1/telemetry", headers=headers, timeout=(3.05, 27))
response.raise_for_status()
data = response.json()
```
