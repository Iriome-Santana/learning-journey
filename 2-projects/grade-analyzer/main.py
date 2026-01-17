
grades = [6, 3, 9, 10, 5, 8, 7, 4, 2]


def analyze_grades(grades, passing_score=5):
    """
    Analyzes a list of grades and returns basic statistics.

    :param grades: list of numeric grades
    :param passing_score: minimum grade to pass
    :return: dictionary with statistics or None if list is empty
    """
    
    if not grades:
        return None
    
    return {"average": sum(grades) / len(grades),
            "max_grade": max(grades),
            "min_grade": min(grades),
            "passing_count": sum(1 for g in grades if g >= passing_score),
            "failing_count": sum(1 for g in grades if g < passing_score)
            }
                
results = analyze_grades(grades)

if results is None:
    print("No grades to analyze.")
else:
    print("----RESULTS----")
    print("Grade Statistics:")
    print(f"The average grade is: {results['average']:.2f}")
    print(f"The highest grade is: {results['max_grade']}")
    print(f"The lowest grade is: {results['min_grade']}")
    print(f"The number of passing grades are: {results['passing_count']}")
    print(f"The number of failing grades are: {results['failing_count']}")


