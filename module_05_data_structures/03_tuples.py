# Code examples from "Tuples" lesson

# Example 1: Create tuple
person = ("Alice", 25, "NYC")
print(person)  # ("Alice", 25, "NYC")

# Example 2: Tuple without parentheses
coords = 10, 20, 30
print(coords)  # (10, 20, 30)

# Example 3: Single element tuple (note the comma!)
single = (5,)
print(single)  # (5,)

# Example 4: Unpacking
point = (10, 20, 30)
x, y, z = point
print(f"x={x}, y={y}, z={z}")

# Example 5: Tuple in functions (return multiple values)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

result = get_stats([1, 2, 3])
print(result)  # (1, 3, 6)
min_val, max_val, total = result
print(f"Min: {min_val}, Max: {max_val}, Total: {total}")


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a tuple with your name, age, city
my_info = ("Alice", 25, "New York")
print(f"My info: {my_info}")

# 2. Unpack it into 3 variables
name, age, city = my_info
print(f"Name: {name}, Age: {age}, City: {city}")

# 3. Try to modify an element (see the error!)
# my_info[0] = "Bob"  # This will raise TypeError!
# Uncomment the line above to see the error

# 4. Return multiple values from a function
def get_name_info():
    return "Alice", 25, "NYC"

result = get_name_info()
print(f"Result: {result}")