import pytest
import pandas as pd
import numpy as np
from src.profiler import profile_dataset


@pytest.fixture
def clean_df() -> pd.DataFrame:
    return pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "score": [85.0, 90.0, 95.0],
    })


@pytest.fixture
def messy_df() -> pd.DataFrame:
    return pd.DataFrame({
        "id": [1, 2, 2, 3, 4],
        "value": [10.0, None, 20.0, 30.0, None],
        "cat": ["a", "b", "b", "a", "c"],
    })


def test_profile_clean_counts(clean_df):
    p = profile_dataset(clean_df)
    assert p.row_count == 3
    assert p.column_count == 3
    assert p.total_missing_cells == 0
    assert p.duplicate_count == 0


def test_profile_missing_values(messy_df):
    p = profile_dataset(messy_df)
    assert "value" in p.missing_values
    assert p.missing_values["value"] == 2


def test_profile_duplicates():
    df = pd.DataFrame({"a": [1, 1, 2, 2, 3], "b": [10, 10, 20, 20, 30]})
    p = profile_dataset(df)
    assert p.duplicate_count >= 1


def test_profile_dtypes(messy_df):
    p = profile_dataset(messy_df)
    assert "int64" in p.dtypes.get("id", "")
    assert "object" in p.dtypes.get("cat", "")


def test_profile_numeric_stats():
    df = pd.DataFrame({"x": [1.0, 2.0, 3.0, 4.0, 5.0]})
    p = profile_dataset(df)
    assert p.numeric_stats["x"]["mean"] == 3.0
    assert p.numeric_stats["x"]["min"] == 1.0
    assert p.numeric_stats["x"]["max"] == 5.0


def test_profile_constant_column():
    df = pd.DataFrame({"a": [1, 1, 1], "b": [2, 3, 4]})
    p = profile_dataset(df)
    assert "a" in p.constant_columns


def test_profile_outliers():
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 100]})
    p = profile_dataset(df)
    assert "x" in p.outlier_candidates


def test_profile_memory_nonzero(clean_df):
    p = profile_dataset(clean_df)
    assert p.memory_usage != ""


def test_profile_uniqueness():
    df = pd.DataFrame({"a": [1, 1, 2, 2, 3]})
    p = profile_dataset(df)
    assert p.uniqueness == 60.0
