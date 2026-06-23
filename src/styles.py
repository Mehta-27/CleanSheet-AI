"""Custom CSS and HTML components for CleanSheet AI brand.""" 

import streamlit as st

BRAND_PRIMARY = "#0891B2"
BRAND_DARK = "#0F172A"
BRAND_SURFACE = "#FFFFFF"
BRAND_BG = "#F8FAFC"
BRAND_TEXT = "#0F172A"
BRAND_MUTED = "#64748B"
BRAND_BORDER = "#E2E8F0"
BRAND_SUCCESS = "#059669"
BRAND_WARNING = "#D97706"
BRAND_DANGER = "#DC2626"
BRAND_ACCENT = "#06B6D4"

CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .stApp {
        background: #F8FAFC;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif;
        color: #0F172A;
        letter-spacing: -0.02em;
    }

    h1 {
        font-weight: 800;
        font-size: 2.5rem;
    }
    h2 {
        font-weight: 700;
        font-size: 1.6rem;
    }
    h3 {
        font-weight: 600;
        font-size: 1.2rem;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: #0F172A;
        border-right: none;
    }
    section[data-testid="stSidebar"] .stButton button {
        background: transparent;
        color: #94A3B8;
        border: 1px solid transparent;
        border-radius: 8px;
        padding: 0.5rem 0.75rem;
        font-size: 0.9rem;
        font-weight: 500;
        text-align: left;
        transition: all 0.15s ease;
        width: 100%;
    }
    section[data-testid="stSidebar"] .stButton button:hover {
        background: rgba(255,255,255,0.08);
        color: #F1F5F9;
        border-color: rgba(255,255,255,0.1);
    }
    section[data-testid="stSidebar"] .stButton button[kind="primary"] {
        background: rgba(8, 145, 178, 0.2);
        color: #67E8F9;
        border-color: rgba(8, 145, 178, 0.4);
        font-weight: 600;
    }
    section[data-testid="stSidebar"] .stButton button[kind="primary"]:hover {
        background: rgba(8, 145, 178, 0.3);
        border-color: rgba(8, 145, 178, 0.6);
    }
    section[data-testid="stSidebar"] .stMarkdown {
        color: #94A3B8;
    }
    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.08);
        margin: 1rem 0;
    }
    section[data-testid="stSidebar"] a {
        color: #67E8F9;
        text-decoration: none;
    }
    section[data-testid="stSidebar"] a:hover {
        text-decoration: underline;
    }

    .sidebar-brand {
        padding: 0.25rem 0 1rem 0;
    }
    .sidebar-brand h1 {
        color: #F1F5F9;
        font-size: 1.3rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.03em;
    }
    .sidebar-brand p {
        color: #64748B;
        font-size: 0.8rem;
        margin: 0.15rem 0 0 0;
    }

    /* ── Cards ── */
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlockBorder"] {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.25rem 1.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }

    .card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.25rem 1.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }

    /* ── Metrics ── */
    [data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 0.75rem 1rem;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    [data-testid="stMetric"] > div {
        gap: 0;
    }
    [data-testid="stMetricLabel"] {
        color: #64748B;
        font-size: 0.8rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }
    [data-testid="stMetricValue"] {
        color: #0F172A;
        font-size: 1.6rem;
        font-weight: 700;
    }
    [data-testid="stMetricDelta"] svg {
        display: none;
    }
    [data-testid="stMetricDelta"] {
        color: #059669 !important;
        font-size: 0.8rem;
        font-weight: 600;
    }

    /* ── Buttons ── */
    .stButton button[kind="primary"] {
        background: linear-gradient(135deg, #0891B2, #06B6D4);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.25rem;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.15s ease;
        box-shadow: 0 1px 3px rgba(8,145,178,0.2);
    }
    .stButton button[kind="primary"]:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(8,145,178,0.3);
    }
    .stButton button[kind="secondary"] {
        background: transparent;
        color: #475569;
        border: 1px solid #CBD5E1;
        border-radius: 8px;
        padding: 0.5rem 1.25rem;
        font-weight: 500;
        font-size: 0.9rem;
        transition: all 0.15s ease;
    }
    .stButton button[kind="secondary"]:hover {
        background: #F1F5F9;
        border-color: #94A3B8;
    }

    /* ── File uploader ── */
    [data-testid="stFileUploader"] {
        background: #FFFFFF;
        border: 2px dashed #CBD5E1;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        transition: all 0.15s ease;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: #0891B2;
        background: #F0FDFA;
    }
    [data-testid="stFileUploader"] section {
        padding: 0;
    }
    [data-testid="stFileUploader"] small {
        color: #94A3B8;
    }

    /* ── Expanders ── */
    [data-testid="stExpander"] {
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        background: #FFFFFF;
        margin-bottom: 0.5rem;
        overflow: hidden;
    }
    [data-testid="stExpander"] summary {
        font-weight: 600;
        color: #0F172A;
        padding: 0.75rem 1rem;
    }
    [data-testid="stExpander"] summary:hover {
        background: #F8FAFC;
    }

    /* ── Alerts ── */
    .stAlert {
        border-radius: 8px;
        border: none;
    }
    div[data-baseweb="notification"] {
        border-radius: 8px;
    }

    /* ── Dataframes ── */
    [data-testid="stDataFrame"] {
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        overflow: hidden;
    }
    [data-testid="stDataFrame"] table {
        font-size: 0.85rem;
    }

    /* ── Tabs ── */
    [data-testid="stTabs"] button {
        font-weight: 500;
        font-size: 0.9rem;
    }

    /* ── Dividers ── */
    hr {
        border-color: #E2E8F0;
        margin: 1.5rem 0;
    }

    /* ── Hero ── */
    .hero-section {
        text-align: center;
        padding: 2rem 0 1.5rem 0;
    }
    .hero-section h1 {
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, #0F172A 0%, #0891B2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    .hero-section .subtitle {
        color: #64748B;
        font-size: 1.1rem;
        font-weight: 400;
        max-width: 500px;
        margin: 0 auto;
    }
    .hero-section .badge {
        display: inline-block;
        background: rgba(8,145,178,0.1);
        color: #0891B2;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* ── Step cards ── */
    .step-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        height: 100%;
    }
    .step-card .icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    .step-card h3 {
        font-size: 1rem;
        font-weight: 600;
        color: #0F172A;
        margin-bottom: 0.35rem;
    }
    .step-card p {
        font-size: 0.85rem;
        color: #64748B;
        line-height: 1.4;
        margin: 0;
    }
    .step-number {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 28px;
        height: 28px;
        border-radius: 50%;
        background: #0891B2;
        color: white;
        font-size: 0.8rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }

    /* ── Pro badge ── */
    .pro-badge {
        display: inline-block;
        background: linear-gradient(135deg, #D97706, #F59E0B);
        color: white;
        font-size: 0.65rem;
        font-weight: 700;
        padding: 0.15rem 0.5rem;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* ── Quality score ── */
    .quality-excellent {
        color: #059669;
        font-weight: 700;
    }
    .quality-good {
        color: #0891B2;
        font-weight: 700;
    }
    .quality-fair {
        color: #D97706;
        font-weight: 700;
    }
    .quality-poor {
        color: #DC2626;
        font-weight: 700;
    }

    /* ── Footer ── */
    .app-footer {
        text-align: center;
        color: #94A3B8;
        font-size: 0.75rem;
        padding: 2rem 0 0.5rem 0;
    }
    .app-footer a {
        color: #0891B2;
        text-decoration: none;
    }

    /* ── Progress ── */
    .stProgress > div > div {
        background: linear-gradient(90deg, #0891B2, #06B6D4);
    }

    /* ── Select boxes ── */
    div[data-baseweb="select"] {
        border-radius: 8px;
    }

    /* ── Multiselect ── */
    div[data-baseweb="tag"] {
        border-radius: 6px;
    }

    /* ── Legend / caption ── */
    .stCaption {
        color: #94A3B8;
        font-size: 0.8rem;
    }

    /* ── Cleaning log ── */
    .cleaning-entry {
        padding: 0.35rem 0;
        border-bottom: 1px solid #F1F5F9;
        font-size: 0.9rem;
        color: #334155;
    }
    .cleaning-entry:last-child {
        border-bottom: none;
    }
    .cleaning-entry .step {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 22px;
        height: 22px;
        border-radius: 50%;
        background: #0891B2;
        color: white;
        font-size: 0.7rem;
        font-weight: 600;
        margin-right: 0.5rem;
        flex-shrink: 0;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    ::-webkit-scrollbar-track {
        background: transparent;
    }
    ::-webkit-scrollbar-thumb {
        background: #CBD5E1;
        border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #94A3B8;
    }

    /* ── Spinner ── */
    .stSpinner > div {
        border-color: #0891B2 transparent transparent transparent;
    }

    /* ── Tooltip ── */
    [data-baseweb="tooltip"] {
        border-radius: 6px;
        font-size: 0.8rem;
    }

    /* ── Responsive tweaks ── */
    @media (max-width: 768px) {
        .hero-section h1 {
            font-size: 2rem;
        }
        .hero-section .subtitle {
            font-size: 0.95rem;
        }
        section[data-testid="stSidebar"] {
            min-width: 200px !important;
            max-width: 250px !important;
        }
    }
</style>
"""


def inject_css() -> None:
    st.markdown(CSS, unsafe_allow_html=True)


def sidebar_header() -> str:
    return """
    <div class="sidebar-brand">
        <h1>CleanSheet AI</h1>
        <p>Your Data, Perfectly Clean.</p>
    </div>
    """


def hero_section() -> str:
    return """
    <div class="hero-section">
        <div class="badge">Free · No sign-up</div>
        <h1>Clean data, clear mind.</h1>
        <p class="subtitle">Upload a messy CSV. Get a pristine dataset in seconds.</p>
    </div>
    """


def step_card(number: int, icon: str, title: str, desc: str) -> str:
    return f"""
    <div class="step-card">
        <div class="step-number">{number}</div>
        <div class="icon">{icon}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
    </div>
    """


def cleaning_log_entry(index: int, text: str) -> str:
    return f"""
    <div class="cleaning-entry">
        <span class="step">{index}</span>{text}
    </div>
    """


def pro_badge() -> str:
    return '<span class="pro-badge">Pro</span>'
