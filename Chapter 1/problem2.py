import os

# Set the directory you want to list
directory = "/"

# List and print contents
contents = os.listdir(directory)
print(f"Contents of '{directory}':")
for item in contents:
    print(item)
