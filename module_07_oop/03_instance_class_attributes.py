# Code examples from "Instance vs Class Attributes" lesson

# Example 1: Instance attributes
class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
car2 = Car("Honda")
print(car1.brand)  # Toyota
print(car2.brand)  # Honda

# Example 2: Class attributes
class Animal:
    kingdom = "Animalia"  # Same for all

print(Animal.kingdom)
a1 = Animal()
a2 = Animal()
print(a1.kingdom)  # Same value for both

# Example 3: Mixed
class Student:
    school = "Python High"  # Class attribute
    
    def __init__(self, name, grade):
        self.name = name    # Instance
        self.grade = grade  # Instance

s1 = Student("Alice", "A")
s2 = Student("Bob", "B")
print(s1.school)  # Python High
print(s2.school)  # Python High

# Example 4: Counter using class attribute
class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    def get_count(self):
        return Counter.count

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(f"Count: {Counter.count}")  # 3

# Example 5: Default values with class attribute
class Database:
    connection_timeout = 30  # Default
    
    def __init__(self, host):
        self.host = host

db1 = Database("localhost")
print(db1.connection_timeout)  # 30 (default)
db2 = Database("server")
print(db2.connection_timeout)  # 30 (default)


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a class with a class attribute (species)
class Animal:
    species = "Dog"  # Class attribute

# 2. Create instances with instance attributes
class Animal:
    species = "Dog"  # Class attribute
    
    def __init__(self, name):
        self.name = name  # Instance attribute

dog1 = Animal("Buddy")
dog2 = Animal("Max")

print(f"dog1.name: {dog1.name}")
print(f"dog2.name: {dog2.name}")
print(f"Species: {Animal.species}")

# 3. Modify class attribute and see effect
Animal.species = "Canine"
print(f"After modification: {dog1.species}")

# 4. Create a counter using class attribute
class Widget:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Widget.count += 1

w1 = Widget("Button")
w2 = Widget("Label")
w3 = Widget("Input")

print(f"Widget count: {Widget.count}")