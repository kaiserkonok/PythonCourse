# Code examples from "Constructors" lesson

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


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a Book class with title and author
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    # 2. Add a method to display book info
    def display_info(self):
        return f"'{self.title}' by {self.author}"

book = Book("1984", "George Orwell")
print(book.display_info())

# 3. Create a Product class with name, price, and quantity
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_value = price * quantity
    
    def info(self):
        return f"{self.name}: ${self.price} x {self.quantity} = ${self.total_value}"

laptop = Product("Laptop", 999, 2)
print(laptop.info())