"""Student Grade Analyzer - Starter Code

Complete every section marked TODO. Keep this file and grades.txt in the
same folder. Rename the completed file to student_grade_analyzer_.py.
"""


def classify_grade(grade):
    """Return the classification and status of a grade."""
    # TODO: Use if/elif/else and return (classification, status).
    
    if 90 <= grade <= 100:
        return ("Excellent", "Passed")
    elif 85 <= grade < 90:
        return ("Very Good", "Passed")
    elif 80 <= grade < 85:
        return ("Good", "Passed")
    elif 75 <= grade < 80:
        return ("Satisfactory", "Passed")
    else:
        return ("Needs Improvement", "Failed")


def load_students(filename):
    """Read valid student records from a text file and return them as a list."""
    students = []

    # TODO: Open filename safely by using with open(...) and try/except.
    # TODO: Loop through the file, clean each line, and skip blank lines.
    # TODO: Split each record and check that it contains three fields.
    # TODO: Convert and validate the grade.
    # TODO: Append a dictionary for every valid record.

    try:
        with open(filename, 'r') as file:
            for line in file:
                cleaned_line = line.strip()

                if not cleaned_line:
                    continue  # Skip blank lines

                parts = cleaned_line.split(',')

                if len(parts) != 3:
                    continue  # Skip records that don't have exactly three fields

                try:
                    grade = float(parts[2])
                    if 0 <= grade <= 100:
                        students.append({
                            "student_number": parts[0].strip(),
                            "name": parts[1].strip(),
                            "grade": grade
                        })
                except ValueError:
                    continue  # Skip records with invalid grade values
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    return students


def calculate_statistics(students):
    """Calculate and return the class statistics."""
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    # TODO: Use one loop to update the accumulator, counters, highest, and lowest.
    # Do not use sum(), max(), or min() for this part.

    # TODO: Calculate the average and return all results in a dictionary.
    for student in students:
        grade = student["grade"]
        total_grade += grade

        if grade >= 75:
            passed_count += 1
        else:
            failed_count += 1

        if grade > highest_student["grade"]:
            highest_student = student

        if grade < lowest_student["grade"]:
            lowest_student = student

    average_grade = total_grade / len(students)

    return {
        "count": len(students),
        "average": average_grade,
        "passed_count": passed_count,
        "failed_count": failed_count,
        "highest": highest_student,
        "lowest": lowest_student
    }


def display_students(students):
    """Display all student records in a formatted table."""
    # TODO: Print column headings.
    # TODO: Loop through students and call classify_grade for each record.

    print(f"{'ID':<12} | {'Name':<15} | {'Grade':<6} | {'Classification':<20} | {'Status'}")
    print("-" * 75)

    for student in students:
        classification, status = classify_grade(student["grade"])
        print(f"{student['student_number']:<12} | {student['name']:<15} | {student['grade']:<6.2f} | {classification:<20} | {status}")


def display_statistics(statistics):
    """Display the calculated class statistics."""
    # TODO: Display every value in statistics clearly.

    if not statistics:
        print("No statistics available.")
        return

    print("\nCLASS STATISTICS")
    print(f"Number of Students: {statistics['count']}")
    print(f"Class Average: {statistics['average']:.2f}")
    print(f"Passed: {statistics['passed_count']}")
    print(f"Failed: {statistics['failed_count']}")
    print(f"Highest: {statistics['highest']['grade']:.2f} - {statistics['highest']['name']} ({statistics['highest']['student_number']})")
    print(f"Lowest: {statistics['lowest']['grade']:.2f} - {statistics['lowest']['name']} ({statistics['lowest']['student_number']})")


def search_student(students, keyword):
    """Return records whose student number or name matches the keyword."""
    matches = []

    clean_keyword = keyword.strip().lower()

    for student in students:
        if clean_keyword in student["name"].lower() or clean_keyword in student["student_number"].lower():
            matches.append(student)

    # TODO: Make keyword lowercase and remove extra whitespace.
    # TODO: Use a loop and partial, case-insensitive matching.

    return matches


def save_report(students, statistics, filename):
    """Write the student results and class statistics to a report file."""
    # TODO: Safely open filename in write mode.
    # TODO: Write all student results and statistics.
    # TODO: Handle a possible OSError.
    try:
        with open(filename, 'w') as file:
            file.write("STUDENT GRADE REPORT\n")
            file.write(f"{'ID':<12} | {'Name':<15} | {'Grade':<6} | {'Classification':<20} | {'Status'}\n")
            file.write("-" * 75 + "\n")

            for student in students:
                classification, status = classify_grade(student["grade"])
                file.write(f"{student['student_number']:<12} | {student['name']:<15} | {student['grade']:<6.2f} | {classification:<20} | {status}\n")

            file.write("\nCLASS STATISTICS\n")
            file.write(f"Number of Students: {statistics['count']}\n")
            file.write(f"Class Average: {statistics['average']:.2f}\n")
            file.write(f"Passed: {statistics['passed_count']}\n")
            file.write(f"Failed: {statistics['failed_count']}\n")
            file.write(f"Highest: {statistics['highest']['grade']:.2f} - {statistics['highest']['name']} ({statistics['highest']['student_number']})\n")
            file.write(f"Lowest: {statistics['lowest']['grade']:.2f} - {statistics['lowest']['name']} ({statistics['lowest']['student_number']})\n")

            print(f"\nSuccess: Report saved to {filename}")
    except OSError:
        print("\nError: Could not write the report file. Please check the file path and permissions.")


def main():
    """Run the menu-driven Student Grade Analyzer."""
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        # TODO: Call the appropriate function for choices 1 to 4.
        # TODO: For choice 3, ask for a keyword and display every match.
        # TODO: Use break for choice 5.
        # TODO: Use continue after an invalid choice.

        if choice == "1":
            print()
            display_students(students)

        elif choice == "2":
            print()
            display_statistics(statistics)

        elif choice == "3":
            keyword = input("Enter student name or ID to search: ")
            matches = search_student(students, keyword)
            print()
            if matches:
                display_students(matches)
            else:
                print("No matching student records found.")

        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")
            continue


if __name__ == "__main__":
    main()

