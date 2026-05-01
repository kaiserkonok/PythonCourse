# Classes & Objects: Moving from Procedural to Object-Oriented Thinking

## Learning Objectives

- Understand what classes and objects are
- Create basic classes and objects
- Think in object-oriented terms

## What is a Class?

A class is a **blueprint** for creating objects:

- **Class** - The blueprint
- **Object** - An instance of the class

```python
# Define a class
class Dog:
    # Class behavior
    def bark(self):
        print("Woof!")

# Create objects (instances)
my_dog = Dog()
your_dog = Dog()

my_dog.bark()  # Woof!
your_dog.bark()  # Woof!
```

## Class vs Object

| Class | Object |
|-------|--------|
| Blueprint | Instance |
| Template | Created from blueprint |
| Defines attributes/behavior | Has actual values |

## Creating Classes

```python
class Person:
    # Constructor - called when creating object
    def __init__(self, name):
        self.name = name
    
    # Method - behavior
    def greet(self):
        return f"Hello, I'm {self.name}"

# Create object
person1 = Person("Alice")
print(person1.greet())  # Hello, I'm Alice
```

## How Objects Work

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        return f"{self.brand} is driving!"

# Create objects
car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.brand)  # Toyota
print(car2.brand)  # Honda
```

## Code Examples

```python
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
```

## Procedural vs OOP

| Procedural | Object-Oriented |
|-----------|------------------|
| Functions + data | Objects + methods |
| Data separate | Data with behavior |
| Top-down | Bottom-up |

## Key Takeaways

1. **class** keyword defines blueprint
2. **__init__** is called when creating object
3. **self** refers to the object
4. **Methods** define behavior
5. **Objects** are instances of classes

## Practice Exercise

1. Create a class called Student
2. Add name and age as attributes
3. Add a method that introduces the student
4. Create two Student objects