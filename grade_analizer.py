scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

A=0
B=0
C=0
D=0
F=0 # it is to make python recognize them as variable

for score in scores:
    if score >= 90:
        A += 1
    elif score >= 80:
        B += 1
    elif score >= 70:
        C += 1
    elif score >= 60:
        D += 1
    else:
        F += 1

total_scores = len(scores)
sum_scores = sum(scores) # will be use to find the average
highest_scores = max(scores)
lowest_scores = min(scores)

passing = 0
failing = 0 # to make python recognize them as variable

for score in scores:
    if score >= 60:
        passing += 1
    else:
        failing += 1

passing_percentage = (passing / total_scores) * 100
failing_percntage = (failing / total_scores) * 100 # formula to have the passing and failing in percentage


print("="*3 + "Grade Analyzer" + "="*3)
print(f"Total scores: {total_scores}")
print(f"Average: {sum_scores/total_scores:.1f}")
print(f"Highest: {highest_scores}")
print(f"Lowest: {lowest_scores}")
print(f"Passing: {passing} ({passing_percentage}%)")
print(f"Failing: {failing} ({failing_percntage}%)")
print("\nGrade Distribution:")
print(f"A: {A} students")
print(f"B: {B} students")
print(f"C: {C} students")
print(f"D: {D} students")
print(f"F: {F} students\n")

print("-"*3 + "Add More Scores" + "-"*3)

while True:
    new_score = input("Enter a score ( or 'done' to finish'): ")

    if new_score == "done":
        final_average = sum(scores) / len(scores)
        print(f"\nFinal average: {final_average:.1f}")
        break # to make python stop
    else:
        new_score = int(new_score)
        scores.append(new_score)

        updated_average = sum(scores) / len(scores)
        print(f"Updated Average: {updated_average:.1f}")
