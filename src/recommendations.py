def generate_recommendations(
    final_score,
    semantic_score,
    keyword_score,
    quality_score,
    missing_skills,
    sections
):
    recommendations = []

    if final_score >= 80:
        recommendations.append("Strong match. This resume is well aligned with the job description.")
    elif final_score >= 65:
        recommendations.append("Good match. Add missing skills and stronger project impact to improve ranking.")
    elif final_score >= 50:
        recommendations.append("Moderate match. Add more role-specific keywords, tools, and measurable achievements.")
    else:
        recommendations.append("Low match. The resume needs stronger alignment with the job description.")

    if missing_skills:
        recommendations.append(
            "Add relevant missing skills if you have experience with them: "
            + ", ".join(missing_skills[:10])
        )

    if semantic_score < 60:
        recommendations.append(
            "Improve semantic alignment by adding project descriptions closer to the job responsibilities."
        )

    if keyword_score < 50:
        recommendations.append(
            "Add important job-description keywords naturally in Skills, Projects, and Experience."
        )

    if quality_score < 70:
        recommendations.append(
            "Use stronger action verbs, measurable outcomes, and complete resume sections."
        )

    missing_sections = [
        section for section, exists in sections.items()
        if not exists
    ]

    if missing_sections:
        recommendations.append(
            "Consider adding these sections: " + ", ".join(missing_sections)
        )

    recommendations.append(
        "Best bullet format: Action Verb + Technical Skill + Task + Measurable Result."
    )

    return recommendations