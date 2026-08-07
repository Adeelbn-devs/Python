# Topic 03: Operators & Booleans Practice Script

# 1, 2, 3. Declare Variables
age = 19
height = 5.9
complex_num = 1 + 2j

# 4. Triangle Area Calculation
base = 20
h_triangle = 10
area_triangle = 0.5 * base * h_triangle
print("Triangle Area:", area_triangle)

# 5. Triangle Perimeter Calculation
side_a, side_b, side_c = 5, 4, 3
perimeter_triangle = side_a + side_b + side_c
print("Triangle Perimeter:", perimeter_triangle)

# 6. Rectangle Area and Perimeter
length, width = 10, 20
area_rect = length * width
perimeter_rect = 2 * (length + width)
print("Rectangle Area:", area_rect, "| Perimeter:", perimeter_rect)

# 7. Circle Area and Circumference
radius = 10
pi = 3.14
area_circle = pi * (radius ** 2)
circum_circle = 2 * pi * radius
print("Circle Area:", area_circle, "| Circumference:", circum_circle)

# 8, 9, 10. Slope Calculations
# Slope of y = 2x - 2 (m = 2)
m1 = 2

# Slope between (2, 2) and (6, 10): m = (y2-y1)/(x2-x1)
x1, y1, x2, y2 = 2, 2, 6, 10
m2 = (y2 - y1) / (x2 - x1)
euclidean_dist = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("Slope 1:", m1, "| Slope 2:", m2)
print("Are slopes equal?:", m1 == m2)
print("Euclidean Distance:", euclidean_dist)

# 11. Find x where y = x^2 + 6x + 9 is 0
# Equation is (x + 3)^2 = 0 => x = -3
x = -3
y = x**2 + 6*x + 9
print("y value at x = -3:", y)

# 12. Length comparison of 'python' and 'dragon'
len_python = len('python')
len_dragon = len('dragon')
print("Falsy Comparison (python len != dragon len):", len_python != len_dragon)

# 13. 'on' in both 'python' and 'dragon'
print("'on' in both words:", ('on' in 'python') and ('on' in 'dragon'))

# 14. Check if 'jargon' is in sentence
sentence = "I hope this course is not full of jargon"
print("'jargon' in sentence:", 'jargon' in sentence)

# 15. Confirm 'on' is present in both
print("No 'on' in both (False check):", ('on' not in 'python') and ('on' not in 'dragon'))

# 16. Convert len('python') to float and then str
len_py_str = str(float(len('python')))
print("Length converted to float then str:", len_py_str, type(len_py_str))

# 17. Even number check
num = 10
is_even = (num % 2 == 0)
print(f"Is {num} even?:", is_even)

# 18. Check floor division 7 // 3 == int(2.7)
print("7 // 3 == int(2.7):", (7 // 3) == int(2.7))

# 19. Check type('10') == type(10)
print("type('10') == type(10):", type('10') == type(10))

# 20. Check float string conversion to int equality
# Note: int('9.8') directly raises Error, so convert float('9.8') to int first
print("int(float('9.8')) == 10:", int(float('9.8')) == 10)

# 21. Weekly Earning Calculation
hours = 40
rate_per_hour = 28
weekly_earning = hours * rate_per_hour
print("Weekly Earning:", weekly_earning)