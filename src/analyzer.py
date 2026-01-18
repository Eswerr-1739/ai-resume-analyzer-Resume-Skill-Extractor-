from fuzzywuzzy import fuzz
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from .utils import clean_text, shorten_text
import pandas as pd
import os
import json

# -------------------
# HuggingFace pipeline setup (token limit safe)
embedding_model = "google/flan-t5-small"  # Open-source model
gen_pipeline = pipeline(
    "text2text-generation",
    model=embedding_model,
    tokenizer=embedding_model,
    max_new_tokens=1000,
    temperature=0.2,
    do_sample=False
)
llm = HuggingFacePipeline(pipeline=gen_pipeline)

# -------------------
# Skill extraction using LLM
def llm_skill_extraction(resume_text, jd_text):
    resume_text = shorten_text(resume_text)
    jd_text = shorten_text(jd_text)
    prompt = f"""
Extract skills from the resume below that match the job description.
Provide as a comma-separated list..

Job Description:
{jd_text}

Resume:
{resume_text}
"""
    result = llm.generate([prompt])
    text = result.generations[0][0].text.strip()
    
    # Convert to list safely
    skills_list = [s.strip() for s in text.split(",") if s.strip()]
    return skills_list

# -------------------
# Resume-JD similarity
def compute_similarity(resume_text, jd_text):
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)
    return fuzz.token_set_ratio(resume_clean, jd_clean)

# -------------------
# Section scoring
def section_scoring(resume_text, sections=["experience", "education", "skills"]):
    scores = {}
    resume_lower = resume_text.lower()
    for sec in sections:
        if sec in resume_lower:
            scores[sec] = 100
        else:
            scores[sec] = 0
    return scores

# -------------------
# Save CSV/JSON reports
def save_reports(skills, similarity, section_scores, output_folder="output"):
    import os, json, pandas as pd

    os.makedirs(output_folder, exist_ok=True)
    
    # -------------------
    # Ensure skills is a list
    if isinstance(skills, list):
        skills_list = skills
    elif isinstance(skills, dict) and "skills" in skills:
        skills_list = skills["skills"]
    else:
        skills_list = []
    
    # Save skills JSON
    json_path = os.path.join(output_folder, "skills_report.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(skills_list, f, indent=4)
    
    # Save skills CSV
    if skills_list:
        df_skills = pd.DataFrame({"Skill": skills_list})
        df_skills.to_csv(os.path.join(output_folder, "skills_report.csv"), index=False)
    
    # -------------------
    # Ensure section_scores is a dictionary
    if not isinstance(section_scores, dict):
        try:
            section_scores = dict(section_scores)  # Convert if possible
        except Exception:
            section_scores = {}
    
    # Summary
    summary = {
        "Resume-JD Similarity": similarity,
        **section_scores
    }

    # Save summary CSV
    df_summary = pd.DataFrame(list(summary.items()), columns=["Metric", "Score"])
    df_summary.to_csv(os.path.join(output_folder, "summary_report.csv"), index=False)
    
    return json_path

