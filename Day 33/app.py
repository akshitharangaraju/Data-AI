import streamlit as st
import os
import sys

# Ensure the root folder is in the path to import local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chatbot.chatbot import generate_response

st.set_page_config(
    page_title="Healthcare Chatbot",
    page_icon="⚕️",
    layout="centered"
)

st.title("⚕️ Healthcare Knowledge Chatbot")
st.markdown("Ask healthcare-related questions based on the provided clinical guidelines.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask a healthcare question..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display bot response
    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base..."):
            try:
                response = generate_response(prompt)
                st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"An error occurred: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
