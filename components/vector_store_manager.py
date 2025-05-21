from langchain.schema import Document
from langchain_core.vectorstores import InMemoryVectorStore
import streamlit as st


@st.cache_resource
def create_vector_store(_embedding_model, faq_data):
    vector_store = InMemoryVectorStore(_embedding_model)
    documents = [
        Document(
            page_content=item["question"],
            metadata={"answer": item["answer"],
                      "original_question": item["question"]}
        ) for item in faq_data
    ]
    vector_store.add_documents(documents)
    return vector_store
