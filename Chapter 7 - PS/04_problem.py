n = int(input("Enter A number you want to check :"))

for i in range(2 , n):
    if(n%i)==0:
     print("number is not a prime.")
     break
else:
    print("Number is Prime.")     