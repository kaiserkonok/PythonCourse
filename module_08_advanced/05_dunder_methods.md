# 🪄 Dunder Methods: Python's Magic Methods

<p align="center">
  <img src="https://img.shields.io/badge/__str__-String%20Rep-blue?style=flat-square" alt="str">
  <img src="https://img.shields.io/badge/__add__-Operator%20Overload-green?style=flat-square" alt="add">
  <img src="https://img.shields.io/badge/__len__-Length-orange?style=flat-square" alt="len">
</p>

> ### 💡 Dunder (double underscore) methods let your objects work with Python's built-in functions. Make your classes behave like native types.
> Master `__str__`, `__add__`, `__len__`, and more.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Understand what dunder methods are and why they matter
- ✅ Implement common dunder methods: `__str__`, `__repr__`, `__len__`, `__eq__`
- ✅ Overload operators with `__add__`, `__sub__`, etc.
- ✅ Make custom classes work with built-in functions

---

## 🧠 Mental Model: A Translator

Dunder methods are like a **translator** between your class and Python:

```
🏗️ Your class → 🔄 Dunder method → 🐍 Python built-in
   Vector      →    __add__      →    + operator
   Person      →    __str__      →    print()
   Cart        →    __len__      →    len()
```

Implement the right dunder methods, and your objects "just work" with Python.

---

## 📖 Common Dunder Methods

| Method | When it's called | What it does |
|--------|-----------------|--------------|
| `__init__` | Object creation | Initialize |
| `__str__` | `print(obj)` | User-friendly string |
| `__repr__` | `repr(obj)` | Developer string |
| `__len__` | `len(obj)` | Length |
| `__eq__` | `obj == other` | Equality |
| `__add__` | `obj + other` | Addition |
| `__getitem__` | `obj[key]` | Indexing |
| `__iter__` | `for x in obj` | Iteration |

---

## 📊 `__str__` vs `__repr__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"  # For users

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"  # For devs

p = Point(3, 4)
print(str(p))   # Point(3, 4)
print(repr(p))  # Point(x=3, y=4)
```

---

## ⚠️ Common Mistakes

```
❌ Returning wrong type from __str__
   def __str__(self):
       return 123  ← TypeError! Must return string
       return f"Value: {self.value}"  ← Correct

❌ Implementing __eq__ without __hash__
   If you override __eq__, objects become unhashable
   Can't use them in sets or as dict keys

❌ Incomplete operator overloading
   def __add__(self, other):
       return self.value + other  ← Only works one way
   # other + self won't work unless __radd__ is implemented

❌ Too many dunder methods
   Implement only what you need
   Don't overload every operator for no reason
```

---

## 💻 Code Examples

### 📌 Example 1 — `__str__` and `__repr__`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 25)
print(p)          # Alice, 25 years old
print(repr(p))    # Person('Alice', 25)
```

### 📌 Example 2 — `__len__`

```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

cart = ShoppingCart()
cart.add("Apple")
cart.add("Banana")
print(len(cart))  # 2
```

### 📌 Example 3 — `__eq__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)  # True
print(p1 == p3)  # False
```

### 📌 Example 4 — `__add__`

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
```

### 📌 Example 5 — `__getitem__` and `__setitem__`

```python
class MyList:
    def __init__(self, data):
        self._data = list(data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return len(self._data)

ml = MyList([10, 20, 30])
print(ml[0])    # 10
ml[1] = 99
print(ml[1])    # 99
print(len(ml))  # 3
```

### 📌 Example 6 — Making Objects Callable

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

---

## 🧪 Practice Exercise

1. Create a class with `__str__` and `__repr__`
2. Implement `__len__` for a custom collection
3. Add `__eq__` to compare two objects
4. Implement `__add__` for a custom math class

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🪄 **Dunder** | Double underscore methods enable built-in behavior |
| 📝 **`__str__`** | User-friendly string representation |
| 📝 **`__repr__`** | Developer-friendly string (debugging) |
| ➕ **Operators** | `__add__`, `__sub__`, etc. enable operator overloading |
| 📏 **Built-ins** | `__len__`, `__getitem__` make objects work with `len()`, `[]` |

---

## 🔗 Further Reading

- 📖 [Special Methods — Official Docs](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- 🌟 [Magic Methods — Real Python](https://realpython.com/python-magic-methods/)
- 🔧 [Emulating Container Types — docs](https://docs.python.org/3/reference/datamodel.html#emulating-container-types)