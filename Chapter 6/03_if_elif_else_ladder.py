a = int(input("Enter Your Age: "))
# ** if else ladder statement
if(a>=18) : #** if condition is true
    print("You are above the age of consent")
    print("Good for You")
    
elif(a<0) :  #** if condition2 is true
    print("You have entered an invalid age")
    
elif(a==0) : #** if condition2 is true
    print("You have entered zero which is not a valid age")
        
else : #** if all condition false the run
    print("You are below the age of consent")
    
print("End of the Program")            