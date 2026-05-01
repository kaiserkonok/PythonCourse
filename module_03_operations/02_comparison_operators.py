# Code examples from "Comparison Operators" lesson

# Example 1: Basic comparisons
a = 10
b = 20
print(a == b)    # False
print(a != b)    # True
print(a > b)     # False
print(a < b)     # True
print(a >= 10)   # True
print(a <= 10)   # True

# Example 2: String comparisons
name1 = "Alice"
name2 = "alice"
print(name1 == name2)     # False (case-sensitive)
print(name1.lower() == name2)  # True

# Example 3: Mixed type comparison
print(10 == "10")        # False (int vs str)
print(10 == 10.0)       # True (int vs float)

# Example 4: In comparisons
text = "Hello Python"
print("Python" in text)  # True
print("python" in text)  # False (case-sensitive)

# Example 5: Checking ranges
score = 75
if 0 <= score <= 100:
    print("Valid score")
else:
    print("Invalid score")


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create variables for your age and a voting age (18)
my_age = 25
voting_age = 18

# 2. Check if you can vote
can_vote = my_age >= voting_age
print(f"Can vote: {can_vote}")

# 3. Check if two strings are equal
string1 = "hello"
string2 = "hello"
print(f"Strings equal: {string1 == string2}")

# 4. Use chained comparison to check if a number is between 1 and 100
number = 50
is_in_range = 1 <= number <= 100
print(f"Number {number} in range 1-100: {is_in_range}")