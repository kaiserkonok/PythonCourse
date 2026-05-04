# 🏗️ Classes & Objects: Blueprint for Data

<p align="center">
  <img src="https://img.shields.io/badge/class-Blueprint-blue?style=flat-square" alt="class">
  <img src="https://img.shields.io/badge/object-Instance-green?style=flat-square" alt="object">
  <img src="https://img.shields.io/badge/OOP-Paradigm-orange?style=flat-square" alt="OOP">
</p>

> ### 💡 A class is a blueprint. An object is the house you build from it. OOP lets you model real-world things in code.
> Learn how to create your own custom data types.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Define classes and create objects
- ✅ Understand the relationship between classes and objects
- ✅ Add attributes and methods to classes

---

## 🧠 Mental Model: A Blueprint

A **class** is like an architect's blueprint:

```
📐 Blueprint (Class)
   └── 🏠 House 1 (Object)
   └── 🏠 House 2 (Object)
   └── 🏠 House 3 (Object)
```

One blueprint can build many houses. Each house is unique but follows the same design.

---

## 📖 Basic Syntax

```python
class ClassName:
    """Docstring explains the class."""

    def __init__(self):
        """Constructor — runs when object is created."""
        pass

    def method(self):
        """A function that belongs to the class."""
        pass
```

### Creating Objects

```python
# Create an object
my_obj = ClassName()

# Call a method
my_obj.method()
```

---

## 📊 Class vs Object

| Concept | What it is | Example |
|---------|------------|---------|
| Class | Blueprint/Template | `Car` |
| Object | Instance of a class | `my_tesla`, `your_bmw` |
| Attribute | Data the object holds | `color`, `speed` |
| Method | Function the object can do | `drive()`, `stop()` |

---

## ⚠️ Common Mistakes

```
❌ Forgetting `self` in methods
   class Dog:
       def bark():  → Missing self!
           print("Woof!")
   def bark(self):  ← Correct

❌ Not calling the class
   my_obj = Dog  ← Just references the class
   my_obj = Dog()  ← Creates an instance

❌ Confusing class and object
   Dog.bark()  ← Wrong (bark needs an instance)
   my_dog.bark()  ← Correct

❌ Capitalizing incorrectly
   class myClass:  ← Should be CamelCase
   class MyClass:  ← Correct
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic Class

```python
class Dog:
    """A simple Dog class."""

    def bark(self):
        print("Woof! Woof!")

# Create objects
dog1 = Dog()
dog2 = Dog()

dog1.bark()  # Woof! Woof!
dog2.bark()  # Woof! Woof!
```

### 📌 Example 2 — Adding Attributes

```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age

    def describe(self):
        print(f"{self.name} is {self.age} years old")

my_dog = Dog("Buddy", 3)
my_dog.describe()  # Buddy is 3 years old
```

### 📌 Example 3 — Multiple Objects

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def honk(self):
        print(f"{self.brand} goes Beep!")

car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Blue")

car1.honk()  # Tesla goes Beep!
car2.honk()  # BMW goes Beep!
```

### 📌 Example 4 — Modifying Attributes

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

c = Counter()
c.increment()
c.increment()
print(f"Count: {c.count}")  # 2
```

### 📌 Example 5 — Type Checking

```python
class Cat:
    pass

class Dog:
    pass

cat = Cat()
dog = Dog()

print(isinstance(cat, Cat))  # True
print(isinstance(cat, Dog))  # False
print(type(cat))             # <class '__main__.Cat'>
```

### 📌 Example 6 — `self` Explained

```python
class Person:
    def __init__(self, name):
        self.name = name  # self.name = this object's name

    def greet(self):
        print(f"Hi, I'm {self.name}")

alice = Person("Alice")
bob = Person("Bob")

# self points to the calling object
alice.greet()  # self → alice
bob.greet()    # self → bob
```

---

## 🧪 Practice Exercise

1. Create a `Person` class with name and age attributes
2. Add a method that prints a greeting
3. Create two Person objects and call their methods
4. Add a method that checks if the person is an adult

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🏗️ **Class** | Blueprint for creating objects |
| 📦 **Object** | Instance of a class |
| 🔧 **`__init__`** | Constructor — runs on object creation |
| 🎯 **`self`** | Reference to the current object |
| 📝 **Attributes** | Data stored in the object |

---

## 🔗 Further Reading

- 📖 [Classes — Official Docs](https://docs.python.org/3/tutorial/classes.html)
- 🌟 [OOP in Python — Real Python](https://realpython.com/python3-object-oriented-programming/)
- 🔧 [Class vs Instance — docs](https://docs.python.org/3/tutorial/classes.html#class-objects)