import streamlit as st
from src.utils import (
    logger,
    MAX_FILE_SIZE_MB,
    MAX_FILE_SIZE_PRO_MB,
    SUPPORTED_EXTENSIONS,
    SUPPORTED_EXTENSIONS_PRO,
)
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
        else "Upload a messy CSV. Get a clean dataset in under 60 seconds. <span style='color:var(--success); font-weight:600;'>Free, no sign-up required.</span>"
    )
    st.markdown(
        f"<div style='text-align:center; padding:2rem 0 1.5rem 0;'>"
        f"<h1 style='font-size:2rem; font-weight:700; margin-bottom:0.5rem;'>Your Data, Perfectly Clean</h1>"
        f"<p style='color:var(--text-secondary); max-width:480px; margin:0 auto; font-size:0.95rem;'>{subtitle}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

    limit = _file_limit()

    uploaded = st.file_uploader(
        "Upload your file",
        type=["csv", "tsv", "txt", "xlsx", "xls"]
        if _is_pro()
        else ["csv", "tsv", "txt"],
        help=f"Max file size: {limit} MB"
        + ("" if _is_pro() else " (upgrade to Pro for 500 MB)"),
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
            with st.container(border=True):
                st.markdown("**📤 1. Upload**")
                st.caption(
                    "Drop your messy CSV or TSV file. Up to 5 MB free — auto-detects delimiters and encoding."
                )
        with col2:
            with st.container(border=True):
                st.markdown("**🔍 2. Detect Issues**")
                st.caption(
                    "Auto-profiling finds missing values, duplicates, outliers, and type mismatches instantly."
                )
        with col3:
            with st.container(border=True):
                st.markdown("**✨ 3. Clean & Export**")
                st.caption(
                    "Fix issues with one click — fill missing values, remove duplicates, and download clean data."
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
        pills_html = "<div style='display:flex; flex-wrap:wrap; justify-content:center; gap:0.3rem; margin-bottom:1rem;'>"
        for feat in free_features:
            pills_html += f"<span style='background:var(--bg-card);border:1px solid var(--border);border-radius:999px;padding:0.15rem 0.6rem;font-size:0.78rem;color:var(--text-secondary);white-space:nowrap;'>✓ {feat}</span>"
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
            pro_pills = "<div style='display:flex; flex-wrap:wrap; justify-content:center; gap:0.3rem; margin-bottom:1rem;'>"
            for feat in pro_features:
                pro_pills += f"<span style='background:var(--bg-card);border:1px solid var(--border);border-radius:999px;padding:0.15rem 0.6rem;font-size:0.78rem;color:var(--text-tertiary);opacity:0.6;white-space:nowrap;'>{feat}</span>"
            pro_pills += (
                "<a href='https://7388507084353.gumroad.com/l/tqqra' target='_blank' "
                "style='background:var(--bg-card);border:1px solid var(--accent-amber);border-radius:999px;padding:0.15rem 0.6rem;font-size:0.78rem;color:var(--accent-amber);font-weight:600;white-space:nowrap;text-decoration:none;'>Unlock Pro →</a>"
            )
            pro_pills += "</div>"
            st.markdown(pro_pills, unsafe_allow_html=True)
        return

    limit = _file_limit()
    if uploaded.size and uploaded.size > limit * 1024 * 1024:
        st.error(
            f"File too large ({format_bytes(uploaded.size)}). Max limit is {limit} MB."
        )
        return

    ext = uploaded.name.rsplit(".", 1)[-1].lower()
    allowed = SUPPORTED_EXTENSIONS_PRO if _is_pro() else SUPPORTED_EXTENSIONS
    if f".{ext}" not in allowed:
        st.error(
            f"Unsupported format (.{ext}). Please upload CSV, TSV"
            + (", or Excel." if _is_pro() else ".")
        )
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
    st.session_state["_fb_msg"] = (
        f"Loaded {len(df):,} rows × {len(df.columns):,} columns"
    )
    st.session_state["_fb_icon"] = "✅"
    st.session_state.page = "overview"
    st.rerun()
