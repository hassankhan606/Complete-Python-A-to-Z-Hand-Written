class Demo:
    a=4
o = Demo()
print (o.a)  #^ Print class attribute 
o.a=0        #^ We made an instance Method
print(o.a)   #^ Print now this method because we made it.

print(Demo.a)