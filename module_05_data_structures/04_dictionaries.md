# Dictionaries: Mapping Data Using Key-Value Pairs (Hash Maps)

## Learning Objectives

- Create and use dictionaries
- Access and modify values by key
- Use common dictionary methods

## What is a Dictionary?

A dictionary stores **key-value pairs**:

- Key: The identifier
- Value: The data
- Fast lookup by key (O(1) complexity)

```python
# Key: Value
user = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}
```

## Creating Dictionaries

```python
# Standard creation
person = {"name": "Alice", "age": 25}

# Using dict()
person2 = dict(name="Bob", age=30)

# Empty dictionary
empty = {}
```

## Accessing Values

```python
user = {"name": "Alice", "age": 25}

# Access by key
print(user["name"])   # Alice
print(user["age"])    # 25

# Using get() - safer (returns None if not found)
print(user.get("name"))   # Alice
print(user.get("city"))   # None (not an error!)
print(user.get("city", "Unknown"))  # Unknown (default)
```

## Modifying Dictionaries

```python
user = {"name": "Alice", "age": 25}

# Change value
user["age"] = 26

# Add new key
user["city"] = "NYC"

# Remove key
del user["name"]
# or
user.pop("name")
```

## Code Examples

```python
# Example 1: Create and access
car = {"brand": "Toyota", "model": "Camry", "year": 2022}
print(car["brand"])  # Toyota
print(car.get("year"))  # 2022

# Example 2: Update dictionary
car["year"] = 2023
car["color"] = "blue"
print(car)  # {'brand': 'Toyota', 'model': 'Camry', 'year': 2023, 'color': 'blue'}

# Example 3: Get all keys/values
user = {"name": "Alice", "age": 25, "city": "NYC"}
print(user.keys())    # dict_keys(['name', 'age', 'city'])
print(user.values()) # dict_values(['Alice', 25, 'NYC'])
print(user.items())  # dict_items([('name', 'Alice'), ...])

# Example 4: Loop through dictionary
for key in user:
    print(f"{key}: {user[key]}")

# Example 5: Nested dictionary
company = {
    "employee": {
        "name": "Alice",
        "role": "Developer"
    }
}
print(company["employee"]["name"])  # Alice
```

## Dictionary Methods

| Method | Description |
|--------|-------------|
| .get(key) | Get value, return None if missing |
| .keys() | Get all keys |
| .values() | Get all values |
| .items() | Get all key-value pairs |
| .pop(key) | Remove key and return value |
| .update(dict) | Add/update from another dict |

## Key Takeaways

1. **Dictionaries use {}** with key: value pairs
2. **Fast lookup** by key
3. **Keys must be immutable** (strings, numbers, tuples)
4. **Values can be anything**
5. **.get()** is safer than []

## Practice Exercise

1. Create a dictionary with your info (name, age, hobby)
2. Add a new key
3. Loop through and print all key-value pairs
4. Use .get() with a default value