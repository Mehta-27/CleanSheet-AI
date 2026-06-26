import streamlit as st
import pandas as pd
import plotly.express as px
from src.profiler import profile_dataset
from src.styles import get_plotly_theme
from src.utils import logger


def render_overview() -> None:
    df = st.session_state.df
    profile = profile_dataset(df)
    theme = get_plotly_theme()

    fb_msg = st.session_state.pop("_fb_msg", None)
    fb_icon = st.session_state.pop("_fb_icon", "✅")
    if fb_msg:
        st.toast(fb_msg, icon=fb_icon)

    st.markdown(
        "<div class='section-header'>📊 Dataset Overview</div>",
        unsafe_allow_html=True,
    )

    # ── Metric Cards ──
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

    # ── Additional stats row ──
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st.metric("Completeness", f"{profile.completeness:.1f}%")
    with col6:
        st.metric("Uniqueness", f"{profile.uniqueness:.1f}%")
    with col7:
        st.metric("Memory", profile.memory_usage)
    with col8:
        n_numeric = len(profile.numeric_stats)
        n_text = len(df.select_dtypes(include="object").columns)
        st.metric("Types", f"{n_numeric}N · {n_text}T")

    # ── Cleaning History ──
    if st.session_state.get("cleaning_log"):
        with st.expander("📋 Cleaning History", expanded=False):
            for i, entry in enumerate(st.session_state.cleaning_log, 1):
                st.markdown(
                    f"<div class='cleaning-entry'>"
                    f"<span class='step'>{i}</span>{entry}</div>",
                    unsafe_allow_html=True,
                )

    # ── Data Preview ──
    with st.expander("👁 Data Preview", expanded=True):
        st.dataframe(df.head(50), use_container_width=True, height=300)

    # ── Column Details ──
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

    # ── Numeric Distributions ──
    if profile.numeric_stats:
        with st.expander("📊 Numeric Distributions"):
            for col, stats in profile.numeric_stats.items():
                if stats.get("mean") is None:
                    continue
                fcols = st.columns([1, 3])
                with fcols[0]:
                    st.markdown(f"**{col}**")
                    st.markdown(
                        f"<span style='color:var(--text-secondary); font-size:0.82rem;'>"
                        f"Min: {stats['min']:.2f} &middot; "
                        f"Max: {stats['max']:.2f} &middot; "
                        f"Mean: {stats['mean']:.2f}</span>",
                        unsafe_allow_html=True,
                    )
                with fcols[1]:
                    fig = px.histogram(df, x=col, nbins=30, title="")
                    fig.update_traces(marker_color="#06B6D4", opacity=0.85)
                    fig.update_layout(
                        height=120, margin=dict(l=0, r=0, t=0, b=0),
                        showlegend=False,
                        **theme,
                    )
                    fig.update_xaxes(showgrid=False, color=theme["font_color"])
                    fig.update_yaxes(showgrid=False, color=theme["font_color"])
                    st.plotly_chart(fig, use_container_width=True)

    # ── Outlier Candidates ──
    if profile.outlier_candidates:
        with st.expander("⚠️ Outlier Candidates"):
            for col, vals in profile.outlier_candidates.items():
                st.markdown(
                    f"<div style='display:flex; align-items:center; gap:0.5rem; margin-bottom:0.3rem;'>"
                    f"<span class='severity-warning'>Warning</span>"
                    f"<span style='color:var(--text-primary); font-size:0.88rem;'>"
                    f"<strong>{col}</strong>: {len(vals)} potential outliers detected "
                    f"(e.g., {', '.join(str(v) for v in vals[:5])})</span></div>",
                    unsafe_allow_html=True,
                )

    st.markdown("---")
    if st.button("⬅ Back to Upload", use_container_width=True):
        _reset_session()
        st.rerun()


def _reset_session() -> None:
    keys = ["df", "df_original", "filename", "page", "cleaning_log"]
    for k in keys:
        st.session_state.pop(k, None)
