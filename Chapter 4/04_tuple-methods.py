# Tuple Methods
# Since tuples are immutable, they do not have methods that modify their content.
# However, you can use the following methods to work with tuples:

# count() - Returns the number of times a specified value occurs in a tuple.
# index() - Searches the tuple for a specified value and returns the position of where it was found.

a = (1, 2, 3, 2, 1)
i = a.index(3)  # Returns the index of the first occurrence of 3
print(i)  # Output: 2
