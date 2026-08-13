# Topic 05: Lists Practice Script.

# ==================== LEVEL 1 ====================
print("--- Level 1 ---")

# 1, 2, 3. Create empty list, list with >5 items, find length
empty_list = []
numbers = [10, 20, 30, 40, 50, 60, 70]
print("Length of numbers list:", len(numbers))

# 4. Get first, middle, and last item
first_item = numbers[0]
middle_item = numbers[len(numbers) // 2]
last_item = numbers[-1]
print("First:", first_item, "| Middle:", middle_item, "| Last:", last_item)

# 5. Mixed data types list
mixed_data_types = ['Adeel', 19, 5.9, 'Single', 'Bengaluru']
print("Mixed List:", mixed_data_types)

# 6, 7. IT Companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("IT Companies:", it_companies)