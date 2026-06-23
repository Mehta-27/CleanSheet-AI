import streamlit as st
from src.exporter import to_csv_bytes, to_excel_bytes
from src.exporter import to_markdown_preview
from src.profiler import profile_dataset


def render_export() -> None:
    df = st.session_state.df
    log = st.session_state.get("cleaning_log", [])
    profile = profile_dataset(df)
    before = profile_dataset(st.session_state.get("df_original", df))

    st.markdown("## Export Cleaned Data")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Rows", f"{profile.row_count:,}")
    with col2:
        miss_delta = -before.total_missing_cells + profile.total_missing_cells
        st.metric("Missing Cells", f"{profile.total_missing_cells:,}",
                  delta=f"{miss_delta:+d}" if miss_delta != 0 else None)
    with col3:
        dup_delta = -before.duplicate_count + profile.duplicate_count
        st.metric("Duplicates", profile.duplicate_count,
                  delta=f"{dup_delta:+d}" if dup_delta != 0 else None)

    with st.expander("👁 Preview Cleaned Data"):
        st.dataframe(df.head(20), use_container_width=True, height=300)
        st.markdown("**Markdown Preview:**")
        st.code(to_markdown_preview(df))

    csv_bytes = to_csv_bytes(df)
    st.download_button(
        label="📥 Download as CSV",
        data=csv_bytes,
        file_name=f"{st.session_state.get('filename', 'data').rsplit('.', 1)[0]}_cleaned.csv",
        mime="text/csv",
        use_container_width=True,
        type="primary",
    )

    col_disabled, col_pro = st.columns([3, 1])
    with col_disabled:
        try:
            xlsx_bytes = to_excel_bytes(df)
            st.download_button(
                label="📥 Download as Excel (.xlsx) — Pro Feature",
                data=xlsx_bytes,
                file_name=f"{st.session_state.get('filename', 'data').rsplit('.', 1)[0]}_cleaned.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True,
                disabled=True,
                help="Upgrade to CleanSheet Pro for Excel export",
            )
        except Exception:
            st.info("⭐ Excel export requires CleanSheet Pro")
    with col_pro:
        st.markdown(
            "<a href='https://gumroad.com' "
            "style='display:block;background:linear-gradient(135deg,#D97706,#F59E0B);"
            "color:white;text-align:center;padding:0.5rem 0.75rem;border-radius:8px;"
            "font-weight:600;font-size:0.85rem;text-decoration:none;white-space:nowrap'>"
            "Get Pro — $9.99</a>",
            unsafe_allow_html=True,
        )

    if log:
        with st.expander("📋 Cleaning Summary", expanded=True):
            for i, entry in enumerate(log, 1):
                st.markdown(
                    f"<div class='cleaning-entry'>"
                    f"<span class='step'>{i}</span>{entry}</div>",
                    unsafe_allow_html=True,
                )

    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("⬅ Back to Cleaning", use_container_width=True):
            st.session_state.page = "clean"
            st.rerun()
    with c2:
        if st.button("🆕 Start Over", use_container_width=True):
            for k in ["df", "df_original", "filename", "page", "cleaning_log"]:
                st.session_state.pop(k, None)
            st.rerun()
