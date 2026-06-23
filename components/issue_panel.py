import streamlit as st
import pandas as pd
import plotly.express as px
from src.profiler import profile_dataset
from src.styles import get_plotly_theme
from src.utils import logger


def render_issues() -> None:
    df = st.session_state.df
    profile = profile_dataset(df)
    theme = get_plotly_theme()

    st.markdown(
        "<div class='section-header'>🚩 Data Quality Issues</div>",
        unsafe_allow_html=True,
    )

    has_issues = False

    # ── Missing Values ──
    if profile.missing_values:
        has_issues = True
        with st.expander("❌ Missing Values", expanded=True):
            total_pct = profile.total_missing_cells / max(profile.total_cells, 1) * 100
            st.markdown(
                f"<div style='display:flex; align-items:center; gap:0.5rem; margin-bottom:0.75rem;'>"
                f"<span class='severity-critical'>Critical</span>"
                f"<span style='color:var(--text-primary);'>"
                f"<strong>{profile.total_missing_cells:,}</strong> missing values across "
                f"<strong>{len(profile.missing_values)}</strong> columns "
                f"({total_pct:.1f}% of all cells)</span></div>",
                unsafe_allow_html=True,
            )

            miss_df = pd.DataFrame({
                "Column": list(profile.missing_values.keys()),
                "Missing": list(profile.missing_values.values()),
                "%": [f"{v}%" for v in profile.missing_pct.values()],
            })
            st.dataframe(miss_df, use_container_width=True, hide_index=True)

            fig = px.bar(
                miss_df, x="Column", y="Missing",
                title="",
                color="Missing", color_continuous_scale=["#06B6D4", "#F43F5E"],
            )
            fig.update_layout(
                height=280,
                showlegend=False,
                coloraxis_showscale=False,
                **theme,
            )
            fig.update_xaxes(showgrid=False, color=theme["font_color"])
            fig.update_yaxes(showgrid=False, color=theme["font_color"])
            st.plotly_chart(fig, use_container_width=True)

    # ── Duplicate Rows ──
    if profile.duplicate_count > 0:
        has_issues = True
        with st.expander("🔁 Duplicate Rows", expanded=True):
            dup_pct = profile.duplicate_count / max(len(df), 1) * 100
            st.markdown(
                f"<div style='display:flex; align-items:center; gap:0.5rem; margin-bottom:0.75rem;'>"
                f"<span class='severity-warning'>Warning</span>"
                f"<span style='color:var(--text-primary);'>"
                f"Found <strong>{profile.duplicate_count:,}</strong> duplicate "
                f"row{'s' if profile.duplicate_count > 1 else ''} "
                f"({dup_pct:.1f}% of data)</span></div>",
                unsafe_allow_html=True,
            )
            if profile.duplicate_rows:
                st.dataframe(
                    df.iloc[profile.duplicate_rows[:10]],
                    use_container_width=True, height=200
                )
                if len(profile.duplicate_rows) > 10:
                    st.caption(f"Showing 10 of {len(profile.duplicate_rows)} duplicate rows")

    # ── Constant Columns ──
    if profile.constant_columns:
        has_issues = True
        with st.expander("📌 Constant Columns"):
            st.markdown(
                f"<div style='display:flex; align-items:center; gap:0.5rem; margin-bottom:0.75rem;'>"
                f"<span class='severity-info'>Info</span>"
                f"<span style='color:var(--text-primary);'>"
                f"These columns have only one unique value and may be redundant:</span></div>",
                unsafe_allow_html=True,
            )
            for col in profile.constant_columns:
                st.markdown(
                    f"<div style='padding:0.3rem 0; color:var(--text-secondary);'>"
                    f"• <strong style='color:var(--text-primary);'>{col}</strong></div>",
                    unsafe_allow_html=True,
                )

    # ── Outlier Candidates ──
    if profile.outlier_candidates:
        has_issues = True
        with st.expander("📊 Potential Outliers"):
            st.markdown(
                f"<div style='display:flex; align-items:center; gap:0.5rem; margin-bottom:0.75rem;'>"
                f"<span class='severity-warning'>Warning</span>"
                f"<span style='color:var(--text-primary);'>"
                f"Columns with values far outside the normal range "
                f"(based on IQR method):</span></div>",
                unsafe_allow_html=True,
            )
            for col, vals in profile.outlier_candidates.items():
                st.markdown(
                    f"<div style='padding:0.3rem 0; color:var(--text-secondary);'>"
                    f"• <strong style='color:var(--text-primary);'>{col}</strong>: "
                    f"{len(vals)} outlier{'s' if len(vals) > 1 else ''} detected</div>",
                    unsafe_allow_html=True,
                )

    # ── No issues ──
    if not has_issues:
        st.markdown(
            "<div style='text-align:center; padding:2rem;'>"
            "<div style='font-size:3rem; margin-bottom:0.5rem;'>✅</div>"
            "<p style='font-size:1.1rem; font-weight:600; color:var(--accent-emerald);'>"
            "No data quality issues detected!</p>"
            "<p style='color:var(--text-secondary); font-size:0.88rem;'>"
            "Your data looks clean. You're ready to export.</p>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.balloons()

    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("⬅ Back to Overview", use_container_width=True):
            st.session_state.page = "overview"
            st.rerun()
    with c2:
        if st.button("🧹 Go to Cleaning", use_container_width=True, type="primary"):
            st.session_state.page = "clean"
            st.rerun()
