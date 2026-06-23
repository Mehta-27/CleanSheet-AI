import io
import pytest
import pandas as pd
from src.loader import detect_delimiter, infer_encoding, load_csv


def _make_file(content: str) -> io.BytesIO:
    return io.BytesIO(content.encode("utf-8"))


def test_detect_delimiter_comma():
    f = _make_file("a,b,c\n1,2,3")
    assert detect_delimiter(f) == ","


def test_detect_delimiter_tab():
    f = _make_file("a\tb\tc\n1\t2\t3")
    assert detect_delimiter(f) == "\t"


def test_detect_delimiter_fallback():
    f = _make_file("hello world")
    assert detect_delimiter(f) == ","


def test_infer_encoding_utf8():
    f = _make_file("hello")
    assert infer_encoding(f) == "utf-8"


def test_infer_encoding_latin1():
    raw = b"caf\xe9"
    f = io.BytesIO(raw)
    assert infer_encoding(f) == "latin-1"


def test_load_csv_basic():
    content = "name,age\nAlice,30\nBob,25"
    f = _make_file(content)
    df = load_csv(f, "test.csv")
    assert len(df) == 2
    assert list(df.columns) == ["name", "age"]


def test_load_csv_strips_column_whitespace():
    content = " name , age \nAlice,30"
    f = _make_file(content)
    df = load_csv(f, "test.csv")
    assert list(df.columns) == ["name", "age"]


def test_load_csv_excel():
    df_orig = pd.DataFrame({"x": [1, 2]})
    buf = io.BytesIO()
    df_orig.to_excel(buf, index=False)
    buf.seek(0)
    df = load_csv(buf, "data.xlsx")
    assert list(df.columns) == ["x"]
