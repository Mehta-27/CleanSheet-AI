"""Clean and minimal CSS — visual design handled separately."""

import streamlit as st

CSS = """
<style>
    .stApp {
        background: #F8FAFC;
    }

    /* Sidebar: keep it clean */
    section[data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid #E2E8F0;
    }

    /* Cards: subtle separation */
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlockBorder"] {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 1rem 1.25rem;
    }

    /* Metrics: card style */
    [data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 0.75rem 1rem;
    }

    /* File uploader: dashed zone */
    [data-testid="stFileUploader"] {
        border: 2px dashed #CBD5E1;
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: #0891B2;
        background: #F0FDFA;
    }

    /* Expanders: clean border */
    [data-testid="stExpander"] {
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        background: #FFFFFF;
        margin-bottom: 0.5rem;
    }

    /* Buttons: default styling, no overrides */
</style>
"""


def inject_css() -> None:
    st.markdown(CSS, unsafe_allow_html=True)
