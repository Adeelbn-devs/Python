letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> ''' # This is a template for the letter

print(letter.replace("<|Name|>", "Adeel").replace("<|Date|", "24 September 2050"))