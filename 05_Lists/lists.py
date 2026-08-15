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

# 8. Add an IT company
it_companies.append('TCS')
print("After append:", it_companies)

# 9. Insert an IT company in the middle
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Infosys')
print("After insert in middle:", it_companies)

# 10. Change one company name to uppercase
it_companies[1] = it_companies[1].upper()
print("Uppercase update:", it_companies)

# 11. Join list with '#; '
joined_companies = '#; '.join(it_companies)
print("Joined Companies:", joined_companies)

# 12. Check if a company exists
company_check = 'Apple' in it_companies
print("Does Apple exist?:", company_check)

# 13. Sort the list
it_companies.sort()
print("Sorted list:", it_companies)

# 14. Reverse the list
it_companies.reverse()
print("Reversed list:", it_companies)

# 15. Slice out first 3 and last 3 companies
print("First 3 companies:", it_companies[:3])
print("Last 3 companies:", it_companies[-3:])

# 16. Remove middle IT company
it_companies.pop(len(it_companies) // 2)
print("After removing middle company:", it_companies)

# 17. Clear the list
it_companies.clear()
print("Cleared list:", it_companies)


# ==================== LEVEL 2 ====================
print("\n--- Level 2 (Ages Statistics) ---")

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]