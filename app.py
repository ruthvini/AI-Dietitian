import streamlit as st
from diet import get_diet_plan

# Streamlit UI
st.title("🥗 AI Dietitian - Personalized Diet Plan")
st.write("Enter your health condition, and AI will generate a customized diet plan for you!")

# User input
health_condition = st.text_area("Describe your health condition:", "Low hemoglobin and vitamin D deficiency")

if st.button("Get My Diet Plan"):
    with st.spinner("Generating your diet plan..."):
        diet_plan = get_diet_plan(health_condition)
        st.success("Here is your personalized diet plan:")
        st.write(diet_plan)

st.sidebar.write("💡 Powered by **Mistral** via **Ollama**")
