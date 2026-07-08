<img width="1584" height="396" alt="resumeparser" src="https://github.com/user-attachments/assets/a245ed43-dfa9-49c4-ba04-a1d97f8dc441" />

---
# AI Resume Parser & ATS Analyzer
---

A Python-based ATS (Applicant Tracking System) Resume Analyzer that parses PDF resumes, compares them against job descriptions, calculates ATS compatibility scores, identifies missing skills, and stores analysis history in MySQL.

---

## Overvieww

This project simulates a simplified Applicant Tracking System used by recruiters to evaluate resumes against job requirements.

The system extracts text from PDF resumes, matches candidate skills against job descriptions, calculates an ATS score, identifies skill gaps, and stores all analyses in a MySQL database for future reference.

---

## Key Features

- PDF Resume Parsing
- ATS Score Calculation
- Skill Gap Detection
- Job Description Matching
- Analysis History Tracking
- MySQL Database Integration
- Command Line Interface
- Persistent Analysis Storage

---

## Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Database | MySQL |
| PDF Processing | PyPDF2 |
| Data Handling | Pandas |
| Database Connector | mysql-connector-python |
| Output Formatting | Tabulate |

---

## Screenshots

### Main Menu

![Main Menu](screenshots/menu.png)

---

### ATS Analysis

![ATS Analysis](screenshots/ats_result.png)

---

### Analysis History

![History](screenshots/history.png)

---

## Project Structure

```text
AI-Resume-Parser
│
├── main.py
├── resume_parser.py
├── ats_engine.py
├── database.py
├── reports.py
├── skills.py
├── requirements.txt
├── README.md
│
├── screenshots
│   ├── menu.png
│   ├── ats_result.png
│   └── history.png
│
└── sql
    └── schema.sql
```

---

## ATS Workflow

```text
Resume PDF
     │
     ▼
Text Extraction
     │
     ▼
Skill Identification
     │
     ▼
Job Description Matching
     │
     ▼
ATS Score Generation
     │
     ▼
Missing Skills Detection
     │
     ▼
MySQL Storage
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/parthh001/AI-Resume-Parser.git
cd AI-Resume-Parser
```

### Install Dependencies

```bash
pip3 install -r requirements.txt
```

---

## Database Setup

Create a MySQL database:

```sql
CREATE DATABASE ats_resume_db;
USE ats_resume_db;
```

Run the schema file located in:

```text
sql/schema.sql
```

Configure database credentials inside:

```text
database.py
```

Example:

```python
host="localhost"
user="your_mysql_username"
password="your_mysql_password"
database="ats_resume_db"
```

---

## Running the Application

```bash
python3 main.py
```

### Menu Options

```text
1. New Analysis
2. View History
3. Exit
```

---

## Example Analysis

### Job Description

```text
Python Developer

Required Skills:
Python
SQL
Machine Learning
Docker
Git
AWS
```

### Output

```text
ATS Score: 70.71%

Missing Skills:
- docker
- aws
```

Results are automatically stored in the MySQL database.

---

## Database Storage

The application stores:

- Resume Information
- ATS Score
- Missing Skills
- Analysis Timestamp

This enables users to review previous analyses through the History menu.

---

## Current Skill Library

```text
Python
SQL
Java
C++
Machine Learning
Deep Learning
AWS
Docker
Kubernetes
Git
TensorFlow
PyTorch
Flask
Django
MongoDB
```

---

## Sample Use Case

1. Upload a Resume PDF.
2. Enter a target Job Description.
3. Receive an ATS Compatibility Score.
4. View Missing Skills.
5. Store Results in MySQL.
6. Access Historical Analyses.

---

## Future Roadmap

### Version 2

- Streamlit Web Interface
- Drag-and-Drop Resume Upload
- ATS Score Visualizations
- Resume Ranking System
- Export Reports to PDF

### Version 3

- AI Resume Recommendations
- GPT-Based Resume Review
- Multiple Resume Comparison
- Job Recommendation Engine

---

## Repository

GitHub Repository:

https://github.com/parthh001/AI-Resume-Parser

---

## Author

Parth Patil

---

## License

This project is intended for educational, learning, and portfolio purposes.
