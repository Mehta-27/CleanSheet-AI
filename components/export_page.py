import streamlit as st
from src.exporter import to_csv_bytes, to_excel_bytes
from src.exporter import to_markdown_preview
from src.profiler import profile_dataset


def render_export() -> None:
    df = st.session_state.df
    log = st.session_state.get("cleaning_log", [])
    profile = profile_dataset(df)
    before = profile_dataset(st.session_state.get("df_original", df))

    st.markdown(
        "<div class='section-header'>📥 Export Cleaned Data</div>",
        unsafe_allow_html=True,
    )

    # ── Before / After Comparison ──
    st.markdown(
        "<p style='color:var(--text-tertiary); font-size:0.82rem; "
        "font-weight:500; text-transform:uppercase; letter-spacing:0.06em; "
        "margin-bottom:0.75rem;'>Before → After</p>",
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        row_delta = profile.row_count - before.row_count
        st.metric(
            "Rows", f"{profile.row_count:,}",
            delta=f"{row_delta:+,}" if row_delta != 0 else None,
        )
    with col2:
        col_delta = profile.column_count - before.column_count
        st.metric(
            "Columns", profile.column_count,
            delta=f"{col_delta:+d}" if col_delta != 0 else None,
        )
    with col3:
        miss_delta = profile.total_missing_cells - before.total_missing_cells
        st.metric(
            "Missing Cells", f"{profile.total_missing_cells:,}",
            delta=f"{miss_delta:+d}" if miss_delta != 0 else None,
        )
    with col4:
        dup_delta = profile.duplicate_count - before.duplicate_count
        st.metric(
            "Duplicates", profile.duplicate_count,
            delta=f"{dup_delta:+d}" if dup_delta != 0 else None,
        )

    # ── Preview ──
    with st.expander("👁 Preview Cleaned Data"):
        st.dataframe(df.head(20), use_container_width=True, height=300)
        st.markdown(
            "<p style='color:var(--text-tertiary); font-size:0.78rem; "
            "margin-top:0.5rem;'>Markdown Preview:</p>",
            unsafe_allow_html=True,
        )
        st.code(to_markdown_preview(df))

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Download CSV ──
    csv_bytes = to_csv_bytes(df)
    st.download_button(
        label="📥 Download as CSV",
        data=csv_bytes,
        file_name=f"{st.session_state.get('filename', 'data').rsplit('.', 1)[0]}_cleaned.csv",
        mime="text/csv",
        use_container_width=True,
        type="primary",
    )

    # ── Pro Upsell Card ──
    st.markdown(
        "<div style='margin-top:1rem;'>"
        "<div class='pro-cta-card'>"
        "<div style='display:flex; align-items:center; gap:0.4rem; margin-bottom:0.6rem;'>"
        "<span class='pro-badge'>✦ PRO</span>"
        "<span style='font-size:0.92rem; font-weight:700; color:var(--text-heading);'>"
        "Unlock More Export Options</span>"
        "</div>"
        "<div style='display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; margin-bottom:0.8rem;'>"
        "<div style='display:flex; align-items:center; gap:0.3rem;'>"
        "<span style='color:var(--accent-amber);'>✦</span>"
        "<span style='font-size:0.82rem; color:var(--text-secondary);'>Excel (.xlsx) export</span></div>"
        "<div style='display:flex; align-items:center; gap:0.3rem;'>"
        "<span style='color:var(--accent-amber);'>✦</span>"
        "<span style='font-size:0.82rem; color:var(--text-secondary);'>PDF quality reports</span></div>"
        "<div style='display:flex; align-items:center; gap:0.3rem;'>"
        "<span style='color:var(--accent-amber);'>✦</span>"
        "<span style='font-size:0.82rem; color:var(--text-secondary);'>AI cleaning suggestions</span></div>"
        "<div style='display:flex; align-items:center; gap:0.3rem;'>"
        "<span style='color:var(--accent-amber);'>✦</span>"
        "<span style='font-size:0.82rem; color:var(--text-secondary);'>500 MB file limit</span></div>"
        "</div>"
        "<a href='https://gumroad.com/l/cleansheet-ai-pro' class='pro-cta-btn' "
        "target='_blank'>Get Pro — $9.99 →</a>"
        "</div></div>",
        unsafe_allow_html=True,
    )

    # ── Cleaning Summary ──
    if log:
        st.markdown("<br>", unsafe_allow_html=True)
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
