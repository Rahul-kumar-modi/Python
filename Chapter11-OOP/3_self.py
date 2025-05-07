class Employee:
    language = "Python" # This is class attribute
    salary = 1200000

    def getInfo(self): #o/p-> We can give other word on place "self"
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod 
    def greet(): #o/p -> If we don't want to pass "self" object on greet() function then we use staticmethod in it.
        print("Good night")

harry = Employee()
harry.language = "Javascript" # This is object/instance attribute.

harry.getInfo() # They both give same o/p->"The language is Javascript. The salary is 1200000"
Employee.getInfo(harry) # They both give same o/p->"The language is Javascript. The salary is 1200000"
harry.greet() #o/p-> Good night