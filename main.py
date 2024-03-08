import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Gemini-Pro!",
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')


def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("Gemini Pro")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message["role"])):
        st.markdown(message["parts"][0]["text"])

# Input field for user's message
user_prompt = st.chat_input("Ask me anything!")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)
    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

# Sidebar for additional features and settings
sidebar = st.sidebar

# Reset Chat Button
if sidebar.button("Reset Chat"):
    st.session_state.chat_session = model.start_chat(history=[])
    st.experimental_rerun()

# User Feedback Form
sidebar.markdown("### Feedback")
feedback = sidebar.text_area("Share your experience with us")
if sidebar.button("Submit Feedback"):
    sidebar.success("Thank you for your feedback!")
