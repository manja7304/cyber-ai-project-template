"""Minimal Streamlit placeholder — replace with project-specific demo UI."""

import streamlit as st

st.set_page_config(page_title="Cyber AI Template", page_icon="🛡️", layout="wide")

st.title("Cyber AI Project Template")
st.caption("Portfolio scaffold — implement agents and wire UI here.")

st.info(
    "This is a placeholder. Copy this template for a portfolio project, "
    "then add chat history, agent traces, and domain-specific visualizations."
)

with st.sidebar:
    st.header("Configuration")
    st.text("LLM_PROVIDER=ollama")
    st.text("OLLAMA_MODEL=llama3.2")

st.subheader("Next steps")
st.markdown(
    """
1. Implement agents in `src/agents/`
2. Add tools in `src/tools/`
3. Expose API routes in `src/api/main.py`
4. Seed demo data via `scripts/seed_demo_data.py`
"""
)
