marks={
    "harry":100,
    "roman":90, 
    "shah":80,
    "amir":70,
}
# print(marks.keys())  
# Returns a view object that displays a list of a dictionary's keys
# print(marks.values())
# Returns a view object that displays a list of a dictionary's values
# print(marks.items())
# Returns a view object that displays a list of a dictionary's key-value pairs
# print(marks.get("harry"))
# Returns the value for the specified key if key is in dictionary, else None
# marks.update({"shah": 85 , "Renuka":95})
# Updates the dictionary with the specified key-value pairs by this the marks dictionary is updated
# and we also add a new key-value pair
print(marks.get("Renuka")) # Returns the value for the specified key if key is in dictionary, else None
print(marks["Renuka"]) # Returns the value for the specified key if key is in dictionary, else None