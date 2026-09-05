from app.services.skill_extractor import extract_skills
from app.services.dynamic_analyzer import extract_dynamic_concepts


def extract_all_skills(text: str) -> list[str]:
    known_skills = extract_skills(text)

    dynamic_concepts = extract_dynamic_concepts(text)

    combined = set(known_skills)

    for concept in dynamic_concepts:
        if concept not in combined:
            combined.add(concept)

    return sorted(combined)