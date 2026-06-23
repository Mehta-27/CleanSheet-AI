import streamlit as st
from src.utils import logger, MAX_FILE_SIZE_MB, SUPPORTED_EXTENSIONS
from src.utils import format_bytes
from src.loader import load_csv, validate_csv


def render_upload() -> None:
    # ── Hero Section ──
    st.markdown(
        "<div style='text-align:center; padding:2rem 0 1.5rem 0;'>"
        "<div class='hero-title'>Your Data, Perfectly Clean</div>"
        "<p class='hero-subtitle' style='margin:0 auto;'>"
        "Upload a messy CSV. Get a clean dataset in under 60 seconds. "
        "<span style='color:var(--accent-emerald); font-weight:600;'>"
        "Free, no sign-up required.</span></p>"
        "</div>",
        unsafe_allow_html=True,
    )

    uploaded = st.file_uploader(
        "Choose a CSV or TSV file",
        type=["csv", "tsv", "txt"],
        help=f"Max file size: {MAX_FILE_SIZE_MB} MB (upgrade to Pro for 500 MB)",
    )

    if uploaded is None:
        # ── How it works — feature cards ──
        st.markdown(
            "<div style='margin-top:0.5rem;'>"
            "<p style='text-align:center; color:var(--text-tertiary); font-size:0.82rem; "
            "font-weight:500; text-transform:uppercase; letter-spacing:0.06em; "
            "margin-bottom:1rem;'>How it works</p></div>",
            unsafe_allow_html=True,
        )

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(
                "<div class='feature-card'>"
                "<span class='icon'>📤</span>"
                "<h4>1. Upload</h4>"
                "<p>Drop your messy CSV or TSV file. Up to 5 MB free — "
                "auto-detects delimiters and encoding.</p>"
                "</div>",
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                "<div class='feature-card'>"
                "<span class='icon'>🔍</span>"
                "<h4>2. Detect Issues</h4>"
                "<p>Auto-profiling finds missing values, duplicates, "
                "outliers, and type mismatches instantly.</p>"
                "</div>",
                unsafe_allow_html=True,
            )
        with col3:
            st.markdown(
                "<div class='feature-card'>"
                "<span class='icon'>✨</span>"
                "<h4>3. Clean & Export</h4>"
                "<p>Fix issues with one click — fill missing values, "
                "remove duplicates, and download clean data.</p>"
                "</div>",
                unsafe_allow_html=True,
            )

        # ── What's included ──
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align:center; color:var(--text-tertiary); font-size:0.82rem; "
            "font-weight:500; text-transform:uppercase; letter-spacing:0.06em; "
            "margin-bottom:0.8rem;'>What's included</p>",
            unsafe_allow_html=True,
        )

        free_features = [
            "CSV & TSV upload",
            "Auto profiling",
            "Missing value handling",
            "Duplicate removal",
            "Text standardization",
            "Type conversion",
            "Interactive preview",
            "Plotly charts",
            "CSV download",
            "Cleaning history",
        ]
        pills_html = "<div style='text-align:center; margin-bottom:1rem;'>"
        for feat in free_features:
            pills_html += f"<span class='feature-pill'>✓ {feat}</span> "
        pills_html += "</div>"
        st.markdown(pills_html, unsafe_allow_html=True)

        # ── Pro teaser ──
        pro_features = [
            "🔒 Excel (.xlsx) export",
            "🔒 AI cleaning suggestions",
            "🔒 PDF quality reports",
            "🔒 500 MB file limit",
            "🔒 Batch processing",
        ]
        pro_pills = "<div style='text-align:center; margin-bottom:1rem;'>"
        for feat in pro_features:
            pro_pills += f"<span class='feature-pill' style='opacity:0.6;'>{feat}</span> "
        pro_pills += (
            "<a href='https://gumroad.com/l/cleansheet-ai-pro' target='_blank' "
            "class='feature-pill' style='border-color:var(--accent-amber); "
            "color:var(--accent-amber); font-weight:600;'>Unlock Pro →</a>"
        )
        pro_pills += "</div>"
        st.markdown(pro_pills, unsafe_allow_html=True)
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
