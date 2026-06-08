from resume_parser import extract_resume_text

from ats_engine import (
    calculate_score,
    find_missing_skills
)

from reports import (
    display_result
)

from database import (
    save_analysis,
    get_history
)


def new_analysis():

    print("\n=== NEW ANALYSIS ===\n")

    pdf_path = input(
        "Enter Resume PDF Path: "
    )

    resume_text = extract_resume_text(
        pdf_path
    )

    print(
        "\nPaste Job Description:\n"
    )

    job_description = input()

    score = calculate_score(
        resume_text,
        job_description
    )

    missing_skills = find_missing_skills(
        resume_text,
        job_description
    )

    display_result(
        score,
        missing_skills
    )

    save_analysis(
        pdf_path,
        resume_text,
        score,
        missing_skills
    )

    print(
        "\nAnalysis Saved Successfully!"
    )


def view_history():

    history = get_history()

    print(
        "\n=== ANALYSIS HISTORY ===\n"
    )

    if len(history) == 0:

        print(
            "No Analysis Found."
        )

        return

    for row in history:

        print(
            f"""
Analysis ID : {row[0]}
ATS Score   : {row[1]}%
Missing     : {row[2]}
Date        : {row[3]}
"""
        )


def main():

    while True:

        print(
            """
==================================
         AI RESUME PARSER
==================================

1. New Analysis

2. View History

3. Exit
"""
        )

        choice = input(
            "Enter Choice: "
        )

        if choice == "1":

            new_analysis()

        elif choice == "2":

            view_history()

        elif choice == "3":

            print(
                "\nThank You For Using AI Resume Parser!"
            )

            break

        else:

            print(
                "\nInvalid Choice."
            )


if __name__ == "__main__":
    main()