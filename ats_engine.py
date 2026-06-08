from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from skills import SKILLS


def calculate_score(resume_text, job_description):

    documents = [resume_text, job_description]

    vectorizer = CountVectorizer()

    matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(matrix)

    score = similarity[0][1]

    return round(score * 100, 2)


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return found_skills


def find_missing_skills(
        resume_text,
        job_description):

    resume_skills = set(
        extract_skills(resume_text)
    )

    jd_skills = set(
        extract_skills(job_description)
    )

    return list(
        jd_skills - resume_skills
    )