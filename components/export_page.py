import streamlit as st
from src.exporter import to_csv_bytes, to_excel_bytes
from src.exporter import to_markdown_preview
from src.profiler import profile_dataset


def render_export() -> None:
    df = st.session_state.df
    log = st.session_state.get("cleaning_log", [])
    profile = profile_dataset(df)

    st.markdown("## 📥 Export Cleaned Data")

    before = profile_dataset(st.session_state.get("df_original", df))

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", f"{profile.row_count:,}")
    col2.metric("Missing Cells", f"{profile.total_missing_cells:,}",
                delta=f"{-before.total_missing_cells + profile.total_missing_cells}")
    col3.metric("Duplicates", profile.duplicate_count,
                delta=f"{-before.duplicate_count + profile.duplicate_count}")

    with st.expander("👁 Preview Cleaned Data", expanded=False):
        st.dataframe(df.head(20), use_container_width=True, height=300)
        st.text(to_markdown_preview(df))

    csv_bytes = to_csv_bytes(df)
    st.download_button(
        label="📥 Download as CSV",
        data=csv_bytes,
        file_name=f"{st.session_state.get('filename', 'data').rsplit('.', 1)[0]}_cleaned.csv",
        mime="text/csv",
        use_container_width=True,
        type="primary",
    )

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

    if log:
        with st.expander("📋 Cleaning Summary", expanded=True):
            for i, entry in enumerate(log, 1):
                st.markdown(f"**{i}.** {entry}")

    st.markdown("---")
    st.markdown("#### ⭐ Like CleanSheet AI?")
    st.markdown(
        "[☕ Buy me a coffee](https://buymeacoffee.com) · "
        "[🚀 Get CleanSheet Pro](https://gumroad.com)"
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
