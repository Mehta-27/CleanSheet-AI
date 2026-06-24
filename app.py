import streamlit as st

st.set_page_config(
    page_title="CleanSheet AI — Data Cleaning Tool",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="expanded",
)

from src.styles import inject_css
from src.analytics import inject_google_tag
from components.upload import render_upload
from components.overview import render_overview
from components.issue_panel import render_issues
from components.action_panel import render_clean
from components.export_page import render_export

PAGES = {
    "upload": ("📤 Upload", render_upload),
    "overview": ("📊 Overview", render_overview),
    "issues": ("🚩 Issues", render_issues),
    "clean": ("🧹 Clean", render_clean),
    "export": ("📥 Export", render_export),
}

PAGE_ORDER = ["upload", "overview", "issues", "clean", "export"]

STEP_ICONS = {
    "upload": "📤",
    "overview": "📊",
    "issues": "🚩",
    "clean": "🧹",
    "export": "📥",
}


def main() -> None:
    inject_google_tag()
    inject_css()

    # ── Init state ──
    if "page" not in st.session_state:
        st.session_state.page = "upload"
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True

    has_data = "df" in st.session_state
    current = st.session_state.page
    current_idx = PAGE_ORDER.index(current) if current in PAGE_ORDER else 0

    with st.sidebar:
        # ── Logo + Theme Toggle row ──
        logo_col, toggle_col = st.columns([3, 1])
        with logo_col:
            st.markdown(
                "<div style='padding: 0.3rem 0;'>"
                "<span style='font-size:1.15rem; font-weight:700; "
                "color:var(--text-heading); letter-spacing:-0.02em;'>🧹 CleanSheet AI</span>"
                "</div>",
                unsafe_allow_html=True,
            )
        with toggle_col:
            dark = st.session_state.dark_mode
            icon = "☀️" if dark else "🌙"
            if st.button(icon, key="theme_toggle", help="Toggle dark/light mode"):
                st.session_state.dark_mode = not dark
                st.rerun()

        # ── Progress stepper ──
        if has_data:
            steps_html = "<div style='display:flex; align-items:center; gap:4px; margin:0.6rem 0 0.3rem 0;'>"
            for i, key in enumerate(PAGE_ORDER):
                if i == current_idx:
                    dot = (
                        f"<div style='width:28px; height:6px; border-radius:999px; "
                        f"background:var(--accent-purple); flex-shrink:0;'></div>"
                    )
                elif i < current_idx:
                    dot = (
                        f"<div style='width:14px; height:6px; border-radius:999px; "
                        f"background:var(--accent-green); opacity:0.7; flex-shrink:0;'></div>"
                    )
                else:
                    dot = (
                        f"<div style='width:14px; height:6px; border-radius:999px; "
                        f"background:var(--border-medium); flex-shrink:0;'></div>"
                    )
                steps_html += dot
            steps_html += "</div>"
            st.markdown(steps_html, unsafe_allow_html=True)
            st.markdown(
                f"<p style='color:var(--text-tertiary); font-size:0.72rem; "
                f"font-weight:500; margin:0 0 0.5rem 0; text-transform:uppercase; "
                f"letter-spacing:0.06em;'>Step {current_idx + 1} of 5</p>",
                unsafe_allow_html=True,
            )

        # ── Navigation ──
        for i, key in enumerate(PAGE_ORDER):
            label, _ = PAGES[key]
            enabled = key == "upload" or has_data

            if not enabled:
                st.button(label, use_container_width=True, disabled=True, key=f"nav_{key}")
                continue

            is_active = current == key
            btn_label = f"**{i + 1}.** {label}" if has_data else label
            kind = "primary" if is_active else "secondary"

            if st.button(btn_label, use_container_width=True, type=kind, key=f"nav_{key}"):
                st.session_state.page = key
                st.rerun()

        st.markdown("---")

        # ── Pro CTA Card ──
        st.markdown(
            "<div class='pro-cta-card'>"
            "<div style='display:flex; align-items:center; gap:0.4rem; margin-bottom:0.5rem;'>"
            "<span class='pro-badge'>✦ PRO</span>"
            "<span style='font-size:0.9rem; font-weight:700; color:var(--text-heading);'>"
            "Upgrade to Pro</span>"
            "</div>"
            "<ul>"
            "<li>Excel (.xlsx) import & export</li>"
            "<li>AI-powered cleaning suggestions</li>"
            "<li>PDF quality reports</li>"
            "<li>500 MB file limit</li>"
            "<li>Outlier detection & filtering</li>"
            "</ul>"
            "<a href='https://7388507084353.gumroad.com/l/tqqra' class='pro-cta-btn' "
            "target='_blank'>Get Pro Now! →</a>"
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # ── Support Card ──
        st.markdown(
            "<div class='support-card'>"
            "<div style='font-size:0.9rem; font-weight:700; color:var(--text-heading); "
            "margin-bottom:0.4rem;'>💜 Support CleanSheet</div>"
            "<p style='font-size:0.78rem; color:var(--text-tertiary); margin:0 0 0.6rem 0; "
            "line-height:1.4;'>"
            "Love CleanSheet? Even a small contribution helps keep it free.</p>"
            "<div style='margin-top:0.6rem; padding:0.5rem; border-radius:var(--radius-sm); "
            "background:var(--bg-glass); border:1px solid var(--border-subtle);'>"
            "<p style='font-size:0.72rem; color:var(--text-tertiary); margin:0 0 0.15rem 0; "
            "font-weight:500;'>🇮🇳 UPI (India)</p>"
            "<code style='font-size:0.78rem; color:var(--accent-cyan);'>"
            "mehtarishit108@oksbi</code>"
            "</div>"
            "<p style='font-size:0.72rem; color:var(--text-tertiary); margin:0.5rem 0 0 0; "
            "font-style:italic;'>PayPal — coming soon</p>"
            "</div>",
            unsafe_allow_html=True,
        )

        # ── Version badge ──
        st.markdown(
            "<div style='text-align:center; margin-top:1rem;'>"
            "<span class='version-badge'>v1.0.0</span>"
            "</div>",
            unsafe_allow_html=True,
        )

    # ── Render current page ──
    current_page = st.session_state.page
    _, page_fn = PAGES.get(current_page, ("", render_upload))
    page_fn()

    # ── Auto-advance footer ──
    if has_data and current in PAGE_ORDER:
        next_idx = current_idx + 1
        if next_idx < len(PAGE_ORDER):
            next_key = PAGE_ORDER[next_idx]
            next_label, _ = PAGES[next_key]
            st.markdown("---")
            if st.button(f"Next: {next_label} →", use_container_width=True, type="primary"):
                st.session_state.page = next_key
                st.rerun()


if __name__ == "__main__":
    main()
