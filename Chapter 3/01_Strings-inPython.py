# Strings:
# They are the data types in python which are used to store the text data.
# They are immutable, which means once created, they cannot be changed.
# Strings can be created by enclosing characters in single quotes, double quotes, or triple quotes.
# primarily these are some examples of strings:
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"   
triple_quote_string = '''Hello, World!'''  # triple quotes can be used for multi-line strings

# String Slicing:
# Slicing is used to access a range of characters in a string.
# It is done using the colon (:) operator inside square brackets.
# For example:
name = "Python Programming"
nameshort = name[0:6]  # This will give 'Python'
print(nameshort)
# accessing a single character
print(name[0])  # This will give 'P'
# accessing a range of characters   
print(name[0:6])  # This will give 'Python'
# accessing characters from the end
print(name[-11:])  # This will give 'Programming'
# accessing characters from the start to a specific index
print(name[:6])  # This will give 'Python'
