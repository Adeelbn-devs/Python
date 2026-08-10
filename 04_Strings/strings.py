# Topic 04: Strings & String Methods Practice Script

# 1. Concatenate 'Thirty', 'Days', 'Of', 'Python'
word1, word2, word3, word4 = 'Thirty', 'Days', 'Of', 'Python'
sentence1 = word1 + ' ' + word2 + ' ' + word3 + ' ' + word4
print("1. Concatenated Sentence:", sentence1)

# 2. Concatenate 'Coding', 'For', 'All'
sentence2 = ' '.join(['Coding', 'For', 'All'])
print("2. Sentence 2:", sentence2)

# 3, 4, 5. Variable declaration & length
company = "Coding For All"
print("3 & 4. Company Name:", company)
print("5. Length of Company:", len(company))

# 6, 7, 8. Case conversions
print("6. Uppercase:", company.upper())
print("7. Lowercase:", company.lower())
print("8. Capitalize & Title:", company.capitalize(), "|", company.title())

# 9. Slice out the first word
first_word = company.split()[0]
print("9. First Word:", first_word)

# 10. Check if string contains 'Coding'
print("10. Contains 'Coding'?:", 'Coding' in company)

# 11, 12. Replace words
print("11. Replace 'Coding' with 'Python':", company.replace('Coding', 'Python'))
sentence_everyone = "Python for Everyone"
print("12. Replace 'Everyone' with 'All':", sentence_everyone.replace('Everyone', 'All'))

# 13, 14. Split operations
print("13. Split 'Coding For All':", company.split(' '))
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("14. Tech Companies List:", tech_companies.split(', '))

# 15, 16, 17. Indexing characters
print("15. Character at index 0:", company[0])
print("16. Character at last index:", company[-1])
print("17. Character at index 10:", company[10])

# 18, 19. Acronym creation
phrase1 = "Python For Everyone"
acronym1 = ''.join([w[0] for w in phrase1.split()])
print("18. Acronym for 'Python For Everyone':", acronym1)

phrase2 = "Coding For All"
acronym2 = ''.join([w[0] for w in phrase2.split()])
print("19. Acronym for 'Coding For All':", acronym2)

# 20, 21, 22. Positions of characters
print("20. Position of 'C':", company.index('C'))
print("21. Position of 'F':", company.index('F'))
print("22. Last position of 'l':", company.rfind('l'))

# 23, 24, 25. Searching in sentences
sentence3 = 'You cannot cut a tree down having stood on it because it is bad'
print("23. First occurrence of 'because':", sentence3.find('because'))
print("24. Last occurrence of 'because':", sentence3.rfind('because'))


# 26. Slice out 'because it is bad'
start_pos = sentence3.find('because')
print("26. Sliced phrase:", sentence3[start_pos:])

# 27. Strip whitespace
spaced_str = '   Coding For All      '
print("27. Stripped String:", f"'{spaced_str.strip()}'")

# 28. Identifier validation
print("28. Is '30DaysOfPython' valid identifier?:", '30DaysOfPython'.isidentifier())
print("    Is 'thirty_days_of_python' valid identifier?:", 'thirty_days_of_python'.isidentifier())

# 29. Join list with hash `#`
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("29. Joined Libraries:", ' # '.join(python_libraries))

# 30. New line escape sequence
print("\n30. Escape Sequences:\nI am enjoying this challenge.\nI wonder what is next.")

# 31. Tab escape sequence formatting
print("\n31. Tab Formatted Table:")
print("Name\t\tAge\tCountry\t\tCity")
print("Adeel\t\t19\tIndia\t\tBengaluru")