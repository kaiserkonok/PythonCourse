# Code examples from "Logical Operators" lesson

# Example 1: Basic and
is_sunny = True
is_warm = True
is_good_weather = is_sunny and is_warm
print(f"Good weather: {is_good_weather}")  # True

# Example 2: Basic or
is_weekend = False
is_holiday = True
can_rest = is_weekend or is_holiday
print(f"Can rest: {can_rest}")  # True

# Example 3: Not
is_raining = False
print(not is_raining)  # True

# Example 4: Complex condition
age = 16
has_parent = True
can_watch_movie = age >= 17 or has_parent
print(f"Can watch: {can_watch_movie}")  # True

# Example 5: Short-circuit evaluation
x = 5
result = x > 10 and x / 0  # Won't divide by 0!
print(result)  # False (stops at first condition)


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create two booleans: is_student (True), has_id (True)
is_student = True
has_id = True

# 2. Use and to check both conditions
both = is_student and has_id
print(f"Both conditions: {both}")

# 3. Use or to check at least one condition
either = is_student or has_id
print(f"Either condition: {either}")

# 4. Use not to invert is_student
not_student = not is_student
print(f"Not student: {not_student}")

# 5. Create a complex condition with and, or, not
age = 20
is_employed = True
can_get_credit = (age >= 18 or is_student) and is_employed
print(f"Can get credit: {can_get_credit}")