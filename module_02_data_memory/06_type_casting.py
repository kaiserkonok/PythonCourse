# Code examples from "Type Casting" lesson

# Example 1: String to Integer
num_str = "42"
num_int = int(num_str)
print(num_int)       # 42
print(type(num_int))  # <class 'int'>

# Example 2: Integer to String
age = 25
age_str = str(age)
print(age_str)        # "25"
print(type(age_str))  # <class 'str'>

# Example 3: String to Float
price = float("19.99")
print(price)         # 19.99
print(type(price))  # <class 'float'>

# Example 4: Float to Integer (truncates decimal)
pi = 3.14159
print(int(pi))       # 3 (not 3.14!)

# Example 5: Integer to Boolean
print(bool(1))        # True
print(bool(0))        # False
print(bool(""))        # False (empty string)
print(bool("Hello"))  # True


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Convert string "100" to integer and multiply by 2
value = int("100") * 2
print(f"100 * 2 = {value}")

# 2. Convert integer 50 to string and concatenate with " dollars"
price = str(50) + " dollars"
print(price)

# 3. Try converting "hello" to integer and handle the error
try:
    result = int("hello")
except ValueError:
    print("Cannot convert 'hello' to integer - ValueError!")

# 4. Convert float 3.14159 to integer
pi = int(3.14159)
print(f"int(3.14159) = {pi}")