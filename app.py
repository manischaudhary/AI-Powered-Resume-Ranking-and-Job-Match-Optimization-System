import pandas as pd
import plotly.express as px
import streamlit as st

from src.pdf_parser import extract_text_from_pdf
from src.text_utils import clean_text, detect_experience_level, detect_resume_sections
from src.skill_extractor import extract_skills, compare_skills
from src.scoring import (
    calculate_keyword_score,
    calculate_semantic_score,
    calculate_resume_quality_score,
    calculate_final_score,
    get_score_label
)
from src.recommendations import generate_recommendations
from src.ui_components import (
    load_css,
    render_circle_metric,
    render_skill_chips,
    render_recommendations
)


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)

load_css("assets/style.css")


with st.sidebar:
    st.markdown("## 🚀 AI Resume<br>Analyzer", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="sidebar-box">
        <b>📊 Dashboard</b><br><br>
        🏠 Dashboard<br><br>
        📈 Score Breakdown<br><br>
        🔗 Skills Match<br><br>
        ❌ Missing Skills<br><br>
        📄 Resume Sections<br><br>
        🧠 AI Recommendations
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-box">
        <b>Scoring Formula</b><br><br>
        🔵 35% Skill Match<br>
        🟣 35% Semantic Match<br>
        🟠 20% Keyword Match<br>
        🟢 10% Resume Quality
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("💡 Add keywords and measurable achievements to improve your score.")


st.markdown(
    """
    <div class="app-title">
        AI-Powered Resume Ranking & ATS Optimization System
    </div>
    <div class="app-subtitle">
        Get AI-driven insights to improve your resume and increase your chances of getting hired.
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown('<div class="glass-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        '<div class="step-title"><span class="badge">1</span>Upload Your Resume</div>',
        unsafe_allow_html=True
    )
    uploaded_resume = st.file_uploader(
    " ",
    type=["pdf"],
    help="Upload a professional resume in PDF format"
    )

    st.caption(
        "📄 Supported format: PDF • Max size: 200MB"
    )

with col2:
    st.markdown(
        '<div class="step-title"><span class="badge">2</span>Paste Job Description</div>',
        unsafe_allow_html=True
    )
    job_description = st.text_area(
        "Paste the job description here...",
        height=210,
        max_chars=5000
    )

analyze_button = st.button("🚀 Analyze Resume", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)


if analyze_button:
    if uploaded_resume is None:
        st.warning("Please upload your resume PDF.")
        st.stop()

    if not job_description.strip():
        st.warning("Please paste the job description.")
        st.stop()

    progress = st.progress(0)
    status = st.empty()

    status.write("📄 Extracting resume text...")
    progress.progress(15)
    resume_text = extract_text_from_pdf(uploaded_resume)

    cleaned_resume = clean_text(resume_text)
    cleaned_job = clean_text(job_description)

    status.write("🧠 Extracting skills...")
    progress.progress(35)
    resume_skills = extract_skills(cleaned_resume)
    job_skills = extract_skills(cleaned_job)

    skill_score, matched_skills, missing_skills = compare_skills(
        resume_skills,
        job_skills
    )

    status.write("🔍 Calculating keyword score...")
    progress.progress(55)
    keyword_score = calculate_keyword_score(cleaned_resume, cleaned_job)

    status.write("🤖 Calculating semantic score...")
    progress.progress(75)
    semantic_score = calculate_semantic_score(cleaned_resume, cleaned_job)

    status.write("📊 Evaluating resume quality...")
    progress.progress(90)
    quality_score = calculate_resume_quality_score(cleaned_resume)

    final_score = calculate_final_score(
        skill_score,
        semantic_score,
        keyword_score,
        quality_score
    )

    sections = detect_resume_sections(cleaned_resume)
    experience_level = detect_experience_level(cleaned_job)

    recommendations = generate_recommendations(
        final_score,
        semantic_score,
        keyword_score,
        quality_score,
        missing_skills,
        sections
    )

    progress.progress(100)
    status.success("✅ Analysis complete!")

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📈 Overall Match Summary")

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    with c1:
        render_circle_metric("Final ATS Score", int(final_score), "#22c55e", get_score_label(final_score))

    with c2:
        render_circle_metric("Skill Match", int(skill_score), "#3b82f6", "Good")

    with c3:
        render_circle_metric("Semantic Match", int(semantic_score), "#a855f7", "Excellent")

    with c4:
        render_circle_metric("Keyword Match", int(keyword_score), "#f59e0b", "Good")

    with c5:
        render_circle_metric("Resume Quality", int(quality_score), "#22c55e", "Good")

    with c6:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Experience Level</div>
                <div style="font-size:42px; margin-top:28px;">💼</div>
                <div style="font-weight:800; margin-top:12px;">{experience_level}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📊 Score Breakdown",
            "🔗 Skills Match",
            "❌ Missing Skills",
            "📄 Resume Sections",
            "🧠 AI Recommendations"
        ]
    )

    with tab1:
        left, right = st.columns(2)

        score_data = pd.DataFrame(
            {
                "Category": [
                    "Skill Match",
                    "Semantic Match",
                    "Keyword Match",
                    "Resume Quality",
                    "Final ATS Score"
                ],
                "Score": [
                    skill_score,
                    semantic_score,
                    keyword_score,
                    quality_score,
                    final_score
                ]
            }
        )

        with left:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("### Score Breakdown")

            radar = px.line_polar(
                score_data,
                r="Score",
                theta="Category",
                line_close=True,
                range_r=[0, 100]
            )

            radar.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)"
            )

            st.plotly_chart(radar, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with right:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("### Score Comparison")

            bar = px.bar(
                score_data,
                x="Category",
                y="Score",
                text="Score",
                range_y=[0, 100],
                color="Category"
            )

            bar.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
            bar.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                showlegend=False
            )

            st.plotly_chart(bar, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### Skills found in both resume and job description")
        render_skill_chips(matched_skills, "matched")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### Skills missing from your resume")
        render_skill_chips(missing_skills, "missing")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

        section_data = pd.DataFrame(
            {
                "Section": list(sections.keys()),
                "Detected": [
                    "Yes" if value else "No"
                    for value in sections.values()
                ]
            }
        )

        st.dataframe(section_data, use_container_width=True)

        pie = px.pie(
            section_data,
            names="Detected",
            title="Resume Section Completeness"
        )

        pie.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(pie, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab5:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        render_recommendations(recommendations)
        st.markdown("</div>", unsafe_allow_html=True)

    with st.expander("📄 View Extracted Resume Text"):
        st.write(resume_text)

    with st.expander("🧾 View Resume Skills"):
        st.write(resume_skills)

    with st.expander("💼 View Job Description Skills"):
        st.write(job_skills)