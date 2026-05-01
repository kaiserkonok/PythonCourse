# Code examples from "File Handling" lesson

# Example 1: Read entire file
# Uncomment to test:
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# Example 2: Read line by line
# with open("example.txt", "r") as file:
#     for line in file:
#         print(line, end="")

# Example 3: Write to file
# Uncomment to test:
# with open("output.txt", "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is line 2\n")

# Example 4: Append to file
# with open("log.txt", "a") as file:
#     file.write("New log entry\n")

# Example 5: Read all lines into list
# with open("example.txt", "r") as file:
#     lines = file.readlines()
#     for i, line in enumerate(lines):
#         print(f"{i}: {line}", end="")


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Write text to a file
with open("test_file.txt", "w") as file:
    file.write("Hello from Python!\n")
    file.write("Learning file handling.\n")

print("File written!")

# 2. Read the file back
with open("test_file.txt", "r") as file:
    content = file.read()
    print(f"Content:\n{content}")

# 3. Append more text
with open("test_file.txt", "a") as file:
    file.write("Appended line.\n")

print("After append:")
with open("test_file.txt", "r") as file:
    print(file.read())

# 4. Handle missing file gracefully
import os

def read_safely(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read()
    else:
        return "File not found"

print(read_safely("nonexistent.txt"))
print(read_safely("test_file.txt"))