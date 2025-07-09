name = "python programming"
print (len(name)) # This will give the length of the string, which is 18
print (name[0]) # This will give the first character of the string, which is 'p'
print (name.endswith("ing")) # This will check if the string ends with 'ing', which is True
print (name.startswith("py")) # This will check if the string starts with 'py', which is True
print(name.capitalize()) # This will capitalize the first character of the string, which is 'Python programming'
print(name.upper()) # This will convert the string to uppercase, which is 'PYTHON PROGRAMMING'
print(name.lower()) # This will convert the string to lowercase, which is 'python programming'
print(name.title()) # This will convert the first character of each word to uppercase, which is 'Python Programming'
print(name.replace("python", "Python")) # This will replace 'python' with 'Python', which is 'Python programming'
print(name.split()) # This will split the string into a list of words, which is ['python', 'programming']
print(name.find("gram")) # This will find the index of 'gram' in the string, which is 10
print(name.index("gram")) # This will also find the index of 'gram' in the string, which is 10
print(name.count("o")) # This will count the number of occurrences of 'o' in the string, which is 2