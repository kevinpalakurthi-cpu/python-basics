# Student Grade Calculator

# List of student marks
marks = [85, 78, 92, 88, 76]

# Calculate average
total = sum(marks)
average = total / len(marks)

print("Marks:", marks)
print("Average:", average)

# Decide grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Final Grade:", grade)
