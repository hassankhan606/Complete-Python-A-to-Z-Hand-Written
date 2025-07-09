# **=============================
# if, elif, else in Python 🐍
# **=============================

# **The 'if' statement is used to check a condition.
# **If the condition is True, the code inside the if block will run.
# **Example:
age = 18
if age == 18:
    print("You are exactly 18")  # **This will run because age is 18

#**The 'elif' (else if) statement is used to check another condition if the first one is False.
#** It stands for "else if". You can use many elif blocks.
# **Only the first True condition will run.
age = 20
if age < 18:
    print("You are a minor")
elif age == 20:
    print("You are 20 years old")  # **This will run because age is 20
elif age > 50:
    print("You are a senior citizen")
# **Even though age > 18, only one block runs!

# **The 'else' block runs if none of the 'if' or 'elif' conditions are True.
# **It is like a "default" action.
age = 70
if age < 18:
    print("Child")
elif age < 50:
    print("Adult")
else:
    print("Senior Citizen")  # **This will run because age is 70 and other conditions were False

#** In short:
#** - 'if' → checks first condition
#** - 'elif' → checks more conditions
#** - 'else' → runs when all above are False
