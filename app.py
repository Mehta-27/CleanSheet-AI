import streamlit as st

st.set_page_config(
    page_title="CleanSheet AI — Data Cleaning Tool",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="expanded",
)

from src.styles import inject_css, sidebar_header
from components.upload import render_upload
from components.overview import render_overview
from components.issue_panel import render_issues
from components.action_panel import render_clean
from components.export_page import render_export

PAGES = {
    "upload": render_upload,
    "overview": render_overview,
    "issues": render_issues,
    "clean": render_clean,
    "export": render_export,
}

NAV = [
    ("upload",     "📤  Upload",     True),
    ("overview",   "📊  Overview",   False),
    ("issues",     "🚩  Issues",     False),
    ("clean",      "🧹  Clean",      False),
    ("export",     "📥  Export",     False),
]


def main() -> None:
    inject_css()

    if "page" not in st.session_state:
        st.session_state.page = "upload"

    has_data = "df" in st.session_state
    current = st.session_state.page

    with st.sidebar:
        st.markdown(sidebar_header(), unsafe_allow_html=True)

        for key, label, _ in NAV:
            enabled = key == "upload" or has_data
            css = "primary" if current == key else "secondary"
            kind = "primary" if current == key else "secondary"
            if enabled:
                if st.button(label, use_container_width=True, type=kind, key=f"nav_{key}"):
                    st.session_state.page = key
                    st.rerun()
            else:
                st.button(label, use_container_width=True, disabled=True, key=f"nav_{key}")

        st.markdown("---")
        st.markdown(
            "<div style='padding:0.25rem 0'>"
            "<p style='color:#F59E0B;font-size:0.75rem;font-weight:600;text-transform:uppercase;"
            "letter-spacing:0.05em;margin:0 0 0.5rem 0'>Upgrade</p>"
            "<ul style='list-style:none;padding:0;margin:0;font-size:0.85rem;color:#94A3B8'>"
            "<li style='padding:2px 0'>✦ Excel export</li>"
            "<li style='padding:2px 0'>✦ AI suggestions</li>"
            "<li style='padding:2px 0'>✦ PDF reports</li>"
            "<li style='padding:2px 0'>✦ 500 MB files</li>"
            "</ul>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<a href='https://gumroad.com' "
            "style='display:block;background:linear-gradient(135deg,#D97706,#F59E0B);"
            "color:white;text-align:center;padding:0.5rem;border-radius:8px;"
            "font-weight:600;font-size:0.85rem;text-decoration:none;margin-top:0.5rem'>"
            "Get Pro — $9.99</a>",
            unsafe_allow_html=True,
        )

        st.markdown("---")
        st.markdown(
            "<div style='font-size:0.8rem;color:#64748B;text-align:center'>"
            "<a href='https://buymeacoffee.com' style='color:#67E8F9;text-decoration:none'>"
            "☕ Buy me a coffee</a><br>"
            "v1.0.0 · Made with ❤️"
            "</div>",
            unsafe_allow_html=True,
        )

    page_fn = PAGES.get(current, render_upload)
    page_fn()

    st.markdown(
        "<div class='app-footer'>"
        "CleanSheet AI · Free for everyone · "
        "<a href='https://gumroad.com'>Get Pro</a>"
        "</div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
