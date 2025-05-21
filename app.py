import streamlit as st
from components.data_loader import load_faq_data
from components.embedding_model import setup_embedding_model
from components.chat_model import setup_chat_model
from components.vector_store_manager import create_vector_store
from components.response_generator import generate_response

# Initialize components
faq_data = load_faq_data()
embedding_model = setup_embedding_model()
chat_model = setup_chat_model()
vector_store = create_vector_store(embedding_model, faq_data)

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# UI
st.title("🛍️ Customer Support Chat Assistant")

# Chat history
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(chat["user"])
    with st.chat_message("assistant"):
        st.write(chat["assistant"])

# Input handling
if user_query := st.chat_input("How can I help you today?"):
    response = generate_response(user_query, vector_store, faq_data)
    st.session_state.chat_history.append({
        "user": user_query,
        "assistant": response
    })
    st.rerun()
