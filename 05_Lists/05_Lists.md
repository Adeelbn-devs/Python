# Topic 05: Lists in Python

A list is a collection of different data types which is ordered and changeable (mutable). Lists are written with square brackets `[]`.

---

## 📌 Table of Contents
1. [Creating a List](#1-creating-a-list)
2. [Accessing List Items](#2-accessing-list-items)
3. [Slicing a List](#3-slicing-a-list)
4. [Modifying Lists (Add & Remove)](#4-modifying-lists)
5. [Useful List Methods](#5-useful-list-methods)

---

## 1. Creating a List

You can create an empty list or a list with initial values. A list can contain mixed data types.

``python
# Empty list
empty_list = []
# or
empty_list = list()

# List with mixed data types
user_info = ['Adeel', 19, True, 'Bengaluru']

---

## 2. Accessing List Items

List items are indexed starting from 0. You can also use negative indexing (-1 for the last item).

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[0])   # banana
print(fruits[-1])  # lemon (last item)