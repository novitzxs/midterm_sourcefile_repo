scores = [85, 72, 91, 64, 78]

print("Students Scores: ")
for score in scores:
    print(score)

passed_count = 0
failed_count = 0

print()

for i, score in enumerate(scores, start=1):

    if score >= 90:
        print(f"Students {i}: {score} - Excellent - Passed")
        passed_count += 1
    elif score >= 80:
        print(f"Students {i}: {score} - Very Good - Passed")
        passed_count += 1
    elif score >= 75:
        print(f"Students {i}: {score} - Good - Passed")
        passed_count += 1
    else:
        print(f"Students {i}: {score} - Failed")
        failed_count += 1

print()

total = sum(scores)
average = total // len(scores)

print(f"Total Score: {total}")
print(f"Average Score: {average}")
print(f"Highest Score: {max(scores)}")
print(f"Lowest Score: {min(scores)}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")