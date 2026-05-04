# 🌐 Namespace & Scope: Where Variables Live

<p align="center">
  <img src="https://img.shields.io/badge/Local-Inside%20Function-blue?style=flat-square" alt="local">
  <img src="https://img.shields.io/badge/Global-Everywhere-green?style=flat-square" alt="global">
  <img src="https://img.shields.io/badge/LEGB-Resolution%20Rule-orange?style=flat-square" alt="LEGB">
</p>

> ### 💡 Scope is like rooms in a house — variables in one room can't see into another. Global is the living room, local is a bedroom.
> Learn how Python decides which variable you're talking about.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Understand local vs global scope
- ✅ Use the LEGB rule to predict variable lookup
- ✅ Use `global` and `nonlocal` keywords safely

---

## 🧠 Mental Model: Rooms in a House

Scope is about **visibility**:

```
🏠 House (Global Scope)
├── 🛋️ Living Room — Everyone can see variables here
├── 🛏️ Bedroom 1 (Function A) — Only sees inside
└── 🛏️ Bedroom 2 (Function B) — Only sees inside
```

Variables created inside a function are **trapped** there — they can't be seen from outside.

---

## 📖 The LEGB Rule

Python looks for variables in this order:

1. **L**ocal — Inside current function
2. **E**nclosing — Inside outer functions (nested)
3. **G**lobal — Top level of the file
4. **B**uilt-in — Python's built-ins (`print`, `len`, etc.)

---

## 📊 Local vs Global

| Type | Where | Example |
|------|-------|---------|
| Local | Inside function | `x = 10` in `def foo()` |
| Global | Top level of file | `x = 10` at file start |

```python
x = 100  # Global

def foo():
    x = 50  # Local
    print(x)  # 50 (local wins)

foo()
print(x)  # 100 (global unchanged)
```

---

## ⚙️ `global` and `nonlocal`

```python
# `global` — modify a global variable
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1

# `nonlocal` — modify variable in outer (non-global) scope
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()
    print(count)  # 1
```

---

## ⚠️ Common Mistakes

```
❌ UnboundLocalError
   x = 10
   def foo():
       print(x)   ← OK
       x = 5      ← Python thinks x is local (because of assignment)
                  → UnboundLocalError: referenced before assignment

❌ Modifying globals without `global`
   count = 0
   def bad():
       count += 1  → UnboundLocalError
   def good():
       global count
       count += 1  ← OK

❌ Overusing globals
   Too many globals make code hard to debug
   Pass values as parameters instead!

❌ Shadowing built-ins
   list = [1, 2, 3]  ← Don't name variables after built-ins!
   x = list("hi")    → TypeError (list is now your variable)
```

---

## 💻 Code Examples

### 📌 Example 1 — Local Scope

```python
def greet():
    message = "Hello!"  # Local variable
    print(message)

greet()
# print(message)  → NameError (not visible outside)
```

### 📌 Example 2 — Global Scope

```python
name = "World"  # Global

def greet():
    print(f"Hello, {name}!")  # Can read globals

greet()  # Hello, World!
```

### 📌 Example 3 — Shadowing

```python
x = 100  # Global

def shadow():
    x = 50  # Local (shadows global)
    print(f"Local: {x}")

shadow()      # Local: 50
print(f"Global: {x}")  # Global: 100
```

### 📌 Example 4 — The `global` Keyword

```python
score = 0

def add_points(pts):
    global score
    score += pts

add_points(10)
add_points(5)
print(f"Score: {score}")  # Score: 15
```

### 📌 Example 5 — Nested Functions

```python
def outer():
    x = "outer"

    def inner():
        x = "inner"
        print(x)  # inner (local)

    inner()
    print(x)  # outer (enclosing)

outer()
```

### 📌 Example 6 — Closures

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

---

## 🧪 Practice Exercise

1. Create a function that uses a local variable
2. Try to access a local variable from outside and see the error
3. Use `global` to modify a global counter
4. Create a closure that remembers a value

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🏠 **LEGB Rule** | Local → Enclosing → Global → Built-in |
| 📍 **Local** | Variables inside functions are private to them |
| 🌐 **Global** | Visible everywhere, but avoid overusing |
| 🔑 **`global`** | Lets you modify a global variable inside a function |
| 🔄 **Closures** | Functions that remember values from their creation scope |

---

## 🔗 Further Reading

- 📖 [Scopes and Namespaces — Official Docs](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- 🌟 [LEGB Rule — Real Python](https://realpython.com/python-scope-legb-rule/)
- 🔧 [Closures — docs](https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python)