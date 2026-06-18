def classify_persona(message: str):

    text = message.lower()

    technical_keywords = [
        "api",
        "database",
        "error",
        "authentication",
        "token",
        "config",
        "server",
        "logs",
        "integration"
    ]

    frustrated_keywords = [
        "nothing works",
        "frustrated",
        "angry",
        "urgent",
        "immediately",
        "hate",
        "issue",
        "problem"
    ]

    executive_keywords = [
        "business",
        "operations",
        "impact",
        "timeline",
        "roi",
        "uptime"
    ]

    tech_score = sum(
        1 for word in technical_keywords
        if word in text
    )

    frust_score = sum(
        1 for word in frustrated_keywords
        if word in text
    )

    exec_score = sum(
        1 for word in executive_keywords
        if word in text
    )

    scores = {
        "Technical Expert": tech_score,
        "Frustrated User": frust_score,
        "Business Executive": exec_score
    }
    
    if max(scores.values()) == 0:
        return {
            "persona": "Frustrated User",
            "confidence": 0,
            "reasoning": "No persona indicators found"
        }
    persona = max(scores, key=scores.get)

    return {
        "persona": persona,
        "confidence": max(scores.values()),
        "reasoning": scores
    }