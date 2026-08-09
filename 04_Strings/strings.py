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