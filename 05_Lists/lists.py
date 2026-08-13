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