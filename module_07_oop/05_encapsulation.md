# Encapsulation: Using Underscores to Manage Data Access

## Learning Objectives

- Understand encapsulation
- Use public, protected, and private
- Create getters and setters

## What is Encapsulation?

Encapsulation restricts **direct access** to attributes:

- Keeps data safe from outside changes
- Controls how data is modified
- Uses underscores to indicate visibility

## Underscore Conventions

| Prefix | Type | Meaning |
|--------|------|---------|
| `name` | Public | Accessible anywhere |
| `_name` | Protected | Don't access directly (convention) |
| `__name` | Private | Name mangled (harder to access) |

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance        # Public
        self._pin = 1234          # Protected (convention)
        self.__secret = "xray"   # Private (name mangled)

account = BankAccount(1000)
print(account.balance)   # 1000 - accessible
# print(account._pin)    # Works but discouraged
# print(account.__secret) # Error!
```

## Getters and Setters

```python
class Person:
    def __init__(self, name):
        self._name = name  # Protected attribute
    
    # Getter
    @property
    def name(self):
        return self._name
    
    # Setter
    @name.setter
    def name(self, value):
        if len(value) > 0:
            self._name = value

person = Person("Alice")
print(person.name)   # Alice (getter)
person.name = "Bob"  # Bob (setter)
print(person.name)
```

## Property Decorator

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Too cold!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.fahrenheit)  # 77.0
```

## Code Examples

```python
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
```

## When to Use Encapsulation

- **Protect data** - prevent invalid values
- **Control access** - decide when/how
- **Clean API** - hide implementation details

## Key Takeaways

1. **Protected (_name)**: Convention, don't access directly
2. **Private (__name)**: Name mangled, use getter/setter
3. **@property**: Define getter
4. **@name.setter**: Define setter with validation
5. **Encapsulation** protects data integrity

## Practice Exercise

1. Create a class with private attribute
2. Add getter using @property
3. Add setter with validation
4. Try accessing directly (see how it fails)