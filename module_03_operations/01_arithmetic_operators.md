# Arithmetic Operators: Basic Math, Floor Division, and Modulo

## Learning Objectives

- Perform basic arithmetic operations
- Understand floor division (//) vs regular division (/)
- Use the modulo operator (%) for remainders

## The Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| + | Addition | 10 + 5 | 15 |
| - | Subtraction | 10 - 5 | 5 |
| * | Multiplication | 10 * 5 | 50 |
| / | Division | 10 / 5 | 2.0 |
| // | Floor Division | 10 // 3 | 3 |
| % | Modulo | 10 % 3 | 1 |
| ** | Exponent | 2 ** 3 | 8 |

## Division vs Floor Division

The difference between / and // is crucial:

```python
# Regular division (/)
print(10 / 3)       # 3.333333... (float)
print(10 / 2)       # 5.0 (always float)

# Floor division (//)
print(10 // 3)      # 3 (rounds down)
print(10 // 2)       # 5 (integer, rounded down)
```

## The Modulo Operator (%)

Returns the **remainder** after division:

```python
# Modulo - what's left over?
print(10 % 3)       # 1 (10 = 3*3 + 1)
print(10 % 2)       # 0 (10 is even)
print(10 % 4)       # 2 (10 = 4*2 + 2)
```

```
10 ÷ 3 = 3 with remainder 1
         └───┬───┘
         10 % 3 = 1
```

## Common Use Cases

```python
# Check if even or odd
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Get last digit
phone = "1234567890"
last_digit = int(phone) % 10
print(last_digit)  # 0

# Wrap around
position = 10
max_position = 8
wrapped = position % max_position
print(wrapped)  # 2 (wraps from 10 back to 2)
```

## Code Examples

```python
# Example 1: Basic operations
a = 15
b = 4
print(a + b)     # 19
print(a - b)     # 11
print(a * b)     # 60
print(a / b)     # 3.75
print(a // b)    # 3
print(a % b)     # 3
print(a ** b)    # 50625 (15^4)

# Example 2: Order of operations (PEMDAS)
result = 2 + 3 * 4
print(result)  # 14 (not 20)

# Use parentheses to control
result = (2 + 3) * 4
print(result)  # 20

# Example 3: Compound assignments
x = 10
x += 5          # x = x + 5
print(x)        # 15

x -= 3          # x = x - 3
print(x)        # 12

x *= 2          # x = x * 2
print(x)        # 24

# Example 4: Practical uses
seconds = 185
minutes = seconds // 60
remaining_seconds = seconds % 60
print(f"{minutes} min {remaining_seconds} sec")  # 3 min 5 sec
```

## Key Takeaways

1. **+ - * /** - Basic math operations
2. **/** - Always returns float
3. **//** - Floor division (rounds down)
4. **%** - Returns remainder
5. **Use // and % together** - Get quotient and remainder

## Practice Exercise

1. Use floor division to calculate how many complete hours in 185 minutes
2. Use modulo to get the remaining minutes
3. Calculate 2^10 using **
4. Check if 42 is even or odd using modulo