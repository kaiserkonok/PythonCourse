# Code examples from "Classes & Objects" lesson

# Example 1: Simple class
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())

# Example 2: Class with multiple methods
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(10, 4))

# Example 3: Multiple objects
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        return f"Driving {self.brand}"

car1 = Car("Toyota")
car2 = Car("Honda")
print(car1.drive())
print(car2.drive())

# Example 4: Class with multiple attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"I'm {self.name}, {self.age} years old"

person = Person("Alice", 25)
print(person.introduce())

# Example 5: Self parameter
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a class called Student
class Student:
    # 2. Add name and age as attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # 3. Add a method that introduces the student
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

# 4. Create two Student objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print(student1.introduce())
print(student2.introduce())