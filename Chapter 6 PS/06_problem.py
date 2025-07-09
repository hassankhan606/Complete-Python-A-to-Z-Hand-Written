grade = int(input("Enter your marks :"))

if(grade<=100 and grade>=90):
    grade = "Ex"
elif(grade<80 and grade >=60):
    grade = "A+" 
elif(grade<60 and grade >=40):
    grade = "pass"
    
else:
    grade = "fail"    
print("Your are :" , grade)    