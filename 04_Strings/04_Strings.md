# Topic 04: Strings in Python

A string is a sequence of characters enclosed in quotes. Strings in Python can be created using single (`'...'`), double (`"..."`), or multiline (`'''...'''` / `"""..."""`) quotes.

---

## 📌 Table of Contents
1. [Creating Strings](#1-creating-strings)
2. [String Concatenation](#2-string-concatenation)
3. [Escape Sequences](#3-escape-sequences)
4. [String Formatting (F-Strings)](#4-string-formatting)
5. [Indexing & Slicing](#5-indexing--slicing)
6. [Useful String Methods](#6-useful-string-methods)

---


## 1. Creating Strings
``python
letter = 'P'                            # Single character string
greeting = 'Hello, World!'              # Single quote string
sentence = "Python is awesome!"         # Double quote string
multiline = '''I am learning Python
step-by-step with daily commits.'''     # Multiline string

---


## 2. String Concatenation
Joining two or more strings together using the + operator or .join().

first_name = 'Adeel'
last_name + 'B N'
full_name = first_name + ' ' + last_name
pront(full_name)   #Output: Adeel B N

---


## 3. Escape Sequences
Special characters used to format output inside strings:

\n: Newline

\t: Tab space (4 spaces)

\\: Backslash

\': Single Quote

\": Double Quote

Example:
print("Day 4\nTopic: Strings\tLanguage: Python")

---


## 4. String Formatting
Python supports modern F-Strings (f"..."), which make variable interpolation easy and readable:

name = "Adeel"
age = 19
role = "Developer"

# Modern F-String (Recommended)
print(f"My name is {name}, I am {age} years old and I am a {role}.")

---


## 5. Indexing & Slicing
Indexing (0-Based)

language = 'Python'
print(language[0])   # 'P'
print(language[-1])  # 'n' (Last character)

Slicing ([start:stop:step])

print(language[0:4])   # 'Pyth' (From index 0 to 3)
print(language[2:])    # 'thon' (From index 2 to end)
print(language[::-1])  # 'nohtyP' (Reverse string shortcut)

---


## 6. Useful String Methods

| Method | Description | Example Output |
|---|---|---|
| `.upper()` | Converts to uppercase | `'PYTHON'` |
| `.lower()` | Converts to lowercase | `'python'` |
| `.title()` | Capitalizes first letter of each word | `'Hello World'` |
| `.strip()` | Removes leading/trailing spaces | `'text'` |
| `.replace(old, new)` | Replaces substring | `'PyJava' -> 'Python'` |
| `.split(delimiter)` | Splits string into a list | `['a', 'b', 'c']` |
| `.join(list)` | Joins list items into string | `'a-b-c'` |
| `.find(sub)` | Returns index of first match (-1 if none) | `2` |
| `.startswith(sub)` | Checks starting substring | `True` / `False` |
