import streamlit as st
from my_bc_st005.generator import refine_prompt



st.set_page_config(
    page_title="Prompt Refiner",
    layout="wide"
)

st.title("🧠 Prompt Refiner")
st.caption("Turn rough prompts into clear, effective instructions for AI models")

user_prompt = st.text_area(
    "Paste your rough prompt below:",
    height=200,
    placeholder="e.g. write something about marketing"
)

refine_button = st.button(
    "Refine Prompt",
    disabled=not user_prompt.strip()
)

if refine_button:
    with st.spinner("Refining prompt..."):
        refined = refine_prompt(user_prompt)

    st.subheader("✨ Refined Prompt")
    st.code(refined)


