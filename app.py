import streamlit as st
from src.utils import read_file
from src.analyzer import compute_similarity, section_scoring, llm_skill_extraction, save_reports

st.title("AI Resume Analyzer (LangChain & Free LLM)")

# -----------------------
# File uploads
resume_file = st.file_uploader("Upload Resume (.pdf, .docx, .txt)", type=["pdf", "docx", "txt"])
jd_file = st.file_uploader("Upload Job Description (.pdf, .docx, .txt)", type=["pdf", "docx", "txt"])

if resume_file and jd_file:
    resume_text = read_file(resume_file)
    jd_text = read_file(jd_file)

    if not resume_text.strip():
        st.error("Resume file is empty or could not be read.")
    elif not jd_text.strip():
        st.error("Job Description file is empty or could not be read.")
    else:
        # -----------------------
        # Compute similarity
        similarity = compute_similarity(resume_text, jd_text)
        st.write(f"Resume-JD Similarity: {similarity:.2f}%")

        # -----------------------
        # Section scoring
        section_scores = section_scoring(resume_text)  # only resume text
        if not isinstance(section_scores, dict):
            section_scores = {}
        st.write("Section Scores:", section_scores)

        # -----------------------
        # Extract skills using LLM
        skills = llm_skill_extraction(resume_text, jd_text)
        if not isinstance(skills, list):
            skills = []
        st.write("Extracted Skills:", skills)

        # -----------------------
        # Save reports safely
        save_reports(
            skills=skills,
            similarity=similarity,
            section_scores=section_scores
        )
        st.success("Reports saved in `output/` folder")
