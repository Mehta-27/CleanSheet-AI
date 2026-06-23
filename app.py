"""CleanSheet AI — Your Data, Perfectly Clean.

Free: cleansheet-ai.streamlit.app
Pro: gumroad.com (downloadable EXE with AI, Excel, PDF, batch)
"""

import streamlit as st

st.set_page_config(
    page_title="CleanSheet AI",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="collapsed",
)

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


def main() -> None:
    if "page" not in st.session_state:
        st.session_state.page = "upload"

    current_page = st.session_state.page
    page_fn = PAGES.get(current_page, render_upload)

    sidebar()

    page_fn()


def sidebar() -> None:
    with st.sidebar:
        st.markdown("### 🧹 CleanSheet AI")
        st.markdown("Your Data, Perfectly Clean.")

        has_data = "df" in st.session_state

        nav_items = [
            ("upload", "📤 Upload", True),
            ("overview", "📊 Overview", has_data),
            ("issues", "🚩 Issues", has_data),
            ("clean", "🧹 Clean", has_data),
            ("export", "📥 Export", has_data),
        ]

        for key, label, enabled in nav_items:
            if enabled:
                if st.button(
                    label,
                    use_container_width=True,
                    type="secondary" if st.session_state.page != key else "primary",
                    key=f"nav_{key}",
                ):
                    st.session_state.page = key
                    st.rerun()
            else:
                st.button(label, use_container_width=True, disabled=True, key=f"nav_{key}")

        st.markdown("---")
        st.markdown(
            "#### ⭐ Upgrade to Pro\n"
            "- Excel .xlsx support\n"
            "- AI cleaning suggestions\n"
            "- PDF quality reports\n"
            "- Batch processing\n"
            "- 500 MB file limit\n"
            "\n[Get Pro on Gumroad](https://gumroad.com)"
        )

        st.markdown("---")
        st.markdown(
            "[☕ Buy me a coffee](https://buymeacoffee.com)  \n"
            "v1.0.0 · Made with ❤️"
        )


if __name__ == "__main__":
    main()
