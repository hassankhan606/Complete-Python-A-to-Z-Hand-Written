#* 🔹 What is a Function?
#* A function is a group of statements that perform a specific task.

#* 🔹 Why are functions important?
#* Functions are very useful because:
#* - They help avoid repeating code.
#* - They make your code cleaner and easier to understand.
#* - You can reuse them multiple times.

# *🔹 Example:
# *Let's say we want to calculate the average of 3 numbers, five times.
# *Without a function, we would have to write the same code 5 times.
# *With a function, we write the logic once and call it whenever needed.
#* Types of functions in Python
#* 1.Built-in-Function:Already built in python like print() len() e.t.c
# *2.User-Defines0Function:These are functions which are defines by user not already built-in
def avg(): #^Function Definition
    a=int(input("Enter Your Number:"))
    b=int(input("Enter Your Number:"))
    c=int(input("Enter Your Number:"))
    average = (a +b + c )/3
    print(average)

avg()    #^Function Call
avg()    
avg()    
avg()    
avg()    


        