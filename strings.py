# Python Strings Example

text = "Hello Python"

print("Original text:", text)

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Replace word
new_text = text.replace("Python", "World")
print("Replaced text:", new_text)

# String length
print("Length of text:", len(text))

# Loop through string
print("Characters in text:")
for char in text:
    print(char)
