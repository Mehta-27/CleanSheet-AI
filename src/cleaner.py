import re

import pandas as pd


def remove_duplicates(
    df: pd.DataFrame, subset: list[str] | None = None, keep: str = "first"
) -> pd.DataFrame:
    return df.drop_duplicates(subset=subset, keep=keep).reset_index(drop=True)


def fill_missing(
    df: pd.DataFrame,
    strategy: str = "mean",
    columns: list[str] | None = None,
    fill_value: object = None,
) -> pd.DataFrame:
    df = df.copy()
    cols = columns or df.columns.tolist()

    if strategy == "drop":
        return df.dropna(subset=cols).reset_index(drop=True)

    if strategy == "value" and fill_value is not None:
        for col in cols:
            if col in df.columns:
                df[col] = df[col].fillna(fill_value)
        return df

    for col in cols:
        if col not in df.columns:
            continue
        if strategy == "mean":
            if pd.api.types.is_numeric_dtype(df[col]):
                val = df[col].mean()
                df[col] = df[col].fillna(val)
        elif strategy == "median":
            if pd.api.types.is_numeric_dtype(df[col]):
                val = df[col].median()
                df[col] = df[col].fillna(val)
        elif strategy == "mode":
            mode_vals = df[col].mode()
            if not mode_vals.empty:
                df[col] = df[col].fillna(mode_vals[0])
    return df


def drop_missing(
    df: pd.DataFrame, columns: list[str] | None = None, how: str = "any"
) -> pd.DataFrame:
    return df.dropna(subset=columns, how=how).reset_index(drop=True)


def standardize_text(
    df: pd.DataFrame,
    columns: list[str] | None = None,
    strip: bool = True,
    lowercase: bool = False,
    uppercase: bool = False,
    title_case: bool = False,
    remove_special: bool = False,
    find_replace: tuple[str, str] | None = None,
) -> pd.DataFrame:
    df = df.copy()
    cols = columns or [c for c in df.columns if df[c].dtype == "object"]

    for col in cols:
        if col not in df.columns:
            continue
        mask = df[col].isna()
        s = df[col].fillna("").astype(str)

        if strip:
            s = s.str.strip()
        if lowercase:
            s = s.str.lower()
        if uppercase:
            s = s.str.upper()
        if title_case:
            s = s.str.title()
        if remove_special:
            s = s.apply(lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", x))
        if find_replace:
            s = s.str.replace(*find_replace, regex=False)

        # Restore original NaN positions instead of leaving empty strings
        s = s.where(~mask, other=None)
        df[col] = s
    return df


def convert_types(df: pd.DataFrame, type_map: dict[str, str]) -> pd.DataFrame:
    df = df.copy()
    for col, dtype in type_map.items():
        if col not in df.columns:
            continue
        try:
            if dtype == "datetime64[ns]":
                df[col] = pd.to_datetime(df[col], errors="coerce")
            elif dtype == "category":
                df[col] = df[col].astype("category")
            elif dtype in ("int64", "Int64"):
                df[col] = pd.to_numeric(df[col], errors="coerce").astype(
                    pd.Int64Dtype()
                )
            elif dtype in ("float64", "float32"):
                df[col] = pd.to_numeric(df[col], errors="coerce").astype("float64")
            elif dtype == "string":
                df[col] = df[col].astype("string")
            else:
                df[col] = df[col].astype(dtype)
        except Exception:
            continue
    return df


def filter_outliers_iqr(
    df: pd.DataFrame, columns: list[str] | None = None, multiplier: float = 1.5
) -> pd.DataFrame:
    df = df.copy()
    cols = columns or df.select_dtypes(include="number").columns.tolist()
    for col in cols:
        if col not in df.columns:
            continue
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - multiplier * iqr
        upper = q3 + multiplier * iqr
        df = df[(df[col] >= lower) & (df[col] <= upper)]
    return df.reset_index(drop=True)


def rename_columns(df: pd.DataFrame, rename_map: dict[str, str]) -> pd.DataFrame:
    return df.rename(columns=rename_map)
