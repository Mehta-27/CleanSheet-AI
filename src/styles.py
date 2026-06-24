"""CleanSheet AI — Professional Design System & Theme Engine.

Data-analyst-grade UI. Clean, readable, trustworthy.
No neon, no glow, no cyberpunk — just professional tool aesthetics.
"""

import streamlit as st

# ── Google Fonts ──────────────────────────────────────────────────────────
FONTS = "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');"

# ── Design Tokens ─────────────────────────────────────────────────────────
DARK_TOKENS = """
    --bg-primary: #0F0E17;
    --bg-secondary: #1A192B;
    --bg-tertiary: #232136;
    --bg-card: #1A192B;
    --bg-card-hover: #232136;
    --bg-sidebar: #121121;
    --border-subtle: rgba(255, 255, 255, 0.07);
    --border-medium: rgba(255, 255, 255, 0.12);
    --border-focus: #A78BFA;
    --text-primary: #E2E8F0;
    --text-secondary: #8B95A5;
    --text-tertiary: #5A6374;
    --text-heading: #F1F5F9;
    --accent-purple: #A78BFA;
    --accent-pink: #F472B6;
    --accent-amber: #E5A019;
    --accent-green: #22C55E;
    --accent-red: #EF4444;
    --accent-orange: #F97316;
    --gradient-btn: linear-gradient(135deg, #A78BFA, #7C3AED);
    --gradient-pro: linear-gradient(135deg, #E5A019, #D97706);
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.25);
    --shadow-md: 0 2px 8px rgba(0, 0, 0, 0.3);
    --radius-sm: 6px;
    --radius-md: 8px;
    --radius-lg: 10px;
"""

LIGHT_TOKENS = """
    --bg-primary: #FAFBFC;
    --bg-secondary: #FFFFFF;
    --bg-tertiary: #F4F5F7;
    --bg-card: #FFFFFF;
    --bg-card-hover: #F9FAFB;
    --bg-sidebar: #FFFFFF;
    --border-subtle: rgba(0, 0, 0, 0.07);
    --border-medium: rgba(0, 0, 0, 0.12);
    --border-focus: #8B5CF6;
    --text-primary: #1A202C;
    --text-secondary: #64748B;
    --text-tertiary: #94A3B8;
    --text-heading: #0F172A;
    --accent-purple: #8B5CF6;
    --accent-pink: #EC4899;
    --accent-amber: #D97706;
    --accent-green: #16A34A;
    --accent-red: #DC2626;
    --accent-orange: #EA580C;
    --gradient-btn: linear-gradient(135deg, #8B5CF6, #6D28D9);
    --gradient-pro: linear-gradient(135deg, #D97706, #B45309);
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.06);
    --shadow-md: 0 2px 8px rgba(0, 0, 0, 0.08);
    --radius-sm: 6px;
    --radius-md: 8px;
    --radius-lg: 10px;
"""

# ── Animations (subtle only) ─────────────────────────────────────────────
ANIMATIONS = """
    @keyframes fadeIn {
        from { opacity: 0; }
        to   { opacity: 1; }
    }
"""

# ── Component Styles ──────────────────────────────────────────────────────
COMPONENT_CSS = """
    /* ── Overflow safety ── */
    html, body, .stApp, #root, .main {
        overflow-x: hidden !important;
        max-width: 100vw !important;
    }

    /* ── Box-sizing ── */
    *, *::before, *::after {
        box-sizing: border-box !important;
    }

    /* ── Typography (emoji-safe — covers elements AND pseudo-elements) ── */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Segoe UI Emoji', 'Apple Color Emoji', 'Noto Color Emoji', sans-serif !important;
    }
    *::before, *::after {
        font-family: inherit !important;
    }
    .material-symbols-rounded,
    .material-symbols-outlined {
        font-family: 'Material Symbols Rounded', sans-serif !important;
    }
    .material-symbols-rounded::before,
    .material-symbols-rounded::after,
    .material-symbols-outlined::before,
    .material-symbols-outlined::after {
        font-family: 'Material Symbols Rounded' !important;
    }

    .stApp {
        background: var(--bg-primary) !important;
        color: var(--text-primary) !important;
    }

    .main .block-container {
        max-width: 1100px !important;
        padding: 1.5rem 1.5rem !important;
        margin: 0 auto !important;
    }

    /* Every column must respect its container */
    div[data-testid="column"] {
        min-width: 0 !important;
        width: 100% !important;
        overflow: hidden !important;
    }

    /* Horizontal rows — wrap when tight */
    div.row-widget.stHorizontal {
        flex-wrap: wrap !important;
        gap: 0.4rem !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: var(--text-heading) !important;
        font-weight: 600 !important;
        letter-spacing: -0.01em !important;
    }
    p, span, label, div { color: var(--text-primary); }
    a { color: var(--accent-purple) !important; text-decoration: none !important; }
    a:hover { text-decoration: underline !important; }
    hr { border-color: var(--border-subtle) !important; margin: 1rem 0 !important; }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: var(--bg-sidebar) !important;
        border-right: 1px solid var(--border-subtle) !important;
        min-width: 260px !important;
        max-width: 300px !important;
    }
    section[data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 2px; height: 100%;
        background: var(--accent-purple);
        z-index: 10;
    }
    [data-testid="stSidebarCollapsedControl"],
    [data-testid="stSidebarNavCollapseButton"],
    button[data-testid="stBaseButton-headerNoPadding"] {
        display: none !important;
    }
    section[data-testid="stSidebar"] [data-testid="stMarkdown"] p,
    section[data-testid="stSidebar"] [data-testid="stMarkdown"] span,
    section[data-testid="stSidebar"] [data-testid="stMarkdown"] li {
        color: var(--text-secondary) !important;
        font-size: 0.82rem !important;
    }
    section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3, section[data-testid="stSidebar"] h4,
    section[data-testid="stSidebar"] h5 { color: var(--text-heading) !important; }
    section[data-testid="stSidebar"] hr { border-color: var(--border-subtle) !important; margin: 0.6rem 0 !important; }

    /* ── Cards / Containers ── */
    div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorder"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        padding: 0.65rem 0.85rem !important;
        transition: border-color 0.15s ease !important;
        overflow: hidden !important;
    }
    div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorder"]:hover {
        border-color: var(--border-medium) !important;
    }
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlockBorder"] div[data-testid="stVerticalBlockBorder"] {
        padding: 0.4rem 0.6rem !important;
        background: var(--bg-tertiary) !important;
    }

    /* Fix expander overflow */
    [data-testid="stExpander"] [data-testid="stVerticalBlock"] {
        overflow: hidden !important;
    }

    /* ── Metrics (compact, prevents overlap in 4-column rows) ── */
    div[data-testid="stMetricRow"] { gap: 0.35rem !important; }
    [data-testid="stMetric"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        padding: 0.45rem 0.6rem !important;
        transition: border-color 0.15s ease !important;
        overflow: hidden !important;
    }
    [data-testid="stMetric"]:hover { border-color: var(--border-medium) !important; }
    [data-testid="stMetric"] [data-testid="stMetricLabel"] {
        color: var(--text-secondary) !important;
        font-weight: 500 !important;
        font-size: 0.65rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.03em !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: var(--text-heading) !important;
        font-weight: 700 !important;
        font-size: 1.15rem !important;
        line-height: 1.2 !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricDelta"] { font-weight: 600 !important; }

    /* ── File Uploader — big centered drop zone ── */
    [data-testid="stFileUploader"] {
        max-width: 480px !important;
        margin: 0.5rem auto !important;
        border: 2px dashed var(--border-medium) !important;
        border-radius: 16px !important;
        padding: 0 !important;
        text-align: center !important;
        background: var(--bg-card) !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        min-height: 140px;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: var(--accent-purple) !important;
        transform: translateY(-2px);
        box-shadow: 0 12px 40px rgba(167, 139, 250, 0.12);
    }
    [data-testid="stFileUploader"]:active {
        transform: translateY(0px) scale(0.98) !important;
    }
    [data-testid="stFileUploader"] section {
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        background: transparent !important;
    }
    [data-testid="stFileUploader"] section > span,
    [data-testid="stFileUploader"] section > small,
    [data-testid="stFileUploader"] section > div > small,
    [data-testid="stFileUploader"] > label,
    [data-testid="stFileUploader"] label,
    [data-testid="stFileUploader"] [data-testid="stMarkdownContainer"] {
        display: none !important;
    }
    [data-testid="stFileUploader"] button {
        background: var(--gradient-btn) !important;
        color: white !important;
        border: none !important;
        border-radius: 999px !important;
        padding: 0.75rem 2.5rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        cursor: pointer !important;
        transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    }
    [data-testid="stFileUploader"] button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 24px rgba(167, 139, 250, 0.35) !important;
    }
    [data-testid="stFileUploader"] button:active {
        transform: translateY(0px) scale(0.94) !important;
    }

    /* ── Expanders ── */
    [data-testid="stExpander"] {
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        background: var(--bg-card) !important;
        margin-bottom: 0.4rem !important;
        transition: border-color 0.15s ease !important;
        overflow: hidden !important;
    }
    [data-testid="stExpander"]:hover { border-color: var(--border-medium) !important; }
    [data-testid="stExpander"] summary { color: var(--text-primary) !important; font-weight: 600 !important; }

    /* ── Buttons ── */
    .stButton > button { width: 100% !important; }
    .stButton > button[kind="primary"],
    .stButton > button[data-testid="stBaseButton-primary"] {
        background: var(--gradient-btn) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        padding: 0.35rem 0.8rem !important;
        transition: all 0.15s ease !important;
    }
    .stButton > button[kind="primary"]:hover {
        opacity: 0.95 !important;
        box-shadow: 0 4px 12px rgba(167, 139, 250, 0.25) !important;
    }
    .stButton > button[kind="secondary"],
    .stButton > button[data-testid="stBaseButton-secondary"] {
        background: var(--bg-card) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-medium) !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 500 !important;
        font-size: 0.85rem !important;
        padding: 0.35rem 0.8rem !important;
        transition: all 0.15s ease !important;
    }
    .stButton > button[kind="secondary"]:hover { border-color: var(--accent-purple) !important; }
    .stDownloadButton > button {
        background: var(--gradient-btn) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        padding: 0.35rem 0.8rem !important;
    }
    .stDownloadButton > button:hover { opacity: 0.9 !important; }

    /* ── Inputs ── */
    [data-testid="stSelectbox"],
    [data-testid="stMultiSelect"],
    [data-testid="stTextInput"],
    [data-testid="stSelectbox"] label,
    [data-testid="stMultiSelect"] label,
    [data-testid="stTextInput"] label { color: var(--text-primary) !important; }
    .stSelectbox > div > div,
    .stMultiSelect > div > div,
    .stTextInput > div > div > input {
        background: var(--bg-card) !important;
        border-color: var(--border-medium) !important;
        color: var(--text-primary) !important;
        border-radius: var(--radius-sm) !important;
        font-size: 0.82rem !important;
    }
    .stSelectbox > div > div:focus-within,
    .stMultiSelect > div > div:focus-within,
    .stTextInput > div > div > input:focus {
        border-color: var(--accent-purple) !important;
        box-shadow: 0 0 0 2px rgba(167, 139, 250, 0.1) !important;
    }
    .stCheckbox label span { color: var(--text-primary) !important; }

    /* ── Dataframes (prevent overflow) ── */
    [data-testid="stDataFrame"] {
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        overflow-x: auto !important;
        overflow-y: auto !important;
    }
    [data-testid="stDataFrame"] [data-testid="stDataFrameContainer"] {
        max-width: 100% !important;
        overflow-x: auto !important;
    }
    [data-testid="stDataFrame"] table {
        font-size: 0.78rem !important;
    }

    /* ── Alerts ── */
    [data-testid="stAlert"] { border-radius: var(--radius-sm) !important; }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab"] { color: var(--text-secondary) !important; font-weight: 500 !important; font-size: 0.85rem !important; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: var(--accent-purple) !important; }

    /* ── Toast ── */
    [data-testid="stToast"] {
        background: var(--bg-secondary) !important;
        border: 1px solid var(--border-subtle) !important;
        color: var(--text-primary) !important;
        border-radius: var(--radius-md) !important;
    }

    /* ── Plotly charts ── */
    .stPlotlyChart {
        overflow: hidden !important;
    }
    .js-plotly-plot, .plot-container {
        max-width: 100% !important;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: var(--bg-primary); }
    ::-webkit-scrollbar-thumb { background: var(--border-medium); border-radius: 999px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--text-tertiary); }

    /* ── Main content fade-in ── */
    .main .block-container { animation: fadeIn 0.3s ease; }

    /* ── Utility classes ── */
    .section-header {
        font-size: 1.35rem;
        font-weight: 600;
        color: var(--text-heading);
        margin-bottom: 1rem;
        padding-bottom: 0.4rem;
        border-bottom: 2px solid var(--accent-purple);
    }

    .feature-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        padding: 0.3rem 0.7rem;
        border-radius: var(--radius-sm);
        font-size: 0.78rem;
        font-weight: 500;
        border: 1px solid var(--border-subtle);
        background: var(--bg-card);
        color: var(--text-secondary);
        margin: 0.15rem;
    }

    .pro-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.15rem 0.5rem;
        border-radius: var(--radius-sm);
        font-size: 0.68rem;
        font-weight: 700;
        background: var(--gradient-pro);
        color: white;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    .cleaning-entry {
        display: flex;
        align-items: center;
        padding: 0.5rem 0.75rem;
        margin-bottom: 0.3rem;
        border-radius: var(--radius-sm);
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        font-size: 0.85rem;
        color: var(--text-primary);
    }
    .cleaning-entry .step {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 20px; height: 20px;
        border-radius: 50%;
        background: var(--accent-purple);
        color: white;
        font-size: 0.65rem;
        font-weight: 700;
        margin-right: 0.6rem;
    }

    .severity-critical {
        display: inline-block;
        padding: 0.1rem 0.45rem;
        border-radius: var(--radius-sm);
        font-size: 0.7rem;
        font-weight: 600;
        background: rgba(239, 68, 68, 0.1);
        color: var(--accent-red);
        border: 1px solid rgba(239, 68, 68, 0.15);
    }
    .severity-warning {
        display: inline-block;
        padding: 0.1rem 0.45rem;
        border-radius: var(--radius-sm);
        font-size: 0.7rem;
        font-weight: 600;
        background: rgba(229, 160, 25, 0.1);
        color: var(--accent-amber);
        border: 1px solid rgba(229, 160, 25, 0.15);
    }
    .severity-info {
        display: inline-block;
        padding: 0.1rem 0.45rem;
        border-radius: var(--radius-sm);
        font-size: 0.7rem;
        font-weight: 600;
        background: rgba(167, 139, 250, 0.1);
        color: var(--accent-purple);
        border: 1px solid rgba(167, 139, 250, 0.15);
    }

    /* ── Pro CTA ── */
    .pro-cta-card {
        background: linear-gradient(180deg, var(--bg-card) 0%, rgba(229, 160, 25, 0.02) 100%) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        padding: 0.85rem !important;
        margin: 0.4rem 0 !important;
        border-left: 3px solid var(--accent-amber) !important;
        transition: all 0.2s ease !important;
    }
    .pro-cta-card:hover {
        border-color: rgba(229, 160, 25, 0.3) !important;
        box-shadow: 0 4px 12px rgba(229, 160, 25, 0.05) !important;
        transform: translateY(-1px) !important;
    }
    .pro-cta-card ul { list-style: none !important; padding: 0 !important; margin: 0.4rem 0 !important; }
    .pro-cta-card li {
        padding: 0.15rem 0 !important;
        font-size: 0.78rem !important;
        color: var(--text-secondary) !important;
    }
    .pro-cta-card li::before { content: '→ ' !important; color: var(--accent-amber) !important; }
    .pro-cta-btn {
        display: block !important;
        background: var(--gradient-pro) !important;
        color: white !important;
        text-align: center !important;
        padding: 0.5rem 0.85rem !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        font-size: 0.82rem !important;
        text-decoration: none !important;
        transition: all 0.2s ease !important;
    }
    .pro-cta-btn:hover {
        opacity: 0.95 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(217, 119, 6, 0.2) !important;
    }
    .pro-cta-btn:active {
        transform: translateY(0px) scale(0.98) !important;
    }

    /* ── Support Card ── */
    .support-card {
        background: linear-gradient(180deg, var(--bg-card) 0%, rgba(20, 184, 166, 0.02) 100%) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        padding: 0.85rem !important;
        margin: 0.4rem 0 !important;
        border-left: 3px solid var(--accent-pink) !important;
        transition: all 0.2s ease !important;
    }
    .support-card:hover {
        border-color: rgba(20, 184, 166, 0.3) !important;
        box-shadow: 0 4px 12px rgba(20, 184, 166, 0.05) !important;
        transform: translateY(-1px) !important;
    }

    /* ── Version Badge ── */
    .version-badge {
        display: inline-block;
        padding: 0.1rem 0.4rem;
        border-radius: var(--radius-sm);
        font-size: 0.68rem;
        font-weight: 500;
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        color: var(--text-tertiary);
    }

    /* ── Feature cards ── */
    .feature-card {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-md);
        padding: 1rem;
        text-align: center;
        transition: all 0.2s ease !important;
        height: 100%;
    }
    .feature-card:hover {
        border-color: var(--border-medium) !important;
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-md) !important;
    }
    .feature-card .icon { font-size: 1.3rem; margin-bottom: 0.3rem; display: block; }
    .feature-card h4 { font-size: 0.85rem; font-weight: 600; margin-bottom: 0.2rem; color: var(--text-heading); }
    .feature-card p { font-size: 0.78rem; color: var(--text-secondary); line-height: 1.4; margin: 0; }

    /* ── Feedback / success banner (inline, survives reruns) ── */
    .feedback-banner {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 0.75rem;
        border-radius: var(--radius-sm);
        margin: 0.4rem 0;
        font-weight: 500;
        font-size: 0.82rem;
        animation: fadeSlideIn 0.3s ease;
    }
    .feedback-banner.success { background: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.25); color: var(--accent-green); }
    .feedback-banner.info { background: rgba(167, 139, 250, 0.1); border: 1px solid rgba(167, 139, 250, 0.25); color: var(--accent-purple); }
    .feedback-banner.warning { background: rgba(229, 160, 25, 0.1); border: 1px solid rgba(229, 160, 25, 0.25); color: var(--accent-amber); }
    .feedback-banner.error { background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.25); color: var(--accent-red); }
    @keyframes fadeSlideIn {
        from { opacity: 0; transform: translateY(-6px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* ── Onboarding / Hero Section ── */
    .hero-title {
        font-size: 2rem !important;
        font-weight: 800 !important;
        color: var(--text-heading) !important;
        letter-spacing: -0.03em !important;
        margin-bottom: 0.4rem !important;
        background: linear-gradient(135deg, var(--text-heading) 40%, var(--accent-purple)) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        text-align: center !important;
        word-break: break-word !important;
    }
    .hero-subtitle {
        font-size: 0.95rem !important;
        color: var(--text-secondary) !important;
        max-width: 540px !important;
        margin: 0 auto 1.2rem auto !important;
        line-height: 1.5 !important;
        text-align: center !important;
        padding: 0 0.5rem !important;
    }
"""


def _build_css(dark: bool) -> str:
    tokens = DARK_TOKENS if dark else LIGHT_TOKENS
    return (
        f"<style>\n"
        f"  {FONTS}\n"
        f"  :root {{ {tokens} }}\n"
        f"  {ANIMATIONS}\n"
        f"  {COMPONENT_CSS}\n"
        f"</style>\n"
    )


def inject_css() -> None:
    """Inject the full design system CSS, respecting dark/light mode state."""
    dark = st.session_state.get("dark_mode", True)
    st.markdown(_build_css(dark), unsafe_allow_html=True)


def get_plotly_theme() -> dict:
    """Return Plotly layout overrides matching the current theme."""
    dark = st.session_state.get("dark_mode", True)
    if dark:
        return {
            "paper_bgcolor": "rgba(0,0,0,0)",
            "plot_bgcolor": "rgba(0,0,0,0)",
            "font_color": "#8B95A5",
            "colorway": ["#A78BFA", "#F472B6", "#E5A019", "#22C55E", "#EF4444", "#60A5FA"],
        }
    return {
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "font_color": "#64748B",
        "colorway": ["#8B5CF6", "#EC4899", "#D97706", "#16A34A", "#DC2626", "#3B82F6"],
    }
