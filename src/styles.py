"""CleanSheet AI — Professional Design System & Theme Engine.

Data-analyst-grade UI. Clean, readable, trustworthy.
No neon, no glow, no cyberpunk — just professional tool aesthetics.
"""

import streamlit as st

# ── Google Fonts ──────────────────────────────────────────────────────────
FONTS = "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');"

# ── Design Tokens ─────────────────────────────────────────────────────────
DARK_TOKENS = """
    --bg-primary: #111318;
    --bg-secondary: #1A1D24;
    --bg-tertiary: #22252E;
    --bg-card: #1A1D24;
    --bg-card-hover: #22252E;
    --bg-sidebar: #15171E;
    --border-subtle: rgba(255, 255, 255, 0.07);
    --border-medium: rgba(255, 255, 255, 0.12);
    --border-focus: #3B82F6;
    --text-primary: #E2E8F0;
    --text-secondary: #8B95A5;
    --text-tertiary: #5A6374;
    --text-heading: #F1F5F9;
    --accent-blue: #3B82F6;
    --accent-teal: #14B8A6;
    --accent-amber: #E5A019;
    --accent-green: #22C55E;
    --accent-red: #EF4444;
    --accent-orange: #F97316;
    --gradient-btn: linear-gradient(135deg, #3B82F6, #2563EB);
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
    --border-focus: #3B82F6;
    --text-primary: #1A202C;
    --text-secondary: #64748B;
    --text-tertiary: #94A3B8;
    --text-heading: #0F172A;
    --accent-blue: #2563EB;
    --accent-teal: #0D9488;
    --accent-amber: #D97706;
    --accent-green: #16A34A;
    --accent-red: #DC2626;
    --accent-orange: #EA580C;
    --gradient-btn: linear-gradient(135deg, #2563EB, #1D4ED8);
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
    /* ── Global Box Sizing ── */
    *, *::before, *::after {
        box-sizing: border-box !important;
    }

    /* ── Typography (emoji-safe) ── */
    body, .stApp, p, span, label, h1, h2, h3, h4, h5, h6, div, a, li, strong, em, small, code, pre, th, td, input, textarea, select, option, button {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Segoe UI Emoji', 'Apple Color Emoji', 'Noto Color Emoji', sans-serif !important;
    }
    .material-symbols-rounded,
    .material-symbols-outlined,
    [data-testid="stSidebarCollapsedControl"] span,
    [data-testid="stSidebarNavCollapseButton"] span,
    button[kind="header"] span {
        font-family: 'Material Symbols Rounded', sans-serif !important;
    }

    .stApp {
        background: var(--bg-primary) !important;
        color: var(--text-primary) !important;
        overflow-x: hidden !important;
    }

    .main .block-container {
        max-width: 1200px !important;
        padding: 2rem 2rem !important;
        margin: 0 auto !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: var(--text-heading) !important;
        font-weight: 600 !important;
        letter-spacing: -0.01em !important;
    }
    p, span, label, div { color: var(--text-primary); }
    a { color: var(--accent-blue) !important; text-decoration: none !important; }
    a:hover { text-decoration: underline !important; }
    hr { border-color: var(--border-subtle) !important; margin: 1rem 0 !important; }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: var(--bg-sidebar) !important;
        border-right: 1px solid var(--border-subtle) !important;
        min-width: 280px !important;
    }
    section[data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 2px; height: 100%;
        background: var(--accent-blue);
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
        font-size: 0.85rem !important;
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4,
    section[data-testid="stSidebar"] h5 {
        color: var(--text-heading) !important;
    }
    section[data-testid="stSidebar"] hr {
        border-color: var(--border-subtle) !important;
        margin: 0.75rem 0 !important;
    }

    /* ── Cards / Containers ── */
    div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorder"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        padding: 0.75rem 1rem !important;
        transition: border-color 0.15s ease !important;
        overflow: hidden !important;
    }
    div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorder"]:hover {
        border-color: var(--border-medium) !important;
    }

    /* Prevent nested container padding stacking */
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlockBorder"] div[data-testid="stVerticalBlockBorder"] {
        padding: 0.5rem 0.75rem !important;
        background: var(--bg-tertiary) !important;
    }

    /* Column spacing fix — prevent overflow */
    section[data-testid="stMain"] div[data-testid="column"] {
        min-width: 0 !important;
    }

    /* Ensure columns don't overflow on narrow screens */
    div.row-widget.stHorizontal {
        flex-wrap: wrap !important;
        gap: 0.5rem !important;
    }

    /* Fix expander overflow */
    [data-testid="stExpander"] [data-testid="stVerticalBlock"] {
        overflow: hidden !important;
    }

    /* ── Metrics ── */
    div[data-testid="stMetricRow"] {
        gap: 0.5rem !important;
    }
    [data-testid="stMetric"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        padding: 0.6rem 0.85rem !important;
        transition: border-color 0.15s ease !important;
        overflow: hidden !important;
        min-width: 0 !important;
    }
    [data-testid="stMetric"]:hover {
        border-color: var(--border-medium) !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricLabel"] {
        color: var(--text-secondary) !important;
        font-weight: 500 !important;
        font-size: 0.72rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.04em !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: var(--text-heading) !important;
        font-weight: 700 !important;
        font-size: 1.35rem !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricDelta"] {
        font-weight: 600 !important;
    }

    /* ── File Uploader ── */
    [data-testid="stFileUploader"] {
        border: 2px dashed var(--border-medium) !important;
        border-radius: var(--radius-lg) !important;
        padding: 1.5rem !important;
        text-align: center !important;
        transition: border-color 0.2s ease !important;
        background: var(--bg-card) !important;
        max-width: 100% !important;
        overflow: hidden !important;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: var(--accent-blue) !important;
    }
    [data-testid="stFileUploader"] button {
        white-space: nowrap !important;
    }
    [data-testid="stFileUploader"] small {
        color: var(--text-tertiary) !important;
    }
    [data-testid="stFileUploader"] section {
        max-width: 100% !important;
        overflow: hidden !important;
    }
    [data-testid="stFileUploader"] div[data-testid="stMarkdown"] {
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }

    /* ── Expanders ── */
    [data-testid="stExpander"] {
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        background: var(--bg-card) !important;
        margin-bottom: 0.5rem !important;
        transition: border-color 0.15s ease !important;
        overflow: hidden !important;
    }
    [data-testid="stExpander"]:hover {
        border-color: var(--border-medium) !important;
    }
    [data-testid="stExpander"] summary {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
    }

    /* ── Buttons ── */
    .stButton > button[kind="primary"],
    .stButton > button[data-testid="stBaseButton-primary"] {
        background: var(--gradient-btn) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    .stButton > button[kind="primary"]:hover,
    .stButton > button[data-testid="stBaseButton-primary"]:hover {
        opacity: 0.95 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25) !important;
    }
    .stButton > button[kind="primary"]:active,
    .stButton > button[data-testid="stBaseButton-primary"]:active {
        transform: translateY(0px) scale(0.98) !important;
    }
    .stButton > button[kind="secondary"],
    .stButton > button[data-testid="stBaseButton-secondary"] {
        background: var(--bg-card) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-medium) !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 500 !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    .stButton > button[kind="secondary"]:hover,
    .stButton > button[data-testid="stBaseButton-secondary"]:hover {
        border-color: var(--accent-blue) !important;
        transform: translateY(-1px) !important;
        box-shadow: var(--shadow-sm) !important;
    }
    .stButton > button[kind="secondary"]:active,
    .stButton > button[data-testid="stBaseButton-secondary"]:active {
        transform: translateY(0px) scale(0.98) !important;
    }

    /* ── Download Buttons ── */
    .stDownloadButton > button {
        background: var(--gradient-btn) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        transition: opacity 0.15s ease !important;
    }
    .stDownloadButton > button:hover { opacity: 0.9 !important; }

    /* ── Inputs ── */
    [data-testid="stSelectbox"],
    [data-testid="stMultiSelect"],
    [data-testid="stTextInput"] { color: var(--text-primary) !important; }
    .stSelectbox > div > div,
    .stMultiSelect > div > div,
    .stTextInput > div > div > input {
        background: var(--bg-card) !important;
        border-color: var(--border-medium) !important;
        color: var(--text-primary) !important;
        border-radius: var(--radius-sm) !important;
    }
    .stSelectbox > div > div:focus-within,
    .stMultiSelect > div > div:focus-within,
    .stTextInput > div > div > input:focus {
        border-color: var(--accent-blue) !important;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.1) !important;
    }
    .stCheckbox label span { color: var(--text-primary) !important; }

    /* ── Dataframes ── */
    [data-testid="stDataFrame"] {
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        overflow: hidden !important;
    }

    /* ── Alerts ── */
    [data-testid="stAlert"] { border-radius: var(--radius-sm) !important; }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab"] { color: var(--text-secondary) !important; font-weight: 500 !important; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: var(--accent-blue) !important; }

    /* ── Toast ── */
    [data-testid="stToast"] {
        background: var(--bg-secondary) !important;
        border: 1px solid var(--border-subtle) !important;
        color: var(--text-primary) !important;
        border-radius: var(--radius-md) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Segoe UI Emoji', 'Apple Color Emoji', 'Noto Color Emoji', sans-serif !important;
    }
    [data-testid="stToast"] [data-testid="stMarkdown"] p {
        font-family: inherit !important;
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
        border-bottom: 2px solid var(--accent-blue);
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
        background: var(--accent-blue);
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
        background: rgba(59, 130, 246, 0.1);
        color: var(--accent-blue);
        border: 1px solid rgba(59, 130, 246, 0.15);
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
        border-left: 3px solid var(--accent-teal) !important;
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
        padding: 1.25rem;
        text-align: center;
        transition: all 0.2s ease !important;
        height: auto !important;
        min-height: 140px;
    }
    .feature-card:hover {
        border-color: var(--border-medium) !important;
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-md) !important;
    }
    .feature-card .icon { font-size: 1.5rem; margin-bottom: 0.5rem; display: block; }
    .feature-card h4 {
        font-size: 0.88rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
        color: var(--text-heading);
    }
    .feature-card p {
        font-size: 0.8rem;
        color: var(--text-secondary);
        line-height: 1.4;
        margin: 0;
    }

    /* ── Processing / Loading indicator ── */
    .processing-overlay {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.6rem;
        padding: 0.75rem;
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-md);
        margin: 0.5rem 0;
        color: var(--accent-blue);
        font-weight: 500;
        font-size: 0.88rem;
    }
    .processing-spinner {
        width: 18px;
        height: 18px;
        border: 2px solid var(--border-medium);
        border-top-color: var(--accent-blue);
        border-radius: 50%;
        animation: spin 0.7s linear infinite;
    }
    @keyframes spin {
        to { transform: rotate(360deg); }
    }

    /* ── Success/Feedback banners ── */
    .feedback-banner {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.6rem 0.85rem;
        border-radius: var(--radius-sm);
        margin: 0.5rem 0;
        font-weight: 500;
        font-size: 0.85rem;
        animation: fadeSlideIn 0.3s ease;
    }
    .feedback-banner.success {
        background: rgba(34, 197, 94, 0.08);
        border: 1px solid rgba(34, 197, 94, 0.2);
        color: var(--accent-green);
    }
    .feedback-banner.info {
        background: rgba(59, 130, 246, 0.08);
        border: 1px solid rgba(59, 130, 246, 0.2);
        color: var(--accent-blue);
    }
    .feedback-banner.warning {
        background: rgba(229, 160, 25, 0.08);
        border: 1px solid rgba(229, 160, 25, 0.2);
        color: var(--accent-amber);
    }
    .feedback-banner.error {
        background: rgba(239, 68, 68, 0.08);
        border: 1px solid rgba(239, 68, 68, 0.2);
        color: var(--accent-red);
    }
    @keyframes fadeSlideIn {
        from { opacity: 0; transform: translateY(-6px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* ── Onboarding / Hero Section ── */
    .hero-title {
        font-size: 2.4rem !important;
        font-weight: 800 !important;
        color: var(--text-heading) !important;
        letter-spacing: -0.03em !important;
        margin-bottom: 0.6rem !important;
        background: linear-gradient(135deg, var(--text-heading) 40%, var(--accent-blue)) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        text-align: center !important;
        word-break: break-word !important;
        overflow-wrap: break-word !important;
    }
    .hero-subtitle {
        font-size: 1.05rem !important;
        color: var(--text-secondary) !important;
        max-width: 600px !important;
        margin: 0 auto 1.5rem auto !important;
        line-height: 1.5 !important;
        text-align: center !important;
        word-break: break-word !important;
        overflow-wrap: break-word !important;
        padding: 0 1rem !important;
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
            "colorway": ["#3B82F6", "#14B8A6", "#E5A019", "#22C55E", "#EF4444", "#A78BFA"],
        }
    return {
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "font_color": "#64748B",
        "colorway": ["#2563EB", "#0D9488", "#D97706", "#16A34A", "#DC2626", "#7C3AED"],
    }
