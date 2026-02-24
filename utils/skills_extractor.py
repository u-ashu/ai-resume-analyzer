from .skills import SKILLS_DB


def extract_skills(text):
    text = text.lower()
    found_skills = []
    for skills in SKILLS_DB:
        if skills in text:
            found_skills.append(skills)
            
    return list(set(found_skills))