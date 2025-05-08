class Employee:
    company = "Tata"
    salary = 130000
    language = "Java"
    def show(self):
        print(f"The name is {self.company} and  the salary is {self.salay}")

# class Programmer: # Without inheritance
#     company = "Tata TCS"
#     language = "Python"
#     salary = 430000
#     def show(self):
#         print(f"The name is {self.company} and  the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.company} and he is good with {self.language} language")



class Programmer(Employee): # Inheritance
    company = "Tata TCS"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()
print(a.company, b.company)
b.showLanguage()