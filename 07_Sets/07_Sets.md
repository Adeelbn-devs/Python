# Topic 07: Sets in Python

A set is a collection of items which is **unordered** and **un-indexed**. Sets are mutable (you can add or remove items), but they **cannot contain duplicate items**. Sets are written with curly brackets `{}`.

---

## 📌 Table of Contents
1. [Creating a Set](#1-creating-a-set)
2. [Adding Items](#2-adding-items)
3. [Removing Items](#3-removing-items)
4. [Set Operations (Union, Intersection, etc.)](#4-set-operations)
5. [Useful Set Methods](#5-useful-set-methods)

---

## 1. Creating a Set

```python
# Empty set (must use set() because {} creates an empty dictionary)
empty_set = set()

# Set with initial values (duplicates are automatically removed)
fruits = {'banana', 'orange', 'mango', 'apple', 'apple'}
print(fruits) # Output will not contain the second 'apple'

```

## 2. Adding Items

You can add a single item using .add() or multiple items using .update().

```python
fruits = {'banana', 'orange'}