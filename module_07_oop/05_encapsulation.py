# Code examples from "Encapsulation" lesson

# Example 1: Protected attribute (convention)
class Student:
    def __init__(self, name):
        self._name = name  # Protected
    
    def get_name(self):
        return self._name

s = Student("Alice")
print(s.get_name())  # Alice

# Example 2: Private attribute (name mangling)
class Secret:
    def __init__(self, code):
        self.__code = code

s = Secret(1234)
# print(s.__code)  # AttributeError!
print(s._Secret__code)  # Still accessible but hidden

# Example 3: Using property
class Rectangle:
    def __init__(self, width):
        self.__width = width
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value

r = Rectangle(5)
print(r.width)  # 5

# Example 4: Read-only property
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def area(self):
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.area)  # 78.5
# c.area = 100  # AttributeError!

# Example 5: Validation in setter
class Person:
    def __init__(self, age):
        self.age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

p = Person(25)
print(p.age)  # 25
p.age = 30
print(p.age)  # 30


# =====================
# PRACTICE EXERCISE
# =====================

# 1. Create a class with private attribute
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    # 2. Add getter using @property
    @property
    def balance(self):
        return self.__balance
    
    # 3. Add setter with validation
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = value
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount

# 4. Try accessing directly (see how it fails)
account = BankAccount(1000)
print(f"Balance: {account.balance}")  # Using getter

account.deposit(500)
print(f"After deposit: {account.balance}")

account.withdraw(200)
print(f"After withdrawal: {account.balance}")

# account.balance = -100  # This would raise ValueError!
account.balance = 500  # Using setter