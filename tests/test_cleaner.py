import pytest
import pandas as pd
import numpy as np
from src.cleaner import (
    remove_duplicates, fill_missing, drop_missing,
    standardize_text, convert_types, filter_outliers_iqr, rename_columns,
)


@pytest.fixture
def df() -> pd.DataFrame:
    return pd.DataFrame({
        "name": ["Alice", "Bob", "Alice", None],
        "age": [25, None, 25, 30],
        "score": [85.0, 90.0, 85.0, None],
    })


def test_remove_duplicates_all_columns(df):
    result = remove_duplicates(df)
    assert len(result) == 3


def test_remove_duplicates_subset(df):
    result = remove_duplicates(df, subset=["name"])
    assert len(result) == 3


def test_fill_missing_mean(df):
    result = fill_missing(df, strategy="mean", columns=["age"])
    assert result["age"].isna().sum() == 0
    assert result.loc[1, "age"] == pytest.approx(26.6667, rel=0.01)


def test_fill_missing_median(df):
    result = fill_missing(df, strategy="median", columns=["score"])
    assert result["score"].isna().sum() == 0


def test_fill_missing_mode(df):
    result = fill_missing(df, strategy="mode", columns=["name"])
    assert result["name"].isna().sum() == 0
    assert result.loc[3, "name"] == "Alice"


def test_fill_missing_drop(df):
    result = fill_missing(df, strategy="drop")
    assert len(result) < len(df)


def test_drop_missing_any(df):
    result = drop_missing(df, how="any")
    assert len(result) == 2


def test_drop_missing_all(df):
    result = drop_missing(df, how="all")
    assert len(result) == 4


def test_standardize_text_lowercase(df):
    result = standardize_text(df, columns=["name"], lowercase=True)
    assert result["name"].iloc[0] == "alice"


def test_standardize_text_strip():
    d = pd.DataFrame({"x": ["  hello  ", "world  "]})
    result = standardize_text(d, columns=["x"], strip=True)
    assert result["x"].iloc[0] == "hello"
    assert result["x"].iloc[1] == "world"


def test_standardize_text_remove_special():
    d = pd.DataFrame({"x": ["hello!", "wor@ld"]})
    result = standardize_text(d, columns=["x"], remove_special=True)
    assert result["x"].iloc[0] == "hello"
    assert result["x"].iloc[1] == "world"


def test_standardize_text_find_replace():
    d = pd.DataFrame({"x": ["hello", "world"]})
    result = standardize_text(d, columns=["x"], find_replace=("o", "0"))
    assert result["x"].iloc[0] == "hell0"


def test_convert_types_int():
    d = pd.DataFrame({"x": ["1", "2", "3"]})
    result = convert_types(d, {"x": "int64"})
    assert result["x"].dtype == pd.Int64Dtype()


def test_convert_types_float():
    d = pd.DataFrame({"x": ["1.5", "2.7", "3.0"]})
    result = convert_types(d, {"x": "float64"})
    assert result["x"].dtype == "float64"


def test_convert_types_datetime():
    d = pd.DataFrame({"x": ["2024-01-01", "2024-02-01"]})
    result = convert_types(d, {"x": "datetime64[ns]"})
    assert pd.api.types.is_datetime64_any_dtype(result["x"])


def test_convert_types_string():
    d = pd.DataFrame({"x": [1, 2, 3]})
    result = convert_types(d, {"x": "string"})
    assert pd.api.types.is_string_dtype(result["x"])


def test_filter_outliers_iqr():
    d = pd.DataFrame({"x": [1, 2, 3, 4, 5, 100]})
    result = filter_outliers_iqr(d, columns=["x"])
    assert len(result) == 5


def test_rename_columns():
    d = pd.DataFrame({"old": [1, 2]})
    result = rename_columns(d, {"old": "new"})
    assert "new" in result.columns
    assert "old" not in result.columns
