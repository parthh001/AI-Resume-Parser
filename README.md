# AI Resume Parser

An ATS (Applicant Tracking System) Resume Analyzer built using Python and MySQL.

This project extracts text from PDF resumes, compares the resume against a job description, calculates an ATS compatibility score, identifies missing skills, and stores all analysis results in a MySQL database for future reference.

---

## Features

### Resume Parsing
- Extracts text from PDF resumes
- Supports ATS-style resume evaluation

### ATS Score Calculation
- Compares resume content with job descriptions
- Calculates compatibility percentage

### Skill Gap Detection
- Detects missing skills
- Highlights important technologies absent from the resume

### Database Integration
- Stores resumes in MySQL
- Stores ATS scores
- Stores missing skills
- Maintains complete analysis history

### Analysis History
- View all previous analyses
- Retrieve ATS scores and missing skills from database

### Command Line Interface
- Simple menu-driven application
- Easy to use and test

---

## Technologies Used

### Programming Language
- Python 3

### Database
- MySQL

### Libraries
- PyPDF2
- mysql-connector-python
- pandas
- scikit-learn
- tabulate

---

## Project Structure

```text
AI-Resume-Parser/
│
├── sql/
│   └── schema.sql
│
├── main.py
├── database.py
├── resume_parser.py
├── ats_engine.py
├── reports.py
├── skills.py
│
├── requirements.txt
├── sample_resume_ai_parser.pdf
├── README.md
└── .gitignore
```

---

## Database Schema

### resumes

Stores uploaded resumes.

| Column | Type |
|----------|----------|
| resume_id | INT |
| resume_name | VARCHAR |
| extracted_text | LONGTEXT |
| upload_date | TIMESTAMP |

---

### analyses

Stores ATS analysis results.

| Column | Type |
|----------|----------|
| analysis_id | INT |
| resume_id | INT |
| ats_score | FLOAT |
| missing_skills | TEXT |
| analyzed_at | TIMESTAMP |

---

## Installation

Clone repository

```bash
git clone https://github.com/parthh001/AI-Resume-Parser.git
```

Move into project

```bash
cd AI-Resume-Parser
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure MySQL

Create database:

```sql
CREATE DATABASE ats_resume_db;
```

Run schema:

```sql
SOURCE sql/schema.sql;
```

Update database credentials inside:

```python
database.py
```

---

## Running The Project

```bash
python3 main.py
```

Menu:

```text
1. New Analysis
2. View History
3. Exit
```

---

## Sample Workflow

1. Upload Resume PDF
2. Paste Job Description
3. ATS Score Generated
4. Missing Skills Displayed
5. Results Stored In MySQL

---

## Future Improvements

### Version 1.1
- Matching Skills Display
- Better ATS Scoring Logic

### Version 1.2
- Resume Recommendations
- Resume Improvement Suggestions

### Version 2.0
- Streamlit Web Dashboard
- Drag & Drop Resume Upload

### Version 3.0
- AI-Powered Resume Feedback
- LLM Integration

---

## Author

Parth Patil

Computer Engineering Student

Python • SQL • AI • Machine Learning
