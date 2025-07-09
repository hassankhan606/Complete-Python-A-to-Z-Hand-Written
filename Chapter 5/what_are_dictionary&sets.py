# **In Python, **dictionaries** and **sets** are both collection data types used to store and manage data. A 
# **dictionary** stores data in the form of **key-value pairs**, 
# **where each key must be unique and is used to access its corresponding value, 
# **For example, if we want to store the marks of students in a class, 
# **we can use the student's name as the key and their marks as the value. 
# **Dictionaries are **unordered** (items are not stored in a fixed order), **mutable** (items can be changed), 
# **and **indexed by keys** (not by position), and they **do not allow duplicate keys**. 
# **On the other hand, a **set** is a collection of **unique items**, meaning it automatically removes duplicate values. 
# **Sets are useful when you want to store only distinct values, such as filtering unique numbers from a list.
# **Like dictionaries, sets are also **unordered** and **mutable**, but **they are not indexed**,
# **There is no way to change items in set,cannot contain duplicate value
# **which means you cannot access items in a set using an index. 
# **To create an empty dictionary, we use `d = {}` 
# **and to create an empty set, we use `s = set()` — note that using `{}` alone creates an empty dictionary, not a set.

# **Example of a dictionary

Example = {
    "name": "John",    
    "age": 30,
    "city": "New York"
}
print(Example)