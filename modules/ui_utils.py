"""
UI Utilities for Cialfo Next-Gen CCR Platform
Provides safe HTML rendering without CommonMark indented code block artifacts.
"""
import re
import textwrap
import streamlit as st


def render_html(html: str) -> None:
    """
    Safely render HTML in Streamlit.
    1. Strips HTML comments (<!-- ... -->) that cause CommonMark parsing anomalies.
    2. Dedents common indentation so root HTML elements start at column 0.
    3. Eliminates internal blank lines so CommonMark doesn't treat indented HTML as code blocks.
    """
    if not html:
        return
    # Strip HTML comments
    cleaned = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    # Dedent leading indentation
    cleaned = textwrap.dedent(cleaned).strip()
    # Remove blank lines inside HTML blocks
    cleaned = re.sub(r'\n\s*\n', '\n', cleaned)
    st.markdown(cleaned, unsafe_allow_html=True)
