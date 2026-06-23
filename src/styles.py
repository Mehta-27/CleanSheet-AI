"""CleanSheet AI — Premium Design System & Theme Engine.

Provides:
- CSS custom properties (design tokens) for dark/light themes
- Google Fonts (Inter) import
- Glassmorphism card system
- Gradient accents and micro-animations
- Theme-aware component overrides for Streamlit
"""

import streamlit as st

# ── Google Fonts ──────────────────────────────────────────────────────────
FONTS = "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');"

# ── Design Tokens ─────────────────────────────────────────────────────────
DARK_TOKENS = """
    --bg-primary: #0B0F19;
    --bg-secondary: #111827;
    --bg-tertiary: #1A1F2E;
    --bg-glass: rgba(255, 255, 255, 0.03);
    --bg-glass-hover: rgba(255, 255, 255, 0.06);
    --bg-sidebar: #0E1225;
    --border-subtle: rgba(255, 255, 255, 0.06);
    --border-medium: rgba(255, 255, 255, 0.10);
    --border-accent: rgba(6, 182, 212, 0.3);
    --text-primary: #F1F5F9;
    --text-secondary: #94A3B8;
    --text-tertiary: #64748B;
    --text-heading: #F8FAFC;
    --accent-cyan: #06B6D4;
    --accent-violet: #8B5CF6;
    --accent-amber: #F59E0B;
    --accent-emerald: #10B981;
    --accent-rose: #F43F5E;
    --accent-blue: #3B82F6;
    --gradient-primary: linear-gradient(135deg, #06B6D4, #8B5CF6);
    --gradient-warm: linear-gradient(135deg, #F59E0B, #EF4444);
    --gradient-pro: linear-gradient(135deg, #F59E0B 0%, #F97316 50%, #EF4444 100%);
    --gradient-support: linear-gradient(135deg, #EC4899, #8B5CF6);
    --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
    --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.4);
    --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.5);
    --shadow-glow-cyan: 0 0 20px rgba(6, 182, 212, 0.15);
    --shadow-glow-violet: 0 0 20px rgba(139, 92, 246, 0.15);
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 20px;
    --chart-bg: rgba(0,0,0,0);
    --chart-grid: rgba(255,255,255,0.06);
    --chart-text: #94A3B8;
"""

LIGHT_TOKENS = """
    --bg-primary: #F1F5F9;
    --bg-secondary: #FFFFFF;
    --bg-tertiary: #F8FAFC;
    --bg-glass: rgba(255, 255, 255, 0.70);
    --bg-glass-hover: rgba(255, 255, 255, 0.85);
    --bg-sidebar: #FFFFFF;
    --border-subtle: rgba(0, 0, 0, 0.06);
    --border-medium: rgba(0, 0, 0, 0.10);
    --border-accent: rgba(6, 182, 212, 0.25);
    --text-primary: #0F172A;
    --text-secondary: #475569;
    --text-tertiary: #94A3B8;
    --text-heading: #020617;
    --accent-cyan: #0891B2;
    --accent-violet: #7C3AED;
    --accent-amber: #D97706;
    --accent-emerald: #059669;
    --accent-rose: #E11D48;
    --accent-blue: #2563EB;
    --gradient-primary: linear-gradient(135deg, #0891B2, #7C3AED);
    --gradient-warm: linear-gradient(135deg, #D97706, #DC2626);
    --gradient-pro: linear-gradient(135deg, #D97706 0%, #EA580C 50%, #DC2626 100%);
    --gradient-support: linear-gradient(135deg, #DB2777, #7C3AED);
    --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.06);
    --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.08);
    --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.12);
    --shadow-glow-cyan: 0 0 20px rgba(6, 182, 212, 0.10);
    --shadow-glow-violet: 0 0 20px rgba(139, 92, 246, 0.10);
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 20px;
    --chart-bg: rgba(0,0,0,0);
    --chart-grid: rgba(0,0,0,0.06);
    --chart-text: #475569;
"""

# ── Animations ────────────────────────────────────────────────────────────
ANIMATIONS = """
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(16px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes shimmer {
        0%   { background-position: -200% center; }
        100% { background-position: 200% center; }
    }
    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 0 8px rgba(6, 182, 212, 0.2); }
        50%      { box-shadow: 0 0 24px rgba(6, 182, 212, 0.45); }
    }
    @keyframes gradientShift {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes borderGlow {
        0%, 100% { border-color: rgba(6, 182, 212, 0.3); }
        50%      { border-color: rgba(139, 92, 246, 0.5); }
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50%      { transform: translateY(-4px); }
    }
"""

# ── Component Styles ──────────────────────────────────────────────────────
COMPONENT_CSS = """
    /* ── Global Reset & Typography ── */
    *, *::before, *::after {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }

    .stApp {
        background: var(--bg-primary) !important;
        color: var(--text-primary) !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: var(--text-heading) !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
    }

    p, span, label, div {
        color: var(--text-primary);
    }

    a {
        color: var(--accent-cyan) !important;
        text-decoration: none !important;
        transition: color 0.2s ease;
    }
    a:hover {
        color: var(--accent-violet) !important;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: var(--bg-sidebar) !important;
        border-right: 1px solid var(--border-subtle) !important;
    }
    section[data-testid="stSidebar"] [data-testid="stMarkdown"] p,
    section[data-testid="stSidebar"] [data-testid="stMarkdown"] span,
    section[data-testid="stSidebar"] [data-testid="stMarkdown"] li {
        color: var(--text-secondary) !important;
        font-size: 0.88rem !important;
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
        margin: 1rem 0 !important;
    }

    /* ── Cards / Containers ── */
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlockBorder"] {
        background: var(--bg-glass) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        padding: 1.25rem 1.5rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        animation: fadeInUp 0.4s ease-out !important;
    }
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlockBorder"]:hover {
        background: var(--bg-glass-hover) !important;
        border-color: var(--border-medium) !important;
        box-shadow: var(--shadow-sm) !important;
        transform: translateY(-1px) !important;
    }

    /* ── Metrics ── */
    [data-testid="stMetric"] {
        background: var(--bg-glass) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        padding: 1rem 1.25rem !important;
        transition: all 0.3s ease !important;
    }
    [data-testid="stMetric"]:hover {
        border-color: var(--border-accent) !important;
        box-shadow: var(--shadow-glow-cyan) !important;
        transform: translateY(-2px) !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricLabel"] {
        color: var(--text-secondary) !important;
        font-weight: 500 !important;
        font-size: 0.8rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: var(--text-heading) !important;
        font-weight: 700 !important;
        font-size: 1.6rem !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricDelta"] {
        font-weight: 600 !important;
    }

    /* ── File Uploader ── */
    [data-testid="stFileUploader"] {
        border: 2px dashed var(--border-medium) !important;
        border-radius: var(--radius-lg) !important;
        padding: 2rem !important;
        text-align: center !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        background: var(--bg-glass) !important;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: var(--accent-cyan) !important;
        background: var(--bg-glass-hover) !important;
        animation: pulseGlow 2s ease-in-out infinite !important;
    }
    [data-testid="stFileUploader"] small {
        color: var(--text-tertiary) !important;
    }

    /* ── Expanders ── */
    [data-testid="stExpander"] {
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        background: var(--bg-glass) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        margin-bottom: 0.75rem !important;
        transition: all 0.3s ease !important;
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
        background: var(--gradient-primary) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        letter-spacing: 0.01em !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 2px 8px rgba(6, 182, 212, 0.2) !important;
    }
    .stButton > button[kind="primary"]:hover,
    .stButton > button[data-testid="stBaseButton-primary"]:hover {
        box-shadow: 0 4px 20px rgba(6, 182, 212, 0.35) !important;
        transform: translateY(-1px) !important;
    }

    .stButton > button[kind="secondary"],
    .stButton > button[data-testid="stBaseButton-secondary"] {
        background: var(--bg-glass) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-medium) !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button[kind="secondary"]:hover,
    .stButton > button[data-testid="stBaseButton-secondary"]:hover {
        background: var(--bg-glass-hover) !important;
        border-color: var(--accent-cyan) !important;
    }

    /* ── Download Buttons ── */
    .stDownloadButton > button {
        background: var(--gradient-primary) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 2px 8px rgba(6, 182, 212, 0.2) !important;
    }
    .stDownloadButton > button:hover {
        box-shadow: 0 4px 20px rgba(6, 182, 212, 0.35) !important;
        transform: translateY(-1px) !important;
    }

    /* ── Select boxes, Multiselects, Inputs ── */
    [data-testid="stSelectbox"],
    [data-testid="stMultiSelect"],
    [data-testid="stTextInput"] {
        color: var(--text-primary) !important;
    }
    .stSelectbox > div > div,
    .stMultiSelect > div > div,
    .stTextInput > div > div > input {
        background: var(--bg-glass) !important;
        border-color: var(--border-medium) !important;
        color: var(--text-primary) !important;
        border-radius: var(--radius-sm) !important;
    }
    .stSelectbox > div > div:focus-within,
    .stMultiSelect > div > div:focus-within,
    .stTextInput > div > div > input:focus {
        border-color: var(--accent-cyan) !important;
        box-shadow: 0 0 0 2px rgba(6, 182, 212, 0.15) !important;
    }

    /* ── Checkbox ── */
    .stCheckbox label span {
        color: var(--text-primary) !important;
    }

    /* ── Dataframes ── */
    [data-testid="stDataFrame"] {
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        overflow: hidden !important;
    }

    /* ── Alerts (success, info, warning, error) ── */
    [data-testid="stAlert"] {
        border-radius: var(--radius-sm) !important;
        border: none !important;
    }

    /* ── Horizontal rule ── */
    hr {
        border-color: var(--border-subtle) !important;
        margin: 1.5rem 0 !important;
    }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab"] {
        color: var(--text-secondary) !important;
        font-weight: 500 !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: var(--accent-cyan) !important;
    }

    /* ── Progress bar ── */
    .stProgress > div > div > div {
        background: var(--gradient-primary) !important;
        border-radius: 999px !important;
    }

    /* ── Toast ── */
    [data-testid="stToast"] {
        background: var(--bg-secondary) !important;
        border: 1px solid var(--border-subtle) !important;
        color: var(--text-primary) !important;
        border-radius: var(--radius-md) !important;
    }

    /* ── Custom utility classes ── */
    .gradient-text {
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        background-size: 200% 200%;
        animation: gradientShift 4s ease infinite;
    }

    .glass-card {
        background: var(--bg-glass);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-md);
        padding: 1.25rem;
        transition: all 0.3s ease;
    }
    .glass-card:hover {
        background: var(--bg-glass-hover);
        border-color: var(--border-medium);
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }

    .feature-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.35rem 0.85rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 500;
        border: 1px solid var(--border-subtle);
        background: var(--bg-glass);
        color: var(--text-secondary);
        margin: 0.2rem;
        transition: all 0.2s ease;
    }
    .feature-pill:hover {
        border-color: var(--accent-cyan);
        color: var(--accent-cyan);
    }

    .pro-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        padding: 0.2rem 0.6rem;
        border-radius: 999px;
        font-size: 0.7rem;
        font-weight: 700;
        background: var(--gradient-pro);
        color: white;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }

    .step-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 24px;
        height: 24px;
        border-radius: 50%;
        background: var(--gradient-primary);
        color: white;
        font-size: 0.72rem;
        font-weight: 700;
        margin-right: 0.5rem;
        flex-shrink: 0;
    }

    .cleaning-entry {
        display: flex;
        align-items: center;
        padding: 0.6rem 0.8rem;
        margin-bottom: 0.4rem;
        border-radius: var(--radius-sm);
        background: var(--bg-glass);
        border: 1px solid var(--border-subtle);
        font-size: 0.88rem;
        color: var(--text-primary);
        transition: all 0.2s ease;
    }
    .cleaning-entry:hover {
        background: var(--bg-glass-hover);
    }
    .cleaning-entry .step {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 22px;
        height: 22px;
        border-radius: 50%;
        background: var(--gradient-primary);
        color: white;
        font-size: 0.68rem;
        font-weight: 700;
        margin-right: 0.65rem;
    }

    .severity-critical {
        display: inline-block;
        padding: 0.15rem 0.55rem;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 600;
        background: rgba(244, 63, 94, 0.12);
        color: var(--accent-rose);
        border: 1px solid rgba(244, 63, 94, 0.2);
    }
    .severity-warning {
        display: inline-block;
        padding: 0.15rem 0.55rem;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 600;
        background: rgba(245, 158, 11, 0.12);
        color: var(--accent-amber);
        border: 1px solid rgba(245, 158, 11, 0.2);
    }
    .severity-info {
        display: inline-block;
        padding: 0.15rem 0.55rem;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 600;
        background: rgba(59, 130, 246, 0.12);
        color: var(--accent-blue);
        border: 1px solid rgba(59, 130, 246, 0.2);
    }

    /* ── Pro CTA Sidebar Card ── */
    .pro-cta-card {
        background: var(--bg-glass);
        border: 1px solid rgba(245, 158, 11, 0.15);
        border-radius: var(--radius-md);
        padding: 1rem;
        margin: 0.5rem 0;
        position: relative;
        overflow: hidden;
    }
    .pro-cta-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: var(--gradient-pro);
    }
    .pro-cta-card ul {
        list-style: none;
        padding: 0;
        margin: 0.5rem 0;
    }
    .pro-cta-card li {
        padding: 0.2rem 0;
        font-size: 0.82rem;
        color: var(--text-secondary);
    }
    .pro-cta-card li::before {
        content: '✦ ';
        color: var(--accent-amber);
    }

    .pro-cta-btn {
        display: block;
        background: var(--gradient-pro);
        color: white !important;
        text-align: center;
        padding: 0.55rem 1rem;
        border-radius: var(--radius-sm);
        font-weight: 700;
        font-size: 0.85rem;
        text-decoration: none !important;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .pro-cta-btn::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s ease;
    }
    .pro-cta-btn:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 20px rgba(245, 158, 11, 0.3);
    }
    .pro-cta-btn:hover::after {
        left: 100%;
    }

    /* ── Support Card ── */
    .support-card {
        background: var(--bg-glass);
        border: 1px solid rgba(236, 72, 153, 0.12);
        border-radius: var(--radius-md);
        padding: 1rem;
        margin: 0.5rem 0;
        position: relative;
        overflow: hidden;
    }
    .support-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: var(--gradient-support);
    }
    .support-link {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        padding: 0.3rem 0.7rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 600;
        background: var(--bg-glass);
        border: 1px solid var(--border-subtle);
        color: var(--text-secondary) !important;
        text-decoration: none !important;
        transition: all 0.2s ease;
        margin: 0.15rem;
    }
    .support-link:hover {
        border-color: var(--accent-violet);
        color: var(--accent-violet) !important;
        transform: translateY(-1px);
    }

    /* ── Version Badge ── */
    .version-badge {
        display: inline-block;
        padding: 0.15rem 0.5rem;
        border-radius: 999px;
        font-size: 0.68rem;
        font-weight: 500;
        background: var(--bg-glass);
        border: 1px solid var(--border-subtle);
        color: var(--text-tertiary);
    }

    /* ── Theme Toggle ── */
    .theme-toggle-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        padding: 0.4rem;
        border-radius: var(--radius-sm);
        background: var(--bg-glass);
        border: 1px solid var(--border-subtle);
        color: var(--text-secondary);
        font-size: 0.82rem;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .theme-toggle-btn:hover {
        background: var(--bg-glass-hover);
        border-color: var(--accent-cyan);
    }

    /* ── Hero Section ── */
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1.15;
        margin-bottom: 0.5rem;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        background-size: 200% 200%;
        animation: gradientShift 4s ease infinite;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: var(--text-secondary);
        font-weight: 400;
        line-height: 1.5;
        max-width: 600px;
    }

    /* ── Feature showcase cards ── */
    .feature-card {
        background: var(--bg-glass);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-md);
        padding: 1.25rem;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
    }
    .feature-card:hover {
        border-color: var(--border-accent);
        box-shadow: var(--shadow-glow-cyan);
        transform: translateY(-3px);
    }
    .feature-card .icon {
        font-size: 1.8rem;
        margin-bottom: 0.6rem;
        display: block;
    }
    .feature-card h4 {
        font-size: 0.92rem;
        font-weight: 700;
        margin-bottom: 0.35rem;
        color: var(--text-heading);
    }
    .feature-card p {
        font-size: 0.82rem;
        color: var(--text-secondary);
        line-height: 1.45;
        margin: 0;
    }

    /* ── Section headers with gradient underline ── */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-heading);
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid transparent;
        border-image: var(--gradient-primary) 1;
    }

    /* ── Main content animation ── */
    .main .block-container {
        animation: fadeInUp 0.5s ease-out;
    }

    /* ── Scrollbar (dark mode polish) ── */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    ::-webkit-scrollbar-track {
        background: var(--bg-primary);
    }
    ::-webkit-scrollbar-thumb {
        background: var(--border-medium);
        border-radius: 999px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: var(--text-tertiary);
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
            "font_color": "#94A3B8",
            "colorway": ["#06B6D4", "#8B5CF6", "#F59E0B", "#10B981", "#F43F5E", "#3B82F6"],
        }
    return {
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "font_color": "#475569",
        "colorway": ["#0891B2", "#7C3AED", "#D97706", "#059669", "#E11D48", "#2563EB"],
    }
