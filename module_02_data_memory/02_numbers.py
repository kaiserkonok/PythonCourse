# Code examples from "Numbers (Int, Float, Complex)" lesson

# Example 1: Integer operations
a = 10
b = 3
print(a + b)    # 13 (addition)
print(a - b)    # 7  (subtraction)
print(a * b)    # 30 (multiplication)
print(a / b)    # 3.333... (division)
print(a // b)   # 3  (floor division)
print(a % b)    # 1  (modulus/remainder)
print(a ** b)   # 1000 (exponent)

# Example 2: Float operations
x = 10.5
y = 2.0
print(x + y)    # 12.5
print(x * y)    # 21.0

# Example 3: Mixed int and float
i = 10   # int
f = 2.5  # float
print(i + f)    # 12.5 (int becomes float automatically)

# Example 4: Complex numbers
c1 = 3 + 4j
c2 = 1 + 2j
print(c1 + c2)  # (4+6j)
print(c1 * c2)  # (-5+10j)

# Example 5: Accessing complex parts
c = 3 + 4j
print(c.real)   # 3.0 (real part)
print(c.imag)   # 4.0 (imaginary part)


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create an integer variable for your age
my_age = 25

# 2. Create a float variable for your height in meters
my_height = 1.75

# 3. Calculate your age in 10 years
age_in_10_years = my_age + 10

# 4. Print the result
print(f"Current age: {my_age}, Height: {my_height}m")
print(f"In 10 years, I will be {age_in_10_years} years old")

# Bonus: Create a complex number
complex_num = 5 + 3j
print(f"Complex: {complex_num}")
print(f"Real part: {complex_num.real}")
print(f"Imaginary part: {complex_num.imag}")