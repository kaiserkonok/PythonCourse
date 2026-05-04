# 🎭 Polymorphism: Many Forms, One Interface

<p align="center">
  <img src="https://img.shields.io/badge/Polymorphism-Many%20Forms-blue?style=flat-square" alt="Polymorphism">
  <img src="https://img.shields.io/badge/Override-Same%20Name-green?style=flat-square" alt="Override">
  <img src="https://img.shields.io/badge/Flexible-Plug%20and%20Play-orange?style=flat-square" alt="Flexible">
</p>

> ### 💡 Polymorphism means "many forms." One method name, different behaviors depending on the object. Like a universal remote — same button, different actions per device.
> Learn how to write flexible code that works with many types.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Understand polymorphism and why it matters
- ✅ Override methods in child classes
- ✅ Write functions that work with multiple types
- ✅ Use duck typing in Python

---

## 🧠 Mental Model: A Universal Remote

Polymorphism is like a **universal remote**:

```
📱 Remote (Interface)
   └── 🔘 "Power" button
       ├── 📺 TV → Turns on screen
       ├── 🔊 Speaker → Starts playing
       └── 💡 Light → Turns on bulb
```

Same button (`power()`), different actions depending on the device.

---

## 📖 How It Works

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Same method call, different results
for animal in [Dog(), Cat()]:
    print(animal.speak())
```

---

## 📊 Types of Polymorphism

| Type | How it works | Example |
|------|-------------|---------|
| **Method Override** | Child replaces parent method | `Dog.speak()` vs `Cat.speak()` |
| **Duck Typing** | "If it quacks, it's a duck" | Any object with `speak()` works |
| **Operator Overloading** | Operators work on custom types | `+` for vectors, strings |

---

## ⚠️ Common Mistakes

```
❌ Checking types instead of using polymorphism
   if isinstance(obj, Dog):
       obj.bark()
   elif isinstance(obj, Cat):
       obj.meow()
   ← Just call obj.speak()!

❌ Forgetting to override
   class Child(Parent):
       pass  ← Uses parent's method, not polymorphic

❌ Inconsistent interfaces
   class Dog:
       def speak(self): ...
   class Cat:
       def talk(self): ...  ← Different name, breaks polymorphism!

❌ Overcomplicating
   Use simple polymorphism first, design patterns later
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic Polymorphism

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Tweet!"

# Works with any object that has speak()
for animal in [Dog(), Cat(), Bird()]:
    print(animal.speak())
```

### 📌 Example 2 — Function Polymorphism

```python
def make_it_speak(animal):
    """Works with ANY object that has speak()."""
    print(animal.speak())

make_it_speak(Dog())   # Woof!
make_it_speak(Cat())   # Meow!
make_it_speak(Bird())  # Tweet!
```

### 📌 Example 3 — Inheritance Polymorphism

```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

shapes = [Rectangle(5, 3), Circle(4), Rectangle(2, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}")
```

### 📌 Example 4 — Duck Typing

```python
# "If it walks like a duck and quacks like a duck, it's a duck"

def process(item):
    """Works with anything that has process() method."""
    item.process()

class File:
    def process(self):
        print("Processing file...")

class Email:
    def process(self):
        print("Processing email...")

process(File())   # Processing file...
process(Email())  # Processing email...
```

### 📌 Example 5 — Operator Overloading

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # (4, 6)
```

### 📌 Example 6 — len() Polymorphism

```python
# Built-in functions use polymorphism too!

print(len("hello"))        # 5 (string)
print(len([1, 2, 3]))      # 3 (list)
print(len({"a": 1, "b": 2}))  # 2 (dict)

# All work because they implement __len__
```

---

## 🧪 Practice Exercise

1. Create two classes with the same method name but different behavior
2. Write a function that accepts either class
3. Use `+` operator on a custom class
4. Create a list of different objects and call the same method on each

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🎭 **Polymorphism** | Same method name, different behaviors |
| 🦆 **Duck typing** | If it has the method, it works |
| 🔄 **Override** | Child classes replace parent methods |
| ➕ **Operators** | `+`, `-`, etc. work via dunder methods |
| 🧩 **Flexible** | Write code that works with many types |

---

## 🔗 Further Reading

- 📖 [Polymorphism — Official Docs](https://docs.python.org/3/tutorial/classes.html#inheritance)
- 🌟 [Duck Typing — Real Python](https://realpython.com/lessons/duck-typing/)
- 🔧 [Operator Overloading — docs](https://docs.python.org/3/reference/datamodel.html#special-method-names)