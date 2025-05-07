# Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode


p = Programmer("Harry", 1222000, 345678)
print(p.name, p.salary, p.pincode,p.company)

s = Programmer("Shubham", 3322000, 445678)
print(s.name, s.salary, s.pincode,s.company)