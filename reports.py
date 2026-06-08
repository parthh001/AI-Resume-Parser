def display_result(
        score,
        missing_skills):

    print("\n========================")

    print(f"ATS Score: {score}%")

    print("\nMissing Skills:")

    if len(missing_skills) == 0:
        print("None")

    else:

        for skill in missing_skills:
            print("-", skill)

    print("========================")