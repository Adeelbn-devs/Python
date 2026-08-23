# Topic 06: Tuples Practice Script

# ==================== LEVEL 1 ====================
print("--- Level 1 ---")

# 1. Create an empty tuple
empty_tuple = ()
print("Empty Tuple:", empty_tuple)

# 2. Create a tuple containing names of your sisters and your brothers
brothers = ('Rehan', 'Musheer', 'Karan')
sisters = ('Saniya', 'Navya', 'Raghavi')

# 3. Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = brothers + sisters
print("Food Stuff Tuple:", food_stuff_tp)

# 4. How many siblings do you have?
print("Number of siblings:", len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother
# Note: Tuples are immutable, so we use string concatenation to add new items
family_members = siblings + ('Father', 'Mother')