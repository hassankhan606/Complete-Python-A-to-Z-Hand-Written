# They give us input
# In Python, variables have different types like int (integer), float (decimal), str (text), etc.
# input() returns a string by default, so we use int() to convert it into an integer for addition.

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

print("Number a is:", a)
print("Number b is:", b)

# Add the numbers
sum = a + b
print("Sum is:", sum)
# We can also use float() if we want to handle decimal numbers