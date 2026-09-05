GENERIC_REQUIREMENT_PHRASES = {
    "apis requirements",
    "backend software",
    "collaborative software development",
    "comfortable designing backend services",
    "scalable web applications",
    "strong proficiency",
    "the candidate",
    "we",
    "frontend",
    "databases",
    "production issues",
}


def build_requirements(
    job_skills: list[str],
    job_dynamic_concepts: list[str]
) -> list[str]:

    requirements = set()

    # Add exact technical skills
    for skill in job_skills:
        skill = skill.lower().strip()

        if skill:
            requirements.add(skill)

    # Add meaningful dynamic requirements
    for concept in job_dynamic_concepts:

        concept = concept.lower().strip()

        if not concept:
            continue

        if concept in GENERIC_REQUIREMENT_PHRASES:
            continue

        requirements.add(concept)

    return sorted(requirements)