# Topic 02: Variables and Built-in Functions

A simple breakdown of Python built-in functions, variable rules, data types, and type casting.

---

## 📌 Built-in Functions

![alt text](image.png)

Built-in functions are globally available in Python without any imports:
- `print()` - Displays output to the console.
- `len()` - Returns the length of an object (string, list, etc.).
- `type()` - Returns the data type of a variable.
- `input()` - Takes input from the user.

---

## 📌 Variable Naming Rules (`snake_case`)
1. Must start with a letter or an underscore `_`.
2. Cannot start with a number.
3. Contains only alphanumeric characters and underscores (`a-z`, `0-9`, `_`).
4. Case-sensitive (`first_name` $\neq$ `First_Name`).

### Examples
- **Valid:** `first_name`, `age_2026`, `_is_active`
- **Invalid:** `1st_name`, `first-name`, `first name`

---

## 📌 Data Types & Casting
### Primary Data Types
- **Integer (`int`):** `10`, `-5`
- **Float (`float`):** `3.14`, `9.81`
- **String (`str`):** `'Python'`
- **Boolean (`bool`):** `True`, `False`

### Type Casting Examples
```python
num_int = 10
num_float = float(num_int) # Convert to 10.0

gravity = 9.81
int_gravity = int(gravity) # Convert to 9
