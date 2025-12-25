import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from config import model, temperature,max_tokens
# Load environment variables
load_dotenv()


# Initialize ChatGroq LLM
llm = ChatGroq(
    groq_api_key=st.secrets["GROQ_API_KEY"],
    model=model,  # you can swap to mixtral if needed
    temperature=temperature,
    max_tokens=max_tokens
)

# Streamlit UI
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Groq-Powered Chatbot")

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are an AI assistant. Give answers precisely."}
    ]

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Append user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get response from Groq
    response = llm.invoke(st.session_state.chat_history)

    # Append assistant response
    st.session_state.chat_history.append({"role": "assistant", "content": response.content})

# Display chat history
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])
