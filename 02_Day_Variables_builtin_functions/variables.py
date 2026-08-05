## 💻 Step 3: Complete `variables.py` (Practice Code)

# Topic 02: Practice Script

# ==================== LEVEL 1 ====================
# Declaring variables
first_name = 'Adeel'
last_name = 'B N'
full_name = first_name + ' ' + last_name
country = 'India'
city = 'Mumbai'
age = 21
year = 2026
is_married = False
is_true = True
is_light_on = True

# Declaring multiple variables in one line
role, skills = 'Developer', ['HTML', 'CSS', 'JS', 'Python']

print("--- Level 1 ---")
print("Full Name:", full_name)
print("Country:", country)
print("Skills:", skills)


# ==================== LEVEL 2 ====================
print("\n--- Level 2 ---")

# 1. Check Data Types

print("Type of first_name:", type(first_name))
print("Type of age:", type(age))
print("Type of is_married:", type(is_married))

# 2. Compare Lengths
print("First Name Length:", len(first_name))
print("Last Name Length:", len(last_name))

# 3. Arithmetic Operations
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exponent = num_one ** num_two
floor_division = num_one // num_two

print("Addition:", total)
print("Subtraction:", diff)
print("Multiplication:", product)
print("Division:", division)
print("Modulus:", remainder)
print("Power (5^4):", exponent)
print("Floor Division:", floor_division)

# 4. Circle Calculations (Radius = 30)
radius = 30
pi = 3.14
area_of_circle = pi * (radius ** 2)
circum_of_circle = 2 * pi * radius

print("\n---Circle Calculations ---")
print("Area of Circle:", area_of_circle)
print("Circumference of Circle:", circum_of_circle)