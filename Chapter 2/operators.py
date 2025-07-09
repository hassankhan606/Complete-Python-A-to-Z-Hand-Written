# Arithmetic operators (+ - * /)
a = 45
b = 35
c = a + b
print("Addition:", c)

# Assignment operators (= += -= *= /=) assign values to variables
d = 5-3 
print ("Subtraction:", d)

c += 2 # Increment d by 2
c = 5
print ("Incremented c:", c)

# Comparison operators (== != < > <= >=) compare values note:their result is a boolean 
a = 34 > 90
print("Is 34 greater than 90?", a) # it is symbol for greater than

b= 45 < 90 
print("Is 45 less than 90?", b) # it is symbol for less than

# Logical operators (and or not) combine boolean expressions
# Truth Table of or
x = True or False
print("True or False:", True or False)
print("True or True:", True or True) 
print("False or False:", False or False)
print("False or True:", False or True)   

# Truth Table of and
y = True and False
print("True and False:", True and False)    
print("True and True:", True and True)
print("False and False:", False and False)
print("False and True:", False and True)

# Truth Table of not
z = not True
print("not True:", not True)
# Identity operators (is is not) check if two variables point to the same object
a = [1, 2, 3]     