import mysql.connector


def get_connection():

    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="password",
        database="ats_resume_db"
    )


def save_analysis(
        resume_name,
        resume_text,
        ats_score,
        missing_skills):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO resumes
        (resume_name, extracted_text)
        VALUES (%s, %s)
        """,
        (
            resume_name,
            resume_text
        )
    )

    resume_id = cursor.lastrowid

    cursor.execute(
        """
        INSERT INTO analyses
        (
            resume_id,
            ats_score,
            missing_skills
        )
        VALUES (%s, %s, %s)
        """,
        (
            resume_id,
            ats_score,
            ", ".join(missing_skills)
        )
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_history():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            analysis_id,
            ats_score,
            missing_skills,
            analyzed_at
        FROM analyses
        ORDER BY analysis_id DESC
        """
    )

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results


def get_dashboard_stats():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM analyses
        """
    )

    total_analyses = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT AVG(ats_score)
        FROM analyses
        """
    )

    avg_score = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT MAX(ats_score)
        FROM analyses
        """
    )

    highest_score = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return {
        "total": total_analyses,
        "average": round(avg_score, 2) if avg_score else 0,
        "highest": round(highest_score, 2) if highest_score else 0
    }