# The Primitive Types: Numbers (Int, Float, Complex)

## Learning Objectives

- Understand integer, float, and complex number types
- Know when to use each number type
- Perform math operations with different number types

## The Three Numeric Types

### Integer (int)
- Whole numbers (no decimal points)
- Positive or negative
- Examples: 42, -10, 0, 1000

### Float (float)
- Numbers with decimal points
- Also called "floating-point" numbers
- Examples: 3.14, -0.5, 100.0

### Complex (complex)
- Numbers with real and imaginary parts
- Format: a + bj
- Used in advanced math and signal processing

```
┌─────────────────────────────────────┐
│        Numeric Types in Python       │
├─────────────────────────────────────┤
│  int    → 42, -10, 0                │
│  float  → 3.14, -0.5, 100.0         │
│  complex → 3+4j, 1-2j              │
└─────────────────────────────────────┘
```

## When to Use Each Type

| Use case | Type |
|----------|------|
| Counting items | int |
| Money/currency | float (or int for cents) |
| Temperatures | float |
| Complex math | complex |
| Boolean (1/0) | int (but use bool!) |

## Checking Type with type()

```python
x = 42
print(type(x))  # <class 'int'>

y = 3.14
print(type(y))  # <class 'float'>

z = 3 + 4j
print(type(z))  # <class 'complex'>
```

## Code Examples

```python
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
```

## Common Mistakes

```python
# ❌ Wrong: Using float for exact math (money)
price = 0.1 + 0.2
print(price)  # 0.30000000000000004 (floating-point error)

# ✅ Better: Use int for money (cents)
price_cents = 10 + 20  # cents
print(price_cents)     # 30 cents (exact)

# ❌ Wrong: Accidental float division
a = 5
b = 2
print(a / b)   # 2.5 (Python 3 always does float division)

# ✅ Best: Explicit floor division when needed
print(a // b)  # 2 (floor division)
print(a % b)   # 1 (remainder)
```

## Key Takeaways

1. **int** = whole numbers (42, -10, 0)
2. **float** = decimal numbers (3.14, -0.5)
3. **complex** = real + imaginary (3 + 4j)
4. **Mixed operations** = int converts to float automatically
5. **For money**: use int (cents) to avoid floating-point errors

## Practice Exercise

1. Create an integer variable for your age
2. Create a float variable for your height in meters
3. Calculate your age in 10 years
4. Print the result

Bonus: Create a complex number and print its real and imaginary parts.