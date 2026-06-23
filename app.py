import streamlit as st

st.set_page_config(
    page_title="CleanSheet AI — Data Cleaning Tool",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="expanded",
)

from src.styles import inject_css
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


def main() -> None:
    inject_css()

    if "page" not in st.session_state:
        st.session_state.page = "upload"

    has_data = "df" in st.session_state
    current = st.session_state.page
    current_idx = PAGE_ORDER.index(current) if current in PAGE_ORDER else 0

    with st.sidebar:
        st.markdown("### 🧹 CleanSheet AI")

        # Progress indicator
        if has_data:
            st.markdown(
                f"<small style='color:#64748B'>Step {current_idx + 1} of 5</small>",
                unsafe_allow_html=True,
            )

        # Navigation as a numbered workflow
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
        st.markdown("##### ⭐ Upgrade to Pro")
        st.markdown(
            "• Excel (.xlsx) export\n"
            "• AI cleaning suggestions\n"
            "• PDF quality reports\n"
            "• 500 MB file limit\n"
        )
        st.markdown(
            "<a href='https://gumroad.com' "
            "style='display:block;background:#D97706;color:white;"
            "text-align:center;padding:0.4rem;border-radius:6px;"
            "font-weight:600;font-size:0.85rem;text-decoration:none'>"
            "Get Pro — $9.99</a>",
            unsafe_allow_html=True,
        )

        st.markdown("---")
        st.markdown("##### ☕ Support")
        st.markdown(
            "[Ko-fi](https://ko-fi.com/your-kofi) — works in India\n\n"
            "Or scan any UPI app:\n"
            "`yourname@upi`\n\n"
            "v1.0.0",
            unsafe_allow_html=True,
        )

    current_page = st.session_state.page
    _, page_fn = PAGES.get(current_page, ("", render_upload))
    page_fn()

    # Auto-advance footer
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
