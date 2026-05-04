# 🔧 Constructors: Initializing Objects

<p align="center">
  <img src="https://img.shields.io/badge/__init__-Constructor-blue?style=flat-square" alt="init">
  <img src="https://img.shields.io/badge/Self-Instance%20Ref-green?style=flat-square" alt="self">
  <img src="https://img.shields.io/badge/Setup-Object%20State-orange?style=flat-square" alt="Setup">
</p>

> ### 💡 The constructor is the setup crew — it prepares your object with all the data it needs before you use it.
> Master `__init__` and learn how to give objects their initial state.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use `__init__` to initialize object attributes
- ✅ Understand the role of `self` in constructors
- ✅ Set default values and validate inputs

---

## 🧠 Mental Model: A Factory Assembly Line

The constructor is like the **setup station** on an assembly line:

```
🏭 Factory (Class)
   → [Station 1: Set name]
   → [Station 2: Set age]
   → [Station 3: Set defaults]
   → ✅ Product ready (Object created)
```

Every object goes through the same setup when it's born.

---

## 📖 The Constructor

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

- **`__init__`** runs automatically when you create an object
- **`self`** refers to the object being created
- **Parameters** after `self` become arguments when creating objects

---

## 📊 Default Values & Validation

```python
class Account:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Balance can't be negative")
        self.owner = owner
        self.balance = balance
```

---

## ⚠️ Common Mistakes

```
❌ Returning from __init__
   def __init__(self):
       return self  ← __init__ must return None!

❌ Forgetting to call super().__init__()
   In inheritance, forgetting parent constructor

❌ Not using self for attributes
   def __init__(self, name):
       name = name  ← Creates local variable, not attribute!
       self.name = name  ← Correct

❌ Mutable default arguments
   def __init__(self, items=[]):  ← Shared across instances!
   def __init__(self, items=None):
       self.items = items or []  ← Safe
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic Constructor

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(10, 5)
print(f"Size: {rect.width}x{rect.height}")
```

### 📌 Example 2 — Default Values

```python
class User:
    def __init__(self, username, role="user"):
        self.username = username
        self.role = role

admin = User("alice", "admin")
guest = User("bob")  # Uses default role

print(f"{admin.username} is {admin.role}")
print(f"{guest.username} is {guest.role}")
```

### 📌 Example 3 — Validation

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.owner = owner
        self.balance = balance

# account = BankAccount("Alice", -100)  # ValueError!
account = BankAccount("Alice", 500)
print(f"{account.owner}: ${account.balance}")
```

### 📌 Example 4 — Computed Attributes

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = 3.14159 * radius ** 2

c = Circle(5)
print(f"Radius: {c.radius}, Diameter: {c.diameter}, Area: {c.area:.2f}")
```

### 📌 Example 5 — `__str__` for Display

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"

item = Product("Laptop", 999)
print(item)  # Laptop - $999
```

### 📌 Example 6 — Optional Parameters

```python
class Book:
    def __init__(self, title, author, year=None, genre="Unknown"):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

b1 = Book("1984", "Orwell", 1949, "Dystopian")
b2 = Book("Dune", "Herbert")  # year=None, genre="Unknown"

print(f"{b1.title} ({b1.year}) - {b1.genre}")
print(f"{b2.title} - {b2.genre}")
```

---

## 🧪 Practice Exercise

1. Create a `Student` class with name, grade, and optional major
2. Add validation to ensure grade is between 0 and 100
3. Create a `__str__` method for nice printing
4. Test with multiple objects

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🔧 **`__init__`** | Runs automatically on object creation |
| 🎯 **`self`** | Always the first parameter — refers to the instance |
| 🛡️ **Validation** | Check inputs in constructor to catch errors early |
| 🛡️ **Defaults** | Use defaults for optional parameters |
| 📝 **`__str__`** | Controls how objects display with `print()` |

---

## 🔗 Further Reading

- 📖 [Class Instances — Official Docs](https://docs.python.org/3/tutorial/classes.html#class-objects)
- 🌟 [Magic Methods — Real Python](https://realpython.com/python-magic-methods/)
- 🔧 [__init__ vs __new__ — docs](https://docs.python.org/3/reference/datamodel.html#object.__init__)