import streamlit as st
from my_bc_st005.generator import refine_prompt



st.set_page_config(
    page_title="Prompt Refiner",
    layout="wide"
)

st.title("🧠 Prompt Refiner")
st.caption("Turn rough prompts into clear, effective instructions for AI models")

tone = st.selectbox(
    "Refinement style:",
    [
        "Neutral / Professional",
        "Concise",
        "Instructional",
        "Creative",
        "Formal"
    ]
)


user_prompt = st.text_area(
    "Paste your rough prompt below:",
    height=200,
    placeholder="e.g. write something about marketing"
)

if not user_prompt.strip():
    st.info("Paste a rough prompt above and choose a tone to refine it.")

refine_button = st.button(
    "Refine Prompt",
    disabled=not user_prompt.strip()
)

if refine_button:
    with st.spinner("Refining prompt..."):
        refined = refine_prompt(user_prompt, tone)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📝 Original Prompt")
        st.code(user_prompt)

    with col2:
        st.subheader("✨ Refined Prompt")
        st.code(refined)
    
    st.toast("Use the copy button in the code blocks ⬆️", icon="📋")






