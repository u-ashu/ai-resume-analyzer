GENERIC_TERMS = {
    "experience",
    "developer",
    "developers",
    "engineer",
    "engineers",
    "person",
    "people",
    "team",
    "teams",
    "project",
    "projects",
    "company",
    "companies",
    "role",
    "roles",
    "work",
    "working",
    "candidate",
    "candidates",
    "databases",
    "frontend",
    "backend",
    "software",
    "technology",
    "technologies",
    "problem",
    "problems",
    "production issues",
    "strong proficiency",
}

def filter_concepts(candidates: list[str]) -> list[str]:

    filtered = []

    for concept in candidates:

        concept = concept.strip().lower()

        if not concept:
            continue

        if concept in GENERIC_TERMS:
            continue

        filtered.append(concept)

    return sorted(set(filtered))