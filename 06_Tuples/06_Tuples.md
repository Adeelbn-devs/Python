# Topic 06: Tuples in Python

A tuple is a collection of different data types which is ordered and **unchangeable (immutable)**. Tuples are written with round brackets `()`. Once a tuple is created, we cannot change its values.

---

## 📌 Table of Contents
1. [Creating a Tuple](#1-creating-a-tuple)
2. [Accessing Tuple Items](#2-accessing-tuple-items)
3. [Slicing a Tuple](#3-slicing-a-tuple)
4. [Changing Tuples to Lists](#4-changing-tuples-to-lists)
5. [Joining Tuples](#5-joining-tuples)
6. [Tuple Methods](#6-tuple-methods)

---

## 1. Creating a Tuple

```python
# Empty tuple
empty_tuple = ()
# or
empty_tuple = tuple()

# Tuple with initial values
fruits = ('banana', 'orange', 'mango', 'lemon')
```

## 2. Accessing Tuple Items

Like lists, we use positive or negative indexing to access tuple items.

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[0])   # banana
print(fruits[-1])  # lemon
```


### 3. Slicing a Tuple

We can slice a tuple to get a range of items.

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[1:3]) # ('orange', 'mango')
```

## 4. Changing Tuples to Lists

Since tuples are unchangeable, if we want to modify a tuple, we must first change it to a list, modify the list, and then change it back to a tuple.

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits_list = list(fruits)
fruits_list[0] = 'apple'
fruits = tuple(fruits_list)
```

### 5. Joining Tuples

We can join two or more tuples using the + operator.

```python
fruits = ('banana', 'orange')
vegetables = ('tomato', 'potato')
food = fruits + vegetables
```

### 6. Tuple Methods

Tuples have very few built-in methods because they are immutable.

| Method 