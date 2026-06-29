"""CleanSheet Pro — Data Quality Scoring.

Calculates a 0-100 quality score across 4 dimensions:
- Completeness (30%) — how few missing values
- Uniqueness (20%) — how few duplicates
- Consistency (25%) — how consistent data types and formats are
- Validity (25%) — how well values conform to expected ranges
"""

from dataclasses import dataclass
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from src.profiler import profile_dataset


@dataclass
class QualityScore:
    overall: float
    completeness: float
    uniqueness: float
    consistency: float
    validity: float


def compute_score(df: pd.DataFrame) -> QualityScore:
    prof = profile_dataset(df)
    total = len(df) * len(df.columns)

    completeness = prof.completeness

    uniqueness = prof.uniqueness

    consistency = _consistency_score(df)

    validity = _validity_score(df, prof)

    overall = (
        completeness * 0.30 + uniqueness * 0.20 + consistency * 0.25 + validity * 0.25
    )

    return QualityScore(
        overall=round(overall, 1),
        completeness=round(completeness, 1),
        uniqueness=round(uniqueness, 1),
        consistency=round(consistency, 1),
        validity=round(validity, 1),
    )


def _consistency_score(df: pd.DataFrame) -> float:
    penalties = 0.0
    n_cols = max(len(df.columns), 1)

    for col in df.columns:
        dtype = df[col].dtype
        if pd.api.types.is_object_dtype(dtype):
            non_null = df[col].dropna()
            if len(non_null) > 0:
                str_lengths = non_null.astype(str).str.len()
                mean_len = str_lengths.mean()
                if mean_len > 0:
                    ratio = str_lengths.std() / mean_len
                    if ratio > 0.5:
                        penalties += 1

        mixed_types = df[col].apply(type).nunique()
        if mixed_types > 2:
            penalties += 1

    score = max(0, 100 - (penalties / n_cols * 50))
    return score


def _validity_score(df: pd.DataFrame, prof) -> float:
    penalties = 0.0
    n_cols = max(len(df.columns), 1)

    for col, stats in prof.numeric_stats.items():
        if stats.get("std") is not None and stats.get("mean") is not None:
            if stats["std"] == 0:
                continue
            cv = abs(stats["std"] / stats["mean"]) if stats["mean"] != 0 else 0
            if cv > 10:
                penalties += 1

    for col in df.columns:
        if pd.api.types.is_object_dtype(df[col]):
            non_null = df[col].dropna()
            if len(non_null) > 0:
                try:
                    numeric_vals = pd.to_numeric(non_null, errors="strict")
                    if len(numeric_vals) == len(non_null):
                        penalties += 1
                except (ValueError, TypeError):
                    pass

    score = max(0, 100 - (penalties / n_cols * 30))
    return score


def render_quality_dashboard(df: pd.DataFrame) -> None:
    score = compute_score(df)

    st.markdown("## 📊 Data Quality Score")

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Overall", f"{score.overall}/100", delta=None)
    col2.metric("Completeness", f"{score.completeness}/100")
    col3.metric("Uniqueness", f"{score.uniqueness}/100")
    col4.metric("Consistency", f"{score.consistency}/100")
    col5.metric("Validity", f"{score.validity}/100")

    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=[score.completeness, score.uniqueness, score.consistency, score.validity],
            theta=["Completeness", "Uniqueness", "Consistency", "Validity"],
            fill="toself",
            name="Current Score",
            line_color="#1E88E5",
        )
    )
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        height=400,
        margin=dict(l=80, r=80, t=20, b=20),
    )
    st.plotly_chart(fig, use_container_width=True)

    quality_emoji = (
        "🟢" if score.overall >= 80 else "🟡" if score.overall >= 50 else "🔴"
    )
    quality_label = (
        "Excellent"
        if score.overall >= 80
        else "Needs Work"
        if score.overall >= 50
        else "Poor"
    )

    st.markdown(f"### {quality_emoji} Quality Rating: **{quality_label}**")

    if score.completeness < 70:
        st.warning("⚠️ Low completeness — address missing values first")
    if score.uniqueness < 70:
        st.warning("⚠️ Many duplicates found — remove them to improve quality")
    if score.consistency < 70:
        st.warning("⚠️ Inconsistent data detected — standardize text formats")
    if score.validity < 70:
        st.warning("⚠️ Potential invalid values — review outliers and data ranges")
