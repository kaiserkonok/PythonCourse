"""
Classes & Objects (Blueprint for Data)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic Class
class Dog:
    """A simple Dog class."""

    def bark(self):
        print("Woof! Woof!")

# Create objects
dog1 = Dog()
dog2 = Dog()

dog1.bark()  # Woof! Woof!
dog2.bark()  # Woof! Woof!


# Example 2 — Adding Attributes
class DogWithName:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age

    def describe(self):
        print(f"{self.name} is {self.age} years old")

my_dog = DogWithName("Buddy", 3)
my_dog.describe()  # Buddy is 3 years old


# Example 3 — Multiple Objects
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


# Example 4 — Modifying Attributes
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


# Example 5 — Type Checking
class Cat:
    pass

class DogType:
    pass

cat = Cat()
dog = DogType()

print(isinstance(cat, Cat))  # True
print(isinstance(cat, DogType))  # False
print(type(cat))             # <class '__main__.Cat'>


# Example 6 — `self` Explained
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


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a Person class with name and age attributes
# 2. Add a method that prints a greeting
# 3. Create two Person objects and call their methods
# 4. Add a method that checks if the person is an adult
# ═══════════════════════════════════════════════════════════════════════════════

# 1-4. Complete Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I'm {self.name}!")

    def is_adult(self):
        return self.age >= 18

p1 = Person("Alice", 25)
p2 = Person("Bob", 15)

p1.greet()
p2.greet()

print(f"{p1.name} is adult: {p1.is_adult()}")
print(f"{p2.name} is adult: {p2.is_adult()}")

# Try modifying it:
# - Add a class attribute (shared by all instances)
class Employee:
    company = "TechCorp"  # Class attribute

    def __init__(self, name):
        self.name = name

e1 = Employee("Alice")
e2 = Employee("Bob")
print(f"{e1.name} works at {e1.company}")
print(f"{e2.name} works at {e2.company}")
