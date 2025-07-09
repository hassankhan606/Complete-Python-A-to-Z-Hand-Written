class thirdEmployee:
    language = "JavaScript"
    Name="John"
    
    def __init__(self):
        print("i am creating an object") #^Dunder Method
    def getInfo(self):
        print(f"The Name is: {self.Name}\nThe Language is {self.language}")
    def greet(self):
        print("Good Morning")
        
john = thirdEmployee()
john.greet()          
john.getInfo()

Elon = thirdEmployee()
  
