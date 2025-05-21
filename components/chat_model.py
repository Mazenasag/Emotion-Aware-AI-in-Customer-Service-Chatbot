import streamlit as st
from langchain.chat_models import ChatOllama


@st.cache_resource
def setup_chat_model():
    return ChatOllama(model="deepseek-r1:1.5b", temperature=0.3)
