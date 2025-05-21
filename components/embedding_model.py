import streamlit as st
from langchain_ollama import OllamaEmbeddings


@st.cache_resource
def setup_embedding_model():
    return OllamaEmbeddings(model="deepseek-r1:1.5b")
