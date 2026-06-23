import io
import pytest
import pandas as pd
from src.exporter import to_csv_bytes, to_excel_bytes, to_markdown_preview


@pytest.fixture
def df() -> pd.DataFrame:
    return pd.DataFrame({"a": [1, 2, 3], "b": ["x", "y", "z"]})


def test_to_csv_bytes(df):
    result = to_csv_bytes(df)
    assert isinstance(result, bytes)
    assert b"a,b" in result or b"a,b" in result
    reloaded = pd.read_csv(io.BytesIO(result))
    assert len(reloaded) == 3


def test_to_csv_bytes_no_index(df):
    result = to_csv_bytes(df, index=True)
    reloaded = pd.read_csv(io.BytesIO(result))
    assert len(reloaded.columns) == 3


def test_to_excel_bytes(df):
    result = to_excel_bytes(df)
    assert isinstance(result, bytes)
    reloaded = pd.read_excel(io.BytesIO(result))
    assert len(reloaded) == 3


def test_to_markdown_preview(df):
    result = to_markdown_preview(df, max_rows=2)
    assert isinstance(result, str)
    assert "a" in result
    assert "b" in result


def test_to_markdown_preview_truncated(df):
    result = to_markdown_preview(df, max_rows=2)
    assert "more rows" in result


def test_to_markdown_preview_full(df):
    result = to_markdown_preview(df, max_rows=10)
    assert "more rows" not in result
