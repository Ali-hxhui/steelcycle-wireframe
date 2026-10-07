from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SteelCycle wireframe", layout="wide")
st.markdown(
    """
    <style>
      #MainMenu, header, footer, [data-testid="stHeader"], [data-testid="stToolbar"] {display: none;}
      .block-container {padding: 0.5rem 0 0; max-width: 1180px;}
    </style>
    """,
    unsafe_allow_html=True,
)
html = Path(__file__).with_name("SteelCycle_Wireframe.html").read_text(encoding="utf-8")
components.html(html, height=980, scrolling=True)
