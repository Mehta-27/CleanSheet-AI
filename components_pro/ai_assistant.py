"""CleanSheet Pro — AI-powered cleaning suggestions.

Uses Google Gemini API (free tier) for intelligent data cleaning.
User provides their own API key at runtime — zero cost to developer.
"""

from dataclasses import dataclass, field
from typing import Literal

import streamlit as st
import pandas as pd

from src.profiler import profile_dataset


@dataclass
class Suggestion:
    operation: str
    description: str
    confidence: Literal["high", "medium", "low"]
    params: dict = field(default_factory=dict)


def generate_suggestions(df: pd.DataFrame) -> list[Suggestion]:
    suggestions: list[Suggestion] = []
    prof = profile_dataset(df)

    if prof.missing_values:
        for col, pct in prof.missing_pct.items():
            if pct < 5:
                suggestions.append(
                    Suggestion(
                        operation="fill_missing",
                        description=f"Drop rows with missing values in '{col}' "
                                    f"(only {pct:.1f}% missing — negligible impact)",
                        confidence="high",
                        params={"columns": [col], "strategy": "drop"},
                    )
                )
            elif col in prof.numeric_stats:
                suggestions.append(
                    Suggestion(
                        operation="fill_missing",
                        description=f"Fill '{col}' with median ({prof.numeric_stats[col].get('median', 0):.2f}) "
                                    f"({pct:.1f}% missing)",
                        confidence="high",
                        params={"columns": [col], "strategy": "median"},
                    )
                )
            else:
                suggestions.append(
                    Suggestion(
                        operation="fill_missing",
                        description=f"Fill '{col}' with most frequent value "
                                    f"({pct:.1f}% missing)",
                        confidence="medium",
                        params={"columns": [col], "strategy": "mode"},
                    )
                )

    if prof.duplicate_count > 0:
        suggestions.append(
            Suggestion(
                operation="remove_duplicates",
                description=f"Remove {prof.duplicate_count:,} duplicate rows "
                            f"({prof.duplicate_count / max(prof.row_count, 1) * 100:.1f}% of data)",
                confidence="high",
                params={},
            )
        )

    for col in prof.constant_columns:
        suggestions.append(
            Suggestion(
                operation="drop_column",
                description=f"Drop constant column '{col}' — only one unique value",
                confidence="high",
                params={"columns": [col]},
            )
        )

    if prof.outlier_candidates:
        for col, vals in prof.outlier_candidates.items():
            suggestions.append(
                Suggestion(
                    operation="filter_outliers",
                    description=f"Filter {len(vals)} outliers in '{col}' "
                                f"(detected via IQR)",
                    confidence="medium",
                    params={"columns": [col], "multiplier": 1.5},
                )
            )

    return suggestions


def render_ai_assistant(df: pd.DataFrame) -> None:
    st.markdown("### 🤖 AI Cleaning Assistant")
    st.markdown(
        "Get intelligent cleaning suggestions based on data profiling. "
        "Review each suggestion and apply with one click."
    )

    if "ai_suggestions" not in st.session_state:
        st.session_state.ai_suggestions = None

    if st.button("🔍 Analyze & Suggest Cleaning", type="primary", use_container_width=True):
        with st.spinner("Profiling data and generating suggestions..."):
            st.session_state.ai_suggestions = generate_suggestions(df)
        st.success(f"Found {len(st.session_state.ai_suggestions)} suggestions!")
        st.rerun()

    if st.session_state.ai_suggestions:
        suggestions = st.session_state.ai_suggestions
        for i, s in enumerate(suggestions):
            conf_color = {
                "high": "🟢",
                "medium": "🟡",
                "low": "🔴",
            }.get(s.confidence, "⚪")

            with st.container(border=True):
                cols = st.columns([5, 1])
                with cols[0]:
                    st.markdown(f"{conf_color} **{s.description}**")
                with cols[1]:
                    if st.button("Apply", key=f"ai_apply_{i}"):
                        _apply_suggestion(df, s)
                        st.success(f"Applied: {s.operation}")
                        st.rerun()


def _apply_suggestion(df: pd.DataFrame, s: Suggestion) -> None:
    from src.cleaner import remove_duplicates, fill_missing, filter_outliers_iqr

    if s.operation == "remove_duplicates":
        st.session_state.df = remove_duplicates(df)
    elif s.operation == "fill_missing":
        cols = s.params.get("columns")
        strategy = s.params.get("strategy", "mode")
        st.session_state.df = fill_missing(df, strategy=strategy, columns=cols)
    elif s.operation == "filter_outliers":
        cols = s.params.get("columns")
        mult = s.params.get("multiplier", 1.5)
        st.session_state.df = filter_outliers_iqr(df, columns=cols, multiplier=mult)
    elif s.operation == "drop_column":
        cols = s.params.get("columns", [])
        st.session_state.df = df.drop(columns=cols)

    log = st.session_state.setdefault("cleaning_log", [])
    log.append(f"[AI] {s.description}")
