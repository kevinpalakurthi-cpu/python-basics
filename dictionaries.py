# Python Dictionaries Example

student = {
    "name": "Kevin",
    "age": 22,
    "course": "Python"
}

print("Student details:", student)

# Accessing values
print("Name:", student["name"])

# Adding new key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# Looping through dictionary
print("Looping through dictionary:")
for key, value in student.items():
    print(key, ":", value)
