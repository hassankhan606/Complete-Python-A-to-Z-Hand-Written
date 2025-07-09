class Calculator:
    def __init__(self,n):
        self.n =n
        
    def square(self):
        print(f"The square of given Number is :{self.n*self.n} ")
    def cube(self):
        print(f"The cube of given Number is : {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The Square Root of given number is : {self.n**1/2}")    
        
    @staticmethod
    def greet():
        print("Hello Dear!")    
a = Calculator(90)
a.greet()
a.square()       
a.cube()
a.squareRoot()            
 
        