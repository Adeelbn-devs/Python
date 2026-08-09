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