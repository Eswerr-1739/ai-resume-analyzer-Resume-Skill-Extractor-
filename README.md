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
```
2. Create a virtual environment:
```bash
   python -m venv venv
```
3. Activate the virtual environment:
Windows (PowerShell)
```bash
.\venv\Scripts\Activate.ps1
```
Linux / Mac:
```bash
source venv/bin/activate
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app

```bash
streamlit run app.py
```
2. Upload a Resume and Job Description file (.pdf, .docx, .txt).

3. View results:

- Resume-JD similarity score
- Section scores (Experience, Education, Skills)
- Extracted skills
- Reports will be saved automatically in the output/ folder as:
- skills_report.json
- skills_report.csv
- summary_report.csv

## Folder Structure

AI-Resume-Analyzer/
├── app.py                  # Streamlit web application
├── src/
│   ├── analyzer.py         # Main analysis functions (skills, similarity, reports)
│   └── utils.py            # File reading, cleaning, and text processing functions
├── output/                 # Generated CSV/JSON reports
├── requirements.txt        # Python dependencies
└── README.md

## Notes & Improvements
1. Skill extraction may currently capture some unwanted text like emails, names, or extra words.
2. Section scoring is basic and can be improved by analyzing actual content instead of just headings.
3. Future improvements could include:
      - RAG-based interactive Q&A
      - Semantic similarity using embeddings
      - Advanced section parsing

## License
This project is open-source and free to use under the MIT License
