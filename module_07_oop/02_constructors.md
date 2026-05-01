# Constructors (__init__): Setting the Initial State of an Object

## Learning Objectives

- Understand what __init__ does
- Set up initial attributes
- Use self to access object attributes

## What is __init__?

`__init__` is a special method (constructor):

- Called **automatically** when creating an object
- Used to **initialize** the object's attributes
- Not called again after creation

```python
class Person:
    def __init__(self, name):
        self.name = name  # Set initial attribute

person = Person("Alice")  # __init__ called automatically
```

## How __init__ Works

```python
class Dog:
    def __init__(self, name, breed):
        # These run automatically when creating Dog()
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} barks!"

my_dog = Dog("Buddy", "Labrador")
print(my_dog.name)      # Buddy
print(my_dog.breed)     # Labrador
```

## Creating Objects

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def info(self):
        return f"{self.year} {self.brand} {self.model}"

car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)

print(car1.info())
print(car2.info())
```

## Code Examples

```python
# Example 1: Basic __init__
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}"

person = Person("Alice")
print(person.greet())

# Example 2: Multiple attributes
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")

# Example 3: Default values
class User:
    def __init__(self, name, role="user"):
        self.name = name
        self.role = role
    
    def info(self):
        return f"{self.name} is a {self.role}"

user1 = User("Alice")
user2 = User("Bob", "admin")
print(user1.info())
print(user2.info())

# Example 4: Calculate in __init__
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * radius * radius
    
    def get_area(self):
        return self.area

circle = Circle(5)
print(f"Area: {circle.get_area()}")

# Example 5: Initialize with default and calculated
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        return self.balance

account = BankAccount(100)
account.deposit(50)
print(f"Balance: {account.withdraw(30)}")
```

## Common Mistakes

```python
# ❌ Wrong: Forgetting self
def __init__(name):  # Missing self!
    name = name  # Just creates local variable

# ✅ Correct: Use self
def __init__(self, name):
    self.name = name  # Object attribute
```

## Key Takeaways

1. **__init__** sets initial state
2. **self** refers to the object being created
3. **Parameters** passed in parentheses
4. **Default values** supported
5. **Called once** when creating object

## Practice Exercise

1. Create a Book class with title and author
2. Add a method to display book info
3. Create a Product class with name, price, and quantity
4. Calculate total value in __init__