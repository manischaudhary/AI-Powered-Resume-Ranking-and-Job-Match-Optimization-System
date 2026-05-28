import re
from src.config import TECHNICAL_SKILLS
from src.text_utils import clean_text


def extract_skills(text: str) -> list:
    text = clean_text(text)
    found_skills = []

    for skill in TECHNICAL_SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(set(found_skills))


def compare_skills(resume_skills: list, job_skills: list):
    if len(job_skills) == 0:
        return 0, [], []

    matched_skills = sorted(set(resume_skills).intersection(set(job_skills)))
    missing_skills = sorted(set(job_skills).difference(set(resume_skills)))

    skill_score = round((len(matched_skills) / len(job_skills)) * 100, 2)

    return skill_score, matched_skills, missing_skills