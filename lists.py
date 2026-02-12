# Python Lists Example

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# Accessing elements
print("First element:", numbers[0])

# Adding element
numbers.append(60)
print("After adding 60:", numbers)

# Removing element
numbers.remove(30)
print("After removing 30:", numbers)

# Loop through list
print("Looping through list:")
for num in numbers:
    print(num)
