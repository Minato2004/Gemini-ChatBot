import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai


load_dotenv()

#page config
st.set_page_config(
    page_title="Chat with Sheldon",
    page_icon=":brain",
    layout="centered"
)

apiKey=os.getenv("GOOGLE_API_KEY")


gen_ai.configure(api_key=apiKey)
model=gen_ai.GenerativeModel('gemini-1.5-pro')


def translate(user):
    if user=='model':
        return 'assistant'
    else:
        return user

if "chat_session" not in st.session_state:
    st.session_state.chat_session=model.start_chat(history=[])

st.title("🤖 Sheldon ChatBot")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask Gemini...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    gemini_response = st.session_state.chat_session.send_message(user_prompt)
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)