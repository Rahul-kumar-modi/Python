class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3
   
o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error ad there is no "b" attribute in Employee class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)