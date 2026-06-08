# AI Resume Parser

A Python and MySQL based ATS Resume Analyzer that extracts text from PDF resumes, compares them against job descriptions, calculates ATS scores, identifies missing skills, and stores analysis history in MySQL.

## Features

- PDF Resume Parsing
- ATS Score Calculation
- Missing Skill Detection
- MySQL Database Integration
- Analysis History Tracking
- Interactive CLI Menu

## Technologies Used

- Python
- MySQL
- Scikit-Learn
- PyPDF2

## Project Structure

```text
main.py
database.py
resume_parser.py
ats_engine.py
reports.py
skills.py
sql/schema.sql
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python3 main.py
```

## Future Improvements

- Dashboard Analytics
- Streamlit Web UI
- Resume Recommendations
- AI-Powered Resume Feedback