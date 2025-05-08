# Create a class 'Employee' and add salary and increment properties to it. Write a method 'salaryAfterincrement' method with a @property decorator with a setter which changes the value of increment based on salary.

class Employee:
    salary = 4000000
    increment = 20

    @property
    def salaryAfterIncrement(self):
            return ((self.salary + self.salary * self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
          self.increment = ((salary / self.salary) - 1) * 100  #salary = new salary and self.salary = old salary

d = Employee()
# print(d.salaryAfterIncrement)
d.salaryAfterIncrement = 4800000
print(d.increment)