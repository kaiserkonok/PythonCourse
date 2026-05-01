# Code examples from "Strings" lesson

# Example 1: Basic string
greeting = "Hello, World!"
print(greeting)

# Example 2: String length
message = "Python"
print(len(message))  # 6

# Example 3: String repetition
echo = "Ha" * 3
print(echo)  # HaHaHa

# Example 4: Escape characters
quote = "She said, \"Hello!\""
print(quote)  # She said, "Hello!"

# Example 5: Multi-line string
poem = """Roses are red,
Violets are blue,
Python is fun,
And so are you!"""
print(poem)


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a string with your full name
full_name = "Alice Smith"

# 2. Print just your first name (using slicing)
first_name = full_name[:5]
print(f"First name: {first_name}")

# 3. Print the length of your name
print(f"Length: {len(full_name)}")

# 4. Convert your name to uppercase
print(f"Uppercase: {full_name.upper()}")

# 5. Create an f-string combining your name and age
age = 25
print(f"My name is {full_name} and I am {age} years old")