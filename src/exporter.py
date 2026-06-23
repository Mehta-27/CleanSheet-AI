import io

import pandas as pd


def to_csv_bytes(df: pd.DataFrame, index: bool = False) -> bytes:
    buf = io.BytesIO()
    df.to_csv(buf, index=index)
    buf.seek(0)
    return buf.getvalue()


def to_excel_bytes(df: pd.DataFrame, index: bool = False) -> bytes:
    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=index, sheet_name="Cleaned")
    buf.seek(0)
    return buf.getvalue()


def to_markdown_preview(df: pd.DataFrame, max_rows: int = 10) -> str:
    preview = df.head(max_rows).to_string(index=False)
    total = len(df)
    if total > max_rows:
        preview += f"\n... ({total - max_rows} more rows)"
    return f"```\n{preview}\n```"
