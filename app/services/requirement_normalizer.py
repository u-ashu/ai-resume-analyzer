def normalize_requirements(concepts: list[str]) -> list[str]:

    normalized = set()

    removable_prefixes = [
        "strong proficiency in ",
        "good knowledge of ",
        "experience with ",
        "experience in ",
        "knowledge of ",
        "understanding of ",
        "familiarity with ",
        "proficiency in ",
    ]

    removable_suffixes = [
        " experience",
        " good knowledge",
        " knowledge",
        " understanding",
        " familiarity",
        " is preferred",
        " preferred",
    ]

    role_phrases = [
        " developer",
        " engineer",
        " specialist",
        " professional",
    ]

    for concept in concepts:

        cleaned = concept.strip().lower()

        if not cleaned:
            continue

        # Remove descriptive prefixes
        for phrase in removable_prefixes:

            if cleaned.startswith(phrase):
                cleaned = cleaned[len(phrase):]

        # Remove descriptive suffixes
        for phrase in removable_suffixes:

            if cleaned.endswith(phrase):
                cleaned = cleaned[:-len(phrase)]

        # Remove role-related phrases
        for phrase in role_phrases:
            cleaned = cleaned.replace(phrase, "")

        # Remove leading articles
        for article in ["a ", "an ", "the "]:

            if cleaned.startswith(article):
                cleaned = cleaned[len(article):]

        # Normalize common technical phrases
        if cleaned.startswith("aws cloud services"):
            cleaned = "aws"

        elif cleaned.startswith("docker and containerized applications"):
            cleaned = "docker"

        elif cleaned.startswith("microservices architecture"):
            cleaned = "microservices architecture"

        elif cleaned.startswith("restful apis"):
            cleaned = "restful apis"

        elif cleaned.startswith("ci cd"):
            cleaned = "ci cd"

        cleaned = cleaned.strip()

        if cleaned:
            normalized.add(cleaned)

    return sorted(normalized)