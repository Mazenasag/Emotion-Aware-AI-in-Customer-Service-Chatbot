import difflib


def keyword_match(user_query, faq_data):
    best_match = None
    highest_ratio = 0
    for item in faq_data:
        ratio = difflib.SequenceMatcher(
            None, user_query, item["question"]).ratio()
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_match = item
    if highest_ratio > 0.3:
        return best_match["answer"], highest_ratio
    return None, 0.0
