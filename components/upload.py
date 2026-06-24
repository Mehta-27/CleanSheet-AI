import streamlit as st
from src.utils import logger, MAX_FILE_SIZE_MB, MAX_FILE_SIZE_PRO_MB, SUPPORTED_EXTENSIONS
from src.utils import format_bytes
from src.loader import load_csv, validate_csv


def _is_pro() -> bool:
    return st.session_state.get("_pro", False)


def _file_limit() -> int:
    return MAX_FILE_SIZE_PRO_MB if _is_pro() else MAX_FILE_SIZE_MB


def render_upload() -> None:
    # ── Hero Section ──
    subtitle = (
        "CleanSheet AI Pro — Premium Version. Unlimited cleaning and exports."
        if _is_pro()
        else "Upload a messy CSV. Get a clean dataset in under 60 seconds. <span style='color:var(--accent-emerald); font-weight:600;'>Free, no sign-up required.</span>"
    )
    st.markdown(
        f"<div style='text-align:center; padding:2rem 0 1.5rem 0;'>"
        f"<div class='hero-title'>Your Data, Perfectly Clean</div>"
        f"<p class='hero-subtitle' style='margin:0 auto;'>{subtitle}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

    limit = _file_limit()
    uploaded = st.file_uploader(
        "Choose a CSV or TSV file",
        type=["csv", "tsv", "txt", "xlsx", "xls"] if _is_pro() else ["csv", "tsv", "txt"],
        help=f"Max file size: {limit} MB" + ("" if _is_pro() else " (upgrade to Pro for 500 MB)"),
        label_visibility="collapsed",
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

        # ── Pro teaser (free version only) ──
        if not _is_pro():
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
                "<a href='https://7388507084353.gumroad.com/l/tqqra' target='_blank' "
                "class='feature-pill' style='border-color:var(--accent-amber); "
                "color:var(--accent-amber); font-weight:600;'>Unlock Pro →</a>"
            )
            pro_pills += "</div>"
            st.markdown(pro_pills, unsafe_allow_html=True)
        return

    limit = _file_limit()
    if uploaded.size and uploaded.size > limit * 1024 * 1024:
        st.error(
            f"File too large ({format_bytes(uploaded.size)}). "
            f"Max limit is {limit} MB."
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

    st.session_state.df = df
    st.session_state.df_original = df.copy()
    st.session_state.filename = uploaded.name
    st.session_state["_fb_msg"] = f"Loaded {len(df):,} rows × {len(df.columns):,} columns"
    st.session_state["_fb_icon"] = "✅"
    st.session_state.page = "overview"
    st.rerun()
