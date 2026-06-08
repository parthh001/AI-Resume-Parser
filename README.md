# AI Resume Parser & ATS Analyzer

An AI-powered Resume Parser and ATS (Applicant Tracking System) Analyzer built using Python and MySQL.

This project allows users to upload a resume PDF, compare it against a job description, calculate an ATS score, identify missing skills, and store analysis history in a MySQL database.

---

## Features

✅ Resume PDF Text Extraction

✅ ATS Score Calculation

✅ Missing Skill Detection

✅ MySQL Database Integration

✅ Analysis History Tracking

✅ Professional CLI Menu

✅ Resume Analysis Storage

✅ Job Description Matching

---

## Tech Stack

- Python
- MySQL
- MySQL Connector
- PyPDF2
- Pandas
- Tabulate

---

## Project Structure

```text
AI-Resume-Parser/
│
├── main.py
├── database.py
├── resume_parser.py
├── ats_engine.py
├── reports.py
├── skills.py
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── menu.png
│   ├── ats_result.png
│   └── history.png
│
└── sql/
    └── schema.sql
```

---

## How It Works

### Step 1

User uploads a Resume PDF.

### Step 2

The system extracts resume text using PDF parsing.

### Step 3

User enters a Job Description.

### Step 4

The ATS Engine compares resume skills with job requirements.

### Step 5

The system calculates:

- ATS Score
- Missing Skills

### Step 6

Analysis results are stored in MySQL.

### Step 7

Users can view previous analyses through the History Menu.

---

## Screenshots

### Main Menu

![Main Menu](screenshots/menu.png)

---

### ATS Analysis Result

![ATS Result](screenshots/ats_result.png)

---

### Analysis History

![History](screenshots/history.png)

---

## Installation

### Clone Repository

```bash
git clone https://github.com/parthh001/AI-Resume-Parser.git
```

```bash
cd AI-Resume-Parser
```

---

### Install Dependencies

```bash
pip3 install -r requirements.txt
```

---

### Setup MySQL Database

Open MySQL Workbench and execute:

```sql
CREATE DATABASE ats_resume_db;
USE ats_resume_db;
```

Then run the SQL schema file located inside:

```text
sql/schema.sql
```

---

### Configure Database Connection

Open:

```text
database.py
```

Update credentials if necessary:

```python
host="127.0.0.1"
user="root"
password="password"
database="ats_resume_db"
```

---

## Usage

Run the application:

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

### New Analysis Flow

Enter Resume PDF Path:

```text
sample_resume_ai_parser.pdf
```

Enter Job Description:

```text
Python Developer

Skills Required:
Python
SQL
Machine Learning
Git
Docker
AWS
```

Output:

```text
ATS Score: 70.71%

Missing Skills:
- docker
- aws
```

Results are automatically stored in MySQL.

---

## Database Schema

### resumes

Stores uploaded resumes.

### analyses

Stores:

- ATS Score
- Missing Skills
- Analysis Date

---

## Example Skills Dataset

Current skill matching includes:

- Python
- SQL
- Java
- C++
- Machine Learning
- Deep Learning
- AWS
- Docker
- Kubernetes
- Git
- TensorFlow
- PyTorch
- Flask
- Django
- MongoDB

---

## Future Improvements

### Version 2

- Streamlit Web Interface
- Drag & Drop Resume Upload
- Better ATS Matching Algorithm
- Resume Ranking
- Resume Recommendations
- Skill Visualization Charts
- Export Analysis to PDF

### Version 3

- AI Resume Suggestions
- GPT-Based Resume Feedback
- Multiple Resume Comparison
- Job Recommendation Engine

---

## Author

Parth Patil

GitHub:
https://github.com/parthh001

---

## License

This project is developed for educational and portfolio purposes.
