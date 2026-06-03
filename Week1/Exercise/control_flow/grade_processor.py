def grade_processor(scores):


    """
    Given a list of student scores, write a program that:

        Uses a for loop with enumerate to process each score.
        Assigns letter grades using if/elif/else.
        Uses continue to skip any negative scores (invalid data).
        Uses break if a score of -999 is encountered (sentinel value — stop processing).
        At the end, prints:
        Each student's grade
        Class average (excluding invalid scores)
        Highest and lowest grades
        Distribution count (how many A's, B's, C's, D's, F's)
    
    """

    valid_scores = []
    dist_count = {}

    for i, score in enumerate(scores):

        # sentinel value 
        if score == -999:
            break

        # invalid score
        if score < 0:
            print(f"Invalid score {score}")
            continue

        # store valid score
        valid_scores.append(score)

        # grade determination
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        print(f"Student {i} got a {grade}")

        # update distribution count
        dist_count[grade] = dist_count.get(grade, 0) + 1

    # calculations
    class_avg = sum(valid_scores) / len(valid_scores)
    highest_grade = max(valid_scores)
    lowest_grade = min(valid_scores)

    # results
    print("\n--- Class Summary ---")
    print(f"Class Average: {class_avg:.2f}")
    print(f"Highest Score: {highest_grade}")
    print(f"Lowest Score: {lowest_grade}")
    print(f"Grade Distribution: {dist_count}")


scores = [88, 92, 75, -1, 63, 95, 81, 70, -5, 55, 100, 78, -999, 90, 85]
grade_processor(scores)