# 🔐 Encapsulation: Protecting Your Data

<p align="center">
  <img src="https://img.shields.io/badge/private-_%20Prefix-blue?style=flat-square" alt="private">
  <img src="https://img.shields.io/badge/property-Getter%2FSetter-green?style=flat-square" alt="property">
  <img src="https://img.shields.io/badge/Protect-Data%20Safety-orange?style=flat-square" alt="Protect">
</p>

> ### 💡 Encapsulation is like a capsule — the inside is protected from the outside world. You control how data is accessed and modified.
> Learn how to hide internal details and expose safe interfaces.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- ✅ Use private attributes with `_` and `__` prefixes
- ✅ Create getter and setter methods
- ✅ Use the `@property` decorator for clean access

---

## 🧠 Mental Model: An ATM Machine

Encapsulation is like an **ATM**:

```
🏧 ATM (Object)
   ├── 💵 Cash (Private — you can't reach inside)
   ├── 🔢 Keypad (Public — you interact with it)
   └── 🖥️ Screen (Public — shows info)
```

You don't touch the cash directly — you use the keypad (methods) to request withdrawals safely.

---

## 📖 Access Levels

| Prefix | Access | Convention |
|--------|--------|------------|
| `name` | Public | Anyone can access |
| `_name` | Protected | "Internal use" (convention only) |
| `__name` | Private | Name-mangled (harder to access) |

---

## 📊 Getters and Setters

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
```

---

## ⚠️ Common Mistakes

```
❌ Thinking _ means truly private
   _name is just a convention — Python doesn't enforce it!
   It says "this is internal, don't touch"

❌ Overusing __name
   __name triggers name mangling (__ClassName__name)
   Usually just use _name unless you really need protection

❌ No validation in setters
   def set_age(self, age):
       self._age = age  ← No check for negative values!
   if age >= 0: self._age = age  ← Correct

❌ Exposing internal data directly
   return self._data  ← Returns reference, caller can modify!
   return self._data.copy()  ← Returns safe copy
```

---

## 💻 Code Examples

### 📌 Example 1 — Public vs Private

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner      # Public
        self._balance = balance # Protected (internal)

acc = Account("Alice", 1000)
print(acc.owner)      # OK — public
print(acc._balance)   # Works, but shouldn't do it!
```

### 📌 Example 2 — Getters and Setters

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if 0 <= age <= 150:
            self._age = age
        else:
            print("Invalid age!")

p = Person("Alice", 25)
p.set_age(30)
print(p.get_age())  # 30
p.set_age(-5)       # Invalid age!
```

### 📌 Example 3 — @property Decorator

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 0 <= value <= 150:
            self._age = value
        else:
            raise ValueError("Invalid age")

p = Person("Alice", 25)
print(p.age)   # 25 (like attribute access)
p.age = 30     # Calls setter
```

### 📌 Example 4 — Read-Only Properties

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2

c = Circle(5)
print(f"Radius: {c.radius}, Area: {c.area}, Diameter: {c.diameter}")
# c.radius = 10  ← AttributeError (no setter)
```

### 📌 Example 5 — Computed Properties

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

t = Temperature(100)
print(f"{t._celsius}°C = {t.fahrenheit}°F")
t.fahrenheit = 212
print(f"{t._celsius}°C = {t.fahrenheit}°F")
```

### 📌 Example 6 — Data Hiding

```python
class Database:
    def __init__(self):
        self.__password = "secret"  # Private (name-mangled)

    def get_password(self):
        # In real code, verify permissions here
        return self.__password

db = Database()
print(db.get_password())  # "secret"
# print(db.__password)    ← AttributeError
```

---

## 🧪 Practice Exercise

1. Create a class with a private attribute
2. Add a getter and setter with validation
3. Convert to use `@property`
4. Create a read-only computed property

---

## 📋 Key Takeaways

| Concept | Takeaway |
|---------|----------|
| 🔒 **`_name`** | Protected — convention, not enforced |
| 🔒 **`__name`** | Private — name-mangled by Python |
| 🏷️ **`@property`** | Clean getter/setter syntax |
| 🛡️ **Validation** | Use setters to enforce rules |
| 📦 **Encapsulation** | Hide internals, expose safe interface |

---

## 🔗 Further Reading

- 📖 [Private Variables — Official Docs](https://docs.python.org/3/tutorial/classes.html#private-variables)
- 🌟 [@property — Real Python](https://realpython.com/python-property/)
- 🔧 [Descriptors — docs](https://docs.python.org/3/howto/descriptor.html)