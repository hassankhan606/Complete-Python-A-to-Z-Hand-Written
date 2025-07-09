class Programmer():
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary= salary
        self.pin = pin
        
p = Programmer("HASSAN", 120000 ,234567)
print(p.name,p.salary,p.pin,p.company)  
r = Programmer("Rohit" ,100000, 679844)
print(f'The Programmer Name is :{r.name}, & Salary is:{r.salary} , &Pin Code is{r.pin} , from Company:{r.company}')       
        