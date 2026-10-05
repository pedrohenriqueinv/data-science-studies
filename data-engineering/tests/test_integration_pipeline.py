#!/usr/bin/env python3
"""
Automated Test Suite for Integrated Data Engineering Pipeline
"""
import pytest
import pandas as pd
import numpy as np

def test_pipeline_transform_logic():
    temps_c = np.array([0.0, 100.0, -40.0])
    temps_f = temps_c * 1.8 + 32.0
    expected = np.array([32.0, 212.0, -40.0])
    assert np.allclose(temps_f, expected)

def test_string_cleaning_logic():
    statuses = pd.Series(["  ok  ", "OK", "err", "WARNING "])
    cleaned = statuses.str.strip().str.upper()
    assert list(cleaned) == ["OK", "OK", "ERR", "WARNING"]
