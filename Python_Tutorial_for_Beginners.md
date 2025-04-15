
# Python Tutorial

Welcome to this beginner-friendly Python tutorial! This guide will introduce you to the basics of Python programming.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Basic Syntax](#basic-syntax)
3. [Variables and Data Types](#variables-and-data-types)
4. [Operators](#operators)
5. [Control Flow](#control-flow)
6. [Functions](#functions)
7. [Lists, Tuples, and Dictionaries](#lists-tuples-and-dictionaries)
8. [File I/O](#file-io)
9. [Modules and Packages](#modules-and-packages)
10. [Further Resources](#further-resources)

---

### Getting Started

- **Download Python:** [python.org/downloads](https://www.python.org/downloads/)
- **Check Python Version:**
  ```bash
  python --version
  ```
- **Run Python:**
  - Interactive Shell: `python`
  - Script: `python your_script.py`

---

### Basic Syntax

```python
print("Hello, world!")
```

---

### Variables and Data Types

```python
name = "ZoHrEh"
age = 3
average = 18.2
is_student = False
```

- **Data Types:**
	- name = `str`
	-  age = `int`
	- average = `float`
	- is_student = `boolean`

- **Other Data Types:** `list`, `tuple`, `dict` 

---

### Operators

```python
# Arithmetic
a = 10 + 5
b = 2 * 3

# Comparison
result = (a > b)  # True
```

---

### Control Flow

#### If Statements

```python
if age >= 18:
    print("Adult")
elif 18 > age > 15 :
    print("Adolescence")
else:
    print ("Child")
```

#### Loops

```python
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

---

### Functions

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("ZoHrEh"))
```

---

### Lists, Tuples, and Dictionaries

```python
# List
fruits = ["apple", "banana", "cherry"]

# Tuple
dimensions = (1920, 1080)

# Dictionary
person = {"name": "ZoHrEh", "age": 3}
```

---

### File I/O

```python
# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, file!")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## Modules and Packages

- **Import a Module**
  ```python
  import math
  print(math.sqrt(25))
  ```
- **Install a Package**
  ```bash
  pip install requests
  ```

---

## Further Resources

- [Official Python Documentation](https://docs.python.org/3/)
- [Learn Python (W3Schools)](https://www.w3schools.com/python/)
- [Python for Beginners (Python.org)](https://www.python.org/about/gettingstarted/)

---

Happy Coding! 🎉

