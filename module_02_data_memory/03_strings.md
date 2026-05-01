# The Primitive Types: Strings (Text Processing)

## Learning Objectives

- Create and use strings in Python
- Understand string indexing and slicing
- Use common string methods

## What is a String?

A string is a **sequence of characters** (text data).

- Created with **single quotes** 'hello'
- Or **double quotes** "hello"
- Or **triple quotes** for multi-line strings

```python
name = "Alice"          # double quotes
message = 'Hello!'      # single quotes
story = """This is a   # triple quotes
multi-line string."""
```

## String Indexing: Accessing Characters

Each character has a position (index):
```
String:  H  e  l  l  o
Index:   0  1  2  3  4
```

```python
word = "Python"
print(word[0])   # P (first character)
print(word[1])   # y (second)
print(word[-1])  # n (last character)
print(word[-2])  # o (second to last)
```

## String Slicing: Getting Substrings

```python
language = "Python"
print(language[0:3])   # Pyt (positions 0, 1, 2)
print(language[1:4])    # yth (positions 1, 2, 3)
print(language[:3])     # Pyt (start to position 3)
print(language[3:])    # hon (position 3 to end)
print(language[:])     # Python (entire string)
```

```
language = "P  y  t  h  o  n"
          0  1  2  3  4  5
         
[0:3] → P  y  t
[1:4] → y  t  h
[:3]  → P  y  t
[3:]  → h  o  n
```

## Common String Methods

```python
text = "  Hello, Python!  "

# Removing whitespace
print(text.strip())           # "Hello, Python!"

# Changing case
print(text.lower())           # "  hello, python!  "
print(text.upper())           # "  HELLO, PYTHON!  "
print(text.title())           # "  Hello, Python!  "

# Finding and replacing
print(text.replace("Python", "World"))  # "  Hello, World!  "
print(text.find("Python"))              # 9 (position)

# Checking content
print("hello" in text.lower())          # True
print(text.isdigit())                   # False
print("123".isdigit())                   # True
```

## String Concatenation

```python
# Using + operator
first = "Hello"
second = "World"
print(first + " " + second)  # "Hello World"

# Using f-strings (recommended)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")
```

## Code Examples

```python
# Example 1: Basic string
greeting = "Hello, World!"
print(greeting)

# Example 2: String length
message = "Python"
print(len(message))  # 6

# Example 3: String repetition
echo = "Ha" * 3
print(echo)  # HaHaHa

# Example 4: Escape characters
quote = "She said, \"Hello!\""
print(quote)  # She said, "Hello!"

# Example 5: Multi-line string
poem = """Roses are red,
Violets are blue,
Python is fun,
And so are you!"""
print(poem)
```

## Key Takeaways

1. **Strings** are text enclosed in quotes
2. **Indexing** accesses single characters [0], [-1]
3. **Slicing** gets substrings [0:3], [:3], [3:]
4. **Methods** modify or analyze strings (.upper(), .strip())
5. **f-strings** combine text and variables cleanly

## Practice Exercise

1. Create a string with your full name
2. Print just your first name (using slicing)
3. Print the length of your name
4. Convert your name to uppercase
5. Create an f-string combining your name and age