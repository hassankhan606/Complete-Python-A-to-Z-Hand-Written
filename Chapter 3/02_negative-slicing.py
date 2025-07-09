# 🔁 String Slicing in Python (With Positive and Negative Indexes)

# 💡 Summary:
# Slicing means cutting part of a string using: [start : end : step]
# - Positive index starts from 0 (left to right)
# - Negative index starts from -1 (right to left)
# - The end index is NOT included
# - You can even add step (like skip value)

# 💡 Negative Indexing:
# -1 = last character
# -2 = second last, and so on...
# It helps when counting from the end of the string.

# Example string
name = "Python Programming"

# Slice from index 0 to 3 (not including 3) → 'Pyt'
print(name[0:3])          # Output: Pyt

# Same as above, with step 1 (default)
print(name[0:3:1])        # Output: Pyt

# Negative slicing: index -6 = 'a', -4 = 'o' → so it gives 'am'
print(name[-6:-4])        # Output: am

# Positive slicing: index 12 = 'a', index 14 = 'm' → gives 'am'
print(name[12:14])        # Output: am
