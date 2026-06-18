import json


SENSITIVE_TOPICS = [
    "billing",
    "refund",
    "legal",
    "account"
]


def should_escalate(
    user_query,
    retrieved_docs
):

    text = user_query.lower()

    for topic in SENSITIVE_TOPICS:

        if topic in text:
            return True

    if len(retrieved_docs) == 0:
        return True

    best_score = retrieved_docs[0]["score"]

    if best_score < 1:
        return True

    return False


def generate_handoff_summary(
    persona,
    user_query,
    retrieved_docs
):

    return {
        "persona": persona,
        "issue": user_query,
        "documents_used": [
            doc["source"]
            for doc in retrieved_docs
        ],
        "recommendation":
        "Human review required"
    }