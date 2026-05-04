"""
Instance vs Class Attributes (Who Owns the Data?)
────────────────────────────────────────────────────────────────────────────
Code examples and practice exercises from the lesson.
────────────────────────────────────────────────────────────────────────────
"""

# Example 1 — Instance Attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice", 25)
bob = Person("Bob", 30)

print(alice.name)  # Alice
print(bob.name)    # Bob (different!)


# Example 2 — Class Attributes
class Employee:
    company = "TechCorp"  # Shared by all

    def __init__(self, name):
        self.name = name

e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.company)  # TechCorp
print(e2.company)  # TechCorp


# Example 3 — Modifying Class Attributes
class Setting:
    theme = "dark"  # Class attribute

s1 = Setting()
s2 = Setting()

# Change via class
Setting.theme = "light"
print(s1.theme)  # light (both affected)
print(s2.theme)  # light


# Example 4 — Counter Pattern
class User:
    user_count = 0  # Class attribute

    def __init__(self, name):
        self.name = name
        User.user_count += 1  # Increment on creation

u1 = User("Alice")
u2 = User("Bob")
u3 = User("Charlie")

print(f"Total users: {User.user_count}")  # 3


# Example 5 — The Mutable Trap
# ❌ Wrong — shared list
class BadTeam:
    members = []  # Shared across ALL instances!

    def __init__(self, name):
        self.name = name
        BadTeam.members.append(name)

t1 = BadTeam("Alice")
t2 = BadTeam("Bob")
print(f"BadTeam: {t1.members}")  # ['Alice', 'Bob'] ← Both see all members!

# ✅ Correct — instance list
class GoodTeam:
    def __init__(self, name):
        self.name = name
        self.members = []  # Each team has own list

    def add_member(self, member):
        self.members.append(member)

g1 = GoodTeam("Team A")
g2 = GoodTeam("Team B")
g1.add_member("Alice")
g2.add_member("Bob")
print(f"GoodTeam A: {g1.members}")  # ['Alice']
print(f"GoodTeam B: {g2.members}")  # ['Bob']


# Example 6 — Combining Both
class Product:
    tax_rate = 0.08  # Class attribute (shared)

    def __init__(self, name, price):
        self.name = name       # Instance attribute
        self.price = price     # Instance attribute

    def total_price(self):
        return self.price * (1 + Product.tax_rate)

p1 = Product("Laptop", 1000)
p2 = Product("Phone", 500)

print(f"{p1.name}: ${p1.total_price()}")
print(f"{p2.name}: ${p2.total_price()}")


# ═══════════════════════════════════════════════════════════════════════════════
# PRACTICE EXERCISE
# ═══════════════════════════════════════════════════════════════════════════════
# 1. Create a class with a class attribute school_name
# 2. Create instances with unique instance attributes
# 3. Modify the class attribute and see how it affects all instances
# 4. Create a counter that tracks how many objects were created
# ═══════════════════════════════════════════════════════════════════════════════

# 1-4. Student class with counter
class Student:
    school_name = "Python Academy"  # Class attribute
    count = 0                       # Counter

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.count += 1

    def __str__(self):
        return f"{self.name} (Grade: {self.grade}) at {Student.school_name}"

s1 = Student("Alice", 95)
s2 = Student("Bob", 88)

print(s1)
print(s2)
print(f"Total students: {Student.count}")

# Modify class attribute
Student.school_name = "Advanced Python Academy"
print(f"After change: {s1}")

# Try modifying it:
# - Track average grade across all students
class TrackedStudent:
    total_grade = 0
    count = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        TrackedStudent.total_grade += grade
        TrackedStudent.count += 1

    @classmethod
    def average_grade(cls):
        return cls.total_grade / cls.count if cls.count > 0 else 0

TrackedStudent("A", 90)
TrackedStudent("B", 80)
TrackedStudent("C", 70)
print(f"Average: {TrackedStudent.average_grade()}")
