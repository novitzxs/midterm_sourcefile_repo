raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    #PART F
    "Fred,90,85",          
    "Gina",                
    "Henry,90,eighty,85",  
    "Ivy,"                 
]

PASSING_GRADE = 75
student_scores = {}

# PART A AND F: Parse data and handle bad records
for record in raw_records:
    fields = record.split(",")

    # Ensure exactly 1 name and 3 scores
    if len(fields) != 4:
        print(f"Skipped invalid record (incorrect field count): {record}")
        continue

    name = fields[0]

    # Convert to floats, safely catching text like "eighty" or blanks
    try:
        scores = [float(fields[1]), float(fields[2]), float(fields[3])]
        student_scores[name] = scores
    except ValueError:
        print(f"Skipped invalid record (non-numeric score): {record}")
        continue

# PART B
print("\nORGANIZED STUDENT RECORDS")
for name, scores in sorted(student_scores.items()):
    formatted_scores = [int(score) for score in scores]
    print(f"{name}: {formatted_scores}")

ranking = []
passed_count = 0
failed_count = 0
sum_of_averages = 0

# PART C: Calculate stats and pass/fail remarks
for name, scores in student_scores.items():
    if len(scores) == 0:
        continue

    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    if average >= PASSING_GRADE:
        remark = "Passed"
        passed_count += 1
    else:
        remark = "Failed"
        failed_count += 1

    sum_of_averages += average
    
    # 'average' is placed first so .sort() will rank by grade instead of name
    ranking.append((average, name, highest_score, lowest_score, remark))

# PART D: Report and Summary
ranking.sort(reverse=True)

print("\nSTUDENT GRADE REPORT")
print(f"{'Rank':<5} {'Name':<6} {'Average':<8} {'Highest':<8} {'Lowest':<8} {'Remark'}")

for rank, (avg, name, highest, lowest, remark) in enumerate(ranking, start=1):
    print(f"{rank:<5} {name:<6} {avg:<8.2f} {int(highest):<8} {int(lowest):<8} {remark}")

print("\nCLASS SUMMARY")
if len(ranking) > 0: # Prevent division by zero if all records were invalid
    class_average = sum_of_averages / len(ranking)
    
    # Pull top and bottom students from the sorted edges
    top_avg, top_name, _, _, _ = ranking[0]
    bottom_avg, bottom_name, _, _, _ = ranking[-1]

    print(f"Number Of Students: {len(ranking)}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print(f"Class Average: {class_average:.2f}")
    print(f"Highest: {top_name} - {top_avg:.2f}")
    print(f"Lowest: {bottom_name} - {bottom_avg:.2f}")
else:
    print("No valid student records found.")