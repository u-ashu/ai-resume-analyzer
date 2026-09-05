GENERIC_TERMS = {
    "software",
    "technology",
    "technologies",
    "development",
    "engineering",
    "experience",
    "skills",
    "technical skills",
    "programming",
    "system",
    "systems",
    "data",
    "analytics",
}


def is_valid_requirement(requirement: str) -> bool:
    requirement = requirement.strip().lower()

    if not requirement:
        return False

    # Ignore generic terms
    if requirement in GENERIC_TERMS:
        return False

    # Ignore very long NLP-generated phrases
    if len(requirement.split()) > 4:
        return False

    return True


def generate_recommendations(
    missing_requirements: list[str],
    semantic_matches: list[dict],
    threshold: float = 0.75
) -> list[str]:

    recommendations = []

    # Recommendations for missing requirements
    for requirement in missing_requirements:

        if not is_valid_requirement(requirement):
            continue

        recommendations.append(
            f"Consider adding experience with {requirement} "
            "to your resume if applicable."
        )

    # Recommendations for weak semantic matches
    for match in semantic_matches:

        similarity = match["similarity"]

        if similarity < threshold:

            job_concept = match["job_concept"]
            resume_concept = match["resume_concept"]

            recommendations.append(
                f"Your resume mentions '{resume_concept}', "
                f"which is related to '{job_concept}'. "
                "Consider describing this experience more explicitly."
            )

    return recommendations