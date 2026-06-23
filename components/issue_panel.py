import streamlit as st
import pandas as pd
import plotly.express as px
from src.profiler import profile_dataset
from src.utils import logger


def render_issues() -> None:
    df = st.session_state.df
    profile = profile_dataset(df)

    st.markdown("## Data Quality Issues")

    has_issues = False

    if profile.missing_values:
        has_issues = True
        with st.expander("❌ Missing Values", expanded=True):
            total_pct = profile.total_missing_cells / max(profile.total_cells, 1) * 100
            st.markdown(
                f"**{profile.total_missing_cells:,}** missing values across "
                f"**{len(profile.missing_values)}** columns "
                f"({total_pct:.1f}% of all cells)"
            )
            miss_df = pd.DataFrame({
                "Column": list(profile.missing_values.keys()),
                "Missing": list(profile.missing_values.values()),
                "%": [f"{v}%" for v in profile.missing_pct.values()],
            })
            st.dataframe(miss_df, use_container_width=True, hide_index=True)

            fig = px.bar(
                miss_df, x="Column", y="Missing",
                title="Missing Values by Column",
                color="Missing", color_continuous_scale="Reds",
            )
            fig.update_layout(
                height=300,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
            )
            fig.update_xaxes(showgrid=False)
            fig.update_yaxes(showgrid=False)
            st.plotly_chart(fig, use_container_width=True)

    if profile.duplicate_count > 0:
        has_issues = True
        with st.expander("🔁 Duplicate Rows", expanded=True):
            dup_pct = profile.duplicate_count / max(len(df), 1) * 100
            st.markdown(
                f"Found **{profile.duplicate_count:,}** duplicate "
                f"row{'s' if profile.duplicate_count > 1 else ''} "
                f"({dup_pct:.1f}% of data)"
            )
            if profile.duplicate_rows:
                st.dataframe(
                    df.iloc[profile.duplicate_rows[:10]],
                    use_container_width=True, height=200
                )
                if len(profile.duplicate_rows) > 10:
                    st.caption(f"Showing 10 of {len(profile.duplicate_rows)} duplicate rows")

    if profile.constant_columns:
        has_issues = True
        with st.expander("📌 Constant Columns"):
            st.markdown("These columns have only one unique value and may be redundant:")
            for col in profile.constant_columns:
                st.markdown(f"- **{col}**")

    if profile.outlier_candidates:
        has_issues = True
        with st.expander("📊 Potential Outliers"):
            st.markdown(
                "Columns with values far outside the normal range "
                "(based on IQR method):"
            )
            for col, vals in profile.outlier_candidates.items():
                st.markdown(f"- **{col}**: {len(vals)} outlier{'s' if len(vals) > 1 else ''} detected")

    if not has_issues:
        st.success("✅ No data quality issues detected! Your data looks clean.")
        st.balloons()

    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("⬅ Back to Overview", use_container_width=True):
            st.session_state.page = "overview"
            st.rerun()
    with c2:
        if st.button("🧹 Go to Cleaning", use_container_width=True):
            st.session_state.page = "clean"
            st.rerun()
