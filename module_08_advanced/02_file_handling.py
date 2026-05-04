"""
File Handling (Reading & Writing Files)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""
import os

# Example 1 — Writing to a File
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Second line\n")

print("Written to output.txt")


# Example 2 — Reading a File
with open("output.txt", "r") as f:
    content = f.read()
    print(content)


# Example 3 — Reading Line by Line
# Create a sample file first
with open("lines.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

# Read line by line
with open("lines.txt", "r") as f:
    for line in f:
        print(line.strip())


# Example 4 — Appending to a File
with open("log.txt", "a") as f:
    f.write("New log entry\n")

with open("log.txt", "r") as f:
    print(f"Log: {f.read().strip()}")


# Example 5 — Working with CSV-like Data
# Write CSV-like data
with open("data.txt", "w") as f:
    f.write("Name,Age,City\n")
    f.write("Alice,25,NY\n")
    f.write("Bob,30,LA\n")

# Read and parse
with open("data.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 3:
            print(f"{parts[0]} is {parts[1]}, from {parts[2]}")


# Example 6 — Error Handling
try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("No permission to read!")
except Exception as e:
    print(f"Unexpected error: {e}")


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a file and write a few lines to it
# 2. Read the file back and print each line
# 3. Append a new line to the file
# 4. Handle the case where the file doesn't exist
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Create and write
filename = "practice.txt"
with open(filename, "w") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")

# 2. Read back
print("Reading file:")
with open(filename, "r") as f:
    for line in f:
        print(f"  {line.strip()}")

# 3. Append
with open(filename, "a") as f:
    f.write("Appended line\n")

# 4. Handle missing file
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File 'nonexistent.txt' not found")

# Cleanup demo files
for f in ["output.txt", "lines.txt", "log.txt", "data.txt", "practice.txt"]:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up {f}")

# Try modifying it:
# - Write a function that counts words in a file
def count_words(filepath):
    try:
        with open(filepath, "r") as f:
            text = f.read()
            return len(text.split())
    except FileNotFoundError:
        return 0

# Create temp file for testing
with open("word_count_test.txt", "w") as f:
    f.write("Hello world this is a test")

print(f"Word count: {count_words('word_count_test.txt')}")
os.remove("word_count_test.txt")
