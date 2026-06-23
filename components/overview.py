import streamlit as st
import pandas as pd
import plotly.express as px
from src.profiler import profile_dataset
from src.utils import logger


def render_overview() -> None:
    df = st.session_state.df
    profile = profile_dataset(df)

    st.markdown("## Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Rows", f"{profile.row_count:,}")
    with col2:
        st.metric("Columns", profile.column_count)
    with col3:
        delta = f"-{profile.total_missing_cells}" if profile.total_missing_cells > 0 else None
        st.metric("Missing Cells", f"{profile.total_missing_cells:,}", delta=delta)
    with col4:
        delta = f"-{profile.duplicate_count}" if profile.duplicate_count > 0 else None
        st.metric("Duplicates", profile.duplicate_count, delta=delta)

    if st.session_state.get("cleaning_log"):
        with st.expander("📋 Cleaning History"):
            for i, entry in enumerate(st.session_state.cleaning_log, 1):
                st.markdown(
                    f"<div class='cleaning-entry'>"
                    f"<span class='step'>{i}</span>{entry}</div>",
                    unsafe_allow_html=True,
                )

    with st.expander("📊 Data Preview"):
        st.dataframe(df.head(50), use_container_width=True, height=300)

    with st.expander("📈 Column Details"):
        col_info = pd.DataFrame([
            {
                "Column": col,
                "Type": profile.dtypes.get(col, ""),
                "Missing": profile.missing_values.get(col, 0),
                "Unique": profile.unique_values.get(col, 0),
                "Constant": "✅" if col in profile.constant_columns else "—",
            }
            for col in df.columns
        ])
        st.dataframe(col_info, use_container_width=True, hide_index=True)

    if profile.numeric_stats:
        with st.expander("📊 Numeric Distributions"):
            for col, stats in profile.numeric_stats.items():
                if stats.get("mean") is None:
                    continue
                fcols = st.columns([1, 3])
                with fcols[0]:
                    st.markdown(f"**{col}**")
                    st.markdown(
                        f"Min: {stats['min']:.2f} &nbsp;·&nbsp; "
                        f"Max: {stats['max']:.2f} &nbsp;·&nbsp; "
                        f"Mean: {stats['mean']:.2f}"
                    )
                with fcols[1]:
                    fig = px.histogram(df, x=col, nbins=30, title="")
                    fig.update_layout(
                        height=120, margin=dict(l=0, r=0, t=0, b=0),
                        showlegend=False,
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                    )
                    fig.update_xaxes(showgrid=False)
                    fig.update_yaxes(showgrid=False)
                    st.plotly_chart(fig, use_container_width=True)

    if profile.outlier_candidates:
        with st.expander("⚠️ Outlier Candidates"):
            for col, vals in profile.outlier_candidates.items():
                st.markdown(
                    f"**{col}**: {len(vals)} potential outliers detected "
                    f"(e.g., {', '.join(str(v) for v in vals[:5])})"
                )

    st.markdown("---")
    if st.button("⬅ Back to Upload", use_container_width=True):
        _reset_session()
        st.rerun()


def _reset_session() -> None:
    keys = ["df", "df_original", "filename", "page", "cleaning_log"]
    for k in keys:
        st.session_state.pop(k, None)
