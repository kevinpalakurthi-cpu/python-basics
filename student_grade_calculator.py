# Student Grade Calculator (Interactive)

marks = []

# Take 5 marks from user
for i in range(5):
    mark = int(input("Enter mark: "))
    marks.append(mark)

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

