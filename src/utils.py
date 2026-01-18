import os
import pdfplumber
import re
import docx
import io
from PyPDF2 import PdfReader
from docx import Document
import spacy

nlp = spacy.load("en_core_web_sm")

# -----------------------
# Text cleaning
def clean_text(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if token.is_alpha and not token.is_stop])

# -----------------------
# File reading
def read_file(uploaded_file):
    if uploaded_file is None:
        return ""

    filename = uploaded_file.name.lower()

    # TEXT FILE
    if filename.endswith(".txt"):
        return uploaded_file.read().decode("utf-8", errors="ignore")

    # PDF FILE
    elif filename.endswith(".pdf"):
        text = ""
        with pdfplumber.open(io.BytesIO(uploaded_file.read())) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    # DOCX FILE
    elif filename.endswith(".docx"):
        doc = docx.Document(io.BytesIO(uploaded_file.read()))
        return "\n".join([p.text for p in doc.paragraphs])

    else:
        return ""

def shorten_text(text: str, max_chars: int = 2000) -> str:
    """
    Shortens text to a maximum number of characters.
    Useful for sending long resumes or JDs to LLMs.
    """
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "..."
# -----------------------
# Extract sections
def extract_sections(text):
    sections = {}
    patterns = ["experience", "education", "skills", "projects", "certifications"]
    for p in patterns:
        match = re.search(p + ".*?:", text, re.IGNORECASE)
        sections[p] = match.group(0) if match else ""
    return sections
