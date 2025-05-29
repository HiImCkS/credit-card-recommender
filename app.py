import streamlit as st
from agent import run_agent

st.set_page_config(page_title="AI Credit Card Recommender")
st.title("💳 Credit Card Recommendation")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask me anything about credit cards...", key="input")

if user_input:
    st.session_state.chat_history.append(("You", user_input))

    with st.spinner("AI is thinking..."):
        output = run_agent(user_input)
        st.session_state.chat_history.append(("AI", output))

 
for speaker, msg in st.session_state.chat_history:
    st.markdown(f"**{speaker}**: {msg}")
