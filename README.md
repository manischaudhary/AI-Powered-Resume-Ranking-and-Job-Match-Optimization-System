# I-Powered Resume Ranking & ATS Optimization System

An advanced AI-powered resume ranking and ATS optimization platform that analyzes resumes against job descriptions using **NLP, Sentence-BERT embeddings, TF-IDF, semantic similarity, and skill extraction** to calculate ATS compatibility, identify missing skills, and generate personalized resume improvement recommendations.

---

## Overview

This project helps job seekers evaluate how well their resume matches a specific job description.

The system intelligently analyzes resumes using **Natural Language Processing (NLP)** and **Machine Learning techniques** to provide:

* ATS Compatibility Score
* Skill Match Percentage
* Semantic Similarity Score
* Missing Skills Detection
* Resume Quality Analysis
* Personalized AI Recommendations

---

## Features

- Resume PDF Upload
- Job Description Analysis
- ATS Compatibility Score
- Semantic Similarity Matching
- Skill Match Detection
- Missing Skill Identification
- Resume Quality Scoring
-Experience Level Detection
-Interactive Dashboard
-AI-based Resume Improvement Suggestions
-Data Visualization Dashboard

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Frontend & Dashboard

* Streamlit

### Natural Language Processing (NLP)

* Sentence-BERT
* TF-IDF
* Semantic Similarity

### Machine Learning Libraries

* Scikit-learn
* Sentence Transformers

### Data Processing

* Pandas
* NumPy

### PDF Processing

* PyMuPDF (fitz)

### Visualization

* Plotly

---

## Project Architecture

```text
AI-Resume-Ranking-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── pdf_parser.py
│   ├── text_utils.py
│   ├── skill_extractor.py
│   ├── scoring.py
│   ├── recommendations.py
│   └── ui_components.py
│
├── assets/
│   └── style.css
│
├── sample_data/
└── screenshots/
```

---

## Project Workflow

```text
Resume PDF
    ↓
PDF Parsing
    ↓
Text Cleaning
    ↓
Skill Extraction
    ↓
Semantic Matching
    ↓
ATS Score Engine
    ↓
Recommendations
    ↓
Interactive Dashboard
```

### Workflow Explanation

### 1. Resume PDF Upload

The system accepts a resume in PDF format from the user.

### 2. PDF Parsing

Resume content is extracted using **PyMuPDF (fitz)**.

### 3. Text Cleaning

The extracted text is preprocessed through lowercasing, whitespace normalization, and text cleaning.

### 4. Skill Extraction

Technical skills are identified from both the resume and job description using NLP-based keyword extraction.

### 5. Semantic Matching

Resume-job similarity is calculated using **Sentence-BERT embeddings** to understand contextual meaning.

### 6. ATS Score Engine

A weighted scoring mechanism evaluates:

* Skill Match (**35%**)
* Semantic Match (**35%**)
* Keyword Match (**20%**)
* Resume Quality (**10%**)

### 7. AI Recommendations

Missing skills, resume improvements, and optimization suggestions are generated.

### 8. Interactive Dashboard

Results are displayed through a professional analytics dashboard with score visualization and insights.

---

## Screenshots

### Dashboard Home

(Add screenshot here)

### Resume Analysis Results

(Add screenshot here)

### Score Breakdown

(Add screenshot here)

### AI Recommendations

(Add screenshot here)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Resume-Ranking-System.git
```

Navigate into the project folder:

```bash
cd AI-Resume-Ranking-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open locally in your browser:

```text
http://localhost:8501
```

---

## Future Improvements

* LLM-based Resume Rewriting
* Resume PDF Export Report
* Multi-Resume Comparison
* Job Recommendation System
* Real ATS Benchmarking
* Personalized Career Guidance
* Cover Letter Generator
* Resume Version Tracking

---

## Author

**Manis Chaudhary**

Master’s in Data Science | AI • Machine Learning • NLP • Computer Vision
