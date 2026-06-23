from pathlib import Path
from typing import BinaryIO

import pandas as pd

from src.utils import logger


def detect_delimiter(file: BinaryIO) -> str:
    raw = file.read(8192)
    file.seek(0)
    if isinstance(raw, bytes):
        try:
            raw = raw.decode("utf-8")
        except UnicodeDecodeError:
            raw = raw.decode("latin-1")
    counts: dict[str, int] = {"," : 0, "\t": 0, ";" : 0, "|" : 0}
    for line in raw.split("\n")[:5]:
        for delim in counts:
            counts[delim] += line.count(delim)
    best = max(counts, key=lambda d: counts[d])
    return best if counts[best] > 0 else ","


def infer_encoding(file: BinaryIO) -> str:
    raw = file.read(4096)
    file.seek(0)
    try:
        raw.decode("utf-8")
        return "utf-8"
    except UnicodeDecodeError:
        try:
            raw.decode("latin-1")
            return "latin-1"
        except UnicodeDecodeError:
            return "utf-8"


def load_csv(file: BinaryIO, filename: str) -> pd.DataFrame:
    ext = Path(filename).suffix.lower()
    if ext in (".xlsx", ".xls"):
        return pd.read_excel(file)
    if ext == ".tsv":
        sep = "\t"
    else:
        sep = detect_delimiter(file)
    encoding = infer_encoding(file)
    logger.info("Loading %s with sep=%r encoding=%s", filename, sep, encoding)
    df = pd.read_csv(file, sep=sep, encoding=encoding, low_memory=False)
    df.columns = df.columns.str.strip()
    return df


def validate_csv(file: BinaryIO, filename: str) -> dict:
    issues = {}
    ext = Path(filename).suffix.lower()
    if ext not in (".csv", ".tsv", ".txt", ".xlsx", ".xls"):
        issues["format"] = f"Unsupported format: {ext}. Use CSV, TSV, or Excel."
    try:
        df = load_csv(file, filename)
        if df.empty:
            issues["empty"] = "File contains no data rows."
        issues["columns"] = len(df.columns)
        issues["rows"] = len(df)
    except Exception as e:
        issues["parse_error"] = str(e)
    return issues
