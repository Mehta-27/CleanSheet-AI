import streamlit as st
from src.utils import logger, MAX_FILE_SIZE_MB, SUPPORTED_EXTENSIONS
from src.utils import format_bytes
from src.loader import load_csv, validate_csv


def render_upload() -> None:
    st.markdown(
        "<h1 style='text-align:center;font-size:2.6rem;margin-bottom:0'>"
        "CleanSheet AI</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align:center;color:#666;font-size:1.1rem;margin-top:-8px'>"
        "Upload a messy CSV. Get a clean dataset. <b>Free, no sign-up.</b></p>",
        unsafe_allow_html=True,
    )

    st.markdown("---")
    uploaded = st.file_uploader(
        "Choose a CSV or TSV file",
        type=["csv", "tsv", "txt"],
        help=f"Max file size: {MAX_FILE_SIZE_MB} MB",
    )

    if uploaded is None:
        _render_getting_started()
        return

    if uploaded.size and uploaded.size > MAX_FILE_SIZE_MB * 1024 * 1024:
        st.error(
            f"File too large ({format_bytes(uploaded.size)}). "
            f"Max is {MAX_FILE_SIZE_MB} MB. "
            "Get CleanSheet Pro for 500 MB limit."
        )
        return

    ext = uploaded.name.rsplit(".", 1)[-1].lower()
    if f".{ext}" not in SUPPORTED_EXTENSIONS:
        st.error(f"Unsupported format. Please upload CSV or TSV.")
        return

    with st.spinner("Loading and validating..."):
        issues = validate_csv(uploaded, uploaded.name)
        if "parse_error" in issues:
            st.error(f"Could not parse file: {issues['parse_error']}")
            return
        uploaded.seek(0)
        df = load_csv(uploaded, uploaded.name)

    st.success(
        f"Loaded {len(df):,} rows × {len(df.columns):,} columns from "
        f"**{uploaded.name}**"
    )

    st.session_state.df = df
    st.session_state.df_original = df.copy()
    st.session_state.filename = uploaded.name
    st.session_state.page = "overview"
    st.rerun()


def _render_getting_started() -> None:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 📤 Upload")
        st.markdown("Upload your messy CSV or TSV file. Excel coming in Pro.")
    with col2:
        st.markdown("### 🔍 Detect Issues")
        st.markdown(
            "Automatic profiling finds missing values, duplicates, "
            "type mismatches, and outliers."
        )
    with col3:
        st.markdown("### ✨ Clean & Export")
        st.markdown(
            "Fix issues with one click. Download a perfectly clean CSV."
        )

    st.markdown("---")
    st.markdown(
        "#### 🚀 Pro Features (coming soon)")
    pro_cols = st.columns(3)
    with pro_cols[0]:
        st.markdown("- Excel (.xlsx) support")
        st.markdown("- AI-powered cleaning suggestions")
    with pro_cols[1]:
        st.markdown("- PDF quality reports")
        st.markdown("- Batch process multiple files")
    with pro_cols[2]:
        st.markdown("- 500 MB file limit")
        st.markdown("- Priority email support")
