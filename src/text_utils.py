import re


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def detect_experience_level(job_text: str) -> str:
    text = clean_text(job_text)

    if any(word in text for word in ["intern", "internship", "entry level", "junior", "new grad"]):
        return "Entry-Level / Internship"

    if any(word in text for word in ["senior", "lead", "principal", "manager"]):
        return "Senior-Level"

    if any(word in text for word in ["2 years", "3 years", "4 years", "mid-level", "mid level"]):
        return "Mid-Level"

    return "Not Clearly Specified"


def detect_resume_sections(resume_text: str) -> dict:
    text = clean_text(resume_text)

    sections = {
        "Summary": ["summary", "profile", "objective", "professional summary"],
        "Skills": ["skills", "technical skills", "technologies"],
        "Experience": ["experience", "work experience", "professional experience"],
        "Projects": ["projects", "academic projects", "personal projects"],
        "Education": ["education", "academic background"],
        "Certifications": ["certifications", "certificates"]
    }

    detected_sections = {}

    for section, keywords in sections.items():
        detected_sections[section] = any(keyword in text for keyword in keywords)

    return detected_sections