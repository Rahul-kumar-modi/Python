class Employee:
    a = 1

    @classmethod
    def show(cls): 
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 34

e.name = "Harry Khan"
# print(e.name)
print(e.fname, e.lname) #In this we do very much work to print "Harry Khan" which we invisible to user(from line 8 to line 15) we pack code in one place, this example show "encapsulation and abstraction".

e.show()