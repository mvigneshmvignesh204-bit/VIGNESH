subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))
subject4 = int(input("Enter marks for subject 4: "))
total_marks = subject1 + subject2 + subject3 + subject4
aggregate_percentage = (total_marks / 400) * 100
if aggregate_percentage >= 75:
    grade = "Distinction"
elif aggregate_percentage >= 60 and aggregate_percentage < 75:
    grade = "First Division"
elif aggregate_percentage >= 50 and aggregate_percentage < 60:
    grade = "Second Division"
elif aggregate_percentage >= 40 and aggregate_percentage < 50:
    grade = "Third Division"
else:
    grade = "Fail"
print("Total Marks:", total_marks)
print("Aggregate Percentage:", aggregate_percentage, "%")
print("Grade:", grade)
