class Employee:
    language = "Python" # This is class attribute
    salary = 1200000

    # def __init__(self):    #In it dundar method which is automatically called
    #     print("I am creating an object")
    
    def __init__(self, name, salary, language): #In it dundar method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod 
    def greet():
        print("Good night")

# harry = Employee()
# harry.name = "Harry"
# print(harry.name, harry.salary, harry.language)#o/p-> I am creating an object
                                                #      Harry 1200000 Python

harry = Employee("Harry", 1300000, "Javascript")
print(harry.name, harry.salary, harry.language) #o/p-> I am creating an object
                                                #      Harry 1300000 Javascript


