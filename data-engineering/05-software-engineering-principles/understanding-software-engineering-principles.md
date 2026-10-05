# 🏗️ Software Engineering Principles in Python

> **Track:** Data Engineering in Python  
> **Module:** 05 - Software Engineering Principles  
> **Focus:** Modularity, PEP 8, OOP Architecture, Package Distribution, Unit Testing (`pytest`)

---

## 1. Modularity & Clean Architecture

In production data engineering, single-file spaghetti scripts create unmaintainable systems. Code must be organized following the **Separation of Concerns (SoC)** principle:

```
data_pipeline_pkg/
├── pyproject.toml            # Packaging & build metadata (PEP 517/621)
├── README.md
├── src/
│   └── data_pipeline/
│       ├── __init__.py       # Package entrypoint & exposed API
│       ├── extractors.py     # Source data acquisition
│       ├── transformers.py   # Business logic & vectorization
│       └── loaders.py        # Database/lake loading routines
└── tests/
    ├── conftest.py           # Shared test fixtures & mock engines
    └── test_transformers.py  # Unit tests with assertions
```

---

## 2. Object-Oriented Design & Polymorphic Extractors

Using classes allows establishing contracts for data connectors:

```python
from abc import ABC, abstractmethod
import pandas as pd

class BaseExtractor(ABC):
    """Abstract base class defining the extractor contract."""
    
    @abstractmethod
    def extract(self) -> pd.DataFrame:
        """Extracts data from the external source and returns a DataFrame."""
        pass

class S3Extractor(BaseExtractor):
    def __init__(self, bucket: str, key: str):
        self.bucket = bucket
        self.key = key
        
    def extract(self) -> pd.DataFrame:
        # Implementation for downloading and reading S3 object
        return pd.read_parquet(f"s3://{self.bucket}/{self.key}")
```

## 3. PEP 8 Standards & Docstrings (PEP 257)

Professional code must be self-documenting and lint-clean:

* **Naming Conventions:**
  * Modules & Packages: `lowercase_with_underscores`
  * Classes: `CapWords` (PascalCase)
  * Functions & Methods: `lowercase_with_underscores`
  * Constants: `UPPER_CASE_WITH_UNDERSCORES`
  * Private/Protected members: `_leading_underscore`
* **Docstring Styles:** Google style or NumPy style, documenting `Args`, `Returns`, and `Raises`.
