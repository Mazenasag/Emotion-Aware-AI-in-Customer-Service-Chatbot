import streamlit as st
import string
from components.keyword_matcher import keyword_match
from components.chat_model import setup_chat_model

chat_model = setup_chat_model()


def preprocess_text(text):
    return text.lower().translate(str.maketrans("", "", string.punctuation)).strip()


def get_best_match(user_query, vector_store):
    results = vector_store.similarity_search_with_score(
        query=user_query,
        k=1
    )
    if not results:
        return None, 0.0
    (doc, score) = results[0]
    return doc.metadata["answer"], score, results


def refine_answer_with_llm(answer):
    prompt = f"write the same following answer in an empathetic and friendly manner with emojes: {answer}"
    return chat_model.invoke(prompt).content


def generate_response(user_query, vector_store, faq_data):
    answer, score, _ = get_best_match(user_query, vector_store)
    if score >= 0.7:
        return refine_answer_with_llm(answer)
    elif 0.2 <= score < 0.7:
        keyword_answer, keyword_score = keyword_match(user_query, faq_data)
        if keyword_score >= 0.3:
            return f"I think you are asking about (keyword match):\n\n{refine_answer_with_llm(keyword_answer)}"
        else:
            return "I'm not sure I understand. Could you please rephrase your question?"
    else:
        return "I'm sorry, I couldn't find an exact match. Let me help you with more details!"
