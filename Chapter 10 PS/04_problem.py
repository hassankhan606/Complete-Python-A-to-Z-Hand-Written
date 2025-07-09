from random import randint


class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
         print(f"Ticket is booked from Train No: {self.trainNo} from :{fro} to {to}")
    def getStatus(self):
        print(f"Train no{self.trainNo} is running on time!")
    def getFare(self,fro,to):
        print(f"Ticket fare in Train no {self.trainNo} from {fro} to {to} is {randint(222,555)}")
        
        
t = Train(12300)
t.book("BWN","MCD")        
t.getStatus()
t.getFare("BWN","MCD")