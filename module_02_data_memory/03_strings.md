# The Primitive Types: Strings (Text Processing)

## Learning Objectives

By the end of this lesson, you will be able to:

- Create and manipulate text data using Python strings
- Access individual characters and substrings using indexing and slicing
- Use common string methods to transform and analyze text

---

## Mental Model: A Beaded Necklace

A string is a sequence of characters — think of it like a **beaded necklace**:

```
  ┌───┬───┬───┬───┬───┬───┐
  │ P │ y │ t │ h │ o │ n │
  └───┴───┴───┴───┴───┴───┘
   0   1   2   3   4   5  ← positions (indices)
```

Each character has a position. You can access any character by its position — like picking a bead from the necklace.

---

## Creating Strings

Strings are text enclosed in quotes. Python gives you three options:

```python
# Single quotes
name = 'Alice'

# Double quotes
name = "Alice"

# Triple quotes (for multi-line strings)
poem = """Roses are red,
Violets are blue."""
```

### Which Quotes to Use?

| Situation | Recommendation |
|-----------|---------------|
| Simple text | Either `'` or `"` — pick one and stay consistent |
| Text with apostrophes | `"I'm happy"` (use double quotes) |
| Text with double quotes | `'She said "hello"'` (use single quotes) |
| Multi-line text | Triple quotes `"""..."""` |

---

## Indexing: Access Individual Characters

Each character has a position (index), starting at 0:

```
String:  P  y  t  h  o  n
Index:   0  1  2  3  4  5
```

```python
word = "Python"

print(word[0])   # P (first character)
print(word[1])   # y (second character)
print(word[-1])  # n (last character)
print(word[-2])  # o (second to last)
```

Negative indices count from the end:

```
String:  P  y  t  h  o  n
Index:  -6 -5 -4 -3 -2 -1
```

---

## Slicing: Get Substrings

Slicing lets you grab a portion of a string:

```python
word = "Python"

print(word[0:3])   # "Pyt" (positions 0, 1, 2)
print(word[1:4])   # "yth" (positions 1, 2, 3)
print(word[:3])    # "Pyt" (start to position 3)
print(word[3:])    # "hon" (position 3 to end)
print(word[:])     # "Python" (entire string)
print(word[::-1])  # "nohtyP" (reverse!)
```

**Slicing rule:** `[start:end]` — includes `start`, excludes `end`.

```
word = "P  y  t  h  o  n"
       0  1  2  3  4  5

[0:3] → P  y  t     (stops before position 3)
[3:]  → h  o  n     (from position 3 to end)
```

---

## String Methods: Transform Text

Strings come with built-in methods — functions you call on the string itself:

| Method | What it does | Example |
|--------|-------------|---------|
| `.upper()` | All uppercase | `"hello" → "HELLO"` |
| `.lower()` | All lowercase | `"HELLO" → "hello"` |
| `.title()` | Title case | `"hello world" → "Hello World"` |
| `.strip()` | Remove whitespace | `"  hi  " → "hi"` |
| `.replace(a, b)` | Replace text | `"hi" → "hello"` |
| `.find(x)` | Find position | `"Python" → 0` |
| `.split(sep)` | Split into list | `"a,b,c" → ["a","b","c"]` |
| `.isdigit()` | Check if digits | `"123" → True` |

---

## Common Mistakes

```
❌ Strings are immutable — you can't change them in place
   s = "hello"
   s[0] = "H"   → TypeError (can't change)
   s = "Hello"  ← Create a new string instead

❌ Forgetting quotes around text
   print(hello)    → NameError (Python looks for a variable)
   print("hello")  ← Correct

❌ Confusing slicing bounds
   "Python"[0:3]  → "Pyt" (not "Pyth"!)
   Remember: end is excluded

❌ Forgetting that strings are case-sensitive
   "Python" == "python"  → False
```

---

## Code Examples

### Example 1 — Basic String

```python
greeting = "Hello, World!"
print(greeting)  # Hello, World!
```

### Example 2 — String Length

```python
message = "Python"
print(len(message))  # 6
```

### Example 3 — String Concatenation & Repetition

```python
# Combine strings with +
first = "Hello"
second = "World"
print(first + " " + second)  # Hello World

# Repeat strings with *
echo = "Ha" * 3
print(echo)  # HaHaHa
```

### Example 4 — Indexing

```python
word = "Python"

print(word[0])    # P (first)
print(word[1])    # y (second)
print(word[-1])   # n (last)
print(word[-2])   # o (second to last)
```

### Example 5 — Slicing

```python
language = "Python"

print(language[0:3])   # "Pyt"
print(language[1:4])   # "yth"
print(language[:3])    # "Pyt" (same as [0:3])
print(language[3:])    # "hon" (from 3 to end)
print(language[::-1])  # "nohtyP" (reverse)
```

### Example 6 — String Methods

```python
text = "  Hello, Python!  "

# Transform
print(text.strip())           # "Hello, Python!"
print(text.upper())           # "  HELLO, PYTHON!  "
print(text.lower())           # "  hello, python!  "
print(text.title())           # "  Hello, Python!  "

# Search and replace
print(text.replace("Python", "World"))  # "  Hello, World!  "
print("hello" in text.lower())           # True
```

---

## Practice Exercise

1. Create a string with your full name
2. Print just your first name (using slicing)
3. Print the length of your name
4. Convert your name to uppercase
5. Create an f-string combining your name and age

---

## Key Takeaways

- **Strings are sequences** — each character has a position (index)
- **Indexing starts at 0** — `"Python"[0]` is `'P'`
- **Negative indices** count from the end — `"Python"[-1]` is `'n'`
- **Slicing `[start:end]`** — includes start, excludes end
- **Strings are immutable** — you create new strings, you don't modify old ones
- **f-strings** are the Pythonic way to combine text and variables

---

## Further Reading

- [Python String Methods — Official Docs](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [String Formatting — Real Python](https://realpython.com/python-string-formatting/) — f-strings deep dive
- [Unicode in Python](https://docs.python.org/3/howto/unicode.html) — For when you need emoji and special characters