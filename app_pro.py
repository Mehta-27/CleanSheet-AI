import os
import sys

# Force Streamlit production mode and configuration at the absolute top
os.environ["STREAMLIT_GLOBAL_DEVELOPMENT_MODE"] = "false"
os.environ["STREAMLIT_DEVELOPMENT_MODE"] = "false"
os.environ["STREAMLIT_SERVER_HEADLESS"] = "false"
os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"

# Force PyInstaller to bundle scriptrunner magic functions
import streamlit.runtime.scriptrunner.magic_funcs
import streamlit as st

from src.styles import inject_css
from src.analytics import inject_google_tag
from components.upload import render_upload
from components.overview import render_overview as free_render_overview
from components.issue_panel import render_issues as free_render_issues
from components.action_panel import render_clean
from components.export_page import render_export as free_render_export
from components_pro.ai_assistant import render_ai_assistant
from components_pro.quality_score import render_quality_dashboard
from components_pro.pdf_reporter import render_pdf_report

PAGES = {
    "upload": ("📤 Upload", render_upload),
    "overview": ("📊 Overview", lambda: _pro_overview()),
    "issues": ("🚩 Issues", lambda: _pro_issues()),
    "clean": ("🧹 Clean", render_clean),
    "export": ("📥 Export", lambda: _pro_export()),
}

PAGE_ORDER = ["upload", "overview", "issues", "clean", "export"]

STEP_ICONS = {
    "upload": "📤", "overview": "📊", "issues": "🚩", "clean": "🧹", "export": "📥",
}


def _pro_overview() -> None:
    free_render_overview()
    if "df" in st.session_state:
        st.markdown("---")
        render_quality_dashboard(st.session_state.df)


def _pro_issues() -> None:
    free_render_issues()
    if "df" in st.session_state:
        st.markdown("---")
        render_ai_assistant(st.session_state.df)


def _pro_export() -> None:
    free_render_export()
    if "df" in st.session_state:
        st.markdown("---")
        render_pdf_report(st.session_state.df)


def main() -> None:
    st.set_page_config(
        page_title="CleanSheet AI Pro — Data Cleaning Tool",
        page_icon="🧹",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_google_tag()
    inject_css()

    if "page" not in st.session_state:
        st.session_state.page = "upload"
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True
    if "_pro" not in st.session_state:
        st.session_state._pro = True

    has_data = "df" in st.session_state
    current = st.session_state.page
    current_idx = PAGE_ORDER.index(current) if current in PAGE_ORDER else 0

    with st.sidebar:
        logo_col, toggle_col = st.columns([3, 1])
        with logo_col:
            st.markdown(
                "<div style='padding: 0.3rem 0;'>"
                "<span style='font-size:1.15rem; font-weight:700; "
                "color:var(--text-heading); letter-spacing:-0.02em;'>🧹 CleanSheet Pro</span>"
                "</div>",
                unsafe_allow_html=True,
            )
        with toggle_col:
            dark = st.session_state.dark_mode
            icon = "☀️" if dark else "🌙"
            if st.button(icon, key="theme_toggle", help="Toggle dark/light mode"):
                st.session_state.dark_mode = not dark
                st.rerun()

        if has_data:
            steps_html = "<div style='display:flex; align-items:center; gap:4px; margin:0.6rem 0 0.3rem 0;'>"
            for i, key in enumerate(PAGE_ORDER):
                if i == current_idx:
                    dot = f"<div style='width:28px;height:6px;border-radius:999px;background:var(--accent-purple);flex-shrink:0;'></div>"
                elif i < current_idx:
                    dot = f"<div style='width:14px;height:6px;border-radius:999px;background:var(--accent-green);opacity:0.7;flex-shrink:0;'></div>"
                else:
                    dot = f"<div style='width:14px;height:6px;border-radius:999px;background:var(--border-medium);flex-shrink:0;'></div>"
                steps_html += dot
            steps_html += "</div>"
            st.markdown(steps_html, unsafe_allow_html=True)
            st.markdown(
                f"<p style='color:var(--text-tertiary);font-size:0.72rem;font-weight:500;"
                f"margin:0 0 0.5rem 0;text-transform:uppercase;letter-spacing:0.06em;'>"
                f"Step {current_idx + 1} of 5</p>",
                unsafe_allow_html=True,
            )

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
        st.markdown(
            "<div style='text-align:center;padding:0.5rem;font-size:0.78rem;color:var(--accent-emerald);font-weight:600;'>"
            "✦ PRO Version — All Features Unlocked</div>",
            unsafe_allow_html=True,
        )

        st.markdown("---")
        st.markdown(
            "<div style='text-align:center;'>"
            "<span class='version-badge'>v1.0.0 Pro</span>"
            "</div>",
            unsafe_allow_html=True,
        )

    current_page = st.session_state.page
    _, page_fn = PAGES.get(current_page, ("", render_upload))
    page_fn()

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
    import streamlit as st
    if st.runtime.exists():
        main()
    else:
        import sys
        from streamlit.web import cli as stcli

        if getattr(sys, "frozen", False):
            meipass = sys._MEIPASS
            script_path = os.path.join(meipass, "app_pro.py")
        else:
            script_path = __file__

        sys.argv = [
            "streamlit", "run", script_path,
            "--server.port", "8501",
            "--server.headless", "false",
            "--global.developmentMode", "false",
            "--browser.gatherUsageStats", "false",
        ]
        sys.exit(stcli.main())
