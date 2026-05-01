# Type Casting: Converting Data Between Types

## Learning Objectives

- Understand explicit type conversion
- Convert between strings, integers, and floats
- Handle conversion errors gracefully

## What is Type Casting?

Type casting (or type conversion) is **changing one data type to another**.

- Sometimes we need to convert to perform operations
- String "10" is different from integer 10!

```
"10" + "5"  → "105"  (string concatenation)
10 + 5     → 15     (numeric addition)
```

## Explicit Type Conversion

Python provides functions to convert types:

| Function | Converts To | Example |
|----------|-------------|----------|
| int() | Integer | int("10") → 10 |
| float() | Float | float("3.14") → 3.14 |
| str() | String | str(10) → "10" |
| bool() | Boolean | bool(1) → True |

## Code Examples

```python
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
print(type(price))   # <class 'float'>

# Example 4: Float to Integer (truncates decimal)
pi = 3.14159
print(int(pi))       # 3 (not 3.14!)

# Example 5: Integer to Boolean
print(bool(1))        # True
print(bool(0))        # False
print(bool(""))        # False (empty string)
print(bool("Hello"))  # True
```

## Common Conversions

```python
# String + Integer concatenation
name = "Alice"
age = 25
print(name + " is " + str(age) + " years old")

# Integer arithmetic from input
a = int("10")
b = int("20")
print(a + b)  # 30

# Float arithmetic from string
price = float("19.99")
quantity = 3
total = price * quantity
print(f"Total: ${total}")  # Total: $59.97
```

## Handling Invalid Conversions

```python
# ❌ Error: Cannot convert this to integer
try:
    result = int("hello")
except ValueError:
    print("Cannot convert 'hello' to integer")

# ✅ Valid: Convert with base
# int(string, base) for different number systems
binary = int("1010", 2)  # Binary to decimal
print(binary)          # 10

hex_num = int("FF", 16)  # Hexadecimal to decimal
print(hex_num)          # 255
```

## Code Examples

```python
# Example 1: User input to number calculation
user_input = "100"
user_number = int(user_input)
print(user_number * 2)  # 200

# Example 2: Multiple type conversions
value = "42"
result = float(int(value))  # String → Int → Float
print(result)              # 42.0

# Example 3: Boolean conversion
print(bool(0))           # False
print(bool(1))           # True
print(bool(-1))          # True (any non-zero is True)

# Example 4: List to string
my_list = ["a", "b", "c"]
result = "".join(my_list)
print(result)  # abc
```

## Key Takeaways

1. **int()** converts to integer
2. **float()** converts to float
3. **str()** converts to string
4. **Truncation** - int("3.9") becomes 3, not 4
5. **Validation** - always check if conversion is valid

## Practice Exercise

1. Convert string "100" to integer and multiply by 2
2. Convert integer 50 to string and concatenate with " dollars"
3. Try converting "hello" to integer and handle the error
4. Convert float 3.14159 to integer