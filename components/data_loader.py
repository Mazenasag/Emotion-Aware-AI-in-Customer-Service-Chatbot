import streamlit as st
import json


@st.cache_data
def load_faq_data():
    with open("data.json", "r") as f:
        return json.load(f)
