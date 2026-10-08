# This is a list in Python
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"] 


print(friends[0])# This will print the first element of the list, which is "Apple"

friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0]) # This will print the updated first element of the list, which is now "Grapes"

print(friends[1:4]) # This will print the elements from index 1 to 3 (4 is not included), which are "Orange", 5, and 345.06