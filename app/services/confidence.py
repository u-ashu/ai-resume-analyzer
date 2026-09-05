def classify_confidence(score: float) -> str:

    if score >= 0.80:
        return "very_high"

    if score >= 0.70:
        return "high"

    if score >= 0.60:
        return "moderate"

    return "low"