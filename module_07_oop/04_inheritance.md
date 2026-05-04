# 🧬 Inheritance: Reusing and Extending Classes

<p align="center">
  <img src="https://img.shields.io/badge/inherit-Extend-blue?style=flat-square" alt="inherit">
  <img src="https://img.shields.io/badge/super()-Parent%20Call-green?style=flat-square" alt="super">
  <img src="https://img.shields.io/badge/DRY-Reuse%20Code-orange?style=flat-square" alt="DRY">
</p>

> ### 💡 Inheritance is like family traits — children get features from their parents but can also develop their own.
> Learn how to create class hierarchies and reuse code.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Create child classes that inherit from parent classes
- ✅ Use `super()` to call parent methods
- ✅ Override methods in child classes
- ✅ Understand the difference between `is-a` and `has-a`

---

## 🧠 Mental Model: A Family Tree

Inheritance is like a **family tree**:

```
👴 Animal (Parent)
   ├── 🐕 Dog (Child) — inherits "breathe", adds "bark"
   ├── 🐈 Cat (Child) — inherits "breathe", adds "meow"
   └── 🐦 Bird (Child) — inherits "breathe", adds "fly"
```

Children get all parent features automatically, plus their own unique stuff.

---

## 📖 Basic Syntax

```python
class Parent:
    def __init__(self):
        pass

class Child(Parent):  # Inherits from Parent
    def __init__(self):
        super().__init__()  # Call parent constructor
```

---

## 📊 Inheritance Concepts

| Concept | What it does | Example |
|---------|-------------|---------|
| **Inherit** | Get parent's attributes/methods | `class Dog(Animal)` |
| **Override** | Replace parent method | Redefine `speak()` |
| **Extend** | Add new methods | `def fetch()` |
| **super()** | Call parent method | `super().__init__()` |

---

## ⚠️ Common Mistakes

```
❌ Forgetting to call super().__init__()
   class Child(Parent):
       def __init__(self, name):
           self.name = name  ← Parent's __init__ never runs!
           super().__init__() ← Should be first

❌ Inheriting from wrong type
   class Dog(list):  ← Only inherit when "is-a" relationship exists
       pass

❌ Diamond inheritance confusion
   Multiple inheritance can get complex — use composition instead

❌ Not using isinstance() correctly
   isinstance(dog, Animal)  ← True (dog is an Animal)
   isinstance(animal, Dog)  ← False (not all Animals are Dogs)
```

---

## 💻 Code Examples

### 📌 Example 1 — Basic Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(f"{dog.name}: {dog.speak()}")
print(f"{cat.name}: {cat.speak()}")
```

### 📌 Example 2 — Using super()

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  # Call parent constructor
        self.team_size = team_size

m = Manager("Alice", 90000, 5)
print(f"{m.name}: ${m.salary}, manages {m.team_size}")
```

### 📌 Example 3 — Method Overriding

```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):  # Override
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):  # Override
        return 3.14 * self.r ** 2

print(f"Rectangle: {Rectangle(5, 3).area()}")
print(f"Circle: {Circle(4).area()}")
```

### 📌 Example 4 — Extending Methods

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def info(self):  # Extend parent method
        base = super().info()
        return f"{base}, Doors: {self.doors}"

car = Car("Tesla", 4)
print(car.info())
```

### 📌 Example 5 — isinstance() and issubclass()

```python
class Animal: pass
class Dog(Animal): pass
class Cat(Animal): pass

dog = Dog()

print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True (Dog IS-A Animal)
print(isinstance(dog, Cat))     # False

print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
```

### 📌 Example 6 — Multiple Inheritance

```python
class Flyer:
    def fly(self):
        return "Flying..."

class Swimmer:
    def swim(self):
        return "Swimming..."

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())   # Flying...
print(duck.swim())  # Swimming...
print(duck.quack()) # Quack!
```

---

## 🧪 Practice Exercise

1. Create a `Vehicle` base class with `brand` and `speed`
2. Create `Car` and `Bike` child classes
3. Override a method in each child
4. Use `super()` to extend functionality

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🧬 **Inheritance** | Child gets parent's attributes and methods |
| 🔧 **super()** | Call parent methods, especially `__init__` |
| 🔄 **Override** | Replace parent method with child version |
| 📏 **is-a** | Only inherit when there's a real "is-a" relationship |
| 🌳 **Hierarchy** | Organize code from general to specific |

---

## 🔗 Further Reading

- 📖 [Inheritance — Official Docs](https://docs.python.org/3/tutorial/classes.html#inheritance)
- 🌟 [super() — Real Python](https://realpython.com/python-super/)
- 🔧 [Multiple Inheritance — docs](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)