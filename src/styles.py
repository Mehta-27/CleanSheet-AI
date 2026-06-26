"""CleanSheet AI — Design System.

Professional dark/light theme. Streamlit-native. Minimal overrides.
"""

import streamlit as st

# ── Font ────────────────────────────────────────────────────────────────────
FONTS = "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');"

# ── Design Tokens ───────────────────────────────────────────────────────────
DARK_TOKENS = """
    --bg-primary: #111827;
    --bg-secondary: #1E293B;
    --bg-card: #1F2937;
    --bg-sidebar: #0F172A;
    --border: #374151;
    --border-light: #4B5563;
    --accent: #6366F1;
    --accent-hover: #818CF8;
    --accent-amber: #F59E0B;
    --success: #22C55E;
    --warning: #F59E0B;
    --danger: #EF4444;
    --text: #F9FAFB;
    --text-secondary: #9CA3AF;
    --text-tertiary: #6B7280;
    --radius: 12px;
    --radius-sm: 8px;
    --shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
"""

LIGHT_TOKENS = """
    --bg-primary: #FFFFFF;
    --bg-secondary: #F9FAFB;
    --bg-card: #FFFFFF;
    --bg-sidebar: #F3F4F6;
    --border: #E5E7EB;
    --border-light: #D1D5DB;
    --accent: #6366F1;
    --accent-hover: #4F46E5;
    --accent-amber: #D97706;
    --success: #16A34A;
    --warning: #D97706;
    --danger: #DC2626;
    --text: #111827;
    --text-secondary: #6B7280;
    --text-tertiary: #9CA3AF;
    --radius: 12px;
    --radius-sm: 8px;
    --shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
"""

# ── Component Styles ────────────────────────────────────────────────────────
COMPONENT_CSS = """
    /* ── Base ── */
    html, body, .stApp, #root { overflow-x: hidden; }
    * { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important; }
    .stApp { background: var(--bg-primary); color: var(--text); }

    h1, h2, h3, h4, h5, h6 { color: var(--text) !important; font-weight: 600 !important; }
    a { color: var(--accent) !important; }
    hr { border-color: var(--border) !important; margin: 1.5rem 0 !important; }

    .main .block-container {
        max-width: 1100px;
        padding: 2rem 1.5rem !important;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: var(--bg-sidebar) !important;
        border-right: 1px solid var(--border) !important;
        min-width: 250px !important;
    }
    section[data-testid="stSidebar"] hr { margin: 0.75rem 0 !important; }

    /* ── Buttons ── */
    .stButton > button { width: 100%; }
    .stButton > button[kind="primary"],
    .stButton > button[data-testid="stBaseButton-primary"] {
        background: var(--accent) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        padding: 0.4rem 1rem !important;
    }
    .stButton > button[kind="primary"]:hover { background: var(--accent-hover) !important; }
    .stButton > button[kind="secondary"],
    .stButton > button[data-testid="stBaseButton-secondary"] {
        background: transparent !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 500 !important;
        padding: 0.4rem 1rem !important;
    }
    .stButton > button[kind="secondary"]:hover { border-color: var(--accent) !important; }
    .stDownloadButton > button {
        background: var(--accent) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        padding: 0.4rem 1rem !important;
    }

    /* ── Cards (native Streamlit containers with border) ── */
    div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorder"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius) !important;
        padding: 1rem !important;
    }

    /* ── Metrics ── */
    [data-testid="stMetric"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius) !important;
        padding: 0.75rem 1rem !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricLabel"] {
        color: var(--text-secondary) !important;
        font-weight: 500 !important;
        font-size: 0.75rem !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: var(--text) !important;
        font-weight: 700 !important;
        font-size: 1.25rem !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricDelta"] {
        font-weight: 600 !important;
    }

    /* ── Expanders ── */
    [data-testid="stExpander"] {
        border: 1px solid var(--border) !important;
        border-radius: var(--radius) !important;
        background: var(--bg-card) !important;
        margin-bottom: 0.5rem !important;
    }

    /* ── File Uploader ── */
    [data-testid="stFileUploader"] {
        max-width: 480px !important;
        margin: 0 auto !important;
        border: 2px dashed var(--border) !important;
        border-radius: var(--radius) !important;
        background: var(--bg-card) !important;
        padding: 2rem !important;
        text-align: center !important;
    }
    [data-testid="stFileUploader"]:hover { border-color: var(--accent) !important; }
    [data-testid="stFileUploader"] > label { display: none !important; }

    /* ── Inputs ── */
    .stSelectbox > div > div,
    .stMultiSelect > div > div,
    .stTextInput > div > div > input {
        background: var(--bg-card) !important;
        border-color: var(--border) !important;
        color: var(--text) !important;
        border-radius: var(--radius-sm) !important;
    }
    .stSelectbox > div > div:focus-within,
    .stMultiSelect > div > div:focus-within,
    .stTextInput > div > div > input:focus {
        border-color: var(--accent) !important;
    }

    /* ── DataFrames ── */
    [data-testid="stDataFrame"] {
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        overflow: auto !important;
    }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab"] {
        color: var(--text-secondary) !important;
        font-weight: 500 !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: var(--accent) !important; }

    /* ── Plotly ── */
    .stPlotlyChart { overflow: hidden; }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 999px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--border-light); }

    /* ── Sidebar Utils ── */
    .sidebar-brand {
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--text);
        padding: 0.25rem 0;
    }
    .sidebar-label {
        color: var(--text-tertiary);
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin: 0.75rem 0 0.25rem 0;
    }

    /* ── Pro card (sidebar) ── */
    .pro-card {
        background: linear-gradient(180deg, var(--bg-card) 0%, rgba(99, 102, 241, 0.03) 100%) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius) !important;
        padding: 0.85rem !important;
        margin: 0.5rem 0 !important;
        border-left: 3px solid var(--accent-amber) !important;
    }
    .pro-card ul { list-style: none; padding: 0; margin: 0.4rem 0; }
    .pro-card li {
        padding: 0.15rem 0;
        font-size: 0.78rem;
        color: var(--text-secondary);
    }
    .pro-card li::before { content: '✦ '; color: var(--accent-amber); }
    .pro-btn {
        display: block;
        background: var(--accent-amber) !important;
        color: white !important;
        text-align: center;
        padding: 0.5rem 0.85rem;
        border-radius: var(--radius-sm);
        font-weight: 600;
        font-size: 0.82rem;
        text-decoration: none !important;
        transition: opacity 0.15s ease;
    }
    .pro-btn:hover { opacity: 0.9; }

    /* ── Support card (sidebar) ── */
    .support-card {
        background: linear-gradient(180deg, var(--bg-card) 0%, rgba(99, 102, 241, 0.02) 100%) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius) !important;
        padding: 0.85rem !important;
        margin: 0.5rem 0 !important;
        border-left: 3px solid var(--accent) !important;
    }

    /* ── Version badge ── */
    .version-badge {
        display: inline-block;
        padding: 0.1rem 0.45rem;
        border-radius: var(--radius-sm);
        font-size: 0.68rem;
        font-weight: 500;
        background: var(--bg-card);
        border: 1px solid var(--border);
        color: var(--text-tertiary);
    }

    /* ── Cleaning history entries ── */
    .cleaning-entry {
        display: flex;
        align-items: center;
        padding: 0.5rem 0.75rem;
        margin-bottom: 0.3rem;
        border-radius: var(--radius-sm);
        background: var(--bg-secondary);
        border: 1px solid var(--border);
        font-size: 0.85rem;
        color: var(--text);
    }
    .cleaning-entry .step {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 22px; height: 22px;
        border-radius: 50%;
        background: var(--accent);
        color: white;
        font-size: 0.65rem;
        font-weight: 700;
        margin-right: 0.6rem;
        flex-shrink: 0;
    }

    /* ── Section header ── */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text);
        margin-bottom: 1.25rem;
    }

    /* ── Responsive ── */
    @media (max-width: 640px) {
        .main .block-container { padding: 1rem 0.75rem !important; }
        [data-testid="stMetric"] { padding: 0.5rem !important; }
        [data-testid="stMetric"] [data-testid="stMetricValue"] { font-size: 1.05rem !important; }
        .section-header { font-size: 1.2rem !important; }
    }
"""


def _build_css(dark: bool) -> str:
    tokens = DARK_TOKENS if dark else LIGHT_TOKENS
    return f"<style>\n{FONTS}\n:root {{{tokens}}}\n{COMPONENT_CSS}\n</style>\n"


def inject_css() -> None:
    dark = st.session_state.get("dark_mode", True)
    st.markdown(_build_css(dark), unsafe_allow_html=True)


def get_plotly_theme() -> dict:
    dark = st.session_state.get("dark_mode", True)
    if dark:
        return {
            "paper_bgcolor": "rgba(0,0,0,0)",
            "plot_bgcolor": "rgba(0,0,0,0)",
            "font_color": "#9CA3AF",
            "colorway": ["#6366F1", "#22C55E", "#F59E0B", "#EF4444", "#818CF8", "#34D399"],
        }
    return {
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "font_color": "#6B7280",
        "colorway": ["#6366F1", "#16A34A", "#D97706", "#DC2626", "#818CF8", "#34D399"],
    }
