# Learning string slicing with skip value (like a child 😊)

name = "PythonProgramming"

# Let's print every 1st letter from index 0 to 6
print(name[0:6:1])  # 👉 P y t h o n → Output: Python

# Let's skip every 2nd letter from index 0 to 6
print(name[0:6:2])  # 👉 P t o → Output: Pto

# Skip every 3rd letter from index 0 to 9
print(name[0:9:3])  # 👉 P h r → Output: Phr

# You can even slice the full string with skips
print(name[::2])    # 👉 Take all letters, but skip every 2nd → Output: Pto rgamn

# Reverse the string using skip (step = -1)
print(name[::-1])   # 👉 g n i m m a r g n o h t y P → Output: gnimmargnohtyP
