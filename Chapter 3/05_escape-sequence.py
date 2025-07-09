# 🔹 Escape Sequences in Python 🔹
# Escape sequences are special characters used in strings that start with a backslash (\).
# They help us format text with effects like newline, tab, quotes, backslash, etc.
# Common escape sequences:
#   \n  → New line
#   \t  → Tab space
#   \\  → Backslash
#   \'  → Single quote
#   \"  → Double quote
#   \b  → Backspace

# Newline: moves text to the next line
a = "Hassan is a Good boy\nbut not a bad boy."
print(a)

# Tab: adds a horizontal space like pressing 'Tab' key
b = "Hassan is a Good boy\tbut not a bad boy."
print(b)

# Backslash: prints a backslash character
c = "Hassan is a Good boy\\but not a bad boy."
print(c)

# Backspace: removes one character before it
d = "Hassan is a Good boy\bbut not a bad boy."
print(d)

# Single quotes inside a string
e = "Hassan is a Good boy but not a 'bad' boy."
print(e)

# Double quotes inside a string
f = "Hassan is a Good boy \"but\" not a bad boy."
print(f)
