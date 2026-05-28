import re
import streamlit as st

from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.config import MODEL_NAME, ACTION_VERBS, SCORING_WEIGHTS
from src.text_utils import clean_text, detect_resume_sections


@st.cache_resource
def load_embedding_model():
    return SentenceTransformer(MODEL_NAME)


def calculate_keyword_score(resume_text: str, job_text: str) -> float:
    try:
        vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2)
        )

        matrix = vectorizer.fit_transform([resume_text, job_text])
        score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]

        return round(score * 100, 2)

    except Exception:
        return 0


def calculate_semantic_score(resume_text: str, job_text: str) -> float:
    model = load_embedding_model()

    embeddings = model.encode([resume_text, job_text])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

    return round(score * 100, 2)


def calculate_resume_quality_score(resume_text: str) -> float:
    text = clean_text(resume_text)
    sections = detect_resume_sections(text)

    score = 0

    score += sum(sections.values()) * 8

    action_count = sum(1 for verb in ACTION_VERBS if verb in text)
    score += min(action_count * 4, 20)

    has_numbers = bool(re.search(r"\d+%|\$\d+|\d+\+", text))

    if has_numbers:
        score += 15

    word_count = len(text.split())

    if 350 <= word_count <= 900:
        score += 15
    elif 250 <= word_count < 350 or 900 < word_count <= 1100:
        score += 8

    return min(score, 100)


def calculate_final_score(
    skill_score: float,
    semantic_score: float,
    keyword_score: float,
    quality_score: float
) -> float:
    final_score = (
        skill_score * SCORING_WEIGHTS["skill_match"]
        + semantic_score * SCORING_WEIGHTS["semantic_match"]
        + keyword_score * SCORING_WEIGHTS["keyword_match"]
        + quality_score * SCORING_WEIGHTS["resume_quality"]
    )

    return round(final_score, 2)


def get_score_label(score: float) -> str:
    if score >= 80:
        return "Excellent Match"

    if score >= 65:
        return "Good Match"

    if score >= 50:
        return "Moderate Match"

    return "Needs Improvement"