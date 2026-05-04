"""
Dictionaries (Key-Value Lookups)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic Dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(person["name"])   # Alice
print(person.get("age"))  # 25


# Example 2 — Adding and Removing
student = {"name": "Bob"}

student["age"] = 20
student["grade"] = "A"
print(student)  # {"name": "Bob", "age": 20, "grade": "A"}

del student["grade"]
print(student)  # {"name": "Bob", "age": 20}


# Example 3 — Iterating
scores = {"Math": 95, "Science": 88, "History": 92}

for subject, score in scores.items():
    print(f"{subject}: {score}")


# Example 4 — Merging Dictionaries
defaults = {"theme": "dark", "font": "12px"}
user_prefs = {"theme": "light", "language": "en"}

# Python 3.9+ merge operator
merged = defaults | user_prefs
print(merged)  # {"theme": "light", "font": "12px", "language": "en"}

# Older Python
merged = {**defaults, **user_prefs}


# Example 5 — Dictionary from Lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "NY"]

person = dict(zip(keys, values))
print(person)  # {"name": "Alice", "age": 25, "city": "NY"}


# Example 6 — Nested Dictionaries
company = {
    "Alice": {"role": "Engineer", "salary": 80000},
    "Bob": {"role": "Designer", "salary": 75000}
}

print(company["Alice"]["role"])  # Engineer


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a dictionary with 3 of your friends' names and ages
# 2. Add a new friend
# 3. Print all names using a loop
# 4. Use get() to safely access a missing key
# ═══════════════════════════════════════════════════════════════════════════════

# 1. Create dictionary
friends = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 28
}

# 2. Add new friend
friends["Diana"] = 22
print(f"Added Diana: {friends}")

# 3. Print all names
print("Friends:")
for name in friends.keys():
    print(f" - {name}")

# 4. Safe access
age = friends.get("Eve", "Not found")
print(f"Eve's age: {age}")

# Try modifying it:
# - Count word frequencies using a dictionary
text = "apple banana apple orange banana apple"
words = text.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(f"Word counts: {counts}")
