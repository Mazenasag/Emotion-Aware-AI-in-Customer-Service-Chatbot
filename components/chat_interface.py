import streamlit as st
from components.data_loader import DataLoader
from components.embedding_model import EmbeddingModel
from components.chat_model import ChatModel
from components.vector_store_manager import VectorStoreManager
from components.response_generator import ResponseGenerator


class ChatInterface:
    def __init__(self):
        self.faq_data = DataLoader.load_faq_data()
        self.embedding_model = EmbeddingModel.setup_embedding_model()
        self.chat_model = ChatModel.setup_chat_model()
        self.vector_store_manager = VectorStoreManager(
            self.embedding_model, self.faq_data)
        self.response_generator = ResponseGenerator(self.chat_model)
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

    def display_chat(self):
        st.title("🛍️ Customer Support Chat Assistant")
        for chat in st.session_state.chat_history:
            with st.chat_message("user"):
                st.write(chat["user"])
            with st.chat_message("assistant"):
                st.write(chat["assistant"])

        if user_query := st.chat_input("How can I help you today?"):
            response = self.response_generator.generate_response(
                user_query, self.vector_store_manager, self.faq_data)
            st.session_state.chat_history.append(
                {"user": user_query, "assistant": response})
            st.rerun()
