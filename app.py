import streamlit as st
from resume_parser import extract_text
from skill_extractor import extract_skills
from ats_score import calculate_ats
from similarity import calculate_similarity
from suggestions import generate_suggestions

st.title("AI Based Resume Analyzer")

resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
jd_text = st.text_area("Paste Job Description")

if resume_file and jd_text:
    resume_text = extract_text(resume_file)
    resume_text = resume_text.lower()
    jd_text = jd_text.lower()

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    ats = calculate_ats(resume_skills, jd_skills)
    similarity = calculate_similarity(resume_text, jd_text)

    missing = list(set(jd_skills) - set(resume_skills))

    st.write("ATS Score:", ats)
    st.write("Resume-JD Similarity:", similarity)

    tips = generate_suggestions(missing, ats, similarity)

    if tips:
        st.subheader("Suggestions")
        for tip in tips:
            st.markdown(f"- {tip}")


