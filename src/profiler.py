from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass
class ProfileResult:
    row_count: int = 0
    column_count: int = 0
    memory_usage: str = ""
    missing_values: dict[str, int] = field(default_factory=dict)
    missing_pct: dict[str, float] = field(default_factory=dict)
    duplicate_count: int = 0
    duplicate_rows: list[int] = field(default_factory=list)
    dtypes: dict[str, str] = field(default_factory=dict)
    unique_values: dict[str, int] = field(default_factory=dict)
    numeric_stats: dict[str, dict] = field(default_factory=dict)
    categorical_top: dict[str, tuple] = field(default_factory=dict)
    outlier_candidates: dict[str, list] = field(default_factory=dict)
    constant_columns: list[str] = field(default_factory=list)
    cardinality_high: list[str] = field(default_factory=list)
    total_missing_cells: int = 0
    total_cells: int = 0
    completeness: float = 100.0
    uniqueness: float = 100.0


NumericCols = list[tuple[str, pd.Series]]


def _pick_numeric(df: pd.DataFrame) -> NumericCols:
    return [(c, df[c]) for c in df.select_dtypes(include=np.number).columns]


def _safe_stat(series: pd.Series, method: str) -> float | None:
    try:
        val = getattr(series, method)()
        return None if pd.isna(val) else float(val)
    except Exception:
        return None


def profile_dataset(df: pd.DataFrame) -> ProfileResult:
    res = ProfileResult(
        row_count=len(df),
        column_count=len(df.columns),
    )

    total_mem = df.memory_usage(deep=True).sum()
    res.memory_usage = _format_bytes(int(total_mem))
    res.total_cells = len(df) * len(df.columns)

    missing = df.isna()
    res.total_missing_cells = int(missing.sum().sum())
    res.completeness = (
        100.0 * (1 - res.total_missing_cells / res.total_cells)
        if res.total_cells
        else 100.0
    )

    for col in df.columns:
        n_miss = int(missing[col].sum())
        if n_miss > 0:
            res.missing_values[col] = n_miss
            res.missing_pct[col] = round(n_miss / len(df) * 100, 1)

    res.dtypes = {col: str(df[col].dtype) for col in df.columns}
    res.unique_values = {col: int(df[col].nunique()) for col in df.columns}

    dupe_mask = df.duplicated(keep="first")
    res.duplicate_count = int(dupe_mask.sum())
    if res.duplicate_count:
        res.duplicate_rows = df.index[dupe_mask].tolist()

    for col in df.columns:
        if df[col].nunique() == 1:
            res.constant_columns.append(col)

    for col in df.columns:
        if df[col].nunique() / max(len(df), 1) > 0.95:
            res.cardinality_high.append(col)

    for col, series in _pick_numeric(df):
        stats: dict = {}
        stats["min"] = _safe_stat(series, "min")
        stats["max"] = _safe_stat(series, "max")
        stats["mean"] = _safe_stat(series, "mean")
        stats["median"] = _safe_stat(series, "median")
        stats["std"] = _safe_stat(series, "std")
        stats["missing"] = int(series.isna().sum())
        res.numeric_stats[col] = stats

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outliers = series[(series < lower) | (series > upper)].dropna()
        if len(outliers) > 0:
            res.outlier_candidates[col] = [float(v) for v in outliers[:10]]

    for col in df.select_dtypes(include="object").columns:
        vc = df[col].value_counts()
        if len(vc) > 0:
            res.categorical_top[col] = (vc.index[0], int(vc.iloc[0]))

    res.uniqueness = (
        100.0 * (1 - res.duplicate_count / max(len(df), 1))
        if len(df)
        else 100.0
    )

    return res


def _format_bytes(n: int) -> str:
    size = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"
