import streamlit as st
from src.utils import logger, MAX_FILE_SIZE_MB, SUPPORTED_EXTENSIONS
from src.utils import format_bytes
from src.loader import load_csv, validate_csv


def render_upload() -> None:
    st.markdown("## CleanSheet AI")
    st.markdown("Upload a messy CSV. Get a clean dataset. **Free, no sign-up.**")

    uploaded = st.file_uploader(
        "Choose a CSV or TSV file",
        type=["csv", "tsv", "txt"],
        help=f"Max file size: {MAX_FILE_SIZE_MB} MB (upgrade to Pro for 500 MB)",
    )

    if uploaded is None:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**📤 1. Upload**")
            st.markdown("Drop your messy CSV or TSV. Up to 5 MB free.")
        with col2:
            st.markdown("**🔍 2. Detect Issues**")
            st.markdown("Auto-profiling finds missing values, duplicates, and outliers.")
        with col3:
            st.markdown("**✨ 3. Clean & Export**")
            st.markdown("Fix issues and download a clean dataset.")

        with st.expander("⭐ Pro Features"):
            st.markdown(
                "- **Excel (.xlsx)** export\n"
                "- **AI-powered** cleaning suggestions\n"
                "- **PDF** quality reports\n"
                "- **500 MB** file limit\n"
                "\n[Get Pro on Gumroad](https://gumroad.com)"
            )
        return

    if uploaded.size and uploaded.size > MAX_FILE_SIZE_MB * 1024 * 1024:
        st.error(
            f"File too large ({format_bytes(uploaded.size)}). "
            f"Max free limit is {MAX_FILE_SIZE_MB} MB. "
            "Upgrade to Pro for 500 MB."
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
        f"Loaded **{len(df):,} rows × {len(df.columns):,} columns** from "
        f"`{uploaded.name}`"
    )

    st.session_state.df = df
    st.session_state.df_original = df.copy()
    st.session_state.filename = uploaded.name
    st.session_state.page = "overview"
    st.rerun()
