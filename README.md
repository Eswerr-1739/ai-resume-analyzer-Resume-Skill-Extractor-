# AI Resume Analyzer

**AI Resume Analyzer** is a Python-based tool that allows users to upload resumes and job descriptions (PDF, DOCX, or TXT) to automatically:

- Extract skills from the resume
- Compute resume-to-job similarity
- Score key sections (Experience, Education, Skills)
- Generate CSV and JSON reports for analysis

This project leverages **open-source NLP and LLM models**, making it completely free to run locally.

---

## Features

- **Multi-format Resume & JD Upload:** PDF, DOCX, and TXT files supported.
- **Skill Extraction:** Uses a language model to extract relevant skills from the resume based on the job description.
- **Resume-JD Similarity:** Calculates a similarity score to quantify how well a resume matches a job description.
- **Section Scoring:** Scores key sections like Experience, Education, and Skills.
- **Report Generation:** Saves extracted skills and summary metrics as CSV and JSON files in the `output/` folder.
- **Interactive Web UI:** Built with Streamlit for easy file upload and result display.

---

## Tech Stack

- **Programming Language:** Python  
- **Web Framework:** Streamlit  
- **NLP & Text Processing:** spaCy, regex  
- **LLM:** HuggingFace Transformers (`google/flan-t5-small`) via LangChain pipeline  
- **Similarity Matching:** fuzzywuzzy  
- **File Parsing:** pdfplumber, python-docx, PyPDF2  
- **Data Handling:** pandas, json  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
