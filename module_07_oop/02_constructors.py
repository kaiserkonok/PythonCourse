"""
Constructors (Initializing Objects)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Basic Constructor
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(10, 5)
print(f"Size: {rect.width}x{rect.height}")


# Example 2 — Default Values
class User:
    def __init__(self, username, role="user"):
        self.username = username
        self.role = role

admin = User("alice", "admin")
guest = User("bob")  # Uses default role

print(f"{admin.username} is {admin.role}")
print(f"{guest.username} is {guest.role}")


# Example 3 — Validation
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.owner = owner
        self.balance = balance

account = BankAccount("Alice", 500)
print(f"{account.owner}: ${account.balance}")


# Example 4 — Computed Attributes
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = math.pi * radius ** 2

c = Circle(5)
print(f"Radius: {c.radius}, Diameter: {c.diameter}, Area: {c.area:.2f}")


# Example 5 — `__str__` for Display
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"

item = Product("Laptop", 999)
print(item)  # Laptop - $999


# Example 6 — Optional Parameters
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


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a Student class with name, grade, and optional major
# 2. Add validation to ensure grade is between 0 and 100
# 3. Create a __str__ method for nice printing
# 4. Test with multiple objects
# ═══════════════════════════════════════════════════════════════════════════════

class Student:
    def __init__(self, name, grade, major="Undeclared"):
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
        self.name = name
        self.grade = grade
        self.major = major

    def __str__(self):
        return f"{self.name} (Grade: {self.grade}, Major: {self.major})"

s1 = Student("Alice", 95, "Computer Science")
s2 = Student("Bob", 82)

print(s1)
print(s2)

# Try modifying it:
# - Add a method to check if student passed
class StudentWithPass:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def passed(self):
        return self.grade >= 50

    def __str__(self):
        status = "Passed" if self.passed() else "Failed"
        return f"{self.name}: {self.grade}% ({status})"

s3 = StudentWithPass("Charlie", 45)
print(s3)
