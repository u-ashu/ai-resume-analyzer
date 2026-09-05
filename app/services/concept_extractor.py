import spacy

nlp = spacy.load("en_core_web_sm")


def extract_candidate_concepts(text: str) -> list[str]:

    doc = nlp(text)

    candidates = set()

    # --------------------------------
    # 1. Noun chunks
    # --------------------------------

    for chunk in doc.noun_chunks:

        phrase = chunk.text.strip().lower()

        if 1 <= len(phrase.split()) <= 5:
            candidates.add(phrase)

    # --------------------------------
    # 2. Technical multi-word phrases
    # --------------------------------

    technical_patterns = [
        "distributed systems",
        "distributed architecture",
        "event driven systems",
        "event-driven systems",
        "event driven architecture",
        "event-driven architecture",
        "microservices architecture",
        "message queues",
        "message brokers",
        "event streaming",
        "natural language processing",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "data engineering",
        "software architecture",
        "system architecture",
        "backend development",
        "frontend development",
        "cloud computing",
        "database management",
        "spring boot",
        "restful apis",
        "rest apis",
        "ci/cd",
        "ci cd",
        "continuous integration",
        "continuous deployment",
    ]

    text_lower = text.lower()

    for pattern in technical_patterns:

        if pattern in text_lower:
            candidates.add(pattern)

    # --------------------------------
    # 3. Technical single-word terms
    # --------------------------------

    technical_terms = [
        "python",
        "java",
        "javascript",
        "typescript",
        "sql",
        "fastapi",
        "django",
        "flask",
        "react",
        "reactjs",
        "angular",
        "vue",
        "docker",
        "kubernetes",
        "kafka",
        "rabbitmq",
        "mongodb",
        "postgresql",
        "mysql",
        "redis",
        "aws",
        "azure",
        "github",
        "graphql",
    ]

    for term in technical_terms:

        if term in text_lower:
            candidates.add(term)

    return sorted(candidates)