import re

from app.data.skills import SKILLS_DB, SKILL_ALIASES


def extract_skills(text: str) -> list[str]:
    text = text.lower()

    found_skills = set()

    for skill in SKILLS_DB:

        aliases = SKILL_ALIASES.get(skill, [])

        terms_to_search = [skill] + aliases

        for term in terms_to_search:

            pattern = r"(?<!\w)" + re.escape(term) + r"(?!\w)"

            if re.search(pattern, text):
                found_skills.add(skill)
                break

    return sorted(found_skills)