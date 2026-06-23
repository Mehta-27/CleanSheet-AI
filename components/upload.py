import streamlit as st
from src.utils import logger, MAX_FILE_SIZE_MB, SUPPORTED_EXTENSIONS
from src.utils import format_bytes
from src.loader import load_csv, validate_csv
from src.styles import hero_section, step_card


def render_upload() -> None:
    st.markdown(hero_section(), unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "Drop your CSV or TSV file here",
        type=["csv", "tsv", "txt"],
        help=f"Max file size: {MAX_FILE_SIZE_MB} MB",
    )

    if uploaded is None:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(
                step_card(1, "📤", "Upload", "Drag & drop your messy CSV or TSV. No sign-up needed."),
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                step_card(2, "🔍", "Detect Issues", "Auto-profiling finds missing values, duplicates, type errors & outliers."),
                unsafe_allow_html=True,
            )
        with col3:
            st.markdown(
                step_card(3, "✨", "Clean & Export", "Fix everything in one click. Download a perfectly clean CSV."),
                unsafe_allow_html=True,
            )

        st.markdown("<div style='margin-top:2rem'>", unsafe_allow_html=True)
        pro_cols = st.columns(3)
        pro_icon = "⭐"
        pro_features = [
            ("Excel (.xlsx) Export", "Download cleaned data directly to Excel"),
            ("AI-Powered Suggestions", "Smart cleaning recommendations based on your data"),
            ("Quality Reports", "Professional PDF reports with data quality scores"),
        ]
        for i, (title, desc) in enumerate(pro_features):
            with pro_cols[i]:
                st.markdown(
                    f"<div style='background:#FFFBEB;border:1px solid #FDE68A;border-radius:8px;"
                    f"padding:0.75rem 1rem;text-align:center;height:100%'>"
                    f"<span style='font-size:0.65rem;font-weight:700;text-transform:uppercase;"
                    f"letter-spacing:0.05em;color:#D97706'>Pro Feature</span>"
                    f"<p style='font-weight:600;margin:0.25rem 0 0 0;font-size:0.9rem;color:#92400E'>{title}</p>"
                    f"<p style='font-size:0.8rem;color:#A16207;margin:0.15rem 0 0 0'>{desc}</p>"
                    f"</div>",
                    unsafe_allow_html=True,
                )
        st.markdown("</div>", unsafe_allow_html=True)
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
        f"Loaded **{len(df):,} rows × {len(df.columns):,} columns** from "
        f"`{uploaded.name}`"
    )

    st.session_state.df = df
    st.session_state.df_original = df.copy()
    st.session_state.filename = uploaded.name
    st.session_state.page = "overview"
    st.rerun()
